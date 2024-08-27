import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class Model:

	@staticmethod
	def BindModelToEntity(entityId, boneName, modelName, offset, rot):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.BindModelToEntity(boneName, modelName, offset, rot)

	@staticmethod
	def BindModelToModel(modelId, boneName, modelName):
		comp = clientApi.GetEngineCompFactory().CreateModel(modelId)
		return comp.BindModelToModel(boneName, modelName)

	@staticmethod
	def CancelAllBoneMask(entityId, modelId, aniName):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.CancelAllBoneMask(modelId, aniName)

	@staticmethod
	def CreateFreeModel(entityId, modelName):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.CreateFreeModel(modelName)

	@staticmethod
	def GetAllBindModelToEntity(entityId, boneName):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.GetAllBindModelToEntity(boneName)

	@staticmethod
	def GetAnimLength(entityId, aniName):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.GetAnimLength(aniName)

	@staticmethod
	def GetBoneWorldPos(entityId, boneName):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.GetBoneWorldPos(boneName)

	@staticmethod
	def GetEntityBoneWorldPos(entityId, boneName):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.GetEntityBoneWorldPos(entityId, boneName)

	@staticmethod
	def GetModelId(entityId):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.GetModelId()

	@staticmethod
	def GetModelStyle(entityId):
		comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
		return comp.GetModelStyle()

	@staticmethod
	def GetPlayingAnimList(entityId, modelId):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.GetPlayingAnimList(modelId)

	@staticmethod
	def GetTexture(entityId):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.GetTexture()

	@staticmethod
	def HideModel(entityId, modelId):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.HideModel(modelId)

	@staticmethod
	def ModelPlayAni(entityId, modelId, aniName, isLoop, isBlended, layer):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.ModelPlayAni(modelId, aniName, isLoop, isBlended, layer)

	@staticmethod
	def ModelStopAni(entityId, modelId, aniName):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.ModelStopAni(modelId, aniName)

	@staticmethod
	def PlayAnim(entityId, aniName, isLoop):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.PlayAnim(aniName, isLoop)

	@staticmethod
	def RegisterAnim1DControlParam(entityId, modelId, leftAniName, rightAniName, paramName):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.RegisterAnim1DControlParam(modelId, leftAniName, rightAniName, paramName)

	@staticmethod
	def RemoveFreeModel(entityId, modelId):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.RemoveFreeModel(modelId)

	@staticmethod
	def ResetModel(entityId):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.ResetModel()

	@staticmethod
	def SetAnim1DControlParam(entityId, modelId, paramName, value):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetAnim1DControlParam(modelId, paramName, value)

	@staticmethod
	def SetAnimLayer(entityId, modelId, aniName, layer):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetAnimLayer(modelId, aniName, layer)

	@staticmethod
	def SetAnimSpeed(entityId, aniName, speed):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetAnimSpeed(aniName, speed)

	@staticmethod
	def SetAnimationAllBoneMask(entityId, modelId, aniName, ignoreBonesList, enable, applyToChild):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetAnimationAllBoneMask(modelId, aniName, ignoreBonesList, enable, applyToChild)

	@staticmethod
	def SetAnimationBoneMask(entityId, modelId, aniName, boneNamesList, enable, applyToChild):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetAnimationBoneMask(modelId, aniName, boneNamesList, enable, applyToChild)

	@staticmethod
	def SetBrightness(entityId, brightness):
		comp = clientApi.GetEngineCompFactory().CreateBrightness(entityId)
		return comp.SetBrightness(brightness)

	@staticmethod
	def SetEntityOpacity(entityId, opacity):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetEntityOpacity(opacity)

	@staticmethod
	def SetEntityShadowShow(entityId, flag):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetEntityShadowShow(flag)

	@staticmethod
	def SetExtraUniformValue(entityId, modelId, uniformIndex, vec4data):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetExtraUniformValue(modelId, uniformIndex, vec4data)

	@staticmethod
	def SetFreeModelAniSpeed(modelId, aniName, speed):
		comp = clientApi.GetEngineCompFactory().CreateModel(levelId)
		return comp.SetFreeModelAniSpeed(modelId, aniName, speed)

	@staticmethod
	def SetFreeModelBoundingBox(modelId, mins, maxs):
		comp = clientApi.GetEngineCompFactory().CreateModel(levelId)
		return comp.SetFreeModelBoundingBox(modelId, mins, maxs)

	@staticmethod
	def SetFreeModelPos(entityId, modelId, x, y, z):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetFreeModelPos(modelId, x, y, z)

	@staticmethod
	def SetFreeModelRot(entityId, modelId, x, y, z):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetFreeModelRot(modelId, x, y, z)

	@staticmethod
	def SetFreeModelScale(entityId, modelId, x, y, z):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetFreeModelScale(modelId, x, y, z)

	@staticmethod
	def SetLegacyBindRot(entityId, enable):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetLegacyBindRot(enable)

	@staticmethod
	def SetModel(entityId, modelName):
		comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
		return comp.SetModelPerspectiveEffect(modelName)