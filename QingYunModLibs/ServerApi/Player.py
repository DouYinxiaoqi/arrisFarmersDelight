import mod.server.extraServerApi as serverApi
levelId = serverApi.GetLevelId()


class Attribute:

	@staticmethod
	def AddPlayerExperience(entityId, exp):
		comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
		return comp.AddPlayerExperience(exp)

	@staticmethod
	def AddPlayerLevel(playerId, level):
		comp = serverApi.GetEngineCompFactory().CreateLv(playerId)
		return comp.AddPlayerLevel(level)

	@staticmethod
	def CollectOnlineClientData(playerId, collectTypes, callback, extraArgs):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.CollectOnlineClientData(collectTypes, callback, extraArgs)

	@staticmethod
	def GetPlayerExp(entityId, isPercent):
		comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
		return comp.GetPlayerExp(isPercent)

	@staticmethod
	def GetPlayerHealthLevel(entityId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.GetPlayerHealthLevel()


	@staticmethod
	def GetPlayerHealthTick(entityId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.GetPlayerHealthTick()


	@staticmethod
	def GetPlayerHunger(playerId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.GetPlayerHunger()

	@staticmethod
	def GetPlayerLevel(playerId):
		comp = serverApi.GetEngineCompFactory().CreateLv(playerId)
		return comp.GetPlayerLevel()

	@staticmethod
	def GetPlayerMaxExhaustionValue(playerId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.GetPlayerMaxExhaustionValue()

	@staticmethod
	def GetPlayerStarveLevel(entityId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.GetPlayerStarveLevel()


	@staticmethod
	def GetPlayerStarveTick(entityId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.GetPlayerStarveTick()


	@staticmethod
	def GetPlayerTotalExp(entityId):
		comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
		return comp.GetPlayerTotalExp()


	@staticmethod
	def IsPlayerNaturalRegen(entityId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.IsPlayerNaturalRegen()


	@staticmethod
	def IsPlayerNaturalStarve(entityId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.IsPlayerNaturalStarve()


	@staticmethod
	def SetPlayerHealthLevel(entityId, healthLevel):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.SetPlayerHealthLevel(healthLevel)

	@staticmethod
	def SetPlayerHealthTick(entityId, healthTick):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.SetPlayerHealthTick(healthTick)

	@staticmethod
	def SetPlayerHunger(playerId, value):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.SetPlayerHunger(value)

	@staticmethod
	def SetPlayerMaxExhaustionValue(playerId, value):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.SetPlayerMaxExhaustionValue(value)

	@staticmethod
	def SetPlayerNaturalRegen(entityId, value):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.SetPlayerNaturalRegen(value)

	@staticmethod
	def SetPlayerNaturalStarve(entityId, value):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.SetPlayerNaturalStarve(value)

	@staticmethod
	def SetPlayerPrefixAndSuffixName(playerId, prefix, prefixColor, suffix, suffixColor):
		comp = serverApi.GetEngineCompFactory().CreateName(playerId)
		return comp.SetPlayerPrefixAndSuffixName(prefix, prefixColor, suffix, suffixColor)

	@staticmethod
	def SetPlayerStarveLevel(entityId, starveLevel):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.SetPlayerStarveLevel(starveLevel)

	@staticmethod
	def SetPlayerStarveTick(entityId, starveTick):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
		return comp.SetPlayerStarveTick(starveTick)

	@staticmethod
	def SetPlayerTotalExp(entityId, exp):
		comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
		return comp.SetPlayerTotalExp(exp)


class Action:

	@staticmethod
	def AddPlayerAroundEntityMotion(playerId, angularVelocity, axis, lockDir, stopRad, radius):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.AddPlayerAroundEntityMotion(playerId, angularVelocity, axis, lockDir, stopRad, radius)

	@staticmethod
	def AddPlayerAroundPointMotion(playerId, center, angularVelocity, axis, lockDir, stopRad):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.AddPlayerAroundPointMotion(center, angularVelocity, axis, lockDir, stopRad)

	@staticmethod
	def AddPlayerTrackMotion(playerId, targetPos, duraTime, startPos, relativeCoord, isLoop, targetRot, startRot, useVelocityDir):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.AddPlayerTrackMotion(targetPos, duraTime, startPos, relativeCoord, isLoop, targetRot, startRot, useVelocityDir)

	@staticmethod
	def AddPlayerVelocityMotion(playerId, velocity, accelerate, useVelocityDir):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.AddPlayerVelocityMotion(velocity, accelerate, useVelocityDir)

	@staticmethod
	def ChangePlayerDimension(playerId, dimensionId, pos):
		comp = serverApi.GetEngineCompFactory().CreateDimension(playerId)
		return comp.ChangePlayerDimension(dimensionId, pos)

	@staticmethod
	def ChangePlayerFlyState(playerId, isFly):
		comp = serverApi.GetEngineCompFactory().CreateFly(playerId)
		return comp.ChangePlayerFlyState(isFly)

	@staticmethod
	def EnableKeepInventory(playerId, enable):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.EnableKeepInventory(enable)

	@staticmethod
	def GetEntityRider(entityId):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.GetEntityRider()

	@staticmethod
	def GetIsBlocking(playerId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.GetIsBlocking()

	@staticmethod
	def GetPlayerExhaustionRatioByType(playerId, types):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.GetPlayerExhaustionRatioByType(types)

	@staticmethod
	def GetPlayerMotions(playerId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.GetPlayerMotions()

	@staticmethod
	def GetPlayerRespawnPos(playerId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.GetPlayerRespawnPos()

	@staticmethod
	def GetRelevantPlayer(playerId, exceptList):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.GetRelevantPlayer(exceptList)

	@staticmethod
	def IsEntityRiding(entityId):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.IsEntityRiding()

	@staticmethod
	def IsPlayerFlying(playerId):
		comp = serverApi.GetEngineCompFactory().CreateFly(playerId)
		return comp.IsPlayerFlying()

	@staticmethod
	def PickUpItemEntity(playerEntityId, itemEntityId):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.PickUpItemEntity(playerEntityId, itemEntityId)

	@staticmethod
	def PlayerDestoryBlock(playerId, pos, particle, sendInv):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
		return comp.PlayerDestoryBlock(pos, particle, sendInv)

	@staticmethod
	def PlayerUseItemToEntity(playerId, entityId):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
		return comp.PlayerUseItemToEntity(entityId)

	@staticmethod
	def PlayerUseItemToPos(playerId, pos, posType, slotPos, facing):
		comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
		return comp.PlayerUseItemToPos(pos, posType, slotPos, facing)

	@staticmethod
	def RemovePlayerMotion(playerId, motionId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.RemovePlayerMotion(motionId)

	@staticmethod
	def SetPickUpArea(playerId, area):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.SetPickUpArea(area)

	@staticmethod
	def SetPlayerAttackSpeedAmplifier(playerId, amplifier):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.SetPlayerAttackSpeedAmplifier(amplifier)

	@staticmethod
	def SetPlayerExhaustionRatioByType(playerId, types, ratio):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.SetPlayerExhaustionRatioByType(types, ratio)

	@staticmethod
	def SetPlayerJumpable(playerId, isJumpable):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.SetPlayerJumpable(isJumpable)

	@staticmethod
	def SetPlayerMotion(entityId, motion):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.SetPlayerMotion(motion)

	@staticmethod
	def SetPlayerMovable(playerId, isMovable):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.SetPlayerMovable(isMovable)

	@staticmethod
	def SetPlayerRespawnPos(playerId, pos, dimensionId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.SetPlayerRespawnPos(pos, dimensionId)

	@staticmethod
	def SetPlayerRideEntity(playerId, rideEntityId, riderIndex):
		comp = serverApi.GetEngineCompFactory().CreateRide(playerId)
		return comp.SetPlayerRideEntity(playerId, rideEntityId, riderIndex)

	@staticmethod
	def StartPlayerMotion(playerId, motionId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.StartPlayerMotion(motionId)

	@staticmethod
	def StopEntityRiding(entityId):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.StopEntityRiding()

	@staticmethod
	def StopPlayerMotion(playerId, motionId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.StopPlayerMotion(motionId)

	@staticmethod
	def isSneaking(playerId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.isSneaking()

	@staticmethod
	def isSwimming(playerId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.isSwimming()


class Knapsack:

	@staticmethod
	def AddEnchantToInvItem(playerId, slotPos, enchantType, level):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.AddEnchantToInvItem(slotPos, enchantType, level)

	@staticmethod
	def AddModEnchantToInvItem(playerId, slotPos, modEnchantId, level):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.AddModEnchantToInvItem(slotPos, modEnchantId, level)

	@staticmethod
	def ChangePlayerItemTipsAndExtraId(playerId, posType, slotPos, customTips, extraId):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.ChangePlayerItemTipsAndExtraId(posType, slotPos, customTips, extraId)

	@staticmethod
	def ChangeSelectSlot(playerId, slot):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.ChangeSelectSlot(slot)

	@staticmethod
	def GetInvItemEnchantData(playerId, slotPos):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetInvItemEnchantData(slotPos)

	@staticmethod
	def GetInvItemModEnchantData(playerId, slotPos):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetInvItemModEnchantData(slotPos)

	@staticmethod
	def GetPlayerAllItems(playerId, posType, getUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetPlayerAllItems(posType, getUserData)

	@staticmethod
	def GetPlayerItem(playerId, posType, slotPos, getUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetPlayerItem(posType, slotPos, getUserData)

	@staticmethod
	def GetSelectSlotId(playerId):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetSelectSlotId()

	@staticmethod
	def RemoveEnchantToInvItem(playerId, slotPos, enchantType):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.RemoveEnchantToInvItem(slotPos, enchantType)

	@staticmethod
	def RemoveModEnchantToInvItem(playerId, slotPos, modEnchantId):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.RemoveModEnchantToInvItem(slotPos, modEnchantId)

	@staticmethod
	def SetInvItemExchange(playerId, pos1, pos2):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetInvItemExchange(pos1, pos2)

	@staticmethod
	def SetInvItemNum(playerId, slotPos, num):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetInvItemNum(slotPos, num)

	@staticmethod
	def SetPlayerAllItems(playerId, itemsDictMap):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SetPlayerAllItems(itemsDictMap)

	@staticmethod
	def SpawnItemToPlayerCarried(itemDict, playerId):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SpawnItemToPlayerCarried(itemDict, playerId)

	@staticmethod
	def SpawnItemToPlayerInv(itemDict, playerId, slotPos):
		comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.SpawnItemToPlayerInv(itemDict, playerId, slotPos)


class PlayerGameType:

	@staticmethod
	def GetPlayerGameType(playerId):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetPlayerGameType(playerId)

	@staticmethod
	def SetPlayerGameType(playerId, gameType):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.SetPlayerGameType(gameType)


class Operation:

	@staticmethod
	def GetPlayerAbilities(playerId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.GetPlayerAbilities()

	@staticmethod
	def GetPlayerOperation(playerId):
		comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.GetPlayerOperation()