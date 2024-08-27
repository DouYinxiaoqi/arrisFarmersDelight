import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class Vignette:

	@staticmethod
	def CheckVignetteEnabled():
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.CheckVignetteEnabled()

	@staticmethod
	def SetEnableVignette(enable):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetEnableVignette(enable)

	@staticmethod
	def SetVignetteCenter(center):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetVignetteCenter(center)

	@staticmethod
	def SetVignetteRGB(color):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetVignetteRGB(color)

	@staticmethod
	def SetVignetteRadius(radius):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetVignetteRadius(radius)

	@staticmethod
	def SetVignetteSmoothness(radius):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetVignetteSmoothness(radius)


class GaussianBlur:

	@staticmethod
	def CheckGaussianBlurEnabled():
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.CheckGaussianBlurEnabled()

	@staticmethod
	def SetEnableGaussianBlur(enable):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetEnableGaussianBlur(enable)

	@staticmethod
	def SetGaussianBlurRadius(radius):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetGaussianBlurRadius(radius)


class Color:

	@staticmethod
	def CheckColorAdjustmentEnabled():
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.CheckColorAdjustmentEnabled()

	@staticmethod
	def SetColorAdjustmentBrightness(brightness):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetColorAdjustmentBrightness(brightness)

	@staticmethod
	def SetColorAdjustmentContrast(contrast):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetColorAdjustmentContrast(contrast)

	@staticmethod
	def SetColorAdjustmentSaturation(saturation):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetColorAdjustmentSaturation(saturation)

	@staticmethod
	def SetColorAdjustmentTint(intensity, color):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetColorAdjustmentTint(intensity, color)

	@staticmethod
	def SetEnableColorAdjustment(enable):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetEnableColorAdjustment(enable)


class LensEffects:

	@staticmethod
	def CheckDepthOfFieldEnabled():
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.CheckDepthOfFieldEnabled()

	@staticmethod
	def CheckLensStainEnabled():
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.CheckLensStainEnabled()

	@staticmethod
	def ResetLensStainTexture():
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.ResetLensStainTexture()

	@staticmethod
	def SetDepthOfFieldBlurRadius(radius):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetDepthOfFieldBlurRadius(radius)

	@staticmethod
	def SetDepthOfFieldFarBlurScale(scale):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetDepthOfFieldFarBlurScale(scale)

	@staticmethod
	def SetDepthOfFieldFocusDistance(distance):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetDepthOfFieldFocusDistance(distance)

	@staticmethod
	def SetDepthOfFieldNearBlurScale(scale):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetDepthOfFieldNearBlurScale(scale)

	@staticmethod
	def SetDepthOfFieldUseCenterFocus(enable):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetDepthOfFieldUseCenterFocus(enable)

	@staticmethod
	def SetEnableDepthOfField(enable):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetEnableDepthOfField(enable)

	@staticmethod
	def SetEnableLensStain(enable):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetEnableLensStain(enable)

	@staticmethod
	def SetLensStainColor(intensity, color):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetLensStainColor(intensity, color)

	@staticmethod
	def SetLensStainIntensity(intensity):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetLensStainIntensity(intensity)

	@staticmethod
	def SetLensStainTexture(texturePath):
		comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
		return comp.SetLensStainTexture(texturePath)