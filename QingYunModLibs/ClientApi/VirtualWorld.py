import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class World:

	@staticmethod
	def VirtualWorldCreate():
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.VirtualWorldCreate()

	@staticmethod
	def VirtualWorldDestroy():
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.VirtualWorldDestroy()

	@staticmethod
	def VirtualWorldSetCollidersVisible(isVisible):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.VirtualWorldSetCollidersVisible(isVisible)

	@staticmethod
	def VirtualWorldSetSkyBgColor(color):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.VirtualWorldSetSkyBgColor(color)

	@staticmethod
	def VirtualWorldSetSkyTexture(texturePath, mode):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.VirtualWorldSetSkyTexture(texturePath, mode)

	@staticmethod
	def VirtualWorldToggleVisibility(isVisible):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.VirtualWorldToggleVisibility(isVisible)


class Camera:

	@staticmethod
	def CameraGetClickModel():
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraGetClickModel()

	@staticmethod
	def CameraGetFov():
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraGetFov()

	@staticmethod
	def CameraGetPos():
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraGetPos()

	@staticmethod
	def CameraGetZoom():
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraGetZoom()

	@staticmethod
	def CameraLookAt(targetPos, upVector):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraLookAt(targetPos, upVector)

	@staticmethod
	def CameraMoveTo(pos, targetPos, upVector, zoom, time, ease):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraMoveTo(pos, targetPos, upVector, zoom, time, ease)

	@staticmethod
	def CameraSetFov(fov):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraSetFov(fov)

	@staticmethod
	def CameraSetPos(pos):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraSetPos(pos)

	@staticmethod
	def CameraSetZoom(zoom):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraSetZoom(zoom)

	@staticmethod
	def CameraStopActions():
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.CameraStopActions()


class Model:

	@staticmethod
	def ModelCancelAllBoneMask(objId, animationName):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelCancelAllBoneMask(objId, animationName)

	@staticmethod
	def ModelCreateMinecraftObject(identifier):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelCreateMinecraftObject(identifier)

	@staticmethod
	def ModelCreateObject(modelName, animationName):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelCreateObject(modelName, animationName)

	@staticmethod
	def ModelGetPos(objId):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelGetPos(objId)

	@staticmethod
	def ModelGetRot(objId):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelGetRot(objId)

	@staticmethod
	def ModelIsVisible(objId):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelIsVisible(objId)

	@staticmethod
	def ModelMoveTo(objId, pos, time, ease):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelMoveTo(objId, pos, time, ease)

	@staticmethod
	def ModelPlayAnimation(objId, animationName, loop, isBlended, layer):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelPlayAnimation(objId, animationName, loop, isBlended, layer)

	@staticmethod
	def ModelRegisterAnim1DControlParam(objId, leftAniName, rightAniName, paramName):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelRegisterAnim1DControlParam(objId, leftAniName, rightAniName, paramName)

	@staticmethod
	def ModelRemove(objId):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelRemove(objId)

	@staticmethod
	def ModelRotate(objId, degreeAngle, axis):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelRotate(objId, degreeAngle, axis)

	@staticmethod
	def ModelRotateTo(objId, rot, time, ease):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelRotateTo(objId, rot, time, ease)

	@staticmethod
	def ModelSetAnim1DControlParam(objId, paramName, value):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelSetAnim1DControlParam(objId, paramName, value)

	@staticmethod
	def ModelSetAnimAllBoneMask(objId, animationName, ignoreBonesList, enable, applyToChild):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelSetAnimAllBoneMask(objId, animationName, ignoreBonesList, enable, applyToChild)

	@staticmethod
	def ModelSetAnimBoneMask(objId, animationName, boneNamesList, enable, applyToChild):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelSetAnimBoneMask(objId, animationName, boneNamesList, enable, applyToChild)

	@staticmethod
	def ModelSetAnimLayer(objId, animationName, layer):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelSetAnimLayer(objId, animationName, layer)

	@staticmethod
	def ModelSetBoxCollider(objId, lengths, offset):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelSetBoxCollider(objId, lengths, offset)

	@staticmethod
	def ModelSetPos(objId, pos):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelSetPos(objId, pos)

	@staticmethod
	def ModelSetRot(objId, rot):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelSetRot(objId, rot)

	@staticmethod
	def ModelSetScale(objId, scales):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelSetScale(objId, scales)

	@staticmethod
	def ModelSetVisible(objId, isVisible):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelSetVisible(objId, isVisible)

	@staticmethod
	def ModelStopActions(objId):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelStopActions(objId)

	@staticmethod
	def ModelStopAnimation(objId, animationName):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelStopAnimation(objId, animationName)

	@staticmethod
	def ModelUpdateAnimationMolangVariable(objId, molangDict):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.ModelUpdateAnimationMolangVariable(objId, molangDict)


class Other:

	@staticmethod
	def BindModel(virtualWorldObjectType, objId, targetId, posOffset, rotOffset, boneName):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.BindModel(virtualWorldObjectType, objId, targetId, posOffset, rotOffset, boneName)

	@staticmethod
	def MoveToVirtualWorld(virtualWorldObjectType, objId):
		virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(levelId)
		return virtualWorldComp.MoveToVirtualWorld(virtualWorldObjectType, objId)