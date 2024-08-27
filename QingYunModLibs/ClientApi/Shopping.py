import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class Shopping:

	@staticmethod
	def CloseShopWindow():
		comp = clientApi.GetEngineCompFactory().CreateNeteaseShop(levelId)
		return comp.CloseShopWindow()

	@staticmethod
	def HideShopGate():
		comp = clientApi.GetEngineCompFactory().CreateNeteaseShop(levelId)
		return comp.HideShopGate()

	@staticmethod
	def OpenItemDetailWindow(categoryName, itemName):
		comp = clientApi.GetEngineCompFactory().CreateNeteaseShop(levelId)
		return comp.OpenItemDetailWindow(categoryName, itemName)

	@staticmethod
	def OpenShopWindow():
		comp = clientApi.GetEngineCompFactory().CreateNeteaseShop(levelId)
		return comp.OpenShopWindow()

	@staticmethod
	def ShowShopGate():
		comp = clientApi.GetEngineCompFactory().CreateNeteaseShop(levelId)
		return comp.ShowShopGate()

