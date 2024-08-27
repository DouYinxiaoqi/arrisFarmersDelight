import mod.server.extraServerApi as serverApi
levelId = serverApi.GetLevelId()


class Map:

	@staticmethod
	def CanSee(fromId, targetId, viewRange, onlySolid, angleX, angleY):
		comp = serverApi.GetEngineCompFactory().CreateGame(fromId)
		return comp.CanSee(fromId, targetId, viewRange, onlySolid, angleX, angleY)

	@staticmethod
	def CheckBlockToPos(fromPos, toPos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.CheckBlockToPos(fromPos, toPos, dimensionId)

	@staticmethod
	def CheckChunkState(dimension, pos):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.CheckChunkState(dimension, pos)

	@staticmethod
	def CreateDimension(dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
		return comp.CreateDimension(dimensionId)

	@staticmethod
	def CreateExplosion(pos, radius, fire, breaks, sourceId, playerId):
		comp = serverApi.GetEngineCompFactory().CreateExplosion(levelId)
		return comp.CreateExplosion(pos, radius, fire, breaks, sourceId, playerId)

	@staticmethod
	def DeleteAllArea():
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.DeleteAllArea()

	@staticmethod
	def DeleteArea(key):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.DeleteArea(key)

	@staticmethod
	def DetectStructure(pattern, defines, touchPos, pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreatePortal(levelId)
		return comp.DetectStructure(None, pattern, defines, touchPos, pos, dimensionId)

	@staticmethod
	def DoTaskOnChunkAsync(dimensionId, posMin, posMax, callback):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.DoTaskOnChunkAsync(dimensionId, posMin, posMax, callback)

	@staticmethod
	def GetAllAreaKeys():
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.GetAllAreaKeys()

	@staticmethod
	def GetBiomeName(pos, dimId):
		comp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
		return comp.GetBiomeName(pos, dimId)

	@staticmethod
	def GetBlockLightLevel(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlockLightLevel(pos, dimensionId)

	@staticmethod
	def GetChunkEntites(dimension, pos):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.GetChunkEntites(dimension, pos)

	@staticmethod
	def GetChunkMaxPos(chunkPos):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.GetChunkMaxPos(chunkPos)

	@staticmethod
	def GetChunkMinPos(chunkPos):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.GetChunkMinPos(chunkPos)

	@staticmethod
	def GetChunkMobNum(dimension, chunkPos):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.GetChunkMobNum(dimension, chunkPos)

	@staticmethod
	def GetChunkPosFromBlockPos(blockPos):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.GetChunkPosFromBlockPos(blockPos)

	@staticmethod
	def GetEntitiesAround(entityId, radius, filters):
		comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
		return comp.GetEntitiesAround(entityId, radius, filters)

	@staticmethod
	def GetEntitiesAroundByType(entityId, radius, entityType):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetEntitiesAroundByType(entityId, radius, entityType)

	@staticmethod
	def GetEntitiesInSquareArea(entityId, startPos, endPos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetEntitiesInSquareArea(entityId, startPos, endPos, dimensionId)

	@staticmethod
	def GetLevelId():
		return serverApi.GetLevelId()

	@staticmethod
	def GetLoadedChunks(dimension):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.GetLoadedChunks(dimension)

	@staticmethod
	def GetSpawnDimension():
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.GetSpawnDimension()

	@staticmethod
	def GetSpawnPosition():
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.GetSpawnPosition()

	@staticmethod
	def GetStructureSize(structureName):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetStructureSize(structureName)

	@staticmethod
	def IsChunkGenerated(dimensionId, chunkPos):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.IsChunkGenerated(dimensionId, chunkPos)

	@staticmethod
	def IsSlimeChunk(dimensionId, chunkPos):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.IsSlimeChunk(dimensionId, chunkPos)

	@staticmethod
	def LocateNeteaseFeatureRule(ruleName, dimensionId, pos):
		comp = serverApi.GetEngineCompFactory().CreateFeature(levelId)
		return comp.LocateNeteaseFeatureRule(ruleName, dimensionId, pos)

	@staticmethod
	def LocateStructureFeature(featureType, dimensionId, pos):
		comp = serverApi.GetEngineCompFactory().CreateFeature(levelId)
		return comp.LocateStructureFeature(featureType, dimensionId, pos)

	@staticmethod
	def MayPlace(identifier, blockPos, facing, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.MayPlace(identifier, blockPos, facing, dimensionId)

	@staticmethod
	def MayPlaceOn(playerId, identifier, auxValue, blockPos, facing):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.MayPlaceOn(identifier, auxValue, blockPos, facing)

	@staticmethod
	def MirrorDimension(fromId, toId):
		comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
		return comp.MirrorDimension(fromId, toId)

	@staticmethod
	def OpenClientChunkGeneration(val):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.OpenClientChunkGeneration(val)

	@staticmethod
	def PlaceFeature(featureName, dimensionId, pos):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.PlaceFeature(featureName, dimensionId, pos)

	@staticmethod
	def PlaceNeteaseLargeFeature(poolName, dimensionId, pos, rotation, maxDepth):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.PlaceNeteaseLargeFeature(poolName, dimensionId, pos, rotation, maxDepth)

	@staticmethod
	def PlaceStructure(playerId, pos, structureName, dimensionId, rotation):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.PlaceStructure(playerId, pos, structureName, dimensionId, rotation)

	@staticmethod
	def SetAddArea(key, dimensionId, minPos, maxPos):
		comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.SetAddArea(key, dimensionId, minPos, maxPos)

	@staticmethod
	def SetMergeSpawnItemRadius(radius):
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.SetMergeSpawnItemRadius(radius)

	@staticmethod
	def SetSpawnDimensionAndPosition(dimensionId, pos):
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.SetSpawnDimensionAndPosition(dimensionId, pos)

	@staticmethod
	def UpgradeMapDimensionVersion(dimension, version):
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.UpgradeMapDimensionVersion(dimension, version)


class Entity:
	@staticmethod
	def CreateExperienceOrb(entityId, exp, position, isSpecial):
		comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
		return comp.CreateExperienceOrb(exp, position, isSpecial)

	@staticmethod
	def CreateProjectileEntity(spawnerId, entityIdentifier, param):
		comp = serverApi.GetEngineCompFactory().CreateProjectile(levelId)
		return comp.CreateProjectileEntity(spawnerId, entityIdentifier, param)

	@staticmethod
	def GetDroppedItem(itemEntityId, getUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetDroppedItem(itemEntityId, getUserData)

	@staticmethod
	def GetEngineActor():
		return serverApi.GetEngineActor()

	@staticmethod
	def GetPlayerList():
		return serverApi.GetPlayerList()


	@staticmethod
	def IsEntityAlive(entityId):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.IsEntityAlive(entityId)

	@staticmethod
	def KillEntity(entityId):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.KillEntity(entityId)

	@staticmethod
	def SpawnItemToLevel(itemDict, dimensionId, pos):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.SpawnItemToLevel(itemDict, dimensionId, pos)

	@staticmethod
	def SpawnLootTable(pos, identifier, playerKillerId, damageCauseEntityId):
		comp = serverApi.GetEngineCompFactory().CreateActorLoot(playerKillerId)
		return comp.SpawnLootTable(pos, identifier, playerKillerId, damageCauseEntityId)

	@staticmethod
	def SpawnLootTableWithActor(pos, entityId, playerKillerId, damageCauseEntityId):
		comp = serverApi.GetEngineCompFactory().CreateActorLoot(entityId)
		return comp.SpawnLootTableWithActor(pos, entityId, playerKillerId, damageCauseEntityId)

	@staticmethod
	def SpawnResources(identifier, pos, aux, probability, bonusLootLevel, dimensionId, allowRandomness):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SpawnResources(identifier, pos, aux, probability, bonusLootLevel, dimensionId, allowRandomness)

	@staticmethod
	def SpawnResourcesSilkTouched(identifier, pos, aux, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SpawnResourcesSilkTouched(identifier, pos, aux, dimensionId)


class Block:

	@staticmethod
	def GetBlockClip(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlockClip(pos, dimensionId)

	@staticmethod
	def GetBlockCollision(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlockCollision(pos, dimensionId)

	@staticmethod
	def GetBlockNew(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlockNew(pos, dimensionId)

	@staticmethod
	def GetDestroyTotalTime(blockName, itemName):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetDestroyTotalTime(blockName, itemName)

	@staticmethod
	def GetLiquidBlock(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetLiquidBlock(pos, dimensionId)

	@staticmethod
	def GetTopBlockHeight(pos, dimension):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetTopBlockHeight(pos, dimension)

	@staticmethod
	def SetBlockNew(pos, blockDict, oldBlockHandling, dimensionId, isLegacy):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetBlockNew(pos, blockDict, oldBlockHandling, dimensionId, isLegacy)

	@staticmethod
	def SetJigsawBlock(pos, blockDict, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetJigsawBlock(pos, blockDict, dimensionId)

	@staticmethod
	def SetLiquidBlock(pos, blockDict, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetLiquidBlock(pos, blockDict, dimensionId)

	@staticmethod
	def SetSnowBlock(pos, dimensionId, height):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetSnowBlock(pos, dimensionId, height)


class Spawn:

	@staticmethod
	def GetEntityLimit():
		return serverApi.GetEntityLimit()


	@staticmethod
	def SetEntityLimit(num):
		return serverApi.SetEntityLimit(num)

	@staticmethod
	def SpawnCustomModule(biomeType, change, entityType, probability, minCount, maxCount, environment, minBrightness, maxBrightness, minHeight, maxHeight):
		comp = serverApi.GetEngineCompFactory().CreateMobSpawn(levelId)
		return comp.SpawnCustomModule(biomeType, change, entityType, probability, minCount, maxCount, environment, minBrightness, maxBrightness, minHeight, maxHeight)


class Recipes:

	@staticmethod
	def AddBrewingRecipes(brewType, inputName, reagentName, outputName):
		comp = serverApi.GetEngineCompFactory().CreateRecipe(levelId)
		return comp.AddBrewingRecipes(brewType, inputName, reagentName, outputName)


	@staticmethod
	def GetRecipeResult(recipeId):
		comp = serverApi.GetEngineCompFactory().CreateRecipe(levelId)
		return comp.GetRecipeResult(recipeId)

	@staticmethod
	def GetRecipesByInput(inputIdentifier, tag, aux, maxResultNum):
		comp = serverApi.GetEngineCompFactory().CreateRecipe(levelId)
		return comp.GetRecipesByInput(inputIdentifier, tag, aux, maxResultNum)


	@staticmethod
	def GetRecipesByResult(resultIdentifier, tag, aux, maxResultNum):
		comp = serverApi.GetEngineCompFactory().CreateRecipe(levelId)
		return comp.GetRecipesByResult(resultIdentifier, tag, aux, maxResultNum)


class BlockPalette:

	@staticmethod
	def CreateMicroBlockResStr(identifier, start, end, colorMap, isMerge, icon):
		comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
		return comp.CreateMicroBlockResStr(identifier, start, end, colorMap=colorMap, isMerge=isMerge, icon=icon)

	@staticmethod
	def GetBlankBlockPalette():
		comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
		return comp.GetBlankBlockPalette()

	@staticmethod
	def GetBlockPaletteBetweenPos(dimensionId, startBlockPos, endBlockPos, eliminateAir):
		comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
		return comp.GetBlockPaletteBetweenPos(dimensionId, startBlockPos, endBlockPos, eliminateAir)

	@staticmethod
	def GetBlockPaletteFromPosList(dimensionId, posList):
		comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
		return comp.GetBlockPaletteFromPosList(dimensionId, posList)


	@staticmethod
	def RegisterBlockPatterns(pattern, defines, result_actor_name):
		comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
		return comp.RegisterBlockPatterns(pattern,defines,result_actor_name)

	@staticmethod
	def SetBlockByBlockPalette(blockPalette, dimensionId, pos, rotation, conflictMode):
		comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
		return comp.SetBlockByBlockPalette(blockPalette, dimensionId, pos, rotation, conflictMode)


class Time:

	@staticmethod
	def GetLocalDoDayNightCycle(dimension):
		comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
		return comp.GetLocalDoDayNightCycle(dimension)

	@staticmethod
	def GetLocalTime(dimension):
		comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
		return comp.GetLocalTime(dimension)

	@staticmethod
	def GetTime():
		comp = serverApi.GetEngineCompFactory().CreateTime(levelId)
		return comp.GetTime()

	@staticmethod
	def GetUseLocalTime(dimension):
		comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
		return comp.GetUseLocalTime(dimension)

	@staticmethod
	def SetLocalDoDayNightCycle(dimension, value):
		comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
		return comp.SetLocalDoDayNightCycle(dimension, value)

	@staticmethod
	def SetLocalTime(dimension, time):
		comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
		return comp.SetLocalTime(dimension, time)

	@staticmethod
	def SetLocalTimeOfDay(dimension, timeOfDay):
		comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
		return comp.SetLocalTimeOfDay(dimension, timeOfDay)

	@staticmethod
	def SetTime(time):
		comp = serverApi.GetEngineCompFactory().CreateTime(levelId)
		return comp.SetTime(time)

	@staticmethod
	def SetTimeOfDay(timeOfDay):
		comp = serverApi.GetEngineCompFactory().CreateTime(levelId)
		return comp.SetTimeOfDay(timeOfDay)

	@staticmethod
	def SetUseLocalTime(dimension, value):
		comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
		return comp.SetUseLocalTime(dimension, value)


class Weather:

	@staticmethod
	def GetDimensionLocalWeatherInfo(dimension):
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.GetDimensionLocalWeatherInfo(dimension)

	@staticmethod
	def GetDimensionUseLocalWeather(dimension):
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.GetDimensionUseLocalWeather(dimension)

	@staticmethod
	def IsRaining():
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.IsRaining()

	@staticmethod
	def IsThunder():
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.IsThunder()

	@staticmethod
	def SetDimensionLocalDoWeatherCycle(dimension, value):
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.SetDimensionLocalDoWeatherCycle(dimension, value)

	@staticmethod
	def SetDimensionLocalRain(dimension, rainLevel, rainTime):
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.SetDimensionLocalRain(dimension, rainLevel, rainTime)

	@staticmethod
	def SetDimensionLocalThunder(dimension, thunderLevel, thunderTime):
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.SetDimensionLocalThunder(dimension, thunderLevel, thunderTime)

	@staticmethod
	def SetDimensionUseLocalWeather(dimension, value):
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.SetDimensionUseLocalWeather(dimension, value)

	@staticmethod
	def SetRaining(level, time):
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.SetRaining(level, time)

	@staticmethod
	def SetThunder(level, time):
		comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
		return comp.SetThunder(level, time)


class GameRule:

	@staticmethod
	def AddBannedItem(itemName):
		comp = serverApi.GetEngineCompFactory().CreateItemBanned(levelId)
		return comp.AddBannedItem(itemName)

	@staticmethod
	def AddBlockProtectField(dimensionId, startPos, endPos):
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.AddBlockProtectField(dimensionId, startPos, endPos)

	@staticmethod
	def CleanBlockProtectField():
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.CleanBlockProtectField()

	@staticmethod
	def ClearBannedItems():
		comp = serverApi.GetEngineCompFactory().CreateItemBanned(levelId)
		return comp.ClearBannedItems()

	@staticmethod
	def DisableVineBlockSpread(disable):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.DisableVineBlockSpread(disable)

	@staticmethod
	def ForbidLiquidFlow(forbid):
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.ForbidLiquidFlow(forbid)

	@staticmethod
	def GetBannedItemList():
		comp = serverApi.GetEngineCompFactory().CreateItemBanned(levelId)
		return comp.GetBannedItemList()

	@staticmethod
	def GetGameDiffculty(entityId):
		comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
		return comp.GetGameDiffculty()

	@staticmethod
	def GetGameRulesInfoServer():
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetGameRulesInfoServer()

	@staticmethod
	def GetGameType(entityId):
		comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
		return comp.GetGameType()

	@staticmethod
	def GetLevelGravity():
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetLevelGravity()

	@staticmethod
	def GetSeed():
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetSeed()

	@staticmethod
	def IsDisableCommandMinecart():
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.IsDisableCommandMinecart()

	@staticmethod
	def IsLockDifficulty():
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.IsLockDifficulty()

	@staticmethod
	def LockDifficulty(lock):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.LockDifficulty(lock)

	@staticmethod
	def OpenCityProtect():
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.OpenCityProtect()

	@staticmethod
	def RemoveBannedItem(itemName):
		comp = serverApi.GetEngineCompFactory().CreateItemBanned(levelId)
		return comp.RemoveBannedItem(itemName)

	@staticmethod
	def RemoveBlockProtectField(field):
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.RemoveBlockProtectField(field)

	@staticmethod
	def SetCanActorSetOnFireByLightning(enable):
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.SetCanActorSetOnFireByLightning(enable)

	@staticmethod
	def SetCanBlockSetOnFireByLightning(enable):
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.SetCanBlockSetOnFireByLightning(enable)

	@staticmethod
	def SetDefaultGameType(gameType, playerId):
		comp = serverApi.GetEngineCompFactory().CreateGame(playerId)
		return comp.SetDefaultGameType(gameType)

	@staticmethod
	def SetDisableCommandMinecart(isDisable):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetDisableCommandMinecart(isDisable)

	@staticmethod
	def SetDisableContainers(isDisable, entityId):
		comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
		return comp.SetDisableContainers(isDisable)

	@staticmethod
	def SetDisableDropItem(isDisable, entityId):
		comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
		return comp.SetDisableDropItem(isDisable)

	@staticmethod
	def SetDisableGravityInLiquid(isDisable):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetDisableGravityInLiquid(isDisable)

	@staticmethod
	def SetDisableHunger(isDisable, entityId):
		comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
		return comp.SetDisableHunger(isDisable)

	@staticmethod
	def SetGameDifficulty(difficulty):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetGameDifficulty(difficulty)

	@staticmethod
	def SetGameRulesInfoServer(gameRuleDict):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetGameRulesInfoServer(gameRuleDict)

	@staticmethod
	def SetHurtCD(cdTime):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetHurtCD(cdTime)

	@staticmethod
	def SetLevelGravity(data):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetLevelGravity(data)


class ExtraData:

	@staticmethod
	def CleanExtraData(key, ID):
		entitycomp = serverApi.GetEngineCompFactory().CreateExtraData(ID)
		return entitycomp.CleanExtraData(key)

	@staticmethod
	def GetExtraData(key, ID):
		comp = serverApi.GetEngineCompFactory().CreateExtraData(ID)
		return comp.GetExtraData(key)

	@staticmethod
	def GetWholeExtraData(ID):
		comp = serverApi.GetEngineCompFactory().CreateExtraData(ID)
		return comp.GetWholeExtraData()

	@staticmethod
	def SaveExtraData(ID):
		entitycomp = serverApi.GetEngineCompFactory().CreateExtraData(ID)
		return entitycomp.SaveExtraData()

	@staticmethod
	def SetExtraData(ID, key, value, autoSave):
		levelcomp = serverApi.GetEngineCompFactory().CreateExtraData(ID)
		return levelcomp.SetExtraData(key,value,autoSave)


class Command:

	@staticmethod
	def GetCommandPermissionLevel():
		comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
		return comp.GetCommandPermissionLevel()

	@staticmethod
	def GetDefaultPlayerPermissionLevel():
		comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
		return comp.GetDefaultPlayerPermissionLevel()

	@staticmethod
	def SetCommand(cmdStr, playerId, showOutput):
		comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
		return comp.SetCommand(cmdStr, playerId, showOutput)

	@staticmethod
	def SetCommandPermissionLevel(opLevel):
		comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
		return comp.SetCommandPermissionLevel(opLevel)

	@staticmethod
	def SetDefaultPlayerPermissionLevel(opLevel):
		comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
		return comp.SetDefaultPlayerPermissionLevel(opLevel)


class Message:

	@staticmethod
	def NotifyOneMessage(playerId, msg, color):
		comp = serverApi.GetEngineCompFactory().CreateMsg(playerId)
		return comp.NotifyOneMessage(playerId, msg, color)

	@staticmethod
	def SendMsg(name, msg):
		comp = serverApi.GetEngineCompFactory().CreateMsg(levelId)
		return comp.SendMsg(name, msg)

	@staticmethod
	def SendMsgToPlayer(fromEntityId, toEntityId, msg):
		comp = serverApi.GetEngineCompFactory().CreateMsg(levelId)
		return comp.SendMsgToPlayer(fromEntityId, toEntityId, msg)

	@staticmethod
	def SetNotifyMsg(msg, color):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetNotifyMsg(msg, color)

	@staticmethod
	def SetOnePopupNotice(playerId, message, subtitle):
		comp = serverApi.GetEngineCompFactory().CreateGame(playerId)
		return comp.SetOnePopupNotice(playerId, message, subtitle)

	@staticmethod
	def SetOneTipMessage(playerId, message):
		comp = serverApi.GetEngineCompFactory().CreateGame(playerId)
		return comp.SetOneTipMessage(playerId, message)

	@staticmethod
	def SetPopupNotice(message, subtitle):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetPopupNotice(message, subtitle)

	@staticmethod
	def SetTipMessage(message):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetTipMessage(message)
