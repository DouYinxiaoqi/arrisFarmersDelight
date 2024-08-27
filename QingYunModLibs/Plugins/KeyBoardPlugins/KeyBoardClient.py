from ...ClientMod import *
__KeyBoardFuncDict = {}
__GamePadFuncDict = {}


def __OnKeyPress(args):
    KeyValue = args['key']
    for KeyValue in [KeyValue+"1", KeyValue+"0"]:
        if KeyValue in __KeyBoardFuncDict:
            for KeyBoardData in __KeyBoardFuncDict[KeyValue]:
                if KeyBoardData["State"] == args["isDown"]:
                    Func = KeyBoardData["Func"]
                    Param = KeyBoardData.get("Param", KeyValue)
                    Func(Param)


def __OnGamePadPress(args):
    KeyValue = args['key']
    for KeyValue in [KeyValue + "1", KeyValue + "0"]:
        if KeyValue in __GamePadFuncDict:
            for KeyBoardData in __GamePadFuncDict[KeyValue]:
                if KeyBoardData["State"] == args["isDown"]:
                    Func = KeyBoardData["Func"]
                    Param = KeyBoardData.get("Param", KeyValue)
                    Func(Param)


def AddKeyFuncBind(KeyValue, Func, Param=None, State="1"):
    if not __KeyBoardFuncDict.get(str(KeyValue)+State, None):
        __KeyBoardFuncDict[str(KeyValue) + State] = []
    KeyData = {
        "Func": Func,
        "Param": Param,
        "State": State
    }
    if KeyData in __KeyBoardFuncDict[str(KeyValue) + State]:
        __KeyBoardFuncDict[str(KeyValue) + State].remove(KeyData)
    __KeyBoardFuncDict[str(KeyValue) + State].append(KeyData)


def AddGamePadFuncBind(KeyValue, Func, Param=None, State="1"):
    if not __GamePadFuncDict.get(str(KeyValue)+State):
        __GamePadFuncDict[str(KeyValue) + State] = []
    keyData = {
        "Func": Func,
        "Param": Param,
        "State": State
    }
    if keyData in __GamePadFuncDict[str(KeyValue) + State]:
        __GamePadFuncDict[str(KeyValue) + State].remove(keyData)
    __GamePadFuncDict[str(KeyValue) + State].append(keyData)


ListenClientEvents(ClientEvents.ControlEvents.OnKeyPressInGame, __OnKeyPress)
ListenClientEvents(ClientEvents.ControlEvents.OnGamepadKeyPressClientEvent, __OnGamePadPress)
