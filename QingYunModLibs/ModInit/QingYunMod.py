# -*- coding: utf-8 -*-
import time

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi
levelId = serverApi.GetLevelId()
ModObject = None
Server = []
Client = []
ClientModuleList = []
ServerModuleList = []
_PluginsServer = []
_PluginsClient = []
ClientEvents = []
ServerEvents = []


def CreateGameTick(BindTickName):
    try:
        clientApi.GetEngineCompFactory().CreateModAttr(clientApi.GetLevelId()).SetAttr("TickName", BindTickName)
    except:
        print "UnClient"


class QingYunMod(object):
    '''
    通过实例化此类来注册Mod

    '''
    def __init__(self):
        self.ModName = None
        global ModObject
        ModObject = self

    def InitMod(self, modname):
        '''
        注册Mod命名空间

        :param modname: ModName(该mod的命名空间，请保持与脚本根目录文件夹名称一致)
        '''
        self.ModName = modname

    def ServerInit(self, server):
        '''
        注册你的服务端脚本到Mod里

        :param server: 服务端脚本文件名称(无需带后缀，例如Server.py，只需写入字符串"Server"，且可注册多个脚本)
        '''
        Server.append(server)

    def ClientInit(self, client):
        '''
        注册你的客户端脚本到Mod里

        :param client: 客户端脚本文件名称(无需带后缀，例如Client.py，只需写入字符串"Client"，且可注册多个脚本)
        '''
        Client.append(client)


@Mod.Binding(name="ModInit", version="0.0.1")
class ModInit(object):
    @Mod.InitServer()
    def Server(self):
        serverApi.RegisterSystem(ModObject.ModName, "Server", "%s.QingYunModLibs.ModInit.QingYunMod._ServerSystem" % ModObject.ModName)
        serverApi.RegisterSystem("QingYunMod", "Server", "%s.QingYunModLibs.ModInit.QingYunMod._ServerSystem" % ModObject.ModName)
        serverApi.RegisterSystem(ModObject.ModName, "SSys", "%s.QingYunModLibs.ModInit.QingYunMod._ServerSys" % ModObject.ModName)

    @Mod.InitClient()
    def Client(self):
        clientApi.RegisterSystem(ModObject.ModName, "Client", "%s.QingYunModLibs.ModInit.QingYunMod._ClientSystem" % ModObject.ModName)
        clientApi.RegisterSystem("QingYunMod", "Client", "%s.QingYunModLibs.ModInit.QingYunMod._ClientSystem" % ModObject.ModName)
        clientApi.RegisterSystem(ModObject.ModName, "CSys", "%s.QingYunModLibs.ModInit.QingYunMod._ClientSys" % ModObject.ModName)


def ImportServerModule(ModulePath):
    return serverApi.ImportModule(ModulePath)


def ImportClientModule(ModulePath):
    return clientApi.ImportModule(ModulePath)


def _InitServer():
    for server in Server:
        print "\n Start Loading " + server + "\n"
        ServerModule = ImportServerModule(ModObject.ModName + "." + server)
        if ServerModule:
            ServerModuleList.append(ServerModule)
            print "\n[SUC] Successfully Finished importing " + server + "\n"
        else:
            print "\n[ERROR] Can not import " + server + "\n" + "[ERROR] Module is " + str(ServerModule) + "\n"
        Config = ImportServerModule(ModObject.ModName + ".QingYunModLibs.Config")
        Config.ServerUser = True
        Config.ServerUserPlayerId = clientApi.GetLocalPlayerId()


def _InitClient():
    reload(ImportClientModule(ModObject.ModName+".QingYunModLibs.SystemApi"))
    for client in Client:
        print "\n Start Loading " + client + "\n"
        ClientModule = ImportClientModule(ModObject.ModName + "." + client)
        if ClientModule:
            ClientModuleList.append(ClientModule)
            print "\n[SUC] Successfully Loading importing " + client + "\n"
        else:
            print "\n[ERROR] Can not import " + client + "\n" + "[ERROR] Module is " + str(ClientModule) + "\n"
        print "These Plugins Was Finished Running\n                 ===========================\n                 ServerPlugins:", _PluginsServer, "\n                 ClientPlugins:", _PluginsClient, "\n                 ==========================="


