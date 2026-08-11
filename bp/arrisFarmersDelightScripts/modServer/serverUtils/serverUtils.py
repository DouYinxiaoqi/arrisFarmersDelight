# -*- coding: utf-8 -*-
from ...QuModLibs.Server import *
from ...modCommon.modConfig import *
import math, random, copy

entityFace = {
    0: (0, -90),
    1: (0, 0),
    2: (0, 90),
    3: (0, 180)
}

# 厨锅/煎锅/炉灶 tick 错峰常量。越大瞬时工作量越低但响应相位越粗。
# 厨锅是 20Hz 的 tick_event、timer 步长 0.05/tick * 20 tick/s = 1.0/s；若 STRIDE=4 则步长需要×4 补偿，一锅的实际 tick 频率仍然 5Hz 足够跟上 UI。
COOKING_POT_TICK_STRIDE = 4

def PosHash(pos):
    # 整型坐标哈希（三维离散化）；用于 tick 错峰加盐，让不同坐标的方块实体落在不同 tick 上
    x, y, z = int(pos[0]), int(pos[1]), int(pos[2])
    return (x * 73856093 ^ y * 19349663 ^ z * 83492791) & 0x7FFFFFFF

def FromAngleGetBlockAux(x1, y1, x2, y2):
    # 计算两点直接的角度并返回特殊值
    dx = x2 - x1
    dy = y2 - y1
    radian = math.atan2(dy, dx)
    angle = math.degrees(radian)
    if -45 < angle < 45:
        aux = 3
    elif 45 < angle < 135:
        aux = 0
    elif 135 < angle < 180 or -180 < angle < -135:
        aux = 1
    else:
        aux = 2
    return aux

def clickBlockFace(x, y, z):
    # 根据点击方块的坐标来判断应该放置方块的坐标
    placePos = {
        0: (x, y - 1, z), # Down
        1: (x, y + 1, z), # Up
        2: (x, y, z - 1), # North
        3: (x, y, z + 1), # South
        4: (x - 1, y, z),  # West
        5: (x + 1, y, z)  # East
    }
    return placePos

def ProbabilityFunc(probability):
    # 以 probability % 的概率返回True否则返回False
    if probability <= 0:
        return False
    if probability >= 100:
        return True
    return random.randint(1, 100) <= probability

def ToAllPlayerPlaySound(dmId, pos, soundName):
    # 播放音效 — 单次广播给全体客户端，由客户端本地检查维度过滤，
    # 避免在服务端每人创建 CreateDimension 组件做维度查询
    Call("*", "OnPlaySound", {"soundName": soundName, "pos": pos, "dimensionId": dmId})

def IsFullBackpack(playerId):
    # 检测玩家背包是否已满
    playerAllItems = compFactory.CreateItem(playerId).GetPlayerAllItems(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY)
    itemList = list(filter(None, playerAllItems))
    if len(itemList) >= 36:
        return True
    else:
        return False

def ResetPlayerUsedCD(playerId):
    # 重置CD
    compFactory.CreateModAttr(playerId).SetAttr("arrisUsedCD", False)

def SetPlayerUsedCD(playerId):
    # 设置CD
    cd = compFactory.CreateModAttr(playerId).GetAttr("arrisUsedCD")
    if cd is False:
        compFactory.CreateModAttr(playerId).SetAttr("arrisUsedCD", True)
        compFactory.CreateGame(levelId).AddTimer(0.2, ResetPlayerUsedCD, playerId)
        Call(playerId, "PlayAttackAnimationCommon", None)
        return False
    else:
        return True

def SetNotCreateItem(playerId, itemDict):
    # 在非创造模式下，扣除1个玩家手持物品
    gameType = compFactory.CreateGame(levelId).GetPlayerGameType(playerId)
    if gameType != 1:
        itemDict["count"] -= 1
        compFactory.CreateItem(playerId).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, itemDict, 0)

def GetItemType(itemDict):
    # 获取物品类型
    if itemDict:
        itemName = itemDict["newItemName"]
        if itemName in platePackagedFoodDict:
            return "food"
        else:
            basicInfo = compFactory.CreateItem(levelId).GetItemBasicInfo(itemName)
            itemType = basicInfo["itemType"]
            return itemType
    else:
        return None

def IsKnife(itemName):
    # 兼容配置内显式登记的刀具和跨附加包提供的刀具标签
    if itemName in knifeList:
        return True
    itemTags = compFactory.CreateItem(levelId).GetItemTags(itemName)
    return "arris:knife" in (itemTags or [])

def DetectionExperimentalHoliday():
    # 检测是否为假日创造者模式
    gameRules = compFactory.CreateGame(levelId).GetGameRulesInfoServer()
    experimental_holiday = gameRules["option_info"]["experimental_holiday"]
    if experimental_holiday is True:
        return {0: 0, 4: 1, 8: 2, 12: 3}
    else:
        return {0: 0, 1: 1, 2: 2, 3: 3}

