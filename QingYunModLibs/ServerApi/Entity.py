import mod.server.extraServerApi as serverApi
levelId = serverApi.GetLevelId()


class EngineType:

	@staticmethod
	def GetEngineType(entityId):
		comp = serverApi.GetEngineCompFactory().CreateEngineType(entityId)
		return comp.GetEngineType()

	@staticmethod
	def GetEngineTypeStr(entityId):
		comp = serverApi.GetEngineCompFactory().CreateEngineType(entityId)
		return comp.GetEngineTypeStr()


class Aux:

	@staticmethod
	def GetAuxValue(entityId):
		comp = serverApi.GetEngineCompFactory().CreateAuxValue(entityId)
		return comp.GetAuxValue()


class Attribute:

	@staticmethod
	def ChangeEntityDimension(entityId, dimensionId, pos):
		comp = serverApi.GetEngineCompFactory().CreateDimension(entityId)
		return comp.ChangeEntityDimension(dimensionId, pos)

	@staticmethod
	def GetAllComponentsName(entityId):
		comp = serverApi.GetEngineCompFactory().CreateEntityComponent(entityId)
		return comp.GetAllComponentsName()


	@staticmethod
	def GetAttrMaxValue(entityId, types):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.GetAttrMaxValue(types)

	@staticmethod
	def GetAttrValue(entityId, attrType):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.GetAttrValue(attrType)

	@staticmethod
	def GetCurrentAirSupply(entityId):
		comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
		return comp.GetCurrentAirSupply()

	@staticmethod
	def GetEntityDimensionId(entityId):
		comp = serverApi.GetEngineCompFactory().CreateDimension(entityId)
		return comp.GetEntityDimensionId()

	@staticmethod
	def GetEntityOwner(entityId):
		comp = serverApi.GetEngineCompFactory().CreateActorOwner(entityId)
		return comp.GetEntityOwner()

	@staticmethod
	def GetFootPos(entityId):
		comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
		return comp.GetFootPos()

	@staticmethod
	def GetGravity(entityId):
		comp = serverApi.GetEngineCompFactory().CreateGravity(entityId)
		return comp.GetGravity()

	@staticmethod
	def GetLoadActors():
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetLoadActors()


	@staticmethod
	def GetMaxAirSupply(entityId):
		comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
		return comp.GetMaxAirSupply()

	@staticmethod
	def GetName(entityId):
		comp = serverApi.GetEngineCompFactory().CreateName(entityId)
		return comp.GetName()

	@staticmethod
	def GetPos(entityId):
		comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
		return comp.GetPos()

	@staticmethod
	def GetRot(entityId):
		comp = serverApi.GetEngineCompFactory().CreateRot(entityId)
		return comp.GetRot()

	@staticmethod
	def GetSize(entityId):
		comp = serverApi.GetEngineCompFactory().CreateCollisionBox(entityId)
		return comp.GetSize()

	@staticmethod
	def GetTypeFamily(entityId):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.GetTypeFamily()

	@staticmethod
	def GetUnitBubbleAirSupply():
		comp = serverApi.GetEngineCompFactory().CreateBreath(levelId)
		return comp.GetUnitBubbleAirSupply()

	@staticmethod
	def HasComponent(entityId, attrType):
		comp = serverApi.GetEngineCompFactory().CreateEntityComponent(entityId)
		return comp.HasComponent(attrType)

	@staticmethod
	def IsConsumingAirSupply(entityId):
		comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
		return comp.IsConsumingAirSupply()

	@staticmethod
	def SetAttrMaxValue(entityId, types, value):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.SetAttrMaxValue(types, value)

	@staticmethod
	def SetAttrValue(entityId, attrType, value):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.SetAttrValue(attrType, value)

	@staticmethod
	def SetCurrentAirSupply(entityId, data):
		comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
		return comp.SetCurrentAirSupply(data)

	@staticmethod
	def SetEntityLookAtPos(entityId, targetPos, minTime, maxTime, reject):
		comp = serverApi.GetEngineCompFactory().CreateRot(entityId)
		return comp.SetEntityLookAtPos(targetPos, minTime, maxTime, reject)

	@staticmethod
	def SetEntityOwner(entityId, targetId):
		comp = serverApi.GetEngineCompFactory().CreateActorOwner(entityId)
		return comp.SetEntityOwner(targetId)

	@staticmethod
	def SetFootPos(entityId, footPos):
		comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
		return comp.SetFootPos(footPos)

	@staticmethod
	def SetGravity(entityId, gravity):
		comp = serverApi.GetEngineCompFactory().CreateGravity(entityId)
		return comp.SetGravity(gravity)

	@staticmethod
	def SetMaxAirSupply(entityId, data):
		comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
		return comp.SetMaxAirSupply(data)

	@staticmethod
	def SetName(entityId, name):
		comp = serverApi.GetEngineCompFactory().CreateName(entityId)
		return comp.SetName(name)

	@staticmethod
	def SetPersistent(entityId, persistent):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.SetPersistent(persistent)

	@staticmethod
	def SetPos(entityId, pos):
		comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
		return comp.SetPos(pos)

	@staticmethod
	def SetRecoverTotalAirSupplyTime(entityId, timeSec):
		comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
		return comp.SetRecoverTotalAirSupplyTime(timeSec)

	@staticmethod
	def SetRot(entityId, rot):
		comp = serverApi.GetEngineCompFactory().CreateRot(entityId)
		return comp.SetRot(rot)

	@staticmethod
	def SetSize(entityId, size):
		comp = serverApi.GetEngineCompFactory().CreateCollisionBox(entityId)
		return comp.SetSize(size)

