# -*- coding: utf-8 -*-
from ..QingYunModLibs.ServerMod import *
from ..QingYunModLibs.SystemApi import *
from ..modCommon.modConfig import *
from serverUtils.serverUtils import *
import random
import time
import copy

def CheckScreen(args):
    if not args:
        return
    dimensionId = args.get("dimensionId")
    blockPos = args.get("blockPos")
    blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
    if blockEntityData:
        blockEntityData["playerId"] = None

@Call()
def SetInventory(args):
    itemsDictMap = args.get("itemsDictMap")
    playerId = args["playerId"]
    inputItemSlot = args["inputItemSlot"]
    vesselItemSlot = args["vesselItemSlot"]
    resultItemSlot = args["resultItemSlot"]
    previewItemSlot = args["previewItemSlot"]
    if itemsDictMap:
        ServerComp.CreateItem(playerId).SetPlayerAllItems(itemsDictMap)
    for i in range(0, 6):
        if inputItemSlot[i] is None:
            inputItemSlot[i] = {}
    blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(args["dimensionId"], args["blockPos"])
    if blockEntityData:
        blockEntityData["inputItemSlot"] = inputItemSlot
        blockEntityData["vesselItemSlot"] = vesselItemSlot
        blockEntityData["resultItemSlot"] = resultItemSlot
        blockEntityData["previewItemSlot"] = previewItemSlot
        resultItem = CheckCookingPotRecipe(blockEntityData)
        if resultItem:
            blockEntityData["resultItem"] = resultItem
        else:
            CallClient("SetArrowProgress", playerId, {"timer": 10.0})
            blockEntityData["timer"] = 10.0
            blockEntityData["resultItem"] = None

        CheckCookingPotVessel(blockEntityData)

@Call()
def PlayerCloseCrabTrap(args):
    blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(args["dimensionId"], args["blockPos"])
    if blockEntityData:
        blockEntityData["playerId"] = None

@ListenServer("ServerItemUseOnEvent")
def OnServerItemUse(args):
    blockName = args["blockName"]
    if blockName == "arris:cooking_pot":
        if ServerComp.CreatePlayer(args["entityId"]).isSneaking() is False:
            args["ret"] = True

@ListenServer("ServerBlockUseEvent")
def OnServerBlockUse(args):
    blockName = args["blockName"]
    blockPos = (args["x"], args["y"], args["z"])
    dimensionId = args["dimensionId"]
    playerId = args["playerId"]
    if blockName == "arris:cooking_pot":
        blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
        if ServerComp.CreatePlayer(playerId).isSneaking() is True:
            return
        if not blockEntityData:
            return
        if blockEntityData["playerId"] is None:
            blockEntityData["playerId"] = playerId
            data = {
                "heatEnable": blockEntityData["heatEnable"],
                "inputItemSlot": blockEntityData["inputItemSlot"],
                "vesselItemSlot": blockEntityData["vesselItemSlot"],
                "resultItemSlot": blockEntityData["resultItemSlot"],
                "previewItemSlot": blockEntityData["previewItemSlot"],
                "blockPos": blockPos,
                "dimensionId": dimensionId
            }
            CallClient("CookingPotUsedEvent", playerId, data)
        else:
            CallClient("CheckPlayerScreen", playerId, {"blockPos": blockPos, "dimensionId": dimensionId}, CheckScreen)
            ServerComp.CreateGame(playerId).SetOneTipMessage(playerId, "已有玩家正在使用这个厨锅")

@ListenServer("ServerBlockEntityTickEvent")
def OnBlockEntityTick(args):
    if args["blockName"] != "arris:cooking_pot":
        return
    dimensionId = args["dimension"]
    blockPos = (args["posX"], args["posY"], args["posZ"])
    if ServerComp.CreateTime(levelId).GetTime() % 2 == 0:
        blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
        if not blockEntityData:
            return
        resultItem = CheckCookingPotRecipe(blockEntityData)
        if resultItem:
            blockEntityData["resultItem"] = resultItem
        else:
            blockEntityData["resultItem"] = None
        if blockEntityData["heatEnable"] is True and blockEntityData["resultItem"]:
            previewItemSlot = blockEntityData["previewItemSlot"]
            resultItem = blockEntityData["resultItem"]

            itemName = resultItem["newItemName"]
            auxValue = resultItem["newAuxValue"]
            basicInfo = ServerComp.CreateItem(levelId).GetItemBasicInfo(itemName, auxValue)
            maxStackSize = basicInfo["maxStackSize"]
            if previewItemSlot[0] and previewItemSlot[0].get("count") >= maxStackSize:
                return

            if not previewItemSlot[0] or resultItem["newItemName"] == previewItemSlot[0].get("newItemName"):
                inputItemSlot = blockEntityData["inputItemSlot"]
                playerId = blockEntityData["playerId"]
                blockEntityData["timer"] -= 0.1
                if blockEntityData["timer"] <= 0.1:
                    blockEntityData["timer"] = 10.0
                    for index in range(0, len(inputItemSlot)):
                        itemDict = inputItemSlot[index]
                        if itemDict != {}:
                            if itemDict["count"] <= 1:
                                itemDict = {}
                            else:
                                itemDict["count"] -= 1
                            inputItemSlot[index] = itemDict
                            blockEntityData["inputItemSlot"] = inputItemSlot
                    if not previewItemSlot[0]:
                        blockEntityData["previewItemSlot"] = [blockEntityData["resultItem"]]
                    else:
                        if not resultItem:
                            return
                        count = previewItemSlot[0]["count"] + resultItem["count"]
                        previewItemSlot[0]["count"] = count
                        blockEntityData["previewItemSlot"] = previewItemSlot
                    update = {
                        "heatEnable": blockEntityData["heatEnable"],
                        "inputItemSlot": blockEntityData["inputItemSlot"],
                        "vesselItemSlot": blockEntityData["vesselItemSlot"],
                        "resultItemSlot": blockEntityData["resultItemSlot"],
                        "previewItemSlot": blockEntityData["previewItemSlot"],
                        "blockPos": blockPos,
                        "dimensionId": dimensionId
                    }
                    CallClient("UpdateCookingPot", blockEntityData["playerId"], update)
                args["timer"] = blockEntityData["timer"]
                if playerId:
                    CallClient("SetArrowProgress", playerId, {"timer": blockEntityData["timer"]})
        else:
            blockEntityData["timer"] = 10.0