def CheckCookingPotRecipe(inputItemSlot):
    # 检查厨锅内的物品是否符合配方
    # 通过预先构建的 _cookingPotRecipeIndex 做 O(1) 字典查找，
    # 替代原来遍历 CookingPotRecipeList × variants + Counter 比较的 O(n*m) 方案。
    inputItemList = []
    for itemDict in inputItemSlot:
        if itemDict != {}:
            inputItemList.append((itemDict["newItemName"], itemDict["newAuxValue"]))
    if not inputItemList:
        return None, None
    key = tuple(sorted(inputItemList))
    hit = LookupCookingPotRecipe(key)
    if not hit:
        return None, None
    cookResult, pushItemList = hit
    resultItem = {"newItemName": cookResult[0], "newAuxValue": cookResult[1], "count": 1}
    return resultItem, pushItemList

def GetDisplayEntityCarriedItemType(itemDict):
    if itemDict:
        itemType = GetItemType(itemDict)
        itemName = itemDict["newItemName"]
        auxValue = itemDict["newAuxValue"]
        key = (itemName, auxValue)
        if key in CuttingBoardDict:
            exceptional = CuttingBoardDict[key].get("type")
            if exceptional is not None:
                itemType = exceptional
            if not itemType or itemType == "" or itemType == "food":
                return 0
            elif itemType == "block":
                return 1
            else:
                return 2
        if not itemType or itemType == "" or itemType == "food":
            return 0
        elif itemType == "block":
            return 1
        else:
            return 2
    else:
        return 0

def StoveDisplayEntity(itemDict, playerId, data):
    posList = [
        (0.25, 0.27),
        (0.5, 0.27),
        (0.75, 0.27),
        (0.25, 0.73),
        (0.5, 0.73),
        (0.75, 0.73)
    ]
    itemDict["count"] = 1
    blockEntityData = data["blockEntityData"]
    x, y, z = data["blockPos"]
    dimensionId = data["dimensionId"]
    blockAuxValue = data["blockAuxValue"]
    aux = DetectionExperimentalHoliday()
    blockAux = aux.get(blockAuxValue, blockAuxValue)
    displayEntityDict = blockEntityData["displayEntityDict"]
    if blockEntityData["cookingIndex"] >= 6:
        blockEntityData["cookingIndex"] = 0
    cookingIndex = blockEntityData["cookingIndex"]
    relativePos = posList[cookingIndex]
    Id = System.CreateEngineEntityByTypeStr("arris:item_display", (x + relativePos[0], y + 0.953, z + relativePos[1]), entityFace[blockAux], dimensionId)
    displayEntityDict[str(cookingIndex)] = Id
    compFactory.CreateEntityEvent(Id).TriggerCustomEvent(Id, "arris:set_small")
    blockEntityData["displayEntityDict"] = displayEntityDict
    blockEntityData[str(cookingIndex)] = {"itemDict": itemDict, "cookTimer": 7}
    compFactory.CreateItem(Id).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, itemDict, 0)

    itemType = GetDisplayEntityCarriedItemType(itemDict)
    compFactory.CreateEntityDefinitions(Id).SetVariant(int(itemType))

def SkilletDisplayEntity(itemDict, playerId, data):
    count = itemDict["count"]
    blockEntityData = data["blockEntityData"]
    displayEntityList = []
    x, y, z = data["blockPos"]
    dimensionId = data["dimensionId"]
    blockAuxValue = data["blockAuxValue"]
    aux = DetectionExperimentalHoliday()
    blockAux = aux.get(blockAuxValue, blockAuxValue)
    step = -0.037
    if count == 1:
        num = 1
    elif 2 <= count <= 16:
        num = 2
    elif 17 <= count <= 32:
        num = 3
    elif 33 <= count <= 48:
        num = 4
    elif 49 <= count <= 64:
        num = 5
    else:
        num = 0
    for i in range(0, num):
        step += 0.037
        Id = System.CreateEngineEntityByTypeStr("arris:item_display", (x + random.uniform(0.43, 0.57), y + step, z + random.uniform(0.43, 0.57)), entityFace[blockAux], dimensionId)
        displayEntityList.append(Id)
        displayDict = copy.deepcopy(itemDict)
        displayDict["count"] = 1
        compFactory.CreateItem(Id).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, displayDict, 0)
        itemType = GetDisplayEntityCarriedItemType(displayDict)
        compFactory.CreateEntityDefinitions(Id).SetVariant(int(itemType))
    blockEntityData["displayEntityList"] = displayEntityList

def CuttingBoardDisplayEntity(itemDict, playerId, data):
    blockEntityData = data["blockEntityData"]
    dimensionId = data["dimensionId"]
    blockAuxValue = data["blockAuxValue"]
    x, y, z = data["blockPos"]
    aux = DetectionExperimentalHoliday()
    blockAux = aux.get(blockAuxValue, blockAuxValue)
    Id = System.CreateEngineEntityByTypeStr("arris:item_display", (x + 0.5, y, z + 0.5), entityFace[blockAux], dimensionId)
    displayDict = copy.deepcopy(itemDict)
    compFactory.CreateItem(Id).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, displayDict, 0)
    blockEntityData["displayEntityId"] = Id
    itemType = GetDisplayEntityCarriedItemType(itemDict)
    basicInfo = compFactory.CreateItem(levelId).GetItemBasicInfo(itemDict["newItemName"])
    compFactory.CreateEntityDefinitions(Id).SetVariant(int(itemType))

