# -*- coding: utf-8 -*-
from ..QingYunModLibs.ServerMod import *
from ..QingYunModLibs.SystemApi import *
from serverUtils.serverUtils import *

@ListenServer("BlockNeighborChangedServerEvent")
def OnBlockNeighborChanged(args):
    # 检测农作物周围方块变化
    blockName = args["blockName"]
    blockPos = (args["posX"], args["posY"], args["posZ"])
    dimensionId = args["dimensionId"]
    neighborPos = (args["neighborPosX"], args["neighborPosY"], args["neighborPosZ"])
    neighborName = args["toBlockName"]
    if blockName in WildCropDict:
        if neighborPos == (args["posX"], args["posY"] - 1, args["posZ"]):
            if neighborName not in WildCropDict[blockName]:
                ServerComp.CreateBlockInfo(levelId).SetBlockNew(blockPos, {"name": "minecraft:air"}, 1, dimensionId)

        toBlockName = args["toBlockName"]
        if toBlockName == "minecraft:snow_layer":
            # 当作物上方的方块变化为顶层雪时清除
            if neighborPos == (args["posX"], args["posY"] + 1, args["posZ"]):
                ServerComp.CreateBlockInfo(levelId).SetBlockNew(neighborPos, {"name": "minecraft:air"}, 0, dimensionId, False, False)

    elif blockName in cropsDict:
        if neighborPos == (args["posX"], args["posY"] - 1, args["posZ"]):
            if neighborName not in ["minecraft:farmland", "arris:rich_soil_farmland_moist", "arris:rich_soil_farmland", "minecraft:grass"]:
                ServerComp.CreateBlockInfo(levelId).SetBlockNew(blockPos, {"name": "minecraft:air"}, 1, dimensionId)

    elif blockName in "arris:rice_supporting":
        neighborName = args["toBlockName"]
        if neighborPos == (args["posX"], args["posY"] - 1, args["posZ"]):
            if neighborName not in ["minecraft:farmland", "minecraft:grass", "minecraft:dirt"]:
                ServerComp.CreateBlockInfo(levelId).SetBlockNew(blockPos, {"name": "minecraft:air"}, 1, dimensionId)
        elif neighborPos == (args["posX"], args["posY"] + 1, args["posZ"]):
            if neighborName not in ["arris:rice_upper_crop_stage0", "arris:rice_upper_crop_stage1", "arris:rice_upper_crop_stage2", "arris:rice_upper_crop_stage3"]:
                ServerComp.CreateBlockInfo(levelId).SetBlockNew(blockPos, {"name": "arris:rice_stage3"}, 0, dimensionId, False, False)

