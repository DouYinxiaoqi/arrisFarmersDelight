# -*- coding: utf-8 -*-
from ..QingYunModLibs.ClientMod import *
from ..QingYunModLibs.SystemApi import *
from ..modCommon.modConfig import *

playerId = clientApi.GetLocalPlayerId()
uiNode = None

@ListenClient("UiInitFinished")
def Ui_Init(args):
    clientApi.RegisterUI("arrisFarmersDelight", "uiCookingPot", uiCookingPotPath, uiCookingPotScreen)

@Call(playerId)
def SetArrowProgress(args):
    global uiNode
    uiNode = clientApi.GetUI("arrisFarmersDelight", "uiCookingPot")
    timer = args.get("timer")
    if uiNode:
        uiNode.SetArrowProgress(timer)
    else:
        return args

@Call(playerId)
def CookingPotUsedEvent(args):
    global uiNode
    uiNode = clientApi.PushScreen("arrisFarmersDelight", "uiCookingPot", args)

@Call(playerId)
def UpdateCookingPot(data):
    global uiNode
    uiNode = clientApi.GetUI("arrisFarmersDelight", "uiCookingPot")
    if uiNode:
        uiNode.UpdateCookingPot(data)

@Call(playerId)
def CheckPlayerScreen(args):
    if uiNode:
        return None
    else:
        return args
