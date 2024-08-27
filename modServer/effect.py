# -*- coding: utf-8 -*-
from ..QingYunModLibs.ServerMod import *
from ..QingYunModLibs.SystemApi import *
from serverUtils.serverUtils import *
import random

@ListenServer("PlayerEatFoodServerEvent")
def OnPlayerEatFoodServer(args):
    playerId = args["playerId"]
    itemDict = args["itemDict"]
    itemName = itemDict["newItemName"]
    effectDictList = ServerComp.CreateEffect(playerId).GetAllEffects()
    if effectDictList:
        if itemName == "arris:milk_bottle":
            # 喝下牛奶瓶后随机清除一个效果
            index = random.randint(0, len(effectDictList) - 1)
            effectName = effectDictList[index]["effectName"]
            ServerComp.CreateEffect(playerId).RemoveEffectFromEntity(effectName)
        elif itemName == "arris:hot_cocoa":
            # 喝下热可可后随机清除一个负面效果
            for index in range(0, len(effectDictList)):
                effectName = effectDictList[index]["effectName"]
                if effectName in negativeEffect:
                    ServerComp.CreateEffect(playerId).RemoveEffectFromEntity(effectName)
                    break

@ListenServer("PlayerHungerChangeServerEvent")
def OnPlayerHungerChange(args):
    playerId = args["playerId"]
    hungerBefore = args["hungerBefore"]
    hunger = args["hunger"]
    if hunger - hungerBefore <= 0:
        effectRes = ServerComp.CreateEffect(playerId).HasEffect("arris:nourishment")
        if effectRes is True:
            args["cancel"] = True

@ListenServer("AddEffectServerEvent")
def OnAddEffectServer(args):
    entityId = args["entityId"]
    effectName = args["effectName"]
    if effectName in negativeEffect:
        effectRes = ServerComp.CreateEffect(entityId).HasEffect("arris:comfort")
        if effectRes is True:
            ServerComp.CreateEffect(entityId).RemoveEffectFromEntity(effectName)
    elif effectName == "arris:comfort":
        effectDictList = ServerComp.CreateEffect(entityId).GetAllEffects()
        for effectDict in effectDictList:
            name = effectDict["effectName"]
            if name in negativeEffect:
                ServerComp.CreateEffect(entityId).RemoveEffectFromEntity(name)

@ListenServer("PlayerDieEvent")
def OnPlayerDie(args):
    playerId = args["id"]
    for effect in ["arris:comfort", "arris:nourishment"]:
        ServerComp.CreateEffect(playerId).RemoveEffectFromEntity(effect)

@ListenServer("DamageEvent")
def OnDamage(args):
    entityId = args["entityId"]
    identifier = ServerComp.CreateEngineType(entityId).GetEngineTypeStr()
    if identifier == "minecraft:player":
        for effect in ["arris:comfort", "arris:nourishment"]:
            ServerComp.CreateEffect(entityId).RemoveEffectFromEntity(effect)
