# coding=utf-8
from .. import SystemApi
if SystemApi.ClientComp.CreateModAttr(SystemApi.levelId):
    import StateMachine_Client

if SystemApi.ServerComp.CreateModAttr(SystemApi.levelId):
    import StateMachine_Server