@ListenServer("ServerPlaceBlockEntityEvent")
def OnServerPlaceBlockEntity(args):
    blockName = args["blockName"]
    blockPos = (args["posX"], args["posY"], args["posZ"])
    dimensionId = args["dimension"]
    blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
    if blockName == "arris:cooking_pot":
        if blockEntityData:
            inputItem = [{} for i in range(0, 6)]
            blockEntityData["inputItemSlot"] = inputItem
            blockEntityData["vesselItemSlot"] = [None]
            blockEntityData["resultItemSlot"] = [None]
            blockEntityData["previewItemSlot"] = [None]
            blockEntityData["playerId"] = None
            blockEntityData["timer"] = 10.0
            blockEntityData["blockPos"] = blockPos
            blockEntityData["dimensionId"] = dimensionId
            blockDict = ServerComp.CreateBlockInfo(levelId).GetBlockNew((args["posX"], args["posY"] - 1, args["posZ"]), dimensionId)
            blockName = blockDict["name"]
            if blockName in ["minecraft:campfire", "minecraft:fire", "minecraft:soul_fire", "minecraft:soul_campfire", "minecraft:lava", "minecraft:flowing_lava"]:
                blockEntityData["shelfEnable"] = 1.0
            else:
                blockEntityData["shelfEnable"] = 0.0
            data = {"molang": blockEntityData["shelfEnable"], "blockPos": blockPos, "name": "variable.mod_shelf"}
            CallAllClient("SetEntityBlockMolang", data)

            if blockName in CanProvideHeatBlockList:
                blockEntityData["heatEnable"] = True
                blockEntityData["heatParticleEnable"] = 1.0
            else:
                blockEntityData["heatEnable"] = False
                blockEntityData["heatParticleEnable"] = 0.0
            data = {"molang": blockEntityData["heatParticleEnable"], "blockPos": blockPos, "name": "variable.mod_heat"}
            CallAllClient("SetEntityBlockMolang", data)

@ListenServer("BlockNeighborChangedServerEvent")
def OnBlockNeighborChanged(args):
    blockName = args["blockName"]
    blockPos = (args["posX"], args["posY"], args["posZ"])
    dimensionId = args["dimensionId"]
    neighborPos = (args["neighborPosX"], args["neighborPosY"], args["neighborPosZ"])
    if blockName == "arris:cooking_pot" and neighborPos == (args["posX"], args["posY"] - 1, args["posZ"]):
        blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
        if blockEntityData:
            neighborName = args["toBlockName"]
            if neighborName in ["minecraft:campfire", "minecraft:fire", "minecraft:soul_fire", "minecraft:soul_campfire", "minecraft:lava", "minecraft:flowing_lava"]:
                blockEntityData["shelfEnable"] = 1.0
            else:
                blockEntityData["shelfEnable"] = 0.0
            data = {"molang": blockEntityData["shelfEnable"], "blockPos": blockPos, "name": "variable.mod_shelf"}
            CallAllClient("SetEntityBlockMolang", data)

            if neighborName in CanProvideHeatBlockList:
                blockEntityData["heatEnable"] = True
                blockEntityData["heatParticleEnable"] = 1.0
            else:
                blockEntityData["heatEnable"] = False
                blockEntityData["heatParticleEnable"] = 0.0
            data = {"molang": blockEntityData["heatParticleEnable"], "blockPos": blockPos, "name": "variable.mod_heat"}
            CallAllClient("SetEntityBlockMolang", data)
            if blockEntityData["playerId"]:
                update = {
                    "heatEnable": blockEntityData["heatEnable"],
                    "inputItemSlot": blockEntityData["inputItemSlot"],
                    "vesselItemSlot": blockEntityData["vesselItemSlot"],
                    "resultItemSlot": blockEntityData["resultItemSlot"],
                    "previewItemSlot": blockEntityData["previewItemSlot"],
                    "blockPos": blockPos,
                    "dimensionId": dimensionId
                }
                CallClient("UpdateCookingPot", blockEntityData["playerId"], update)

@ListenServer("BlockRemoveServerEvent")
def OnBlockRemoveServer(args):
    blockName = args["fullName"]
    if blockName == "arris:cooking_pot":
        blockPos = (args["x"], args["y"], args["z"])
        dimensionId = args["dimension"]
        blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
        if blockEntityData:
            inputItemSlot = blockEntityData["inputItemSlot"]
            vesselItemSlot = blockEntityData["vesselItemSlot"]
            resultItemSlot = blockEntityData["resultItemSlot"]
            spawnItemPos = (args["x"] + 0.5, args["y"] + 0.5, args["z"] + 0.5)
            spawnItemList = []
            for itemDict in inputItemSlot:
                spawnItemList.append(itemDict)
            if vesselItemSlot[0]:
                spawnItemList.append(vesselItemSlot[0])
            if resultItemSlot[0]:
                spawnItemList.append(resultItemSlot[0])
            for itemDict in spawnItemList:
                ServerObj.CreateEngineItemEntity(itemDict, dimensionId, spawnItemPos)
