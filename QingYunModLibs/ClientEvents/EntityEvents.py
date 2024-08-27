# coding=utf-8
ApproachEntityClientEvent = "ApproachEntityClientEvent"
'''
描述

玩家靠近生物时触发

参数
playerId	str	玩家实体id
entityId	str	靠近的生物实体id

返回值
无

在零件中直接声明一个同名函数，即可完成监听，详情参考零件事件
'''


EntityModelChangedClientEvent = "EntityModelChangedClientEvent"
'''
描述

触发时机：实体模型切换时触发

参数

entityId	str	实体id
newModel	str	新的模型名字
oldModel	str	原来的模型名字

返回值
无

在零件中直接声明一个同名函数，即可完成监听，详情参考零件事件
'''


EntityStopRidingEvent = "EntityStopRidingEvent"
'''
描述

触发时机：当实体停止骑乘时

参数

id	str	实体id
rideId	str	坐骑id
exitFromRider	bool	是否下坐骑
entityIsBeingDestroyed	bool	坐骑是否将要销毁
switchingRides	bool	是否换乘坐骑
cancel	bool	设置为True可以取消（需要与服务端事件一同取消）

返回值
无

备注
以下情况不允许取消
ride组件StopEntityRiding接口
玩家传送时
坐骑死亡时
玩家睡觉时
玩家死亡时
未驯服的马
怕水的生物坐骑进入水里
切换维度
在零件中直接声明一个同名函数，即可完成监听，详情参考零件事件
'''


HealthChangeClientEvent = "HealthChangeClientEvent"
'''
描述

生物生命值发生变化时触发

参数

entityId	str	实体id
from	float	变化前的生命值
to	float	变化后的生命值
返回值

无
'''


LeaveEntityClientEvent = "LeaveEntityClientEvent"
'''
描述

玩家远离生物时触发

参数

playerId	str	玩家实体id
entityId	str	远离的生物实体id
返回值

无
'''


OnGroundClientEvent = "OnGroundClientEvent"
'''
描述

实体着地事件。玩家，沙子，铁砧，掉落的物品，点燃的TNT掉落地面时触发，其余实体着地不触发。

参数

id	str	实体id
返回值

无

备注

因为掉落是服务端与客户端各自计算的，对于掉落的方块，有时会出现服务端先着地，然后把FallingBlock实体移除掉了，导致客户端没触发着地事件的情况。
'''


OnMobHitMobClientEvent = "OnMobHitMobClientEvent"
'''
描述

触发时机：通过OpenPlayerHitMobDetection打开生物碰撞检测后，当生物间（包含玩家）碰撞时触发该事件。注：客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。

参数

mobId	str	当前生物的id
hittedMobList	list[str]	当前生物碰撞到的其他所有生物id的list
返回值

无

备注

本事件代替原有的OnPlayerHitMobClientEvent事件
'''


StartRidingClientEvent = "StartRidingClientEvent"
'''
描述

触发时机：一个实体即将骑乘另外一个实体

参数

actorId	str	骑乘者的唯一ID
victimId	str	被骑乘实体的唯一ID
返回值

无

备注

如果需要修改cancel，请通过服务端事件StartRidingServerEvent同步修改，客户端触发该事件时，实体已经骑乘成功。
'''