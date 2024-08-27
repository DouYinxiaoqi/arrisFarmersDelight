import mod.server.extraServerApi as serverApi
levelId = serverApi.GetLevelId()


class Item:

	@staticmethod
	def CancelShearsDestoryBlockSpeed(entityId, blockName):
		comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
		return comp.CancelShearsDestoryBlockSpeed(blockName)

	@staticmethod
	def CancelShearsDestoryBlockSpeedAll(entityId):
		comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
		return comp.CancelShearsDestoryBlockSpeedAll()

	@staticmethod
	def GetCustomName(playerId, itemDict):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetCustomName(itemDict)

	@staticmethod
	def GetItemBasicInfo(itemName, auxValue, isEnchanted):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetItemBasicInfo(itemName, auxValue, isEnchanted)

	@staticmethod
	def GetItemDefenceAngle(playerId, posType, slotPos):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetItemDefenceAngle(posType, slotPos)

	@staticmethod
	def GetItemDurability(playerId, posType, slotPos):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetItemDurability(posType, slotPos)

	@staticmethod
	def GetItemLayer(playerId, itemDict, layer):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetItemLayer(itemDict, layer)

	@staticmethod
	def GetItemMaxDurability(playerId, posType, slotPos, isUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetItemMaxDurability(posType, slotPos, isUserData)

	@staticmethod
	def GetLoadItems(flag):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetLoadItems(flag)

	@staticmethod
	def GetUserDataInEvent(eventName):
		comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetUserDataInEvent(eventName)

	@staticmethod
	def LookupItemByName(itemName):
		gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return gameComp.LookupItemByName(itemName)

	@staticmethod
	def RemoveItemLayer(playerId, itemDict, layer):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.RemoveItemLayer(itemDict, layer)

	@staticmethod
	def SetAttackDamage(playerId, itemDict, attackDamage):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetAttackDamage(itemDict, attackDamage)

	@staticmethod
	def SetCustomName(playerId, itemDict, name):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetCustomName(itemDict, name)

	@staticmethod
	def SetItemDefenceAngle(playerId, posType, slotPos, angleLeft, angleRight):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetItemDefenceAngle(posType, slotPos, angleLeft, angleRight)

	@staticmethod
	def SetItemDurability(playerId, posType, slotPos, durability):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetItemDurability(posType, slotPos, durability)

	@staticmethod
	def SetItemLayer(playerId, itemDict, layer, texture):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetItemLayer(itemDict, layer, texture)

	@staticmethod
	def SetItemMaxDurability(playerId, posType, slotPos, maxDurability, isUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetItemMaxDurability(posType, slotPos, maxDurability, isUserData)

	@staticmethod
	def SetItemTierLevel(playerId, itemDict, level):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetItemTierLevel(itemDict, level)

	@staticmethod
	def SetItemTierSpeed(playerId, itemDict, speed):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetItemTierSpeed(itemDict, speed)

	@staticmethod
	def SetMaxStackSize(playerId, itemDict, maxStackSize):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetMaxStackSize(itemDict, maxStackSize)

	@staticmethod
	def SetShearsDestoryBlockSpeed(entityId, blockName, speed):
		comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
		return comp.SetShearsDestoryBlockSpeed(blockName, speed)