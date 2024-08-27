# coding=utf-8
import uuid

from ..StateMachineSystem import StateMachine_Server
from ..ServerMod import *


class State(StateMachine_Server.State):
    def __init__(self, entityId, StateType):
        StateMachine_Server.State.__init__(self, entityId, StateType)
        self.ComponentGroup = []

    def TranslateToState(self, OldState):
        StateMachine_Server.State.TranslateToState(self, OldState)
        for Component in self.ComponentGroup:
            ServerComp.CreateEntityEvent(self.ControllerId).AddActorComponentGroup(Component)

    def TranslateOutState(self, NewState):
        StateMachine_Server.State.TranslateOutState(self, NewState)
        for Component in self.ComponentGroup:
            ServerComp.CreateEntityEvent(self.ControllerId).RemoveActorComponentGroup(Component)


def RegisterComponentController(identifier):
    def OnRegister(EntityComponentController):
        def OnCreateEntity(args):
            entityId = args['id']
            if identifier == ServerApi.Entity.EngineType.GetEngineTypeStr(entityId):
                EntityComponentController(entityId, identifier)
        OnCreateEntity.func_name += "_" + str(uuid.uuid4())
        ListenServerEvents(ServerEvents.WorldEvents.AddEntityServerEvent, OnCreateEntity)
        return EntityComponentController
    return OnRegister


class EntityComponentController(object):
    def __init__(self, entityId, identifier):
        self.identifier = identifier
        self.entityId = entityId
        DefaultState = State(entityId, "Default")
        self.EntityStateMachine = StateMachine_Server.StateMachine(DefaultState)
        self.OnCreate()

        def OnTick():
            self.OnTick()
        self.TickTimer = CreateTimer(0.0, OnTick, True)

        def OnDestroy(args):
            if args['id'] == self.entityId:
                self.OnDestroy()
                self.EntityStateMachine.Destroy()
                DestroyTimer(self.TickTimer)
                UnListenServer(ServerEvents.WorldEvents.EntityRemoveEvent, OnDestroy)
        OnDestroy.func_name += "_" + str(uuid.uuid4())
        ListenServerEvents(ServerEvents.WorldEvents.EntityRemoveEvent, OnDestroy)

    def OnCreate(self):
        print "%s has created and that entityId is %s" % (self.identifier, self.entityId)

    def OnTick(self):
        print "%s Tick %s" % (self.identifier, self.entityId)

    def OnDestroy(self):
        print "%s has destroy and that entityId is %s" % (self.identifier, self.entityId)
