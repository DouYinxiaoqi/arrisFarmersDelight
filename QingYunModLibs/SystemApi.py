# -*- coding: utf-8 -*-
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi
import ModInit.QingYunMod as QingYunMod


levelId = serverApi.GetLevelId()
_ServerSys = serverApi.GetServerSystemCls()
_ClientSys = clientApi.GetClientSystemCls()
ServerComp = serverApi.GetEngineCompFactory()
ClientComp = clientApi.GetEngineCompFactory()
_ServerEventDataName = QingYunMod.ModObject.ModName + "ServerEventData"
_ClientEventDataName = QingYunMod.ModObject.ModName + "ClientEventData"
if ServerComp.CreateModAttr(levelId):
    ServerComp.CreateModAttr(levelId).SetAttr(_ServerEventDataName, [])
if ClientComp.CreateModAttr(levelId):
    ClientComp.CreateModAttr(levelId).SetAttr(_ClientEventDataName, [])
_BackFuncDict = dict()
_CallBackFuncDict = dict()


class Universal(object):
    """
    通用类，可做存储数据使用
    """
    def __init__(self, ClassName):
        self.ClassName = ClassName
        print "Create Universal"

    def __setattr__(self, key, value):
        print "%s Set Value {%s:%s}" % (self.ClassName, str(key), str(value))

    def __delattr__(self, item):
        print "%s Remove Value %s" % (self.ClassName, item)


def GetClientModAttr(entityId, AttrName):
    """
    安全获取客户端ModAttr数据
    """
    AttrComp = ClientComp.CreateModAttr(entityId)
    if not AttrComp:
        return []
    else:
        return ClientComp.CreateModAttr(entityId).GetAttr(AttrName)


def SetClientModAttr(entityId, AttrName, Attr):
    """
    安全设置客户端ModAttr数据
    """
    AttrComp = ClientComp.CreateModAttr(entityId)
    if not AttrComp:
        return []
    else:
        return ClientComp.CreateModAttr(entityId).SetAttr(AttrName, Attr)


class Bcolors(object):
    """
    颜色日志输出
    SUC # GREEN
    ERROR # YELLOW
    FAIL # RED
    RESET # RESET COLOR
    """
    SUC = '[SUC]'  # GREEN
    ERROR = '[ERROR]'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


ServerObj = serverApi.GetSystem(QingYunMod.ModObject.ModName, "Server")
ClientObj = clientApi.GetSystem(QingYunMod.ModObject.ModName, "Client")
AllServer = serverApi.GetSystem("QingYunMod", "Server")
AllClient = clientApi.GetSystem("QingYunMod", "Client")


def CallBack(BackFunc, TargetId="-1", ForAllMod=False):
    """
    通信绑定函数，用于绑定目标函数，发信端发信时该接口绑定的函数会被调用，可返回某值

    :param BackFunc: 自定义通信的回调函数
    :param TargetId: 自定义通信的目标id，客户端一般为playerId，服务端则为-1，服务端无需传参
    :param ForAllMod: 是否为框架全局通信
    """
    if TargetId == "-1":
        if ServerObj:
            ServerObj.ListenCall(BackFunc)
            if ForAllMod:
                if AllServer:
                    AllServer.ListenAllCall.__call__(BackFunc)

    else:
        if ClientObj:
            ClientObj.ListenCall(BackFunc)
            if ForAllMod:
                if AllClient:
                    AllClient.ListenAllCall.__call__(BackFunc)


def CallClient(FuncName, TargetId, EventData, BackFunc=None, ForAllMod=False):
    """
    发起通信请求函数，服务端接口，从服务端向客户端发起单向请求，可调用被通信端指定函数

    :param FuncName: 需要调用的函数名称
    :param TargetId: 需要请求的客户端玩家id
    :param EventData: 需要一并传入指定函数的参数数据(仅支持基本数据类型)
    :param BackFunc: 目标函数运行结束以后将用于获取返回值的回调函数
    :param ForAllMod: 是否为框架全局通信
    """
    args = {
        'args': EventData,
        'DataId': FuncName,
    }
    DataId = FuncName
    if ForAllMod:
        if AllServer:
            AllServer.NotifyToClient(TargetId, FuncName, args)
    else:
        if ServerObj:
            ServerObj.NotifyToClient(TargetId, FuncName, args)
    _BackFuncDict[DataId] = BackFunc


