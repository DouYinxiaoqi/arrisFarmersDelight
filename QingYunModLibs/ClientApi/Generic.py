import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()

class LocalDevice:

	@staticmethod
	def GetIP():
		return clientApi.GetIP()

	@staticmethod
	def GetPlatform():
		return clientApi.GetPlatform()


class localStorage:

	@staticmethod
	def GetConfigData(configName, isGlobal):
		comp = clientApi.GetEngineCompFactory().CreateConfigClient(levelId)
		return comp.GetConfigData(configName, isGlobal)

	@staticmethod
	def SetConfigData(configName, value, isGlobal):
		comp = clientApi.GetEngineCompFactory().CreateConfigClient(levelId)
		return comp.SetConfigData(configName, value, isGlobal)


class Math:

	@staticmethod
	def GetDirFromRot(rot):
		return clientApi.GetDirFromRot(rot)

	@staticmethod
	def GetLocalPosFromWorld(pos, entityId):
		return clientApi.GetLocalPosFromWorld(pos, entityId)

	@staticmethod
	def GetRotFromDir(dir):
		return clientApi.GetRotFromDir(dir)

	@staticmethod
	def GetWorldPosFromLocal(pos, entityId):
		return clientApi.GetWorldPosFromLocal(pos, entityId)


class Tool:

	@staticmethod
	def AddRepeatedTimer(delay, func, args):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.AddRepeatedTimer(delay, func, args)

	@staticmethod
	def AddTimer(delay, func, args=None):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		if args == None:
			return comp.AddTimer(delay, func)
		return comp.AddTimer(delay, func, args)


	@staticmethod
	def CancelTimer(timer):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.CancelTimer(timer)

	@staticmethod
	def CheckNameValid(name):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.CheckNameValid(name)

	@staticmethod
	def CheckWordsValid(words):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.CheckWordsValid(words)

	@staticmethod
	def GetChinese(langStr):
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetChinese(langStr)

	@staticmethod
	def GetFps():
		comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
		return comp.GetFps()

	@staticmethod
	def GetMinecraftEnum():
		return clientApi.GetMinecraftEnum()

	@staticmethod
	def GetModConfigJson(path):
		return clientApi.GetModConfigJson(path)

	@staticmethod
	def StartCoroutine(iterOrFunc, callback):
		return clientApi.StartCoroutine(iterOrFunc, callback)

	@staticmethod
	def StopCoroutine(iter):
		return clientApi.StopCoroutine(iter)


class DeBug:

	@staticmethod
	def GetEnableReconnectNetgame():
		return clientApi.GetEnableReconnectNetgame()

	@staticmethod
	def GetKeepResourceWhenTransfer():
		return clientApi.GetKeepResourceWhenTransfer()

	@staticmethod
	def GetMcpModLogCanPostDump():
		return clientApi.GetMcpModLogCanPostDump()

	@staticmethod
	def GetResourceFastload():
		return clientApi.GetResourceFastload()

	@staticmethod
	def PostMcpModDump(msg, *args, **kwargs):
		return clientApi.PostMcpModDump(msg, *args, **kwargs)

	@staticmethod
	def ReloadAllMaterials():
		return clientApi.ReloadAllMaterials()

	@staticmethod
	def ReloadAllShaders():
		return clientApi.ReloadAllShaders()

	@staticmethod
	def ReloadOneShader(shaderName):
		return clientApi.ReloadOneShader(shaderName)

	@staticmethod
	def SetEnableReconnectNetgame(keep):
		return clientApi.SetEnableReconnectNetgame(keep)

	@staticmethod
	def SetKeepResourceWhenTransfer(keep):
		return clientApi.SetKeepResourceWhenTransfer(keep)

	@staticmethod
	def SetMcpModLogCanPostDump(canPost):
		return clientApi.SetMcpModLogCanPostDump(canPost)

	@staticmethod
	def SetResourceFastload(fastload):
		return clientApi.SetResourceFastload(fastload)

	@staticmethod
	def StartMemProfile():
		return clientApi.StartMemProfile()

	@staticmethod
	def StartMultiProfile():
		return clientApi.StartMultiProfile()

	@staticmethod
	def StartProfile():
		return clientApi.StartProfile()

	@staticmethod
	def StopMemProfile(fileName):
		return clientApi.StopMemProfile(fileName)

	@staticmethod
	def StopMultiProfile(fileName):
		return clientApi.StopMultiProfile(fileName)

	@staticmethod
	def StopProfile(fileName):
		return clientApi.StopProfile(fileName)