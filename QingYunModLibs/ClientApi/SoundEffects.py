import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class SoundEffects:

	@staticmethod
	def DisableOriginMusic(disable):
		comp = clientApi.GetEngineCompFactory().CreateCustomAudio(levelId)
		return comp.DisableOriginMusic(disable)

	@staticmethod
	def PlayCustomMusic(name, pos, volume, pitch, loop, entityId):
		comp = clientApi.GetEngineCompFactory().CreateCustomAudio(levelId)
		return comp.PlayCustomMusic(name, pos, volume, pitch, loop, entityId)

	@staticmethod
	def PlayGlobalCustomMusic(name, volume, loop):
		comp = clientApi.GetEngineCompFactory().CreateCustomAudio(levelId)
		return comp.PlayGlobalCustomMusic(name, volume, loop)

	@staticmethod
	def SetCustomMusicLoop(name, loop):
		comp = clientApi.GetEngineCompFactory().CreateCustomAudio(levelId)
		return comp.SetCustomMusicLoop(name, loop)

	@staticmethod
	def SetCustomMusicLoopById(musicId, loop):
		comp = clientApi.GetEngineCompFactory().CreateCustomAudio(levelId)
		return comp.SetCustomMusicLoopById(musicId, loop)

	@staticmethod
	def StopCustomMusic(name, fadeOutTime):
		comp = clientApi.GetEngineCompFactory().CreateCustomAudio(levelId)
		return comp.StopCustomMusic(name, fadeOutTime)

	@staticmethod
	def StopCustomMusicById(musicId, fadeOutTime):
		comp = clientApi.GetEngineCompFactory().CreateCustomAudio(levelId)
		return comp.StopCustomMusicById(musicId, fadeOutTime)