# coding=utf-8
lobbyGoodBuySucServerEvent = "lobbyGoodBuySucServerEvent"
'''
描述

玩家登录联机大厅服务器，或者联机大厅游戏内购买商品时触发。如果是玩家登录，触发时玩家客户端已经触发了UiInitFinished事件

参数

eid	str	购买商品的玩家实体id
buyItem	bool	玩家登录时为False，玩家购买了商品时为True
返回值

无
'''