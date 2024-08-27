import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class EngineType:

	@staticmethod
	def GetEngineType(entityId):
		comp = clientApi.GetEngineCompFactory().CreateEngineType(entityId)
		return comp.GetEngineType()

	@staticmethod
	def GetEngineTypeStr(entityId):
		comp = clientApi.GetEngineCompFactory().CreateEngineType(entityId)
		return comp.GetEngineTypeStr()


class Aux:

	@staticmethod
	def GetAuxValue(entityId):
		comp = clientApi.GetEngineCompFactory().CreateAuxValue(entityId)
		return comp.GetAuxValue()


class Attribute:

	@staticmethod
	def GetAttrMaxValue(entityId, types):
		comp = clientApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.GetAttrMaxValue(types)

	@staticmethod
	def GetAttrValue(entityId, attrType):
		comp = clientApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.GetAttrValue(attrType)

	@staticmethod
	def GetBodyRot(entityId):
		comp = clientApi.GetEngineCompFactory().CreateRot(entityId)
		return comp.GetBodyRot()

	@staticmethod
	def GetFootPos(entityId):
		comp = clientApi.GetEngineCompFactory().CreatePos(entityId)
		return comp.GetFootPos()

	@staticmethod
	def GetName(entityId):
		comp = clientApi.GetEngineCompFactory().CreateName(entityId)
		return comp.GetName()

	@staticmethod
	def GetPos(entityId):
		comp = clientApi.GetEngineCompFactory().CreatePos(entityId)
		return comp.GetPos()

	@staticmethod
	def GetRiderId(playerId):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetRiderId(playerId)

	@staticmethod
	def GetRot(entityId):
		comp = clientApi.GetEngineCompFactory().CreateRot(entityId)
		return comp.GetRot()

	@staticmethod
	def GetSize(entityId):
		comp = clientApi.GetEngineCompFactory().CreateCollisionBox(entityId)
		return comp.GetSize()

	@staticmethod
	def LockLocalPlayerRot(entityId, lock):
		comp = clientApi.GetEngineCompFactory().CreateRot(entityId)
		return comp.LockLocalPlayerRot(lock)

	@staticmethod
	def SetPlayerLookAtPos(targetPos, pitchStep, yawStep, blockInput):
		comp = clientApi.GetEngineCompFactory().CreateRot(playerId)
		return comp.SetPlayerLookAtPos(targetPos, pitchStep, yawStep, blockInput)

	@staticmethod
	def SetRot(entityId, rot):
		comp = clientApi.GetEngineCompFactory().CreateRot(entityId)
		return comp.SetRot(rot)

	@staticmethod
	def isEntityInLava(entityId):
		comp = clientApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.isEntityInLava()

	@staticmethod
	def isEntityOnGround(entityId):
		comp = clientApi.GetEngineCompFactory().CreateAttr(entityId)
		return comp.isEntityOnGround()


class Action:

	@staticmethod
	def GetAttackTarget(entityId):
		comp = clientApi.GetEngineCompFactory().CreateAction(entityId)
		return comp.GetAttackTarget()

	@staticmethod
	def GetMotion(entityId):
		motionComp = clientApi.GetEngineCompFactory().CreateActorMotion(entityId)
		return motionComp.GetMotion()

	@staticmethod
	def GetOwnerId(entityId):
		comp = clientApi.GetEngineCompFactory().CreateTame(entityId)
		return comp.GetOwnerId()

	@staticmethod
	def SetMotion(motion):
		motionComp = clientApi.GetEngineCompFactory().CreateActorMotion(playerId)
		motionComp.SetMotion(motion)


class Effect:

	@staticmethod
	def GetAllEffects(entityId):
		comp = clientApi.GetEngineCompFactory().CreateEffect(entityId)
		return comp.GetAllEffects()

	@staticmethod
	def HasEffect(entityId, effectName):
		comp = clientApi.GetEngineCompFactory().CreateEffect(entityId)
		return comp.HasEffect(effectName)