@ListenServer("BlockRandomTickServerEvent")
def OnBlockRandomTick(args):
    # 农作物自然生长以及有机肥料变为沃土
    blockName = args["fullName"]
    x, y, z = (args["posX"], args["posY"], args["posZ"])
    dimensionId = args["dimensionId"]
    comp = ServerComp.CreateBlockInfo(levelId)
    if blockName in cropsDict:
        if 9 <= args["brightness"] <= 15:
            if blockName == "arris:budding_tomatoes_stage6":
                blockDict = comp.GetBlockNew((x, y + 1, z), dimensionId)
                if blockDict["name"] == "arris:rope":
                    comp.SetBlockNew((x, y + 1, z), {"name": "arris:tomatoes_vine_stage0"}, 0, dimensionId, False, False)
            elif blockName == "arris:tomatoes_vine_stage3":
                blockDict = comp.GetBlockNew((x, y + 1, z), dimensionId)
                if blockDict["name"] == "arris:rope":
                    comp.SetBlockNew((x, y + 1, z), {"name": "arris:tomatoes_vine_stage0"}, 0, dimensionId, False, False)
            elif blockName == "arris:rice_stage3":
                blockDict = comp.GetBlockNew((x, y + 1, z), dimensionId)
                if blockDict["name"] == "minecraft:air":
                    comp.SetBlockNew((x, y, z), {"name": "arris:rice_supporting"}, 0, dimensionId, False, False)
                    comp.SetBlockNew((x, y + 1, z), {"name": "arris:rice_upper_crop_stage0"}, 0, dimensionId, False, False)
            else:
                comp.SetBlockNew((x, y, z), {"name": cropsDict[blockName]}, 0, dimensionId, False, False)

    if blockName == "arris:rich_soil_farmland":
        PosList = [(x + testX, y, z + testZ) for testX in xrange(-4, 5) for testZ in xrange(-4, 5)]
        PosList.remove((x, y, z))
        blockList = []
        for pos in PosList:
            blockDict = comp.GetBlockNew(pos, dimensionId)
            blockList.append(blockDict["name"])
        if "minecraft:water" in blockList or "minecraft:flowing_water" in blockList:
            comp.SetBlockNew((x, y, z), {"name": "arris:rich_soil_farmland_moist"}, 0, dimensionId, False, False)

    elif blockName == "arris:rich_soil_farmland_moist":
        PosList = [(x + testX, y, z + testZ) for testX in xrange(-4, 5) for testZ in xrange(-4, 5)]
        PosList.remove((x, y, z))
        blockList = []
        for pos in PosList:
            blockDict = comp.GetBlockNew(pos, dimensionId)
            blockList.append(blockDict["name"])
        if "minecraft:water" in blockList or "minecraft:flowing_water" in blockList:
            pass
        else:
            comp.SetBlockNew((x, y, z), {"name": "arris:rich_soil_farmland"}, 0, dimensionId, False, False)

        upBlock = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x, y + 1, z), dimensionId)
        data = {
            "blockName": upBlock["name"],
            "playerId": None,
            "itemDict": None,
            "dimensionId": dimensionId,
            "blockPos": (x, y + 1, z)
        }
        if upBlock["name"] in cropsDict:
            CropAccelerateTheRipening(data, "rich_soil_farmland")

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
    if itemName == "arris:rice":
        if blockName in ["minecraft:dirt", "minecraft:grass", "arris:rich_soil"] and face == 1:
            upBlock = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x, y + 1, z), dimensionId)
            if upBlock["name"] == "minecraft:water":
                SetNotCreateItem(playerId, itemDict)
                ToAllPlayerPlaySound(dimensionId, (x + 0.5, y + 1, z + 0.5), "dig.grass")
                ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y + 1, z), {"name": "arris:rice_stage0"}, 0, dimensionId, False, False)
            else:
                ServerComp.CreateGame(playerId).SetOneTipMessage(playerId, "水稻需要种植在静止的水中")
        else:
            ServerComp.CreateGame(playerId).SetOneTipMessage(playerId, "水稻貌似无法种植在这个方块上...")

    elif itemName == "minecraft:bone_meal":
        data = {
            "blockName": blockName,
            "playerId": playerId,
            "itemDict": itemDict,
            "dimensionId": dimensionId,
            "blockPos": (x, y, z)
        }
        if blockName in cropsDict:
            CropAccelerateTheRipening(data)

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
    itemName = itemDict["newItemName"]
    itemType = GetItemType(itemDict)
    if blockName == "arris:rich_soil":
        if itemType == "hoe":
            SetCarriedDurability(playerId, itemDict, dimensionId, (x, y, z))
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": "arris:rich_soil_farmland"}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x, y, z), "use.gravel")

    elif blockName == "arris:rich_soil_farmland_moist" or blockName == "arris:rich_soil_farmland":
        upBlock = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x, y + 1, z), dimensionId)
        if upBlock["name"] == "minecraft:air":
            if face == 1:
                seedsDict = {
                    "minecraft:wheat_seeds": "arris:rich_soil_wheat0",
                    "minecraft:beetroot_seeds": "arris:rich_soil_beetroot0",
                    "minecraft:potato": "arris:rich_soil_potatoes0",
                    "minecraft:carrot": "arris:rich_soil_carrots0",
                    "minecraft:torchflower_seeds": "arris:rich_soil_torchflower0",
                }
                if itemName in seedsDict:
                    ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y + 1, z), {"name": seedsDict[itemName]}, 0, dimensionId, False, False)
                    ToAllPlayerPlaySound(dimensionId, (x + 0.5, y + 1, z + 0.5), "dig.grass")
                    SetNotCreateItem(playerId, itemDict)

@ListenServer("ServerBlockUseEvent")
def OnServerBlockUse(args):
    # 成熟作物采摘
    blockName = args["blockName"]
    x = args["x"]
    y = args["y"]
    z = args["z"]
    dimensionId = args["dimensionId"]
    playerId = args["playerId"]
    carriedDict = ServerComp.CreateItem(playerId).GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, 0)
    if blockName == "arris:budding_tomatoes_stage6":
        blockPos = (x + 0.5, y, z + 0.5)
        if carriedDict is None:
            carriedDict = {}
        itemName = carriedDict.get("newItemName")
        if itemName == "minecraft:bone_meal":
            blockDict = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x, y + 1, z), dimensionId)
            if blockDict["name"] == "arris:rope":
                ToAllPlayerPlaySound(dimensionId, (x + 0.5, y + 1, z + 0.5), "item.bone_meal.use")
                CallAllClient("PlayParticle", (x + 0.5, y + 1, z + 0.5))
        else:
            count = random.randint(1, 2)
            ServerObj.CreateEngineItemEntity({"itemName": "arris:tomato", "count": count}, dimensionId, blockPos)
            ToAllPlayerPlaySound(dimensionId, blockPos, "block.sweet_berry_bush.pick")
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": "arris:budding_tomatoes_stage3"}, 0, dimensionId, False, False)
        args["ret"] = True

    elif blockName == "arris:tomatoes_vine_stage3":
        blockPos = (x + 0.5, y, z + 0.5)
        if carriedDict is None:
            carriedDict = {}
        itemName = carriedDict.get("newItemName")
        if itemName == "minecraft:bone_meal":
            blockDict = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x, y + 1, z), dimensionId)
            if blockDict["name"] == "arris:rope":
                ToAllPlayerPlaySound(dimensionId, (x + 0.5, y + 1, z + 0.5), "item.bone_meal.use")
                CallAllClient("PlayParticle", (x + 0.5, y + 1, z + 0.5))
                ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y + 1, z), {"name": "arris:tomatoes_vine_stage0"}, 0, dimensionId, False, False)
        else:
            count = random.randint(1, 2)
            ServerObj.CreateEngineItemEntity({"itemName": "arris:tomato", "count": count}, dimensionId, blockPos)
            ToAllPlayerPlaySound(dimensionId, blockPos, "block.sweet_berry_bush.pick")
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": "arris:tomatoes_vine_stage0"}, 0, dimensionId, False, False)
        args["ret"] = True

    elif blockName == "arris:cabbages_stage7":
        blockPos = (x + 0.5, y, z + 0.5)
        count = random.randint(1, 2)
        ServerObj.CreateEngineItemEntity({"itemName": "arris:cabbage_leaf", "count": count}, dimensionId, blockPos)
        ToAllPlayerPlaySound(dimensionId, blockPos, "block.sweet_berry_bush.pick")
        ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": "arris:cabbages_stage3"}, 0, dimensionId, False, False)
        args["ret"] = True

    elif blockName == "arris:rice_stage3":
        if carriedDict is None:
            return
        itemName = carriedDict.get("newItemName")
        if itemName == "minecraft:bone_meal":
            blockDict = ServerComp.CreateBlockInfo(levelId).GetBlockNew((x, y + 1, z), dimensionId)
            if blockDict["name"] == "minecraft:air":
                ToAllPlayerPlaySound(dimensionId, (x + 0.5, y + 1, z + 0.5), "item.bone_meal.use")
                CallAllClient("PlayParticle", (x + 0.5, y + 1, z + 0.5))
                ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y + 1, z), {"name": "arris:rice_upper_crop_stage0"}, 0, dimensionId, False, False)

