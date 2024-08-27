import mod.server.extraServerApi as serverApi
levelId = serverApi.GetLevelId()

class LocalDevice:

	@staticmethod
	def GetPlatform():
		return serverApi.GetPlatform()

	@staticmethod
	def IsInApollo():
		return serverApi.IsInApollo()

	@staticmethod
	def IsInServer():
		return serverApi.IsInServer()


class Math:

	@staticmethod
	def GetDirFromRot(rot):
		return serverApi.GetDirFromRot(rot)

	@staticmethod
	def GetLocalPosFromWorld(pos, entityId):
		return serverApi.GetLocalPosFromWorld(pos, entityId)

	@staticmethod
	def GetRotFromDir(dir):
		return serverApi.GetRotFromDir(dir)

	@staticmethod
	def GetWorldPosFromLocal(pos, entityId):
		return serverApi.GetWorldPosFromLocal(pos, entityId)


class Tool:

	@staticmethod
	def AddRepeatedTimer(delay, func, args):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.AddRepeatedTimer(delay, func, args)

	@staticmethod
	def AddTimer(delay, func, args):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.AddTimer(delay, func, args)

	@staticmethod
	def CancelTimer(timer):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.CancelTimer(timer)

	@staticmethod
	def CheckNameValid(name):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.CheckNameValid(name)

	@staticmethod
	def CheckWordsValid(words):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.CheckWordsValid(words)

	@staticmethod
	def GetChinese(langStr):
		comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetChinese(langStr)

	@staticmethod
	def GetMinecraftEnum():
		return serverApi.GetMinecraftEnum()

	@staticmethod
	def StartCoroutine(iterOrFunc, callback):
		return serverApi.StartCoroutine(iterOrFunc, callback)

	@staticmethod
	def StopCoroutine(iter):
		return serverApi.StopCoroutine(iter)


class DeBug:

	@staticmethod
	def GetMcpModLogCanPostDump():
		return serverApi.GetMcpModLogCanPostDump()


	@staticmethod
	def PostMcpModDump(msg, *args, **kwargs):
		return serverApi.PostMcpModDump(msg, *args, **kwargs)

	@staticmethod
	def SetMcpModLogCanPostDump(canPost):
		return serverApi.SetMcpModLogCanPostDump(canPost)

	@staticmethod
	def StartMemProfile():
		return serverApi.StartMemProfile()

	@staticmethod
	def StartMultiProfile():
		return serverApi.StartMultiProfile()

	@staticmethod
	def StartProfile():
		return serverApi.StartProfile()

	@staticmethod
	def StartRecordEvent():
		return serverApi.StartRecordEvent()

	@staticmethod
	def StartRecordPacket():
		return serverApi.StartRecordPacket()

	@staticmethod
	def StopMemProfile(fileName):
		return serverApi.StopMemProfile(fileName)

	@staticmethod
	def StopMultiProfile(fileName):
		return serverApi.StopMultiProfile(fileName)

	@staticmethod
	def StopProfile(fileName):
		return serverApi.StopProfile(fileName)

	@staticmethod
	def StopRecordEvent():
		return serverApi.StartRecordEvent()

	@staticmethod
	def StopRecordPacket():
		return serverApi.StartRecordPacket()