class Action:

	@staticmethod
	def AddEntityAroundEntityMotion(entityId, eID, angularVelocity, axis, lockDir, stopRad, radius):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.AddEntityAroundEntityMotion(eID, angularVelocity, axis, lockDir, stopRad, radius)

	@staticmethod
	def AddEntityAroundPointMotion(entityId, center, angularVelocity, axis, lockDir, stopRad):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.AddEntityAroundPointMotion(center, angularVelocity, axis, lockDir, stopRad)

	@staticmethod
	def AddEntitySeat(entityId, pos, rot, lock_rot):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.AddEntitySeat(pos, rot, lock_rot)

	@staticmethod
	def AddEntityTrackMotion(entityId, targetPos, duraTime, startPos, relativeCoord, isLoop, targetRot, startRot, useVelocityDir):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.AddEntityTrackMotion(targetPos, duraTime, startPos, relativeCoord, isLoop, targetRot, startRot, useVelocityDir)

	@staticmethod
	def AddEntityVelocityMotion(entityId, velocity, accelerate, useVelocityDir):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.AddEntityVelocityMotion(velocity, accelerate, useVelocityDir)

	@staticmethod
	def ChangeRiderSeat(entityId, riderIndex):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.ChangeRiderSeat(riderIndex)

	@staticmethod
	def DeleteEntitySeat(entityId, seatIndex):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.DeleteEntitySeat(seatIndex)

	@staticmethod
	def GetAttackTarget(entityId):
		comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
		return comp.GetAttackTarget()

	@staticmethod
	def GetBlockControlAi(entityId):
		comp = serverApi.GetEngineCompFactory().CreateControlAi(entityId)
		return comp.GetBlockControlAi()

	@staticmethod
	def GetCustomGoalCls():
		return serverApi.GetCustomGoalCls()

	@staticmethod
	def GetEntityMotions(entityId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.GetEntityMotions()

	@staticmethod
	def GetMotion(entityId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.GetMotion()

	@staticmethod
	def GetOwnerId(entityId):
		comp = serverApi.GetEngineCompFactory().CreateTame(entityId)
		return comp.GetOwnerId()

	@staticmethod
	def GetRiders(entityId):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.GetRiders()

	@staticmethod
	def GetStepHeight(entityId):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.GetStepHeight()


	@staticmethod
	def Hurt(EntityId, damage, cause, attackerId, childAttackerId=None, knocked=True):
		comp = serverApi.GetEngineCompFactory().CreateHurt(EntityId)
		return comp.Hurt(damage, cause, attackerId, childAttackerId, knocked)

	@staticmethod
	def ImmuneDamage(entityId, immune):
		comp = serverApi.GetEngineCompFactory().CreateHurt(entityId)
		return comp.ImmuneDamage(immune)

	@staticmethod
	def IsEntityOnFire(entityId):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.IsEntityOnFire()

	@staticmethod
	def RemoveEntityMotion(entityId, motionId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.RemoveEntityMotion(motionId)

	@staticmethod
	def ResetAttackTarget(entityId):
		comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
		return comp.ResetAttackTarget()

	@staticmethod
	def ResetMotion(entityId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.ResetMotion()

	@staticmethod
	def ResetStepHeight(entityId):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.ResetStepHeight()

	@staticmethod
	def SetActorCollidable(entityId, isCollidable):
		comp = serverApi.GetEngineCompFactory().CreateActorCollidable(entityId)
		return comp.SetActorCollidable(isCollidable)

	@staticmethod
	def SetActorPushable(entityId, isPushable):
		comp = serverApi.GetEngineCompFactory().CreateActorPushable(entityId)
		return comp.SetActorPushable(isPushable)

	@staticmethod
	def SetAttackTarget(entityId, targetId):
		comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
		return comp.SetAttackTarget(targetId)

	@staticmethod
	def SetBlockControlAi(entityId, isBlock, freezeAnim):
		comp = serverApi.GetEngineCompFactory().CreateControlAi(entityId)
		return comp.SetBlockControlAi(isBlock, freezeAnim)

	@staticmethod
	def SetCanOtherPlayerRide(entityId, tamedEntityId, canRide):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.SetCanOtherPlayerRide(tamedEntityId, canRide)

	@staticmethod
	def SetControl(entityId, tamedEntityId, isControl):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.SetControl(tamedEntityId, isControl)

	@staticmethod
	def SetEntityInteractFilter(entityId, index, interactFilter):
		comp = serverApi.GetEngineCompFactory().CreateInteract(entityId)
		return comp.SetEntityInteractFilter(index, interactFilter)

	@staticmethod
	def SetEntityLockRider(entityId, isLock):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.SetEntityLockRider(isLock)

	@staticmethod
	def SetEntityOnFire(entityId, seconds, burn_damage):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.SetEntityOnFire(seconds, burn_damage)

	@staticmethod
	def SetEntityRide(entityId, playerId, tamedEntityId):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.SetEntityRide(playerId, tamedEntityId)

	@staticmethod
	def SetEntitySeat(entityId, seatIndex, pos, rot, lock_rot):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.SetEntitySeat(seatIndex, pos, rot, lock_rot)

	@staticmethod
	def SetEntityShareablesItems(entityId, items):
		comp = serverApi.GetEngineCompFactory().CreateShareables(entityId)
		return comp.SetEntityShareablesItems(items)

	@staticmethod
	def SetEntityTamed(playerId, tamedId):
		tameComp = serverApi.GetEngineCompFactory().CreateTame(tamedId)
		return tameComp.SetEntityTamed(playerId,tamedId)

	@staticmethod
	def SetJumpPower(entityId, jumpPower):
		comp = serverApi.GetEngineCompFactory().CreateGravity(entityId)
		return comp.SetJumpPower(jumpPower)

	@staticmethod
	def SetMobKnockback(entityId, xd, zd, power, height, heightCap):
		comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
		return comp.SetMobKnockback(xd, zd, power, height, heightCap)

	@staticmethod
	def SetMotion(entityId, motion):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.SetMotion(motion)

	@staticmethod
	def SetMoveSetting(entityId, pos, speed, maxIteration, callback):
		comp = serverApi.GetEngineCompFactory().CreateMoveTo(entityId)
		return comp.SetMoveSetting(pos,speed,maxIteration,callback)

	@staticmethod
	def SetPersistence(entityId, isPersistent):
		comp = serverApi.GetEngineCompFactory().CreatePersistence(entityId)
		return comp.SetPersistence(isPersistent)

	@staticmethod
	def SetRidePos(entityId, tamedEntityId, pos):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.SetRidePos(tamedEntityId, pos)

	@staticmethod
	def SetRiderRideEntity(entityId, riderId, riddenEntityId, riderIndex):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.SetRiderRideEntity(riderId, riddenEntityId, riderIndex)

	@staticmethod
	def SetStepHeight(entityId, stepHeight):
		comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.SetStepHeight(stepHeight)

	@staticmethod
	def StartEntityMotion(entityId, motionId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.StartEntityMotion(motionId)

	@staticmethod
	def StopEntityMotion(entityId, motionId):
		motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.StopEntityMotion(motionId)

	@staticmethod
	def TriggerCustomEvent(entityId, eventName):
		comp = serverApi.GetEngineCompFactory().CreateEntityEvent(entityId)
		return comp.TriggerCustomEvent(entityId, eventName)


class Effect:

	@staticmethod
	def AddEffectToEntity(entityId, effectName, duration, amplifier, showParticles):
		comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
		return comp.AddEffectToEntity(effectName, duration, amplifier, showParticles)

	@staticmethod
	def GetAllEffects(entityId):
		comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
		return comp.GetAllEffects()

	@staticmethod
	def HasEffect(entityId, effectName):
		comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
		return comp.HasEffect(effectName)

	@staticmethod
	def RemoveEffectFromEntity(entityId, effectName):
		comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
		return comp.RemoveEffectFromEntity(effectName)


class Knapsack:

	@staticmethod
	def GetEntityItem(entityId, posType, slotPos, getUserData):
		comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
		return comp.GetEntityItem(posType, slotPos, getUserData)

	@staticmethod
	def GetEquItemEnchant(entityId, slotPos):
		comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
		return comp.GetEquItemEnchant(slotPos)

	@staticmethod
	def GetEquItemModEnchant(entityId, slotPos):
		comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
		return comp.GetEquItemModEnchant(slotPos)

	@staticmethod
	def SetEntityItem(entityId, posType, itemDict, slotPos):
		comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
		return comp.SetEntityItem(posType, itemDict, slotPos)


class ExtraAttribute:


	@staticmethod
	def GetAttr(entityId, paramName, defaultValue):
		comp = serverApi.GetEngineCompFactory().CreateModAttr(entityId)
		return comp.GetAttr(paramName, defaultValue)

	@staticmethod
	def SetAttr(entityId, paramName, paramValue, needRestore):
		comp = serverApi.GetEngineCompFactory().CreateModAttr(entityId)
		return comp.SetAttr(paramName, paramValue, needRestore)


class ExtraData:

	@staticmethod
	def CleanExtraData(ID, key):
		entitycomp = serverApi.GetEngineCompFactory().CreateExtraData(ID)
		return entitycomp.CleanExtraData(key)

	@staticmethod
	def GetExtraData(ID, key):
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
		entitycomp = serverApi.GetEngineCompFactory().CreateExtraData(ID)
		return entitycomp.SetExtraData(key,value,autoSave)


class Projectile:

	@staticmethod
	def GetSourceEntityId(entityId):
		comp = serverApi.GetEngineCompFactory().CreateBulletAttributes(entityId)
		return comp.GetSourceEntityId()


class ExperienceBall:

	@staticmethod
	def GetOrbExperience(entityId):
		comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
		return comp.GetOrbExperience()

	@staticmethod
	def SetOrbExperience(entityId, exp):
		comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
		return comp.SetOrbExperience(exp)


class OfficialPartner:

	@staticmethod
	def Disable():
		comp = serverApi.GetEngineCompFactory().CreatePet(levelId)
		return comp.Disable()

	@staticmethod
	def Enable():
		comp = serverApi.GetEngineCompFactory().CreatePet(levelId)
		return comp.Enable()


class Tag:

	@staticmethod
	def AddEntityTag(entityId, tag):
		comp = serverApi.GetEngineCompFactory().CreateTag(entityId)
		return comp.AddEntityTag(tag)

	@staticmethod
	def EntityHasTag(entityId, tag):
		comp = serverApi.GetEngineCompFactory().CreateTag(entityId)
		return comp.EntityHasTag(tag)

	@staticmethod
	def GetEntityTags(entityId):
		comp = serverApi.GetEngineCompFactory().CreateTag(entityId)
		return comp.GetEntityTags()

	@staticmethod
	def RemoveEntityTag(entityId, tag):
		comp = serverApi.GetEngineCompFactory().CreateTag(entityId)
		return comp.RemoveEntityTag(tag)


class OfficialChatExpansion:

	@staticmethod
	def Disable(playerId):
		comp = serverApi.GetEngineCompFactory().CreateChatExtension(playerId)
		return comp.Disable()

	@staticmethod
	def Enable(playerId):
		comp = serverApi.GetEngineCompFactory().CreateChatExtension(playerId)
		return comp.Enable()

	@staticmethod
	def RegisterChatPrefix(playerId, prefix, prefixColor):
		comp = serverApi.GetEngineCompFactory().CreateChatExtension(playerId)
		return comp.RegisterChatPrefix(prefix, prefixColor)

	@staticmethod
	def SetShowSocialNearbyInfo(playerId, show):
		comp = serverApi.GetEngineCompFactory().CreateChatExtension(playerId)
		return comp.SetShowSocialNearbyInfo(show)

