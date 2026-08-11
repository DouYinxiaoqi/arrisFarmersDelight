# -*- coding: utf-8 -*-
from serverUtils.serverUtils import *

@Listen("BlockNeighborChangedServerEvent")
def OnCuttingBoardNeighborChanged(args):
    blockName = args["blockName"]
    blockPos = (args["posX"], args["posY"], args["posZ"])
    dimensionId = args["dimensionId"]
    neighborPos = (args["neighborPosX"], args["neighborPosY"], args["neighborPosZ"])
    neighborName = args["toBlockName"]
    if blockName == "arris:cutting_board":
        if neighborPos == (args["posX"], args["posY"] - 1, args["posZ"]):
            if neighborName == "minecraft:air":
                compFactory.CreateBlockInfo(levelId).SetBlockNew(blockPos, {"name": "minecraft:air"}, 1, dimensionId)

@Listen("ServerItemUseOnEvent")
def OnServerCuttingBoardItemUse(args):
    # 玩家在对方块使用物品之前服务端抛出的事件
    blockName = args["blockName"]
    if blockName == "arris:cutting_board":
        args["ret"] = True

@Listen("ServerBlockUseEvent")
def OnServerCuttingBoardBlockUse(args):
    # 使用空手拿取砧板上的物品
    blockName = args["blockName"]
    blockPos = (args["x"], args["y"], args["z"])
    dimensionId = args["dimensionId"]
    playerId = args["playerId"]
    x, y, z = blockPos
    if blockName != "arris:cutting_board":
        return
    if SetPlayerUsedCD(playerId) is True:
        return
    blockEntityData = compFactory.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
    if not blockEntityData:
        return
    carriedDict = compFactory.CreateItem(playerId).GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, 0, True)
    if carriedDict:
        itemType = GetItemType(carriedDict)
        displayEntityId = blockEntityData["displayEntityId"]
        cuttingDict = blockEntityData["cuttingDict"]
        if displayEntityId and cuttingDict:
            result = CuttingBoardDict.get((cuttingDict["newItemName"], cuttingDict["newAuxValue"]))
            if not result:
                return
            toolList = result["tool"]
            itemName = carriedDict["newItemName"]
            if itemName in toolList or (toolList == knifeList and IsKnife(itemName)):
                for resultDict in result["itemList"]:
                    System.CreateEngineItemEntity(resultDict, dimensionId, (x + 0.5, y + 0.5, z + 0.5))
                DestroyEntity(displayEntityId)
                ToAllPlayerPlaySound(dimensionId, (x, y, z), "ambient.cutting_board.knife")
                SetCarriedDurability(playerId, carriedDict, dimensionId, (x, y, z))
                blockEntityData["cuttingDict"] = None
                blockEntityData["displayEntityId"] = None
        else:
            itemName = carriedDict["newItemName"]
            auxValue = carriedDict["newAuxValue"]
            if itemName == "arris:skillet_item":
                return
            if itemType in ["sword", "axe", "hoe", "shovel", "pickaxe"] or (itemName, auxValue) in CuttingBoardDict:
                ToAllPlayerPlaySound(dimensionId, (x, y, z), "dig.wood")
                SetNotCreateItem(playerId, carriedDict)
                carriedDict["count"] = 1
                blockEntityData["cuttingDict"] = carriedDict
                data = {"blockEntityData": blockEntityData, "blockPos": (x, y, z), "blockAuxValue": args["aux"], "dimensionId": dimensionId}
                CuttingBoardDisplayEntity(carriedDict, playerId, data)
            else:
                compFactory.CreateGame(playerId).SetOneTipMessage(playerId, "该物品无法放置在砧板上...")
    else:
        displayEntityId = blockEntityData["displayEntityId"]
        cuttingDict = blockEntityData["cuttingDict"]
        if cuttingDict:
            compFactory.CreateItem(playerId).SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, cuttingDict, 0)
            ToAllPlayerPlaySound(dimensionId, blockPos, "armor.equip_leather")
            blockEntityData["cuttingDict"] = None
        if displayEntityId:
            DestroyEntity(displayEntityId)
            blockEntityData["displayEntityId"] = None

@Listen("BlockRemoveServerEvent")
def OnCuttingBoardRemove(args):
    # 砧板销毁时触发
    blockPos = (args["x"], args["y"], args["z"])
    blockName = args["fullName"]
    dimensionId = args["dimension"]
    if blockName == "arris:cutting_board":
        blockEntityData = compFactory.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
        displayEntityId = blockEntityData["displayEntityId"]
        cuttingDict = blockEntityData["cuttingDict"]
        if displayEntityId:
            DestroyEntity(displayEntityId)
        if cuttingDict:
            System.CreateEngineItemEntity(cuttingDict, dimensionId, (args["x"] + 0.5, args["y"] + 0.5, args["z"] + 0.5))
