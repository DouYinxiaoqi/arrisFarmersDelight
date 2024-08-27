# coding=utf-8
from ..ClientMod import *
_TickList = []


@ListenClient(ClientEvents.WorldEvents.OnScriptTickClient)
def _AnimationTick():
    for Func in _TickList:
        Func()


class _EffectAnimation(object):
    def __init__(self, RotationDict, Distance):
        self.RotationDict = RotationDict
        self.Distance = Distance
        self.AnimTime = 0

        def Tick():
            self.__Tick()
        _TickList.append(Tick)

    def __Tick(self):
        pass

    def CheckTick(self):
        self.AnimTime

