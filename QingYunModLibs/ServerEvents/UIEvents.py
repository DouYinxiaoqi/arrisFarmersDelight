# coding=utf-8
PlayerInventoryOpenScriptServerEvent = "PlayerInventoryOpenScriptServerEvent"
'''
描述

某个客户端打开物品背包界面时触发

参数

playerId	str	客户端对应的玩家entity的唯一ID
isCreative	bool	是否是创造模式背包界面
返回值

无

备注

可以监听此事件判定客户端是否打开了创造背包
'''


UrgeShipEvent = "UrgeShipEvent"
'''
描述

玩家点击商城催促发货按钮时触发该事件

参数

playerId	str	玩家id
返回值

无
'''