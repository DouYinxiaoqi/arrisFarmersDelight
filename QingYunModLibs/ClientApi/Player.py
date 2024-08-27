import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class Attribute:

	@staticmethod
	def GetArmorValue():
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetArmorValue(playerId)

	@staticmethod
	def GetPlayerCurLevelExp():
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetPlayerCurLevelExp(playerId)

	@staticmethod
	def GetPlayerHunger():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.GetPlayerHunger()

	@staticmethod
	def Swing():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(levelId)
		return comp.Swing()

	@staticmethod
	def getUid():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.getUid()


class Action:

	@staticmethod
	def BeginSprinting():
		comp = clientApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return comp.BeginSprinting()

	@staticmethod
	def EndSprinting():
		comp = clientApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return comp.EndSprinting()

	@staticmethod
	def GetEntityRider():
		comp = clientApi.GetEngineCompFactory().CreateRide(playerId)
		return comp.GetEntityRider()

	@staticmethod
	def isGliding():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.isGliding()

	@staticmethod
	def isInWater():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.isInWater()

	@staticmethod
	def isMoving():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.isMoving()

	@staticmethod
	def isRiding():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.isRiding()

	@staticmethod
	def isSneaking():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.isSneaking()

	@staticmethod
	def isSprinting():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.isSprinting()

	@staticmethod
	def isSwimming():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.isSwimming()

	@staticmethod
	def setMoving():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.setMoving()

	@staticmethod
	def setSneaking():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.setSneaking()

	@staticmethod
	def setSprinting():
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.setSprinting()

	@staticmethod
	def setUsingShield(flag):
		comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
		return comp.setUsingShield(flag)


