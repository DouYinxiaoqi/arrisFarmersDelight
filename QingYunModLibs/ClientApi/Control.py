import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class Control:

	@staticmethod
	def AddPickBlacklist(entityId):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.AddPickBlacklist(entityId)

	@staticmethod
	def ClearPickBlacklist():
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.ClearPickBlacklist()

	@staticmethod
	def GetChosen():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetChosen()

	@staticmethod
	def GetChosenEntity():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.GetChosenEntity()

	@staticmethod
	def GetHoldTimeThresholdInMs():
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.GetHoldTimeThresholdInMs()

	@staticmethod
	def GetInputVector():
		comp = clientApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return comp.GetInputVector()

	@staticmethod
	def GetMousePosition():
		comp = clientApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return comp.GetMousePosition()

	@staticmethod
	def GetTouchPos():
		return clientApi.GetTouchPos()

	@staticmethod
	def LockInputVector(inputVector):
		motionComp = clientApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.LockInputVector(inputVector)

	@staticmethod
	def LockVerticalMove(flag):
		comp = clientApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return comp.LockVerticalMove(flag)

	@staticmethod
	def PickFacing():
		comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
		return comp.PickFacing()

	@staticmethod
	def SetCanAll(all):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanAll(all)

	@staticmethod
	def SetCanAttack(attack):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanAttack(attack)

	@staticmethod
	def SetCanChat(chat):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanChat(chat)

	@staticmethod
	def SetCanDrag(drag):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanDrag(drag)

	@staticmethod
	def SetCanInair(inair):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanInair(inair)

	@staticmethod
	def SetCanJump(jump):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanJump(jump)

	@staticmethod
	def SetCanMove(move):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanMove(move)

	@staticmethod
	def SetCanOpenInv(open):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanOpenInv(open)

	@staticmethod
	def SetCanPause(pause):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanPause(pause)

	@staticmethod
	def SetCanPerspective(persp):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanPerspective(persp)

	@staticmethod
	def SetCanScreenShot(shot):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanScreenShot(shot)

	@staticmethod
	def SetCanWalkMode(walkmode):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetCanWalkMode(walkmode)

	@staticmethod
	def SetDeviceVibrate(milliSeconds):
		comp = clientApi.GetEngineCompFactory().CreateDevice(playerId)
		return comp.SetDeviceVibrate(milliSeconds)

	@staticmethod
	def SetHoldTimeThreshold(time):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetHoldTimeThreshold(time)

	@staticmethod
	def SetMoveLock(movelock):
		comp = clientApi.GetEngineCompFactory().CreateOperation(levelId)
		return comp.SetMoveLock(movelock)

	@staticmethod
	def SimulateTouchWithMouse(touch):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.SimulateTouchWithMouse(touch)

	@staticmethod
	def UnLockVerticalMove():
		comp = clientApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return comp.UnLockVerticalMove()

	@staticmethod
	def UnlockInputVector():
		motionComp = clientApi.GetEngineCompFactory().CreateActorMotion(playerId)
		return motionComp.UnlockInputVector()