def __GetClientResult(args):
    DataId = args["DataId"]
    Result = args["Result"]
    BackFunc = _BackFuncDict.get(DataId, None)
    if BackFunc:
        BackFunc(Result)


def CallAllClient(FuncName, EventData, BackFunc=None, ForAllMod=False):
    """
    发起通信请求函数，服务端接口，从服务端向所有客户端发起单向请求，可调用被通信端指定函数

    :param FuncName: 需要调用的函数名称
    :param EventData: 需要一并传入指定函数的参数数据(仅支持基本数据类型)
    :param BackFunc: 目标函数运行结束以后将用于获取返回值的回调函数
    :param ForAllMod: 是否为框架全局通信
    """
    args = {
        'args': EventData,
        'DataId': FuncName
    }
    DataId = FuncName
    if ForAllMod:
        if AllServer:
            AllServer.BroadcastToAllClient(FuncName, args)
    else:
        if ServerObj:
            ServerObj.BroadcastToAllClient(FuncName, args)
    _BackFuncDict[DataId] = BackFunc


def CallServer(FuncName, EventData, BackFunc=None, ForAllMod=False):
    """
    发起通信请求函数，客户端接口，从客户端向服务端发起单向请求，可调用被通信端指定函数

    :param FuncName: 需要调用的函数名称
    :param EventData: 需要一并传入指定函数的参数数据(仅支持基本数据类型)
    :param BackFunc: 目标函数运行结束以后将用于获取返回值的回调函数
    :param ForAllMod: 是否为框架全局通信
    """
    args = {
        'args': EventData,
        'DataId': FuncName,
        'playerId': clientApi.GetLocalPlayerId()
    }
    DataId = FuncName
    if ForAllMod:
        AllClient.NotifyToServer(FuncName, args)
    else:
        if ClientObj:
            ClientObj.NotifyToServer(FuncName, args)
    _BackFuncDict[DataId] = BackFunc


def __GetServerResult(args):
    DataId = args["DataId"]
    Result = args["Result"]
    BackFunc = _BackFuncDict.get(DataId, None)
    if BackFunc:
        BackFunc(Result)


def MappingCall(FuncName, EventData):
    """
    发起通信请求函数，客户端接口，从客户端向所有客户端发起单向请求，可调用被通信端指定函数(暂不支持获取返回值以及选为全局框架通信)

    :param FuncName: 需要调用的函数名称
    :param EventData: 需要一并传入指定函数的参数数据(仅支持基本数据类型)
    """
    args = {
        "FuncName": FuncName,
        "EventData": EventData
    }
    CallServer("__Mapping", args, )


def __Mapping(args):
    FuncName = args['FuncName']
    EventData = args['EventData']
    CallAllClient(FuncName, EventData)


def ListenServerEvents(EventName, BackFunc):
    """
    监听服务端游戏原生事件

    :param EventName: 事件名称
    :param BackFunc: 用于触发事件逻辑的回调函数
    """
    if ServerObj:
        ServerObj.ListenEvent(EventName, BackFunc)


def ListenClientEvents(EventName, BackFunc):
    """
    监听客户端游戏原生事件

    :param EventName: 事件名称
    :param BackFunc: 用于触发事件逻辑的回调函数
    """
    if ClientObj:
        ClientObj.ListenEvent(EventName, BackFunc)


def DesEntityClient(entityId):
    """
    基于客户端的该接口用于销毁实体，理论上所有实体通用，包括特效类实体

    :param entityId: 需要销毁的实体id
    """
    if ClientObj:
        ClientObj.DestroyEntity(entityId)


def CreateParticle(Effect, Pos, IsPlay=False):
    """
    基于客户端的该接口用于根据MCS制作的粒子特效配置文件生成粒子特效

    :param Effect: 需要创建的粒子特效配置文件路径，例如："effects/fire.json"
    :param Pos: 将要创建粒子特效的位置坐标
    :param IsPlay: 是否立刻播放特效
    :return particleId 创建的粒子特效实体id
    """
    if ClientObj:
        ParticleId = ClientObj.CreateEngineParticle(Effect, Pos)
        if IsPlay:
            clientApi.GetEngineCompFactory().CreateParticleControl(ParticleId).Play()
        return ParticleId


