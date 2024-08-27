# -*- coding: utf-8 -*-
from ...QingYunModLibs.ServerMod import *
from ...QingYunModLibs.SystemApi import *
from ...modCommon.modConfig import *
from collections import Counter
import math
import random
import copy

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
    randomList = []
    for i in range(probability):
        randomList.append(1)
    for x in range(100 - probability):
        randomList.append(0)
    extract = random.choice(randomList)
    if extract == 1:
        return True
    else:
        return False

def ToAllPlayerPlaySound(dmId, pos, soundName):
    # 播放音效
    playerList = serverApi.GetPlayerList()
    for playerId in playerList:
        dimensionId = ServerComp.CreateDimension(playerId).GetEntityDimensionId()
        if dimensionId == dmId:
            data = {"soundName": soundName, "pos": pos}
            CallClient("OnPlaySound", playerId, data)

def IsFullBackpack(playerId):
    # 检测玩家背包是否已满
    playerAllItems = ServerComp.CreateItem(playerId).GetPlayerAllItems(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY)
    itemList = list(filter(None, playerAllItems))
    if len(itemList) >= 36:
        return True
    else:
        return False

def SetNotCreateItem(playerId, itemDict):
    # 在非创造模式下，扣除1个玩家手持物品
    gameType = ServerComp.CreateGame(levelId).GetPlayerGameType(playerId)
    if gameType != 1:
        itemDict["count"] -= 1
        ServerComp.CreateItem(playerId).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, itemDict, 0)

def GetItemType(itemDict):
    # 获取物品类型
    if itemDict:
        itemName = itemDict["newItemName"]
        if itemName in platePackagedFoodDict:
            return "food"
        else:
            basicInfo = ServerComp.CreateItem(levelId).GetItemBasicInfo(itemName)
            itemType = basicInfo["itemType"]
            return itemType
    else:
        return None

def DetectionExperimentalHoliday():
    # 检测是否为假日创造者模式
    gameRules = ServerComp.CreateGame(levelId).GetGameRulesInfoServer()
    experimental_holiday = gameRules["option_info"]["experimental_holiday"]
    if experimental_holiday is True:
        return {0: 0, 4: 1, 8: 2, 12: 3}
    else:
        return {0: 0, 1: 1, 2: 2, 3: 3}

def CheckCookingPotRecipe(blockEntityData):
    # 检查厨锅内的物品是否符合配方
    inputItemSlot = blockEntityData["inputItemSlot"]
    inputItemList = list()
    for itemDict in inputItemSlot:
        if itemDict != {}:
            tupleRecipe = (itemDict["newItemName"], itemDict["newAuxValue"])
            inputItemList.append(tupleRecipe)
    for RecipeDict in CookingPotRecipeList:
        for recipe in RecipeDict["Recipe"]:
            if Counter(recipe) == Counter(inputItemList):
                resultItem = {"newItemName": RecipeDict["CookResult"][0], "newAuxValue": RecipeDict["CookResult"][1], "count": 1}
                return resultItem
    return None

def CheckCookingPotVessel(blockEntityData):
    # 检查厨锅内的容器是否符合并更新
    previewItemSlot = blockEntityData["previewItemSlot"][0]
    vesselItemSlot = blockEntityData["vesselItemSlot"][0]
    for RecipeDict in CookingPotRecipeList:
        cookResult = RecipeDict["CookResult"]
        vessel = RecipeDict["Vessel"]
        resultItemName = cookResult[0]
        resultAuxValue = cookResult[1]
        vesselDict = {"newItemName": vessel[0], "newAuxValue": vessel[1]}
        if not vesselItemSlot:
            return
        if previewItemSlot and previewItemSlot.get("newItemName") == resultItemName:
            if vesselDict.get("newItemName") == vesselItemSlot.get("newItemName"):
                count = vesselItemSlot["count"] - previewItemSlot["count"]

                basicInfo = ServerComp.CreateItem(levelId).GetItemBasicInfo(resultItemName, resultAuxValue)
                maxStackSize = basicInfo["maxStackSize"]
                resultItemSlot = blockEntityData["resultItemSlot"]
                if resultItemSlot[0] and resultItemSlot[0]["count"] >= maxStackSize:
                    return

                if count >= 0:
                    previewItemCount = previewItemSlot["count"]
                    blockEntityData["previewItemSlot"] = [None]
                    vesselItemSlot["count"] = count
                    blockEntityData["vesselItemSlot"] = [vesselItemSlot]
                    if not resultItemSlot[0]:
                        resultCount = previewItemCount
                    else:
                        resultCount = previewItemCount + resultItemSlot[0]["count"]
                    blockEntityData["resultItemSlot"] = [{"newItemName": resultItemName, "newAuxValue": resultAuxValue, "count": resultCount, "enchantData": []}]
                else:
                    previewItemSlot["count"] = abs(count)
                    blockEntityData["previewItemSlot"] = [previewItemSlot]
                    blockEntityData["vesselItemSlot"] = [None]
                    if not resultItemSlot[0]:
                        resultCount = abs(count)
                    else:
                        resultCount = abs(count) + resultItemSlot[0]["count"]
                    blockEntityData["resultItemSlot"] = [{"newItemName": resultItemName, "newAuxValue": resultAuxValue, "count": resultCount, "enchantData": []}]

                update = {
                    "heatEnable": blockEntityData["heatEnable"],
                    "inputItemSlot": blockEntityData["inputItemSlot"],
                    "vesselItemSlot": blockEntityData["vesselItemSlot"],
                    "resultItemSlot": blockEntityData["resultItemSlot"],
                    "previewItemSlot": blockEntityData["previewItemSlot"],
                    "blockPos": blockEntityData["blockPos"],
                    "dimensionId": blockEntityData["dimensionId"]
                }
                CallClient("UpdateCookingPot", blockEntityData["playerId"], update)

def SetCarriedDurability(playerId, itemDict, dimensionId, pos):
    # 设置手持物品耐久-1
    gameType = ServerComp.CreateGame(levelId).GetPlayerGameType(playerId)
    if gameType != 1:
        itemDict["durability"] -= 1
        if itemDict["durability"] <= 0:
            ToAllPlayerPlaySound(dimensionId, pos, "random.break")
            ServerComp.CreateItem(playerId).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, None, 0)
        else:
            ServerComp.CreateItem(playerId).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, itemDict, 0)

def InitSnowClean(args):
    # 清理野生作物顶部的雪
    blockEntityData = args["blockEntityData"]
    blockPos = args["blockPos"]
    dimensionId = args["dimensionId"]
    if blockEntityData:
        blockEntityData["initSnowClean"] = True
        blockDict = ServerComp.CreateBlockInfo(levelId).GetBlockNew(blockPos, dimensionId)
        if blockDict["name"] == "minecraft:snow_layer":
            ServerComp.CreateBlockInfo(levelId).SetBlockNew(blockPos, {"name": "minecraft:air"}, 0, dimensionId, False, False)

def InitFloodClean(args):
    blockEntityData = args["blockEntityData"]
    blockPos = args["blockPos"]
    dimensionId = args["dimensionId"]
    if blockEntityData:
        blockEntityData["initFloodClean"] = True
        blockDict = ServerComp.CreateBlockInfo(levelId).GetBlockNew(blockPos, dimensionId)
        if blockDict["name"] != "minecraft:air":
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((blockPos[0], blockPos[1] - 1, blockPos[2]), {"name": "minecraft:air"}, 0, dimensionId, False, False)
