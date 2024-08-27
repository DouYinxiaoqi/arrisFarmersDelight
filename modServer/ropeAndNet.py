# -*- coding: utf-8 -*-
from ..QingYunModLibs.ServerMod import *
from ..QingYunModLibs.SystemApi import *
from serverUtils.serverUtils import *
import random

@Call()
def SetPlayerIsJumpExtra(data):
    playerId = data["playerId"]
    isJump = data["isJump"]
    ServerComp.CreateExtraData(playerId).SetExtraData("isJump", isJump)

@ListenServer("OnEntityInsideBlockServerEvent")
def OnEntityInsideBlockServer(args):
    # 攀爬绳子
    blockName = args["blockName"]
    entityId = args["entityId"]
    if blockName in canClimbList:
        isJump = ServerComp.CreateExtraData(entityId).GetExtraData("isJump")
        if isJump is True:
            ServerComp.CreateActorMotion(entityId).SetPlayerMotion((0, 0.15, 0))
        else:
            isFly = ServerComp.CreateFly(entityId).IsPlayerFlying()
            if isFly is False:
                ServerComp.CreateActorMotion(entityId).SetPlayerMotion((0, -0.15, 0))

@ListenServer("MobGriefingBlockServerEvent")
def OnMobGriefingBlock(args):
    # 取消玩家在攀爬绳子掉落时，踩坏耕地
    entityId = args["entityId"]
    blockName = args["blockName"]
    if blockName == "minecraft:farmland":
        dimensionId = args["dimensionId"]
        x, y, z = ServerComp.CreatePos(entityId).GetPos()
        upBlockName = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x // 1, (y // 1), z // 1), dimensionId)["name"]
        if upBlockName in canClimbList:
            args["cancel"] = True

@ListenServer("OnBeforeFallOnBlockServerEvent")
def OnBeforeFallOnBlock(args):
    # 将掉落在安全网上的实体弹起来，并取消伤害
    entityId = args["entityId"]
    blockName = args["blockName"]
    if blockName == "arris:safety_net":
        fallDistance = args["fallDistance"]
        entityName = ServerComp.CreateEngineType(entityId).GetEngineTypeStr()
        if entityName == "minecraft:player":
            isSneaking = serverApi.GetEngineCompFactory().CreatePlayer(entityId).isSneaking()
            if isSneaking is False and fallDistance > 0.5:
                if fallDistance <= 10:
                    fallDistance *= 0.1
                elif 10 < fallDistance <= 50:
                    fallDistance *= 0.05
                else:
                    fallDistance *= 0.01
                ServerComp.CreateActorMotion(entityId).SetPlayerMotion((0, fallDistance, 0))
                args["cancel"] = True
        else:
            if fallDistance > 0.5:
                if fallDistance <= 10:
                    fallDistance *= 0.1
                elif 10 < fallDistance <= 50:
                    fallDistance *= 0.05
                else:
                    fallDistance *= 0.01
                ServerComp.CreateActorMotion(entityId).SetMotion((0, fallDistance, 0))
                args["cancel"] = True

@ListenServer("ServerBlockUseEvent")
def OnServerBlockUse(args):
    blockName = args["blockName"]
    x = args["x"]
    y = args["y"]
    z = args["z"]
    dimensionId = args["dimensionId"]
    if blockName == "arris:rope":
        # 通过绳子连接的钟可以敲响
        blockList = []
        for i in range(y, y + 25):
            blockDict = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x, i, z), dimensionId)
            blockList.append(blockDict["name"])
        if "minecraft:bell" in blockList:
            index = blockList.index("minecraft:bell")
            blockList = blockList[0:index + 1]
            count = blockList.count("arris:rope")
            length = len(blockList) - 1
            if count == length:
                ServerObj.CreateEngineEntityByTypeStr("arris:toll_entity", (x + 0.5, y + index + 0.6, z + 0.5), (0, 0), dimensionId)

@ListenServer("DamageEvent")
def OnDamage(args):
    # 取消玩家在攀爬绳子时的掉落伤害
    entityId = args["entityId"]
    identifier = ServerComp.CreateEngineType(entityId).GetEngineTypeStr()
    if identifier == "minecraft:player":
        if args["cause"] == "fall":
            x, y, z = ServerComp.CreatePos(entityId).GetPos()
            dimensionId = ServerComp.CreateDimension(entityId).GetEntityDimensionId()
            blockName = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x // 1, (y // 1), z // 1), dimensionId)["name"]
            if blockName in canClimbList:
                args["damage"] = 0