def CreateFrame(Effect, Pos=None, Rot=None, Scale=None, IsPlay=False):
    """
    基于客户端的该接口用于根据MCS制作的序列帧特效配置文件生成序列帧特效

    :param Effect: 需要创建的序列帧特效配置文件路径，例如："effects/fire.json"
    :param Pos: 将要创建序列帧特效的位置坐标
    :param Rot: 将要创建序列帧特效的旋转角度
    :param Scale: 将要创建序列帧特效的缩放大小
    :param IsPlay: 是否立刻播放特效
    :return: frameId 创建的序列帧特效实体id
    """
    if ClientObj:
        FrameId = ClientObj.CreateEngineSfxFromEditor(Effect, Pos, Rot, Scale)
        if IsPlay:
            clientApi.GetEngineCompFactory().CreateFrameAniControl(FrameId).Play()
        return FrameId


def CreateFrameTexture(Effect, Pos=None, Rot=None, Scale=None, IsPlay=True):
    """
    基于客户端的该接口用于使用序列帧图片直接生成序列帧特效

    :param Effect: 需要创建的序列帧特效配置文件路径，例如："textures/sfxs/effect.png"
    :param Pos: 将要创建序列帧特效的位置坐标
    :param Rot: 将要创建序列帧特效的旋转角度
    :param Scale: 将要创建序列帧特效的缩放大小
    :param IsPlay: 是否立刻播放特效
    :return: frameId 创建的序列帧特效实体id
    """
    if ClientObj:
        FrameId = ClientObj.CreateEngineSfx(Effect, Pos, Rot, Scale)
        if IsPlay:
            clientApi.GetEngineCompFactory().CreateFrameAniControl(FrameId).Play()
        return FrameId


def DesEntityServer(entityId):
    """
    基于服务端的该接口用于销毁实体，理论上所有实体通用，包括特效类实体

    :param entityId: 需要销毁的实体id
    """
    if ServerObj:
        ServerObj.DestroyEntity(entityId)


def CreateEntityServer(EntityTypeStr, Pos, Rot=(0, 0), DimId=0, IsNpc=False):
    """
    基于服务端的该接口用于根据命名标识符来创建实体，可指定实体的生成位置，面向角度（默认为0，0），所处维度id（默认为主世界--0），是否为NPC（默认为否）
    :param EntityTypeStr: 实体的命名标识符
    :param Pos: 生成位置
    :param Rot: 面向角度 --> (0,0)
    :param DimId: 维度id --> 0
    :param IsNpc: 是否为NPC --> False
    :return: 生成的实体id
    """
    if ServerObj:
        return ServerObj.CreateEngineEntityByTypeStr(EntityTypeStr, Pos, Rot, DimId, IsNpc)


def GetClientModule(ModuleName):
    """
    获取全局框架环境中某一客户端模块文件(本地客户端)

    :param ModuleName: 将要获取的模块名称(无后缀)
    """
    if ModuleName in ClientComp.CreateModAttr(clientApi.GetLocalPlayerId()).GetAttr("ClientModules"):
        return ClientComp.CreateModAttr(clientApi.GetLocalPlayerId()).GetAttr("ClientModules")[ModuleName]
    else:
        print Bcolors.ERROR + ModuleName + " not in package"


def GetServerModule(ModuleName):
    """
    获取全局框架环境中某一服务端模块文件

    :param ModuleName: 将要获取的模块名称
    """
    if ModuleName in ServerComp.CreateModAttr("qingyun").GetAttr("ServerModules"):
        return ServerComp.CreateModAttr("qingyun").GetAttr("ServerModules")[ModuleName]
    else:
        print Bcolors.ERROR + ModuleName + " not in package"


def __RegisterModule_Client(event):
    for Module in QingYunMod.ClientModuleList:
        print Module.__name__, "Client"
        PlayerId = clientApi.GetLocalPlayerId()
        ClientModules = ClientComp.CreateModAttr(PlayerId).GetAttr("ClientModules")
        if ClientModules == None:
            ClientModules = {}
        ClientModules[Module.__name__] = Module
        ClientComp.CreateModAttr(PlayerId).SetAttr("ClientModules", ClientModules)


