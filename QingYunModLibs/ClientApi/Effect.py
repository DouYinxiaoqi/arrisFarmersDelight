import mod.client.extraClientApi as clientApi
levelId = clientApi.GetLevelId()
playerId = clientApi.GetLocalPlayerId()


class TextPanel:

	@staticmethod
	def CreateTextBoardInWorld(text, textColor, boardColor, faceCamera):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.CreateTextBoardInWorld(text, textColor, boardColor, faceCamera)

	@staticmethod
	def RemoveTextBoard(boardId):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.RemoveTextBoard(boardId)

	@staticmethod
	def SetBoardBackgroundColor(boardId, backgroundColor):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.SetBoardBackgroundColor(boardId, backgroundColor)

	@staticmethod
	def SetBoardBindEntity(boardId, bindEntityId, offset, rot):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.SetBoardBindEntity(boardId, bindEntityId, offset, rot)

	@staticmethod
	def SetBoardDepthTest(boardId, depthTest):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.SetBoardDepthTest(boardId, depthTest)

	@staticmethod
	def SetBoardFaceCamera(boardId, faceCamera):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.SetBoardFaceCamera(boardId, faceCamera)

	@staticmethod
	def SetBoardPos(boardId, pos):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.SetBoardPos(boardId, pos)

	@staticmethod
	def SetBoardRot(boardId, rot):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.SetBoardRot(boardId, rot)

	@staticmethod
	def SetBoardScale(boardId, scale):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.SetBoardScale(boardId, scale)

	@staticmethod
	def SetBoardTextColor(boardId, textColor):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.SetBoardTextColor(boardId, textColor)

	@staticmethod
	def SetText(boardId, text):
		comp = clientApi.GetEngineCompFactory().CreateTextBoard(levelId)
		return comp.SetText(boardId, text)


class SFX:

	@staticmethod
	def Bind(frameEntityId, bindEntityId, offset, rot):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniEntityBind(frameEntityId)
		return comp.Bind(bindEntityId, offset, rot)

	@staticmethod
	def GetPos(frameEntityId):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
		return comp.GetPos()

	@staticmethod
	def GetRot(frameEntityId):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
		return comp.GetRot()

	@staticmethod
	def GetScale(frameEntityId):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
		return comp.GetScale()

	@staticmethod
	def Pause(frameEntityId):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.Pause()

	@staticmethod
	def Play(frameEntityId):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.Play()

	@staticmethod
	def SetDeepTest(frameEntityId, deepTest):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.SetDeepTest(deepTest)

	@staticmethod
	def SetFaceCamera(frameEntityId, face):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.SetFaceCamera(face)

	@staticmethod
	def SetFadeDistance(frameEntityId, fadeDistance):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.SetFadeDistance(fadeDistance)

	@staticmethod
	def SetLayer(frameEntityId, layer):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.SetLayer(layer)

	@staticmethod
	def SetLoop(frameEntityId, loop):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.SetLoop(loop)

	@staticmethod
	def SetMixColor(frameEntityId, color):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.SetMixColor(color)

	@staticmethod
	def SetPos(frameEntityId, pos):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
		return comp.SetPos(pos)

	@staticmethod
	def SetRot(frameEntityId, rot):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
		return comp.SetRot(rot)

	@staticmethod
	def SetRotUseZXY(frameEntityId, rot):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
		return comp.SetRotUseZXY(rot)

	@staticmethod
	def SetScale(frameEntityId, scale):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
		return comp.SetScale(scale)

	@staticmethod
	def SetUsePointFiltering(frameEntityId, use):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.SetUsePointFiltering(use)

	@staticmethod
	def Stop(frameEntityId):
		comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
		return comp.Stop()


