# -*- coding: utf-8 -*-
from ..QingYunModLibs.ServerMod import *
from ..QingYunModLibs.SystemApi import *
from serverUtils.serverUtils import *

@ListenServer("ItemUseOnAfterServerEvent")
def OnItemUseOnAfter(args):
    # 玩家在对方块使用物品之后服务端抛出的事件
    playerId = args["entityId"]
    itemDict = args["itemDict"]
    dimensionId = args["dimensionId"]
    x = args["x"]
    y = args["y"]
    z = args["z"]
    face = args["face"]
    blockName = args["blockName"]
    placePos = clickBlockFace(x, y, z)
    setPos = placePos[face]
    itemName = itemDict["newItemName"]
    if itemName == "arris:skillet_item" and blockName not in ["minecraft:frame", "minecraft:glow_frame", "arris:cutting_board"]:
        pX, pY, pZ = ServerComp.CreatePos(playerId).GetFootPos()
        aux = DetectionExperimentalHoliday()
        blockAux = aux.get(FromAngleGetBlockAux(x, z, pX, pZ), FromAngleGetBlockAux(x, z, pX, pZ))
        blockDict = {"name": itemChangeBlockDict[itemName]}
        placeBlock = ServerComp.CreateBlockInfo(levelId).GetBlockNew(setPos, dimensionId)["name"]
        if placeBlock == "minecraft:air":
            SetNotCreateItem(playerId, itemDict)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew(setPos, blockDict, 0, dimensionId)
            blockStates = ServerComp.CreateBlockState(levelId).GetBlockStates(setPos, dimensionId)
            if blockStates:
                blockStates["direction"] = blockAux
                ServerComp.CreateBlockState(levelId).SetBlockStates(setPos, blockStates, dimensionId)
            blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, setPos)
            if blockEntityData:
                ToAllPlayerPlaySound(dimensionId, setPos, "dig.stone")

@ListenServer("ServerItemUseOnEvent")
def OnServerItemUse(args):
    # 玩家在对方块使用物品之前服务端抛出的事件
    itemDict = args["itemDict"]
    itemName = itemDict["newItemName"]
    dimensionId = args["dimensionId"]
    x = args["x"]
    y = args["y"]
    z = args["z"]
    playerId = args["entityId"]
    blockName = args["blockName"]
    if blockName == "arris:skillet":
        blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, (x, y, z))
        if blockEntityData:
            if itemDict["newItemName"] in CanCookedFoodDict:
                print(itemDict)
                # data = {"blockEntityData": blockEntityData, "blockPos": (x, y, z), "dimensionId": dimensionId}
                # SetItemDisplay(itemDict, playerId, data, 4)
                downBlockName = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x, y - 1, z), dimensionId)["name"]
                if downBlockName in CanProvideHeatBlockList:
                    ToAllPlayerPlaySound(dimensionId, (x, y, z), "ambient.skillet.addfood")
                else:
                    ToAllPlayerPlaySound(dimensionId, (x, y, z), "armor.equip_leather")
            else:
                if itemName in ["arris:spatula", "arris:cutting_board", "arris:cooking_pot", "arris:skillet_item"]:
                    args["ret"] = True
                else:
                    ServerComp.CreateGame(playerId).SetOneTipMessage(playerId, "这个貌似不可以进行烹饪...")

@ListenServer("BlockNeighborChangedServerEvent")
def OnBlockNeighborChanged(args):
    blockName = args["blockName"]
    blockPos = (args["posX"], args["posY"], args["posZ"])
    dimensionId = args["dimensionId"]
    neighborPos = (args["neighborPosX"], args["neighborPosY"], args["neighborPosZ"])
    if blockName == "arris:skillet" and neighborPos == (args["posX"], args["posY"] - 1, args["posZ"]):
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

@ListenServer("ServerPlaceBlockEntityEvent")
def OnServerPlaceBlockEntity(args):
    blockName = args["blockName"]
    blockPos = (args["posX"], args["posY"], args["posZ"])
    dimensionId = args["dimension"]
    blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
    if blockName == "arris:skillet":
        if blockEntityData:
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

