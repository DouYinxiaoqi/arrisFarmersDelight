from ... import SystemApi
if SystemApi.ClientComp.CreateModAttr(SystemApi.levelId):
    import KeyBoardClient

if SystemApi.ServerComp.CreateModAttr(SystemApi.levelId):
    import KeyBoardServer