def CheckCookingPotVessel(blockEntityData, blockPos, dimensionId):
    # 检查厨锅内的容器是否符合并更新
    x, y, z = blockPos
    previewItemSlot = blockEntityData["previewItemSlot"][0]
    # 前置短路：预览槽为空时不可能有成品待出料，跳过整段配方扫描
    if not previewItemSlot:
        return
    vesselItemSlot = compFactory.CreateItem(levelId).GetContainerItem(blockPos, 6, dimensionId)

    for RecipeDict in CookingPotRecipeList:
        cookResult = RecipeDict["CookResult"]
        vessel = RecipeDict.get("Vessel")
        resultItemName = cookResult[0]
        resultAuxValue = cookResult[1]
        if vessel:
            vesselDict = {"newItemName": vessel[0], "newAuxValue": vessel[1]}
        else:
            vesselDict = {}

        if previewItemSlot and previewItemSlot.get("newItemName") == resultItemName:
            if not vessel:
                basicInfo = compFactory.CreateItem(levelId).GetItemBasicInfo(resultItemName, resultAuxValue)
                maxStackSize = basicInfo["maxStackSize"]
                resultItemSlot = compFactory.CreateItem(levelId).GetContainerItem(blockPos, 7, dimensionId)
                if resultItemSlot and resultItemSlot["newItemName"] != resultItemName:
                    return
                if resultItemSlot and resultItemSlot["count"] >= maxStackSize:
                    return
                previewItemCount = previewItemSlot["count"]
                blockEntityData["previewItemSlot"] = [None]
                if not resultItemSlot:
                    resultCount = previewItemCount
                else:
                    resultCount = previewItemCount + resultItemSlot[0]["count"]
                itemDict = {"newItemName": resultItemName, "newAuxValue": resultAuxValue, "count": resultCount, "enchantData": []}
                compFactory.CreateItem(levelId).SpawnItemToContainer(itemDict, 7, (x,y,z), dimensionId)
                System.CreateEngineEntityByTypeStr("minecraft:xp_orb", (x + 0.5, y + 1, z + 0.5), (0, 0), dimensionId)

            elif vesselItemSlot and vesselDict.get("newItemName") == vesselItemSlot.get("newItemName"):
                count = vesselItemSlot["count"] - previewItemSlot["count"]

                basicInfo = compFactory.CreateItem(levelId).GetItemBasicInfo(resultItemName, resultAuxValue)
                maxStackSize = basicInfo["maxStackSize"]
                resultItemSlot = compFactory.CreateItem(levelId).GetContainerItem(blockPos, 7, dimensionId)
                if resultItemSlot and resultItemSlot["newItemName"] != resultItemName:
                    return
                if resultItemSlot and resultItemSlot["count"] >= maxStackSize:
                    return
                if count >= 0:
                    previewItemCount = previewItemSlot["count"]
                    blockEntityData["previewItemSlot"] = [None]
                    vesselItemSlot["count"] = count
                    compFactory.CreateItem(levelId).SpawnItemToContainer(vesselItemSlot, 6, (x,y,z), dimensionId)

                    if not resultItemSlot:
                        resultCount = previewItemCount
                    else:
                        resultCount = previewItemCount + resultItemSlot["count"]
                    resultDict = {"newItemName": resultItemName, "newAuxValue": resultAuxValue, "count": resultCount, "enchantData": []}
                    compFactory.CreateItem(levelId).SpawnItemToContainer(resultDict, 7, (x,y,z), dimensionId)
                else:
                    previewItemSlot["count"] = abs(count)
                    blockEntityData["previewItemSlot"] = [previewItemSlot]

                    compFactory.CreateItem(levelId).SpawnItemToContainer({}, 6, (x,y,z), dimensionId)

                    if not resultItemSlot:
                        resultCount = vesselItemSlot["count"]
                    else:
                        resultCount = abs(count) + resultItemSlot["count"]
                    resultDict = {"newItemName": resultItemName, "newAuxValue": resultAuxValue, "count": resultCount, "enchantData": []}
                    compFactory.CreateItem(levelId).SpawnItemToContainer(resultDict, 7, (x,y,z), dimensionId)

                System.CreateEngineEntityByTypeStr("minecraft:xp_orb", (x + 0.5, y + 1, z + 0.5), (0, 0), dimensionId)

def SetCarriedDurability(playerId, itemDict, dimensionId, pos):
    # 设置手持物品耐久-1
    gameType = compFactory.CreateGame(levelId).GetPlayerGameType(playerId)
    if gameType != 1:
        if GetItemType(itemDict) in ["", "block"]:
            return
        itemDict["durability"] -= 1
        if itemDict["durability"] <= 0:
            ToAllPlayerPlaySound(dimensionId, pos, "random.break")
            compFactory.CreateItem(playerId).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, None, 0)
        else:
            compFactory.CreateItem(playerId).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, itemDict, 0)
