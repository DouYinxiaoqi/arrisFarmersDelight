# -*- coding: utf-8 -*-
from ..QingYunModLibs.ServerMod import *
from ..QingYunModLibs.SystemApi import *
from ..modCommon.modConfig import *
from serverUtils.serverUtils import *

@ListenServer("ServerBlockUseEvent")
def OnServerBlockUse(args):
    blockName = args["blockName"]
    x = args["x"]
    y = args["y"]
    z = args["z"]
    blockPos = (args["x"], args["y"], args["z"])
    dimensionId = args["dimensionId"]
    playerId = args["playerId"]
    if blockName in platePackagedFoodDict:
        handItemDict = ServerComp.CreateItem(playerId).GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, 0)
        if handItemDict is None:
            handItemDict = {}
        itemName = handItemDict.get("newItemName")
        packagedFoodDict = platePackagedFoodDict[blockName]
        name = packagedFoodDict.get("target")
        item = packagedFoodDict.get("item")
        aux = DetectionExperimentalHoliday()
        blockAux = aux.get(args["aux"], args["aux"])
        if name is not None:
            itemDict = {
                "itemName": item,
                "count": 1
            }
            if blockName[0:28] == "arris:rice_roll_medley_block":
                ServerComp.CreateBlockInfo(levelId).SetBlockNew(blockPos, {"name": name}, 0, dimensionId)
                blockStates = ServerComp.CreateBlockState(levelId).GetBlockStates(blockPos, dimensionId)
                if blockStates:
                    blockStates["direction"] = blockAux
                    ServerComp.CreateBlockState(levelId).SetBlockStates(blockPos, blockStates, dimensionId)
                ToAllPlayerPlaySound(dimensionId, (x, y, z), "armor.equip_leather")
                ServerComp.CreateItem(playerId).SpawnItemToPlayerInv(itemDict, playerId)
            elif itemName == "minecraft:bowl":
                ServerComp.CreateBlockInfo(levelId).SetBlockNew(blockPos, {"name": name}, 0, dimensionId)
                blockStates = ServerComp.CreateBlockState(levelId).GetBlockStates(blockPos, dimensionId)
                if blockStates:
                    blockStates["direction"] = blockAux
                    ServerComp.CreateBlockState(levelId).SetBlockStates(blockPos, blockStates, dimensionId)
                ToAllPlayerPlaySound(dimensionId, (x, y, z), "armor.equip_leather")
                SetNotCreateItem(playerId, handItemDict)
                ServerComp.CreateItem(playerId).SpawnItemToPlayerInv(itemDict, playerId)
            else:
                ServerComp.CreateGame(playerId).SetOneTipMessage(playerId, "你需要一个碗来食用它")
        else:
            ServerComp.CreateBlockInfo(levelId).SetBlockNew(blockPos, {"name": "minecraft:air"}, 1, dimensionId)