class _ServerSys(serverApi.GetServerSystemCls()):
    def __init__(self, ns, sys):
        self.Inited = False

    def Update(self):
        if not self.Inited:
            _InitServer()
            self.Inited = True


class _ClientSys(clientApi.GetClientSystemCls()):
    def __init__(self, ns, sys):
        self.Inited = False

    def Update(self):
        if not self.Inited:
            _InitClient()
            self.Inited = True


class _ClientSystem(clientApi.GetClientSystemCls()):
    def __init__(self, ns, sys):
        clientApi.GetClientSystemCls().__init__(self, ns, sys)
        self.CallBackFuncDict = {}
        self.ClientListen = {
            "EventList": [],
            "Update": False
        }
        self.ClientCall = {
            "CallList": [],
            "Update": False
        }
        self.ClientAllCall = {
            "CallList": [],
            "Update": False
        }
        self.ClientResult = {
            "CallList": [],
            "Update": False
        }
        self.ClientNotify = {
            "CallList": [],
            "Update": False
        }

    def Update(self):
        if self.ClientListen["Update"]:
            for EventData in self.ClientListen["EventList"]:
                EventName, BackFunc = EventData
                self._ListenEvent(EventName, BackFunc)
                self.ClientListen["Update"] = False

        if self.ClientCall["Update"]:
            for CallData in self.ClientCall["CallList"]:
                BackFunc = CallData
                self._ListenCall(BackFunc)
                self.ClientCall["Update"] = False

        if self.ClientAllCall["Update"]:
            for CallData in self.ClientAllCall["CallList"]:
                BackFunc = CallData
                self._ListenAllCall(BackFunc)
                self.ClientAllCall["Update"] = False

        if self.ClientResult["Update"]:
            for CallData in self.ClientResult["CallList"]:
                BackFunc = CallData
                self._ListenResult(BackFunc)
                self.ClientResult["Update"] = False

        if self.ClientNotify["Update"]:
            for CallData in self.ClientNotify["CallList"]:
                BackFunc, EventName = CallData
                self._ListenNotify(BackFunc, EventName)
                self.ClientNotify["Update"] = False

    def ListenEvent(self, EventName, BackFunc):
        self.ClientListen["EventList"].append([EventName, BackFunc])
        self.ClientListen["Update"] = True

    def _ListenEvent(self, EventName, BackFunc):
        from types import MethodType
        try:
            self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), EventName, self, getattr(self, EventName + "Listen"))
        except:
            pass

        def BFunc(self, *args):
            BackFunc(*args)

        BFunc.__name__ = BackFunc.__name__ + EventName+"Listen"
        setattr(self, BackFunc.__name__ + EventName+"Listen", MethodType(BFunc, self))
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), EventName, self, getattr(self, BackFunc.__name__ + EventName+"Listen"))

    def UnListenEvent(self, EventName, BackFunc):
        try:
            getattr(self, BackFunc.__name__ + EventName + "Listen")
        except:
            return
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), EventName, self, getattr(self, BackFunc.__name__ + EventName + "Listen"))

    def UnListenCall(self, BackFunc):
        self.UnListenForEvent(ModObject.ModName, "Server", BackFunc.__name__, self, self.ListenBackForCall)

    def ListenBackForCall(self, args):
        DataId = args['DataId']
        result = self.CallBackFuncDict[DataId](args['args'])
        args = {
            "DataId": DataId,
            "Result": result
        }
        self.NotifyToServer("__GetClientResultResult", args)

    def ListenCall(self, BackFunc):
        self.ClientCall["CallList"].append(BackFunc)
        self.ClientCall["Update"] = True

    def _ListenCall(self, BackFunc):
        if self.CallBackFuncDict.get(BackFunc.__name__, None):
            self.UnListenCall(BackFunc)
        self.CallBackFuncDict[BackFunc.__name__] = BackFunc
        self.ListenForEvent(ModObject.ModName, "Server", BackFunc.__name__, self, self.ListenBackForCall)

    def ListenAllCall(self, BackFunc):
        self.ClientAllCall["CallList"].append(BackFunc)
        self.ClientAllCall["Update"] = True

    def _ListenAllCall(self, BackFunc):
        if self.CallBackFuncDict.get(BackFunc.__name__, None):
            self.UnListenAllCall(BackFunc)
        self.CallBackFuncDict[BackFunc.__name__] = BackFunc
        self.ListenForEvent("QingYunMod", "Server", BackFunc.__name__, self, self.ListenBackForCall)

    def UnListenAllCall(self, BackFunc):
        self.UnListenForEvent("QingYunMod", "Server", BackFunc.__name__, self, self.ListenBackForCall)

    def ListenResult(self, BackFunc):
        self.ClientResult["CallList"].append(BackFunc)
        self.ClientResult["Update"] = True

    def _ListenResult(self, BackFunc):
        from types import MethodType
        try:
            self.UnListenForEvent(ModObject.ModName, "Server", BackFunc.__name__ + "Result", self, getattr(self, BackFunc.__name__ + "Result"))
        except:
            pass

        def BFunc(self, *args):
            BackFunc(*args)

        BFunc.__name__ = BackFunc.__name__+"Result"
        setattr(self, BackFunc.__name__+"Result", MethodType(BFunc, self))
        self.ListenForEvent(ModObject.ModName, "Server", BackFunc.__name__+"Result", self,
                            getattr(self, BackFunc.__name__+"Result"))

    def ListenNotify(self, BackFunc, EventName):
        self.ClientNotify["CallList"].append([BackFunc, EventName])
        self.ClientNotify["Update"] = True

    def _ListenNotify(self, BackFunc, EventName):
        from types import MethodType
        try:
            self.UnListenForEvent(ModObject.ModName, "Server", BackFunc.__name__ + "Notify", self, getattr(self, BackFunc.__name__ + "Notify"))
        except:
            pass

        def BFunc(self, *args):
            BackFunc(*args)

        BFunc.__name__ = EventName+"Notify"
        setattr(self, EventName+"Notify", MethodType(BFunc, self))
        self.ListenForEvent(ModObject.ModName, "Server", EventName+"Notify", self, getattr(self, EventName+"Notify"))


