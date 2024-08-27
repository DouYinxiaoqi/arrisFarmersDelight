import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class Item:

	@staticmethod
	def ChangeArmorTextures(armorIdentifier, texturesDict, uiIconTexture):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
		return comp.ChangeArmorTextures(armorIdentifier, texturesDict, uiIconTexture)

	@staticmethod
	def ChangeItemTexture(identifier, texturePath):
		comp = clientApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.ChangeItemTexture(identifier, texturePath)

	@staticmethod
	def GetItemBasicInfo(itemName, auxValue, isEnchanted):
		comp = clientApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetItemBasicInfo(itemName, auxValue, isEnchanted)

	@staticmethod
	def GetItemEffectName(itemName, auxValue, userData):
		comp = clientApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetItemEffectName(itemName, auxValue, userData)

	@staticmethod
	def GetItemFormattedHoverText(itemName, auxValue, showCategory, userData):
		comp = clientApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetItemFormattedHoverText(itemName, auxValue, showCategory, userData)

	@staticmethod
	def GetItemHoverName(itemName, auxValue, userData):
		comp = clientApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetItemHoverName(itemName, auxValue, userData)

	@staticmethod
	def GetUserDataInEvent(eventName):
		comp = clientApi.GetEngineCompFactory().CreateItem(levelId)
		return comp.GetUserDataInEvent(eventName)

