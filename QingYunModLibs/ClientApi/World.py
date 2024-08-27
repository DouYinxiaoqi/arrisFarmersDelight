import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class Map:

	@staticmethod
	def GetBiomeName(pos, dimId):
		comp = clientApi.GetEngineCompFactory().CreateBiome(levelId)
		return comp.GetBiomeName(pos, dimId)

	@staticmethod
	def GetChunkPosFromBlockPos(blockPos):
		comp = clientApi.GetEngineCompFactory().CreateChunkSource(levelId)
		return comp.GetChunkPosFromBlockPos(blockPos)

	@staticmethod
	def GetCurrentDimension():
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetCurrentDimension()

	@staticmethod
	def GetEntitiesAround(entityId, radius, filters):
		comp = clientApi.GetEngineCompFactory().CreateGame(entityId)
		return comp.GetEntitiesAround(entityId, radius, filters)

	@staticmethod
	def GetEntitiesAroundByType(entityId, radius, entityType):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetEntitiesAroundByType(entityId, radius, entityType)

	@staticmethod
	def GetEntitiesInSquareArea(entityId, startPos, endPos, dimensionId):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetEntitiesInSquareArea(entityId, startPos, endPos, dimensionId)

	@staticmethod
	def GetEntityInArea(entityId, pos_a, pos_b, exceptEntity):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetEntityInArea(entityId, pos_a, pos_b, exceptEntity)

	@staticmethod
	def GetLevelId():
		return clientApi.GetLevelId()


class Entity:

	@staticmethod
	def GetEngineActor():
		return clientApi.GetEngineActor()

	@staticmethod
	def GetLocalPlayerId():
		return clientApi.GetLocalPlayerId()

	@staticmethod
	def GetPlayerList():
		return clientApi.GetPlayerList()


	@staticmethod
	def HasEntity(entityId):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.HasEntity(entityId)

	@staticmethod
	def IsEntityAlive(entityId):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.IsEntityAlive(entityId)


class Block:

	@staticmethod
	def GetBlock(pos):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlock(pos)

	@staticmethod
	def GetBlockClip(pos, dimensionId):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlockClip(pos, dimensionId)

	@staticmethod
	def GetBlockCollision(pos, dimensionId):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlockCollision(pos, dimensionId)

	@staticmethod
	def GetDestroyTotalTime(blockName, itemName):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetDestroyTotalTime(blockName, itemName)

	@staticmethod
	def GetTopBlockHeight(pos, dimension):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetTopBlockHeight(pos, dimension)


class Recipes:

	@staticmethod
	def GetRecipesByInput(inputIdentifier, tag, aux, maxResultNum):
		comp = clientApi.GetEngineCompFactory().CreateRecipe(levelId)
		return comp.GetRecipesByInput(inputIdentifier, tag, aux, maxResultNum)


	@staticmethod
	def GetRecipesByResult(resultIdentifier, tag, aux, maxResultNum):
		comp = clientApi.GetEngineCompFactory().CreateRecipe(levelId)
		return comp.GetRecipesByResult(resultIdentifier, tag, aux, maxResultNum)


class BlockPalette:

	@staticmethod
	def GetBlankBlockPalette():
		comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
		return comp.GetBlankBlockPalette()

	@staticmethod
	def GetBlockPaletteBetweenPos(dimensionId, startBlockPos, endBlockPos, eliminateAir):
		comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
		return comp.GetBlockPaletteBetweenPos(dimensionId, startBlockPos, endBlockPos, eliminateAir)

	@staticmethod
	def GetBlockPaletteFromPosList(dimensionId, posList):
		comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
		return comp.GetBlockPaletteFromPosList(dimensionId, posList)


class Render:

	@staticmethod
	def GetAmbientBrightness():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetAmbientBrightness()

	@staticmethod
	def GetFogColor():
		comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
		return comp.GetFogColor()

	@staticmethod
	def GetFogLength():
		comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
		return comp.GetFogLength()

	@staticmethod
	def GetMoonRot():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetMoonRot()

	@staticmethod
	def GetSkyColor():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetSkyColor()

	@staticmethod
	def GetSkyTextures():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetSkyTextures()

	@staticmethod
	def GetStarBrightness():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetStarBrightness()

	@staticmethod
	def GetSunRot():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetSunRot()

	@staticmethod
	def GetUseAmbientBrightness():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetUseAmbientBrightness()

	@staticmethod
	def GetUseFogColor():
		comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
		return comp.GetUseFogColor()

	@staticmethod
	def GetUseFogLength():
		comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
		return comp.GetUseFogLength()

	@staticmethod
	def GetUseMoonRot():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetUseMoonRot()

	@staticmethod
	def GetUseSkyColor():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetUseSkyColor()

	@staticmethod
	def GetUseStarBrightness():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetUseStarBrightness()

	@staticmethod
	def GetUseSunRot():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.GetUseSunRot()

	@staticmethod
	def HideNameTag(isHide):
		return clientApi.HideNameTag(isHide)

	@staticmethod
	def ResetAmbientBrightness():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.ResetAmbientBrightness()

	@staticmethod
	def ResetFogColor():
		comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
		return comp.ResetFogColor()

	@staticmethod
	def ResetFogLength():
		comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
		return comp.ResetFogLength()

	@staticmethod
	def ResetMoonRot():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.ResetMoonRot()

	@staticmethod
	def ResetSkyColor():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.ResetSkyColor()

	@staticmethod
	def ResetSkyTextures():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.ResetSkyTextures()

	@staticmethod
	def ResetStarBrightness():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.ResetStarBrightness()

	@staticmethod
	def ResetSunRot():
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.ResetSunRot()

	@staticmethod
	def SetAmbientBrightness(brightness):
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.SetAmbientBrightness(brightness)

	@staticmethod
	def SetFogColor(color):
		comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
		return comp.SetFogColor(color)

	@staticmethod
	def SetFogLength(start, end):
		comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
		return comp.SetFogLength(start, end)

	@staticmethod
	def SetMoonRot(rot):
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.SetMoonRot(rot)

	@staticmethod
	def SetSkyColor(color):
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.SetSkyColor(color)

	@staticmethod
	def SetSkyTextures(textureList):
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.SetSkyTextures(textureList)

	@staticmethod
	def SetStarBrightness(brightness):
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.SetStarBrightness(brightness)

	@staticmethod
	def SetSunRot(rot):
		comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
		return comp.SetSunRot(rot)


class Time:

	@staticmethod
	def GetTime():
		comp = clientApi.GetEngineCompFactory().CreateTime(levelId)
		return comp.GetTime()


class Message:

	@staticmethod
	def SetLeftCornerNotify(textMsg):
		comp = clientApi.GetEngineCompFactory().CreateTextNotifyClient(levelId)
		return comp.SetLeftCornerNotify(textMsg)

	@staticmethod
	def SetPopupNotice(message, subtitle):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetPopupNotice(message, subtitle)

	@staticmethod
	def SetTipMessage(message):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetTipMessage(message)