class _ServerSystem(serverApi.GetServerSystemCls()):
    def __init__(self, ns, sys):
        serverApi.GetServerSystemCls().__init__(self, ns, sys)
        self.CallBackFuncDict = {}
        self.ServerListen = {
            "EventList": [],
            "Update": False
        }
        self.ServerCall = {
            "CallList": [],
            "Update": False
        }
        self.ServerAllCall = {
            "CallList": [],
            "Update": True
        }
        self.ServerResult = {
            "CallList": [],
            "Update": False
        }
        self.ServerNotify = {
            "CallList": [],
            "Update": False
        }

    def Update(self):
        if self.ServerListen["Update"]:
            for EventData in self.ServerListen["EventList"]:
                EventName, BackFunc = EventData
                self._ListenEvent(EventName, BackFunc)
            self.ServerListen["EventList"] = []
            self.ServerListen["Update"] = False

        if self.ServerCall["Update"]:
            for CallData in self.ServerCall["CallList"]:
                BackFunc = CallData
                self._ListenCall(BackFunc)
            self.ServerListen["CallList"] = []
            self.ServerCall["Update"] = False

        if self.ServerAllCall["Update"]:
            for CallData in self.ServerAllCall["CallList"]:
                BackFunc = CallData
                self._ListenAllCall(BackFunc)
            self.ServerListen["CallList"] = []
            self.ServerAllCall["Update"] = False

        if self.ServerResult["Update"]:
            for CallData in self.ServerResult["CallList"]:
                BackFunc = CallData
                self._ListenResult(BackFunc)
            self.ServerListen["CallList"] = []
            self.ServerResult["Update"] = False

        if self.ServerNotify["Update"]:
            for CallData in self.ServerNotify["CallList"]:
                BackFunc, EventName = CallData
                self._ListenNotify(BackFunc, EventName)
            self.ServerListen["CallList"] = []
            self.ServerNotify["Update"] = False

    def ListenEvent(self, EventName, BackFunc):
        self.ServerListen["EventList"].append([EventName, BackFunc])
        self.ServerListen["Update"] = True

    def _ListenEvent(self, EventName, BackFunc):
        from types import MethodType
        try:
            self.UnListenForEvent(ModObject.ModName, "Client", BackFunc.__name__ + "Listen", self, getattr(self, BackFunc.__name__ + "Listen"))
        except:
            pass

        def BFunc(self, *args):
            BackFunc(*args)
        BFunc.__name__ = BackFunc.__name__+EventName+"Listen"
        setattr(self, BackFunc.__name__+EventName+"Listen", MethodType(BFunc, self))
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), EventName, self, getattr(self, BackFunc.__name__+EventName+"Listen"))

    def UnListenEvent(self, EventName, BackFunc):
        try:
            getattr(self, BackFunc.__name__ + EventName + "Listen")
        except:
            return
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), EventName, self, getattr(self, BackFunc.__name__+EventName + "Listen"))

    def UnListenCall(self, BackFunc):
        self.UnListenForEvent(ModObject.ModName, "Client", BackFunc.__name__, self, self.ListenBackForCall)

    def ListenBackForCall(self, args):
        DataId = args['DataId']
        result = self.CallBackFuncDict[DataId](args['args'])
        TargetId = args['playerId']
        args = {
            "DataId": DataId,
            "Result": result
        }
        self.NotifyToClient(TargetId, "__GetServerResultResult", args)

    def ListenCall(self, BackFunc):
        self.ServerCall["CallList"].append(BackFunc)
        self.ServerCall["Update"] = True

    def _ListenCall(self, BackFunc):
        if self.CallBackFuncDict.get(BackFunc.__name__, None):
            self.UnListenCall(BackFunc)
        self.CallBackFuncDict[BackFunc.__name__] = BackFunc
        self.ListenForEvent(ModObject.ModName, "Client", BackFunc.__name__, self, self.ListenBackForCall)

    def ListenAllCall(self, BackFunc):
        self.ServerAllCall["CallList"].append(BackFunc)
        self.ServerAllCall["Update"] = True

    def _ListenAllCall(self, BackFunc):
        if self.CallBackFuncDict.get(BackFunc.__name__, None):
            self.UnListenAllCall(BackFunc)
        self.CallBackFuncDict[BackFunc.__name__] = BackFunc
        self.ListenForEvent("QingYunMod", "Client", BackFunc.__name__, self, self.ListenBackForCall)

    def UnListenAllCall(self, BackFunc):
        self.UnListenForEvent("QingYunMod", "Client", BackFunc.__name__, self, self.ListenBackForCall)

    def ListenResult(self, BackFunc):
        self.ServerResult["CallList"].append(BackFunc)
        self.ServerResult["Update"] = True

    def _ListenResult(self, BackFunc):
        from types import MethodType
        try:
            self.UnListenForEvent(ModObject.ModName, "Client", BackFunc.__name__ + "Result", self, getattr(self, BackFunc.__name__ + "Result"))
        except:
            pass

        def BFunc(self, *args):
            BackFunc(*args)
        BFunc.__name__ = BackFunc.__name__+"Result"
        setattr(self, BackFunc.__name__+"Result", MethodType(BFunc, self))
        self.ListenForEvent(ModObject.ModName, "Client", BackFunc.__name__+"Result", self, getattr(self, BackFunc.__name__+"Result"))

    def ListenNotify(self, BackFunc, EventName):
        self.ServerNotify["CallList"].append([BackFunc, EventName])
        self.ServerNotify["Update"] = True

    def _ListenNotify(self, BackFunc, EventName):
        from types import MethodType
        try:
            self.UnListenForEvent(ModObject.ModName, "Client", BackFunc.__name__ + "Result", self, getattr(self, BackFunc.__name__ + "Result"))
        except:
            pass

        def BFunc(self, *args):
            BackFunc(*args)
        BFunc.__name__ = EventName+"Notify"
        setattr(self, EventName+"Notify", MethodType(BFunc, self))
        self.ListenForEvent(ModObject.ModName, "Client", EventName+"Notify", self, getattr(self, EventName+"Notify"))