def __RegisterModule_Server(event):
    for Module in QingYunMod.ServerModuleList:
        print Module.__name__, "Server"
        ServerModules = ServerComp.CreateModAttr("qingyun").GetAttr("ServerModules")
        if ServerModules == None:
            ServerModules = {}
        ServerModules[Module.__name__] = Module
        ServerComp.CreateModAttr("qingyun").SetAttr("ServerModules", ServerModules)


def DestroyAllServerEvents(args):
    """
    注销服务端所有监听事件(不建议在游戏运行结束前随意调用该接口)
    """
    from .Config import ServerUserPlayerId
    if args["playerId"] != ServerUserPlayerId: return
    if ServerObj:
        ServerObj.UnListenAllEvents()


def DestroyAllClientEvents(args=None):
    """
    注销本地客户端所有监听事件(不建议在游戏运行结束前随意调用该接口)
    """
    if ClientObj:
        ClientObj.UnListenAllEvents()


def Call(TargetId="-1", ForAllMod=False):
    """
    通信绑定函数，用于绑定目标函数，发信端发信时该接口绑定的函数会被调用，可返回某值

    :param TargetId: 自定义通信的目标id，客户端一般为playerId，服务端则为-1，服务端无需传参
    :param ForAllMod: 是否为框架全局通信
    """

    def SetCall(BackFunc):
        if TargetId == "-1":
            if ServerObj:
                ServerObj.ListenCall(BackFunc)
                if ForAllMod:
                    if AllServer:
                        AllServer.ListenAllCall(BackFunc)
        else:
            if ClientObj:
                ClientObj.ListenCall(BackFunc)
                if ForAllMod:
                    if AllClient:
                        AllClient.ListenAllCall(BackFunc)
        return BackFunc
    return SetCall


def ListenServer(EventName):
    """
    监听服务端游戏原生事件

    :param EventName: 事件名称
    """
    def Listen(BackFunc):
        if ServerObj:
            ServerObj.ListenEvent(EventName, BackFunc)
        return BackFunc
    return Listen


def ListenClient(EventName):
    """
    监听客户端游戏原生事件

    :param EventName: 事件名称
    """
    def Listen(BackFunc):
        if ClientObj:
            ClientObj.ListenEvent(EventName, BackFunc)
        return BackFunc
    return Listen


def UnListenServer(EventName, BackFunc):
    """
    注销监听服务端游戏原生事件

    :param EventName: 事件名称
    :param BackFunc: 用于触发事件逻辑的回调函数
    """
    if ServerObj:
        ServerObj.UnListenEvent(EventName, BackFunc)


def UnListenServerCall(BackFunc):
    """
    注销绑定服务端通信

    :param BackFunc: 用于绑定通信的回调函数
    """
    if ServerObj:
        ServerObj.UnListenCall(BackFunc)


def UnListenClientCall(BackFunc):
    """
    注销绑定客户端通信

    :param BackFunc: 用于绑定通信的回调函数
    """
    if ClientObj:
        ClientObj.UnListenCall(BackFunc)


def UnListenClient(EventName, BackFunc):
    """
    注销监听客户端游戏原生事件

    :param EventName: 事件名称
    :param BackFunc: 用于触发事件逻辑的回调函数
    """
    if ClientObj:
        ClientObj.UnListenEvent(EventName, BackFunc)


CallBack(__Mapping)
ListenClientEvents("LoadClientAddonScriptsAfter", __RegisterModule_Client)
ListenServerEvents("LoadServerAddonScriptsAfter", __RegisterModule_Server)
if ServerObj:
    ServerObj.ListenResult(__GetClientResult)
if ClientObj:
    ClientObj.ListenResult(__GetServerResult)
ListenServerEvents("PlayerIntendLeaveServerEvent", DestroyAllServerEvents)
ListenServerEvents("UnLoadClientAddonScriptsBefore", DestroyAllClientEvents)


print "\n%s[QyMod] SystemApi加载完毕" % Bcolors.SUC
