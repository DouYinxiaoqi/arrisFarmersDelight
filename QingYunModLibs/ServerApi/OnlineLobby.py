import mod.server.extraServerApi as serverApi
levelId = serverApi.GetLevelId()


class OnlineLobby:

	@staticmethod
	def GetPlayerUid(playerId):
		comp = serverApi.GetEngineCompFactory().CreateHttp(levelId)
		return comp.GetPlayerUid(playerId)

	@staticmethod
	def LobbyGetStorage(callback, uid, keys):
		comp = serverApi.GetEngineCompFactory().CreateHttp(levelId)
		return comp.LobbyGetStorage(callback, uid, keys)

	@staticmethod
	def LobbyGetStorageBySort(callback, key, ascend, offset, length):
		comp = serverApi.GetEngineCompFactory().CreateHttp(levelId)
		return comp.LobbyGetStorageBySort(callback, key, ascend, offset, length)

	@staticmethod
	def LobbySetStorageAndUserItem(callback, uid, orderId, entitiesGetter):
		comp = serverApi.GetEngineCompFactory().CreateHttp(levelId)
		return comp.LobbySetStorageAndUserItem(callback, uid, orderId, entitiesGetter)

	@staticmethod
	def QueryLobbyUserItem(callback, uid):
		comp = serverApi.GetEngineCompFactory().CreateHttp(levelId)
		return comp.QueryLobbyUserItem(callback, uid)