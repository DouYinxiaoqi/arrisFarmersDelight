import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class BlockEntity:

	@staticmethod
	def CreateFrameEffectForBlockEntity(pos, path, frameKeyName, effectPos):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.CreateFrameEffectForBlockEntity(pos, path, frameKeyName, effectPos)

	@staticmethod
	def CreateParticleEffectForBlockEntity(pos, path, particleKeyName, effectPos):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.CreateParticleEffectForBlockEntity(pos, path, particleKeyName, effectPos)

	@staticmethod
	def GetBlockEntityData(pos, variableName):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlockEntityMolangValue(pos, variableName)

	@staticmethod
	def GetFrameEffectIdInBlockEntity(pos, frameKeyName):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetFrameEffectIdInBlockEntity(pos, frameKeyName)

	@staticmethod
	def GetParticleEffectIdInBlockEntity(pos, particleKeyName):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetParticleEffectIdInBlockEntity(pos, particleKeyName)

	@staticmethod
	def RemoveFrameEffectInBlockEntity(pos, frameKeyName):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.RemoveFrameEffectInBlockEntity(pos, frameKeyName)

	@staticmethod
	def RemoveParticleEffectInBlockEntity(pos, particleKeyName):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.RemoveParticleEffectInBlockEntity(pos, particleKeyName)

	@staticmethod
	def SetBlockEntityMolangValue(pos, variableName, value):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetBlockEntityMolangValue(pos, variableName, value)

	@staticmethod
	def SetEnableBlockEntityAnimations(pos, enable):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetEnableBlockEntityAnimations(pos, enable)


class BlockGeometry:

	@staticmethod
	def CombineBlockBetweenPosToGeometry(startPos, endPos, geometryName, unsupportedMode, useStructureVoid):
		blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
		return blockGeometryComp.CombineBlockBetweenPosToGeometry(startPos, endPos, geometryName, unsupportedMode, useStructureVoid)

	@staticmethod
	def CombineBlockFromPosListToGeometry(posList, geometryName, unsupportedMode, useStructureVoid):
		blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
		return blockGeometryComp.CombineBlockFromPosListToGeometry(posList, geometryName, unsupportedMode, useStructureVoid)

	@staticmethod
	def CombineBlockPaletteToGeometry(blockPalette, geometryName, unsupportedMode):
		blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
		return blockGeometryComp.CombineBlockPaletteToGeometry(blockPalette, geometryName, unsupportedMode)

	@staticmethod
	def EnableActorBlockGeometryTransparent(entityId, geometryName, enable):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return actorRenderComp.EnableActorBlockGeometryTransparent(geometryName, enable)

	@staticmethod
	def SetActorBlockGeometryOffset(entityId, geometryName, offset):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return actorRenderComp.SetActorBlockGeometryOffset(geometryName, offset)

	@staticmethod
	def SetActorBlockGeometryRotation(entityId, geometryName, rotation):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return actorRenderComp.SetActorBlockGeometryRotation(geometryName, rotation)

	@staticmethod
	def SetActorBlockGeometryTransparency(entityId, geometryName, transparent):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return actorRenderComp.SetActorBlockGeometryTransparency(geometryName, transparent)


class BlockPalette:

	@staticmethod
	def DeleteBlockInBlockPalette(palette, blockName, auxValue):
		return palette.DeleteBlockInBlockPalette(blockName, auxValue)

	@staticmethod
	def DeserializeBlockPalette(dataDict):
		comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
		newPalette = comp.GetBlankBlockPalette()
		return newPalette.DeserializeBlockPalette(dataDict)

	@staticmethod
	def GetBlockCountInBlockPalette(palette, blockName, auxValue):
		return palette.GetBlockCountInBlockPalette(blockName, auxValue)

	@staticmethod
	def GetLocalPosListOfBlocks(palette, blockName, auxValue):
		return palette.GetLocalPosListOfBlocks(blockName, auxValue)

	@staticmethod
	def GetVolumeOfBlockPalette(palette):
		return palette.GetVolumeOfBlockPalette()


	@staticmethod
	def ReplaceAirByStructureVoid(palette, enable):
		return palette.ReplaceAirByStructureVoid(enable)

	@staticmethod
	def ReplaceBlockInBlockPalette(palette, newblockName, newBlockAux, oldBlockName, oldBlockAux):
		return palette.ReplaceBlockInBlockPalette(newblockName, newBlockAux, oldBlockName, oldBlockAux)

	@staticmethod
	def SerializeBlockPalette(sourcePalette):
		return sourcePalette.SerializeBlockPalette()


class Render:

	@staticmethod
	def AddDropItemToWorld(itemDict, dimension_id, position, bobSpeed, spinSpeed):
		comp = clientApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.AddDropItemToWorld(itemDict, dimension_id, position, bobSpeed, spinSpeed)

	@staticmethod
	def ChangeBlockTextures(blockName, tileName, texturePath):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.ChangeBlockTextures(blockName, tileName, texturePath)

	@staticmethod
	def DeleteClientDropItemEntity(entityId):
		comp = clientApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.DeleteClientDropItemEntity(entityId)

	@staticmethod
	def GetBlockTextures(blockName, face):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlockTextures(blockName, face)

	@staticmethod
	def GetClientDropItemEntityIdList():
		comp = clientApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetClientDropItemEntityIdList()


	@staticmethod
	def SetBlockEntityFramePosOffset(pos, frameKeyName, effectPosOffset):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetBlockEntityFramePosOffset(pos, frameKeyName, effectPosOffset)

	@staticmethod
	def SetBlockEntityModelPosOffset(pos, modelPosOffset):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetBlockEntityModelPosOffset(pos, modelPosOffset)

	@staticmethod
	def SetBlockEntityModelRotation(pos, angles, rotateAxis):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetBlockEntityModelRotation(pos, angles, rotateAxis)

	@staticmethod
	def SetBlockEntityModelScale(pos, scale):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetBlockEntityModelScale(pos, scale)

	@staticmethod
	def SetBlockEntityParticlePosOffset(pos, particleKeyName, effectPosOffset):
		comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetBlockEntityParticlePosOffset(pos, particleKeyName, effectPosOffset)