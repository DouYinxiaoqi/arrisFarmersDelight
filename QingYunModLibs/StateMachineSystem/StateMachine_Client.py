# coding=utf-8
from .. import ClientMod


class TranslateCondition(object):
    def Compute(self):
        pass


class State(object):
    def __init__(self, ControllerId, StateType):
        self.ControllerId = ControllerId
        self.StateType = StateType
        self.StateId = self.ControllerId+"_"+self.StateType
        self.TranslateDict = {}
        self.MustKeepTime = 0

    def SetTranslatingState(self, StateId, TranslateCondition):
        self.TranslateDict[StateId] = TranslateCondition

    def TranslateToState(self, OldState):
        print OldState.StateId, "OldState"
        self.InState(OldState)

    def TranslateOutState(self, NewState):
        print NewState.StateId, "NewState"
        self.OutState(NewState)

    def InState(self, OldState):
        pass

    def OutState(self, NewState):
        pass


class StateMachine(object):
    def __init__(self, DefaultState):
        self.DefaultState = DefaultState
        self.NowState = self.DefaultState  # type:State
        self.NewState(DefaultState)
        self.StateMechineToggle = False
        self.FinishState = True

        def OnTick():
            if self.StateMechineToggle:
                self.TranslatingState()
            else:
                if self.NowState:
                    self.NowState.TranslateOutState(self.NowState)
                    self.NowState = None
        Timer = ClientMod.CreateTimer(0.0, OnTick, True)
        self.Timer = Timer

    def Destroy(self):
        self.StateMechineToggle = False

    def NewState(self, State):
        self.__setattr__(State.StateId, State)

    def TranslatingState(self):
        if not self.NowState:
            self.NowState = self.DefaultState
        TranslateDict = self.NowState.TranslateDict
        for StateId in TranslateDict:
            Condition = TranslateDict[StateId]  # type:TranslateCondition
            if Condition.Compute():
                NewState = self.__getattribute__(StateId)  # type:State
                if NewState == self.NowState:
                    continue
                if not self.FinishState:
                    return
                self.FinishState = False
                ClientMod.CreateTimer(NewState.MustKeepTime, self.AfterState, False)
                NewState.TranslateToState(self.NowState)
                self.NowState.TranslateOutState(NewState)
                self.NowState = NewState
                return

    def AfterState(self):
        self.FinishState = True