class Render:

	@staticmethod
	def AddActorAnimation(actorIdentifier, animationKey, animationName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.AddActorAnimation(actorIdentifier, animationKey, animationName)

	@staticmethod
	def AddActorAnimationController(entityId, actorIdentifier, animationControllerKey, animationControllerName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return comp.AddActorAnimationController(actorIdentifier, animationControllerKey, animationControllerName)

	@staticmethod
	def AddActorBlockGeometry(entityId, geometryName, offset, rotation):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return actorRenderComp.AddActorBlockGeometry(geometryName, offset, rotation)

	@staticmethod
	def AddActorGeometry(actorIdentifier, geometryKey, geometryName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.AddActorGeometry(actorIdentifier, geometryKey, geometryName)

	@staticmethod
	def AddActorParticleEffect(actorIdentifier, effectKey, effectName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.AddActorParticleEffect(actorIdentifier, effectKey, effectName)

	@staticmethod
	def AddActorRenderController(actorIdentifier, renderControllerName, condition):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.AddActorRenderController(actorIdentifier, renderControllerName, condition)

	@staticmethod
	def AddActorRenderControllerArray(entityId, actorIdentifier, renderControllerName, arrayType, arrayName, expression):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return comp.AddActorRenderControllerArray(actorIdentifier, renderControllerName, arrayType, arrayName, expression)

	@staticmethod
	def AddActorRenderMaterial(actorIdentifier, materialKey, materialName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.AddActorRenderMaterial(actorIdentifier, materialKey, materialName)

	@staticmethod
	def AddActorScriptAnimate(actorIdentifier, animateName, condition, autoReplace):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(actorIdentifier)
		return comp.AddActorScriptAnimate(actorIdentifier, animateName, condition, autoReplace)

	@staticmethod
	def AddActorSoundEffect(actorIdentifier, soundKey, soundName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.AddActorSoundEffect(actorIdentifier, soundKey, soundName)

	@staticmethod
	def AddActorTexture(actorIdentifier, textureKey, texturePath):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.AddActorTexture(actorIdentifier, textureKey, texturePath)

	@staticmethod
	def BindEntityToEntity(entityId):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.BindEntityToEntity(entityId)

	@staticmethod
	def ClearActorBlockGeometry(entityId):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return actorRenderComp.ClearActorBlockGeometry()

	@staticmethod
	def CopyActorGeometryFromPlayer(fromPlayerId, toActorIdentifier, fromGeometryKey, newGeometryKey):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.CopyActorGeometryFromPlayer(fromPlayerId, toActorIdentifier, fromGeometryKey, newGeometryKey)

	@staticmethod
	def CopyActorRenderMaterialFromPlayer(fromPlayerId, toActorIdentifier, fromMaterialKey, newMaterialKey):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.CopyActorRenderMaterialFromPlayer(fromPlayerId, toActorIdentifier, fromMaterialKey, newMaterialKey)

	@staticmethod
	def CopyActorTextureFromPlayer(fromPlayerId, toActorIdentifier, fromTextureKey, newTextureKey):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.CopyActorTextureFromPlayer(fromPlayerId, toActorIdentifier, fromTextureKey, newTextureKey)

	@staticmethod
	def DeleteActorBlockGeometry(entityId, geometryName):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return actorRenderComp.DeleteActorBlockGeometry(geometryName)

	@staticmethod
	def GetActorRenderParams(entityId, paramTypeStr):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.GetActorRenderParams(entityId, paramTypeStr)

	@staticmethod
	def GetNotRenderAtAll(entityId):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return comp.GetNotRenderAtAll()

	@staticmethod
	def RebuildActorRender(actorIdentifier):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.RebuildActorRender(actorIdentifier)

	@staticmethod
	def RemoveActorAnimationController(entityId, actorIdentifier, animationControllKey):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return comp.RemoveActorAnimationController(actorIdentifier, animationControllKey)

	@staticmethod
	def RemoveActorGeometry(actorIdentifier, geometryKey):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.RemoveActorGeometry(actorIdentifier, geometryKey)

	@staticmethod
	def RemoveActorRenderController(actorIdentifier, renderControllerName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.RemoveActorRenderController(actorIdentifier, renderControllerName)

	@staticmethod
	def RemoveActorTexture(actorIdentifier, textureKey):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.RemoveActorTexture(actorIdentifier, textureKey)

	@staticmethod
	def ResetBindEntity(entityId):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.ResetBindEntity()

	@staticmethod
	def SetActorAllBlockGeometryVisible(entityId, visible):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return actorRenderComp.SetActorAllBlockGeometryVisible(visible)

	@staticmethod
	def SetActorBlockGeometryVisible(entityId, geometryName, visible):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return actorRenderComp.SetActorBlockGeometryVisible(geometryName, visible)

	@staticmethod
	def SetAlwaysShowName(entityId, show):
		comp = clientApi.GetEngineCompFactory().CreateName(entityId)
		return comp.SetAlwaysShowName(show)

	@staticmethod
	def SetColor(entityId, front, back):
		comp = clientApi.GetEngineCompFactory().CreateHealth(entityId)
		return comp.SetColor(front, back)

	@staticmethod
	def SetHealthBarDeviation(entityId, health_bar_deviation):
		comp = clientApi.GetEngineCompFactory().CreateHealth(entityId)
		return comp.SetHealthBarDeviation(health_bar_deviation)

	@staticmethod
	def SetNameDeeptest(deeptest):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetNameDeeptest(deeptest)

	@staticmethod
	def SetNotRenderAtAll(entityId, notRender):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return comp.SetNotRenderAtAll(notRender)

	@staticmethod
	def SetRenderLocalPlayer(render):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SetRenderLocalPlayer(render)

	@staticmethod
	def SetShowName(entityId, show):
		comp = clientApi.GetEngineCompFactory().CreateName(entityId)
		return comp.SetShowName(show)

	@staticmethod
	def ShowHealth(entityId, show):
		comp = clientApi.GetEngineCompFactory().CreateHealth(entityId)
		return comp.ShowHealth(show)

	@staticmethod
	def ShowHealthBar(show):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.ShowHealthBar(show)


class ExtraAttribute:


	@staticmethod
	def GetAttr(entityId, paramName, defaultValue=None):
		comp = clientApi.GetEngineCompFactory().CreateModAttr(entityId)
		return comp.GetAttr(paramName, defaultValue)

	@staticmethod
	def RegisterUpdateFunc(entityId, paramName, func):
		comp = clientApi.GetEngineCompFactory().CreateModAttr(entityId)
		return comp.RegisterUpdateFunc(paramName, func)

	@staticmethod
	def SetAttr(entityId, paramName, paramValue):
		comp = clientApi.GetEngineCompFactory().CreateModAttr(entityId)
		return comp.SetAttr(paramName, paramValue)

	@staticmethod
	def UnRegisterUpdateFunc(entityId, paramName, func):
		comp = clientApi.GetEngineCompFactory().CreateModAttr(entityId)
		return comp.UnRegisterUpdateFunc(paramName, func)


class Molang:

	@staticmethod
	def Get(entityId, variableName):
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(entityId)
		return comp.Get(variableName)

	@staticmethod
	def GetMolangValue(entityId, molangName):
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(entityId)
		return comp.GetMolangValue(molangName)

	@staticmethod
	def GetStringHash64(key):
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(levelId)
		return comp.GetStringHash64(key)

	@staticmethod
	def Register(variableName, defalutValue):
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(levelId)
		return comp.Register(variableName, defalutValue)

	@staticmethod
	def Set(entityId, variableName, value):
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(entityId)
		return comp.Set(variableName, value)

	@staticmethod
	def UnRegister(variableName):
		comp = clientApi.GetEngineCompFactory().CreateQueryVariable(levelId)
		return comp.UnRegister(variableName)

