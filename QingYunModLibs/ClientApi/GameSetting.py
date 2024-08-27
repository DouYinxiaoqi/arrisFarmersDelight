import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class GameSetting:

	@staticmethod
	def GetToggleOption(optionId):
		comp = clientApi.GetEngineCompFactory().CreatePlayerView(levelId)
		return comp.GetToggleOption(optionId)

	@staticmethod
	def GetUIProfile():
		comp = clientApi.GetEngineCompFactory().CreatePlayerView(levelId)
		return comp.GetUIProfile()

	@staticmethod
	def HighlightBoxSelection(isHighlight):
		comp = clientApi.GetEngineCompFactory().CreatePlayerView(levelId)
		return comp.HighlightBoxSelection(isHighlight)

	@staticmethod
	def SetSplitControlCanChange(canChange):
		comp = clientApi.GetEngineCompFactory().CreatePlayerView(levelId)
		return comp.SetSplitControlCanChange(canChange)

	@staticmethod
	def SetToggleOption(optionId, isOn):
		comp = clientApi.GetEngineCompFactory().CreatePlayerView(levelId)
		return comp.SetToggleOption(optionId, isOn)

	@staticmethod
	def SetUIProfile(profileType):
		comp = clientApi.GetEngineCompFactory().CreatePlayerView(levelId)
		return comp.SetUIProfile(profileType)