class Particle:

	@staticmethod
	def Bind(particleEntityId, bindEntityId, offset, rot, correction):
		comp = clientApi.GetEngineCompFactory().CreateParticleEntityBind(particleEntityId)
		return comp.Bind(bindEntityId, offset, rot, correction)

	@staticmethod
	def GetParticleEmissionRate(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.GetParticleEmissionRate()

	@staticmethod
	def GetParticleMaxNum(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.GetParticleMaxNum()

	@staticmethod
	def GetParticleMaxSize(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.GetParticleMaxSize()

	@staticmethod
	def GetParticleMinSize(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.GetParticleMinSize()

	@staticmethod
	def GetParticleVolumeSize(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.GetParticleVolumeSize()

	@staticmethod
	def GetPos(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleTrans(particleEntityId)
		return comp.GetPos()

	@staticmethod
	def GetRot(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleTrans(particleEntityId)
		return comp.GetRot()

	@staticmethod
	def Pause(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.Pause()

	@staticmethod
	def Play(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.Play()

	@staticmethod
	def SetFadeDistance(particleEntityId, fadeDistance):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.SetFadeDistance(fadeDistance)

	@staticmethod
	def SetLayer(particleEntityId, layer):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.SetLayer(layer)

	@staticmethod
	def SetParticleEmissionRate(particleEntityId, minRate, maxRate):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.SetParticleEmissionRate(minRate, maxRate)

	@staticmethod
	def SetParticleMaxNum(particleEntityId, num):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.SetParticleMaxNum(num)

	@staticmethod
	def SetParticleSize(particleEntityId, minSize, maxSize):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.SetParticleSize(minSize, maxSize)

	@staticmethod
	def SetParticleVolumeSize(particleEntityId, scale):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.SetParticleVolumeSize(scale)

	@staticmethod
	def SetPos(particleEntityId, pos):
		comp = clientApi.GetEngineCompFactory().CreateParticleTrans(particleEntityId)
		return comp.SetPos(pos)

	@staticmethod
	def SetRelative(particleEntityId, relative):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.SetRelative(relative)

	@staticmethod
	def SetRotUseZXY(particleEntityId, rot):
		comp = clientApi.GetEngineCompFactory().CreateParticleTrans(particleEntityId)
		return comp.SetRotUseZXY(rot)

	@staticmethod
	def SetUsePointFiltering(particleEntityId, enable):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.SetUsePointFiltering(enable)

	@staticmethod
	def Stop(particleEntityId):
		comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
		return comp.Stop()


class ModelEffect:

	@staticmethod
	def Pause(effectEntityId):
		comp = clientApi.GetEngineCompFactory().CreateEngineEffectBindControl(effectEntityId)
		return comp.Pause()

	@staticmethod
	def Resume(effectEntityId):
		comp = clientApi.GetEngineCompFactory().CreateEngineEffectBindControl(effectEntityId)
		return comp.Resume()


class MicrosoftParticle:

	@staticmethod
	def BindEntity(par_id, entity_id, bone_name, offset, rotation):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.BindEntity(par_id, entity_id, bone_name, offset, rotation)

	@staticmethod
	def BindModel(par_id, model_id, bone_name, offset, rotation):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(levelId)
		return comp.BindModel(par_id, model_id, bone_name, offset, rotation)

	@staticmethod
	def Create(effect_name, offset, rotation):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Create(effect_name, offset, rotation)

	@staticmethod
	def CreateBindEntity(effect_name, entity_id, bone_name, offset, rotation):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.CreateBindEntity(effect_name, entity_id, bone_name, offset, rotation)

	@staticmethod
	def EmitManually(par_id):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.EmitManually(par_id)

	@staticmethod
	def Exist(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Exist(parId)

	@staticmethod
	def GetActiveDuration(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetActiveDuration(parId)

	@staticmethod
	def GetBindingID(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetBindingID(parId)

	@staticmethod
	def GetBindingModelID(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetBindingModelID(parId)

	@staticmethod
	def GetDuration(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetDuration(parId)

	@staticmethod
	def GetFacingMode(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetFacingMode(parId)

	@staticmethod
	def GetLoopAge(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetLoopAge(parId)

	@staticmethod
	def GetPos(parId, is_local):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetPos(parId, is_local)

	@staticmethod
	def GetRot(parId, is_local):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetRot(parId, is_local)

	@staticmethod
	def GetSleepDuration(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetSleepDuration(parId)

	@staticmethod
	def GetTimeScale(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetTimeScale(parId)

	@staticmethod
	def GetVariable(parId, variable_name):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.GetVariable(parId, variable_name)

	@staticmethod
	def Hide(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Hide(parId)

	@staticmethod
	def IsHiding(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.IsHiding(parId)

	@staticmethod
	def IsPausing(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.IsPausing(parId)

	@staticmethod
	def Pause(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Pause(parId)

	@staticmethod
	def Play(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Play(parId)

	@staticmethod
	def PlayAt(parId, at_second):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.PlayAt(parId, at_second)

	@staticmethod
	def Remove(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Remove(parId)

	@staticmethod
	def RemoveByName(effect_name):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.RemoveByName(effect_name)

	@staticmethod
	def Replay(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Replay(parId)

	@staticmethod
	def Resume(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Resume(parId)

	@staticmethod
	def SetPos(parId, pos):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.SetPos(parId, pos)

	@staticmethod
	def SetRelative(parId, is_relative):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.SetRelative(parId, is_relative)

	@staticmethod
	def SetRot(parId, rot):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.SetRot(parId, rot)

	@staticmethod
	def SetTimeScale(parId, scale):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.SetTimeScale(parId, scale)

	@staticmethod
	def SetVariable(parId, variable_name, value):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.SetVariable(parId, variable_name, value)

	@staticmethod
	def Show(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Show(parId)

	@staticmethod
	def Stop(parId):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Stop(parId)

	@staticmethod
	def Unbind(parId, keep_position, keep_rotation):
		comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
		return comp.Unbind(parId)