# -*- coding: utf-8 -*-
from ..QingYunModLibs.ServerMod import *
from ..QingYunModLibs.SystemApi import *
from serverUtils.serverUtils import *
import arrisFarmersDelightScripts.modCommon.modConfig as ArrisFarmersDelight

@ListenServer("LoadServerAddonScriptsAfter")
def OnLoadServerAddonScriptsAfter(args):
    # 此事件用于为其它副包或者模组提供接口
    ServerComp.CreateModAttr("arris").SetAttr("farmersDelight", ArrisFarmersDelight, False, True)

@ListenServer("ServerBlockUseEvent")
def OnServerBlockUse(args):
    # 播放橱柜打开声音
    blockName = args["blockName"]
    blockPos = (args["x"], args["y"], args["z"])
    dimensionId = args["dimensionId"]
    if blockName in cabinetList:
        ToAllPlayerPlaySound(dimensionId, blockPos, "block.barrel.open")

@ListenServer("OnEntityInsideBlockServerEvent")
def OnEntityInsideBlockServer(args):
    # 将篮子内的掉落物吸取进篮子内
    blockName = args["blockName"]
    entityId = args["entityId"]
    if blockName == "arris:basket":
        identifier = ServerComp.CreateEngineType(entityId).GetEngineTypeStr()
        if identifier == "minecraft:item":
            itemDict = ServerComp.CreateItem(levelId).GetDroppedItem(entityId)
            blockPos = (args["blockX"], args["blockY"], args["blockZ"])
            dimensionId = ServerComp.CreateDimension(entityId).GetEntityDimensionId()
            for index in range(0, 27):
                containerItem = ServerComp.CreateItem(levelId).GetContainerItem(blockPos, index, dimensionId)
                if containerItem is None:
                    ServerComp.CreateItem(levelId).SpawnItemToContainer(itemDict, index, blockPos, dimensionId)
                    DesEntityServer(entityId)
                    break

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
    face = args["face"]
    if blockName in ["arris:cutting_board", "arris:cabbages_stage7", "arris:budding_tomatoes_stage6", "arris:tomatoes_vine_stage3"]:
        args["ret"] = True

    if itemName in WildCropDict:
        # 野生作物正确放置
        face = args["face"]
        faceDict = clickBlockFace(x, y, z)
        pos = faceDict[face]
        blockDict = ServerComp.CreateBlockInfo(levelId).GetBlockNew((pos[0], pos[1] - 1, pos[2]), dimensionId)
        blockName = blockDict["name"]
        if blockName not in WildCropDict[itemName]:
            args["ret"] = True
        if itemName == "arris:wild_rice":
            # 单独判断野生稻米的放置条件
            upBlockDict = ServerComp.CreateBlockInfo(levelId).GetBlockNew((pos[0], pos[1] + 1, pos[2]), dimensionId)
            upBlockName = upBlockDict["name"]
            if upBlockName != "minecraft:air":
                args["ret"] = True

@ListenServer("HealthChangeBeforeServerEvent")
def OnHealthChangeBefore(args):
    # 防止展示物品的实体被Kill
    entityId = args["entityId"]
    identifier = ServerComp.CreateEngineType(entityId).GetEngineTypeStr()
    if identifier == "arris:item_display":
        args["cancel"] = True

@ListenServer("WillTeleportToServerEvent")
def OnWillTeleportToServer(args):
    # 阻止展示物品的实体被传送走。
    entityId = args["entityId"]
    identifier = ServerComp.CreateEngineType(entityId).GetEngineTypeStr()
    if identifier == "arris:item_display":
        args["cancel"] = True

@ListenServer("WillAddEffectServerEvent")
def OnWillAddEffectServer(args):
    # 阻止展示物品的实体被给予药水效果。
    entityId = args["entityId"]
    identifier = ServerComp.CreateEngineType(entityId).GetEngineTypeStr()
    if identifier == "arris:item_display":
        args["cancel"] = True

@Call()
def PlayerShapedRecipe(args):
    itemDict = args["itemDict"]
    playerId = args["playerId"]
    isFullBackpack = IsFullBackpack(playerId)
    if isFullBackpack is False:
        ServerComp.CreateItem(playerId).SpawnItemToPlayerInv(itemDict, playerId)
    else:
        dimensionId = args["dimensionId"]
        playerPos = args["playerPos"]
        ServerObj.CreateEngineItemEntity(itemDict, dimensionId, playerPos)
        ServerComp.CreateGame(playerId).SetOneTipMessage(playerId, "背包已满，已生成对应掉落物在脚下")

@Call()
def GetBlockHeat(args):
    blockPos = args["blockPos"]
    dimensionId = args["dimensionId"]
    blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
    if blockEntityData:
        data = {"molang": blockEntityData["heatParticleEnable"], "blockPos": blockPos, "name": "variable.mod_heat"}
        CallAllClient("SetEntityBlockMolang", data)

@Call()
def ClientGetBlockEntityData(args):
    blockPos = args["blockPos"]
    dimensionId = args["dimensionId"]
    blockName = args["blockName"]
    blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
    if blockEntityData:
        if blockName in ["arris:skillet", "arris:cooking_pot"]:
            data = {"molang": blockEntityData["shelfEnable"], "blockPos": blockPos, "name": "variable.mod_shelf"}
            CallAllClient("SetEntityBlockMolang", data)
