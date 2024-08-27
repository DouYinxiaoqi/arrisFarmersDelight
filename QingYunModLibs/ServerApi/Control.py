import mod.server.extraServerApi as serverApi
levelId = serverApi.GetLevelId()


class Control:

	@staticmethod
	def SetShowRideUI(entityId, tamedEntityId, isShowUI):
		comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
		return comp.SetShowRideUI(tamedEntityId, isShowUI)