@ListenServer("ServerBlockEntityTickEvent")
def OnServerBlockEntityTick(args):
    # 自定义方块实体Tick触发
    blockName = args["blockName"]
    dimensionId = args["dimension"]
    blockPos = (args["posX"], args["posY"], args["posZ"])
    blockEntityData = ServerComp.CreateBlockEntityData(levelId).GetBlockEntityData(dimensionId, blockPos)
    if blockName in WildCropDict:
        if blockEntityData:
            if blockEntityData["initSnowClean"] is None:
                upBlockPos = (args["posX"], args["posY"] + 1, args["posZ"])
                data = {"blockEntityData": blockEntityData, "blockPos": upBlockPos, "dimensionId": dimensionId}
                InitSnowClean(data)

            if blockName == "arris:wild_rice":
                if blockEntityData["initFloodClean"] is None:
                    upBlockPos = (args["posX"], args["posY"] + 1, args["posZ"])
                    data = {"blockEntityData": blockEntityData, "blockPos": upBlockPos, "dimensionId": dimensionId}
                    InitFloodClean(data)

def CropAccelerateTheRipening(data, mode=None):
    # 作物催熟
    blockName = data["blockName"]
    playerId = data["playerId"]
    itemDict = data["itemDict"]
    dimensionId = data["dimensionId"]
    x, y, z = data["blockPos"]
    stage = int(blockName[-1])
    num = random.randint(2, 3)
    if mode == "rich_soil_farmland":
        num = 1
    if playerId:
        SetNotCreateItem(playerId, itemDict)

    if blockName[:-1] == "arris:cabbages_stage":
        if stage < 7:
            stage += num
            if stage > 7:
                stage = 7
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:budding_tomatoes_stage":
        if stage < 6:
            stage += num
            if stage >= 6:
                stage = 6
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:tomatoes_vine_stage":
        if stage < 3:
            stage += num
            if stage >= 3:
                stage = 3
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:onions_stage":
        if stage < 3:
            stage += num
            if stage >= 3:
                stage = 3
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:rich_soil_wheat":
        if stage < 7:
            stage += num
            if stage >= 7:
                stage = 7
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:rich_soil_beetroot":
        if stage < 3:
            stage += num
            if stage >= 3:
                stage = 3
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:rich_soil_carrots":
        if stage < 3:
            stage += num
            if stage >= 3:
                stage = 3
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:rich_soil_potatoes":
        if stage < 3:
            stage += num
            if stage >= 3:
                stage = 3
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:rice_stage":
        if stage < 3:
            stage += num
            if stage >= 3:
                stage = 3
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:rice_upper_crop_stage":
        if stage < 3:
            stage += num
            if stage >= 3:
                stage = 3
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))

    elif blockName[:-1] == "arris:rich_soil_torchflower":
        if stage < 2:
            stage += num
            if stage >= 2:
                stage = 2
            blockName = blockName[:-1] + str(stage)
            ServerComp.CreateBlockInfo(levelId).SetBlockNew((x, y, z), {"name": blockName}, 0, dimensionId, False, False)
            ToAllPlayerPlaySound(dimensionId, (x + 0.5, y, z + 0.5), "item.bone_meal.use")
            CallAllClient("PlayParticle", (x + 0.5, y, z + 0.5))