import mod.server.extraServerApi as serverApi
levelId = serverApi.GetLevelId()


class StatusAndAddedValue:

	@staticmethod
	def GetBlockAuxValueFromStates(blockName, states):
		comp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
		return comp.GetBlockAuxValueFromStates(blockName, states)

	@staticmethod
	def GetBlockStates(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
		return comp.GetBlockStates(pos, dimensionId)

	@staticmethod
	def GetBlockStatesFromAuxValue(blockName, auxValue):
		comp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
		return comp.GetBlockStatesFromAuxValue(blockName, auxValue)

	@staticmethod
	def SetBlockStates(pos, data, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
		return comp.SetBlockStates(pos, data, dimensionId)


class BlockEntity:

	@staticmethod
	def CleanBlockTileEntityCustomData(playerId, pos):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
		return comp.CleanBlockTileEntityCustomData(pos)

	@staticmethod
	def GetBlockEntityData(dimension, pos):
		blockEntitycomp = serverApi.GetEngineCompFactory().CreateBlockEntityData(levelId)
		return blockEntitycomp.GetBlockEntityData(dimension, pos)

	@staticmethod
	def GetBlockTileEntityCustomData(playerId, pos, key):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
		return comp.GetBlockTileEntityCustomData(pos, key)

	@staticmethod
	def GetBlockTileEntityWholeCustomData(playerId, pos):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
		return comp.GetBlockTileEntityWholeCustomData(pos)

	@staticmethod
	def SetBlockTileEntityCustomData(playerId, pos, key, value):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
		return comp.SetBlockTileEntityCustomData(pos, key, value)


class BlockPalette:

	@staticmethod
	def DeleteBlockInBlockPalette(palette, blockName, auxValue):
		return palette.DeleteBlockInBlockPalette(blockName, auxValue)

	@staticmethod
	def DeserializeBlockPalette(dataDict):
		comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
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


class Container:

	@staticmethod
	def GetChestBoxSize(playerId, pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateChestBlock(levelId)
		return comp.GetChestBoxSize(playerId, pos, dimensionId)

	@staticmethod
	def GetChestPairedPosition(pos):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetChestPairedPosition(pos)

	@staticmethod
	def GetContainerItem(pos, slotPos, dimensionId, getUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetContainerItem(pos, slotPos, dimensionId, getUserData)

	@staticmethod
	def GetContainerSize(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetContainerSize(pos, dimensionId)

	@staticmethod
	def GetEnderChestItem(playerId, slotPos, getUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetEnderChestItem(playerId, slotPos, getUserData)

	@staticmethod
	def GetInputSlotItem(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetInputSlotItem(pos, dimensionId)

	@staticmethod
	def GetOpenContainerItem(playerId, containerId, getUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetOpenContainerItem(playerId, containerId, getUserData)

	@staticmethod
	def GetOutputSlotItem(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetOutputSlotItem(pos, dimensionId)

	@staticmethod
	def GetPlayerUIItem(playerId, slot, getUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetPlayerUIItem(playerId, slot, getUserData)

	@staticmethod
	def SetChestBoxItemExchange(playerId, pos, slotPos1, slotPos2):
		comp = serverApi.GetEngineCompFactory().CreateChestBlock(playerId)
		return comp.SetChestBoxItemExchange(playerId, pos, slotPos1, slotPos2)

	@staticmethod
	def SetChestBoxItemNum(playerId, pos, slotPos, num, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateChestBlock(levelId)
		return comp.SetChestBoxItemNum(playerId, pos, slotPos, num, dimensionId)

	@staticmethod
	def SetInputSlotItem(itemDict, pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.SetInputSlotItem(itemDict, pos, dimensionId)

	@staticmethod
	def SetPlayerUIItem(playerId, slot, itemDict, needBack):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetPlayerUIItem(playerId, slot, itemDict)

	@staticmethod
	def SpawnItemToContainer(itemDict, slotPos, blockPos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.SpawnItemToContainer(itemDict, slotPos, blockPos, dimensionId)

	@staticmethod
	def SpawnItemToEnderChest(playerId, itemDict, slotPos):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SpawnItemToEnderChest(itemDict, slotPos)


class Redstone:

	@staticmethod
	def GetBlockPoweredState(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateRedStone(levelId)
		return comp.GetBlockPoweredState(pos, dimensionId)

	@staticmethod
	def GetStrength(pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreateRedStone(levelId)
		return comp.GetStrength(pos, dimensionId)


class Noticeboard:

	@staticmethod
	def GetSignBlockText(pos):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetSignBlockText(pos)

	@staticmethod
	def SetSignBlockText(pos, text):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetSignBlockText(pos, text)


class Bed:

	@staticmethod
	def GetBedColor(pos):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBedColor(pos)

	@staticmethod
	def SetBedColor(pos, color):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetBedColor(pos, color)


class Attribute:

	@staticmethod
	def GetBlockBasicInfo(blockName):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetBlockBasicInfo(blockName)

	@staticmethod
	def GetLoadBlocks():
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.GetLoadBlocks()

	@staticmethod
	def SetBlockBasicInfo(blockName, infoDict, auxValue):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
		return comp.SetBlockBasicInfo(blockName, infoDict, auxValue)