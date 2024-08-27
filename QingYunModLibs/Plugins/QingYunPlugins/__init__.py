from ... import SystemApi
if SystemApi.ClientComp.CreateModAttr(SystemApi.levelId):
    import QingYunClient

if SystemApi.ServerComp.CreateModAttr(SystemApi.levelId):
    import QingYunServer