class Render:

	@staticmethod
	def AddPlayerAnimation(playerId, animationKey, animationName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.AddPlayerAnimation(animationKey, animationName)

	@staticmethod
	def AddPlayerAnimationController(playerId, animationControllerKey, animationControllerName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.AddPlayerAnimationController(animationControllerKey, animationControllerName)

	@staticmethod
	def AddPlayerAnimationIntoState(playerId, animationControllerName, stateName, animationName, condition):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.AddPlayerAnimationIntoState(animationControllerName, stateName, animationName, condition)

	@staticmethod
	def AddPlayerGeometry(playerId, geometryKey, geometryName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.AddPlayerGeometry(geometryKey, geometryName)

	@staticmethod
	def AddPlayerParticleEffect(playerId, effectKey, effectName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.AddPlayerParticleEffect(effectKey, effectName)

	@staticmethod
	def AddPlayerRenderController(playerId, renderControllerName, condition):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.AddPlayerRenderController(renderControllerName, condition)

	@staticmethod
	def AddPlayerRenderMaterial(playerId, materialKey, materialName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.AddPlayerRenderMaterial(materialKey, materialName)

	@staticmethod
	def AddPlayerScriptAnimate(playerId, animateName, condition="", autoReplace=False):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.AddPlayerScriptAnimate(animateName, condition, autoReplace)

	@staticmethod
	def AddPlayerSoundEffect(playerId, soundKey, soundName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender()
		return comp.AddPlayerSoundEffect(soundKey, soundName)

	@staticmethod
	def AddPlayerTexture(playerId, geometryKey, geometryName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.AddPlayerTexture(geometryKey, geometryName)

	@staticmethod
	def RebuildPlayerRender(playerId):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.RebuildPlayerRender()

	@staticmethod
	def RemovePlayerAnimationController(playerId, animationControllKey):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.RemovePlayerAnimationController(animationControllKey)

	@staticmethod
	def RemovePlayerGeometry(playerId, geometryKey):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.RemovePlayerGeometry(geometryKey)

	@staticmethod
	def RemovePlayerRenderController(playerId, renderControllerName):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return comp.RemovePlayerRenderController(renderControllerName)

	@staticmethod
	def ResetSkin(playerId):
		comp = clientApi.GetEngineCompFactory().CreateModel(playerId)
		return comp.ResetSkin()

	@staticmethod
	def SetPlayerItemInHandVisible(playerId, visible, mode):
		actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
		return actorRenderComp.SetPlayerItemInHandVisible(visible, mode)


	@staticmethod
	def SetSkin(playerId, skin):
		comp = clientApi.GetEngineCompFactory().CreateModel(playerId)
		return comp.SetSkin(skin)


class Knapsack:

	@staticmethod
	def GetCarriedItem(getUserData):
		comp = clientApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetCarriedItem(getUserData)

	@staticmethod
	def GetOffhandItem(getUserData):
		comp = clientApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetOffhandItem(getUserData)

	@staticmethod
	def GetPlayerAllItems(posType, getUserData):
		comp = clientApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetPlayerAllItems(posType, getUserData)

	@staticmethod
	def GetPlayerItem(posType, slotPos, getUserData):
		comp = clientApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetPlayerItem(posType, slotPos, getUserData)

	@staticmethod
	def GetSlotId():
		comp = clientApi.GetEngineCompFactory().CreateItem(playerId)
		return comp.GetSlotId()

class Camera:

	@staticmethod
	def AddCameraAroundEntityMotion(eID, angularVelocity, axis, lockDir, stopRad, radius):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.AddCameraAroundEntityMotion(eID, angularVelocity, axis, lockDir, stopRad, radius)

	@staticmethod
	def AddCameraAroundPointMotion(center, angularVelocity, axis, lockDir, stopRad):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.AddCameraAroundPointMotion(center, angularVelocity, axis, lockDir, stopRad)

	@staticmethod
	def AddCameraTrackMotion(targetPos, duraTime, startPos, relativeCoord, isLoop, targetRot, startRot, useVelocityDir):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.AddCameraTrackMotion(targetPos, duraTime, startPos, relativeCoord, isLoop, targetRot, startRot, useVelocityDir)

	@staticmethod
	def AddCameraVelocityMotion(velocity, accelerate, useVelocityDir):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.AddCameraVelocityMotion(velocity, accelerate, useVelocityDir)

	@staticmethod
	def DepartCamera():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.DepartCamera()

	@staticmethod
	def GetCameraAnchor():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetCameraAnchor()

	@staticmethod
	def GetCameraMotions():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetCameraMotions()

	@staticmethod
	def GetCameraOffset():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetCameraOffset()

	@staticmethod
	def GetCameraPitchLimit():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetCameraPitchLimit()

	@staticmethod
	def GetCameraRotation():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetCameraRotation()

	@staticmethod
	def GetForward():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetForward()

	@staticmethod
	def GetFov():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetFov()

	@staticmethod
	def GetFpHeight():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetFpHeight()

	@staticmethod
	def GetPerspective(entityId):
		comp = clientApi.GetEngineCompFactory().CreatePlayerView(entityId)
		return comp.GetPerspective()

	@staticmethod
	def GetPosition():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetPosition()

	@staticmethod
	def IsModCameraLockPitch():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.IsModCameraLockPitch()

	@staticmethod
	def IsModCameraLockYaw():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.IsModCameraLockYaw()

	@staticmethod
	def LockCamera(lockPos, lockRot):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.LockCamera(lockPos, lockRot)

	@staticmethod
	def LockModCameraPitch(enable):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.LockModCameraPitch(enable)

	@staticmethod
	def LockModCameraYaw(enable):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.LockModCameraYaw(enable)

	@staticmethod
	def LockPerspective(entityId, lock):
		comp = clientApi.GetEngineCompFactory().CreatePlayerView(entityId)
		return comp.LockPerspective(lock)

	@staticmethod
	def RemoveCameraMotion(motionId):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.RemoveCameraMotion(motionId)

	@staticmethod
	def ResetCameraBindActorId():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.ResetCameraBindActorId()

	@staticmethod
	def SetCameraAnchor(offset):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.SetCameraAnchor(offset)

	@staticmethod
	def SetCameraBindActorId(targetId):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.SetCameraBindActorId(targetId)

	@staticmethod
	def SetCameraOffset(offset):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.SetCameraOffset(offset)

	@staticmethod
	def SetCameraPitchLimit(limit):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		comp.DepartCamera()
		return comp.SetCameraPitchLimit(limit)

	@staticmethod
	def SetCameraPos(pos):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.SetCameraPos(pos)

	@staticmethod
	def SetCameraRotation(rot):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.SetCameraRotation(rot)

	@staticmethod
	def SetFov(fov):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.SetFov(fov)

	@staticmethod
	def SetPerspective(persp):
		comp = clientApi.GetEngineCompFactory().CreatePlayerView(playerId)
		return comp.SetPerspective(persp)

	@staticmethod
	def SetSpeedFovLock(isLocked):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.SetSpeedFovLock(isLocked)

	@staticmethod
	def StartCameraMotion(motionId):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.StartCameraMotion(motionId)

	@staticmethod
	def StopCameraMotion(motionId):
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.StopCameraMotion(motionId)

	@staticmethod
	def UnDepartCamera():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.UnDepartCamera()

	@staticmethod
	def UnLockCamera():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.UnLockCamera()


class Animation:

    @staticmethod
    def PlayTpAnimation(anim):
        comp = clientApi.GetEngineCompFactory().CreatePlayerAnim(playerId)
        return comp.PlayTpAnimation(anim)

    @staticmethod
    def StopAnimation(anim):
        comp = clientApi.GetEngineCompFactory().CreatePlayerAnim(playerId)
        comp.StopAnimation(anim)


class PlayerGameType:

	@staticmethod
	def GetPlayerGameType(playerId):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetPlayerGameType(playerId)