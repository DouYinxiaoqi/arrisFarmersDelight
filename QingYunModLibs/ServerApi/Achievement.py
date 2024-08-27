import mod.server.extraServerApi as serverApi
levelId = serverApi.GetLevelId()


class Achievement:

	@staticmethod
	def LobbyGetAchievementStorage(callback, playerId):
		comp = serverApi.GetEngineCompFactory().CreateAchievement(levelId)
		return comp.LobbyGetAchievementStorage(callback, playerId)

	@staticmethod
	def LobbySetAchievementStorage(callback, playerId, nodeId, delta, getExtraData):
		comp = serverApi.GetEngineCompFactory().CreateAchievement(levelId)
		return comp.LobbySetAchievementStorage(callback, playerId, nodeId, delta, getExtraData)