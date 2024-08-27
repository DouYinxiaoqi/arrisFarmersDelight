# coding=utf-8
from ..ClientMod import *
from ..StateMachineSystem import StateMachine_Client


class TranslateCondition(object):
    def Compute(self):
        pass


class State(StateMachine_Client.State):
    def __init__(self, roleId, StateType):
        StateMachine_Client.State.__init__(self, roleId, StateType)
        self.StateAnimation = []
        self.MovingAnimation = False
        self.ReloadStateAnimation = False

    def TranslateToState(self, OldState):
        StateMachine_Client.State.TranslateToState(self, OldState)
        import BaseApi
        if self.ReloadStateAnimation:
            for Animation in self.StateAnimation:
                BaseApi.PlayerRender(clientApi.GetLocalPlayerId()).AddPlayerAnimation(Animation, Animation, True)
        BaseApi.SetMolang("query.mod." + self.StateId, 1.0, True)

    def TranslateOutState(self, NewState):
        StateMachine_Client.State.TranslateOutState(self, NewState)
        import BaseApi
        BaseApi.SetMolang("query.mod." + self.StateId, 0.0, True)


class BaseState(object):
    def __init__(self):
        self.StateAnimation = []
        self.TranslateDict = {}
        self.MustKeepTime = 0
        self.MovingAnimation = False
        self.ReloadStateAnimation = False

    def InState(self, OldState):
        print OldState.StateId, " OldState"
        pass

    def OutState(self, NewState):
        print NewState.StateId, " NewState"
        pass


class AnimationStateMachine(StateMachine_Client.StateMachine):
    def __init__(self, DefaultState):
        StateMachine_Client.StateMachine.__init__(self, DefaultState)

    def NewState(self, State):
        StateMachine_Client.StateMachine.NewState(self, State)
        import BaseApi
        PR = BaseApi.PlayerRender(BaseApi.playerId)
        for Animation in State.StateAnimation:
            PR.AddPlayerAnimation(Animation, Animation, True)
            if State.MovingAnimation:
                PR.AddPlayerScriptAnimate(Animation, "query.mod."+State.StateId, False, True)
            else:
                PR.AddPlayerScriptAnimate(Animation, "", False, True)
        BaseApi.RegisterMolang("query.mod."+State.StateId, 0.0, True)