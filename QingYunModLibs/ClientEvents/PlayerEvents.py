# coding=utf-8
CameraMotionStartClientEvent = "CameraMotionStartClientEvent"
'''
描述

相机运动器开始事件。相机添加运动器后，运动器开始运行时触发

参数

motionId	int	运动器id
返回值

无
'''


CameraMotionStopClientEvent = "CameraMotionStopClientEvent"
'''
描述

相机运动器停止事件。相机添加运动器并开始运行后，运动器自动停止时触发

参数

motionId	int	运动器id
remove	bool	是否移除该运动器，设置为False则保留，默认为True，即运动器停止后自动移除
返回值

无

备注

注意：该事件触发表示运动器播放顺利完成，手动调用的StopCameraMotion、RemoveCameraMotion不会触发该事件。
'''


DimensionChangeClientEvent = "DimensionChangeClientEvent"
'''
描述

玩家维度改变时客户端抛出

参数

playerId	str	玩家实体id
fromDimensionId	int	维度改变前的维度
toDimensionId	int	维度改变后的维度
fromX	float	改变前的位置x
fromY	float	改变前的位置Y
fromZ	float	改变前的位置Z
toX	float	改变后的位置x
toY	float	改变后的位置Y
toZ	float	改变后的位置Z
返回值

无

备注

当通过传送门从末地回到主世界时，toY值为32767，其他情况一般会比设置值高1.62
'''


DimensionChangeFinishClientEvent = "DimensionChangeFinishClientEvent"
'''
描述

玩家维度改变完成后客户端抛出

参数

playerId	str	玩家实体id
fromDimensionId	int	维度改变前的维度
toDimensionId	int	维度改变后的维度
toPos	tuple(float,float,float)	改变后的位置x,y,z,其中y值为脚底加上角色的身高值
返回值

无

备注

当通过传送门从末地回到主世界时，toPos的y值为32767，其他情况一般会比设置值高1.62
'''


ExtinguishFireClientEvent = "ExtinguishFireClientEvent"
'''
描述

玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。

参数

pos	tuple(float,float,float)	火焰方块的坐标
playerId	str	玩家id
cancel	bool	修改为True时，可阻止玩家扑灭火焰。需要与ExtinguishFireServerEvent一起修改。
返回值

无
'''


GameTypeChangedClientEvent = "GameTypeChangedClientEvent"
'''
描述

个人游戏模式发生变化时客户端触发。

参数

playerId	str	玩家Id
oldGameType	int	切换前的游戏模式
newGameType	int	切换后的游戏模式
返回值

无

备注

游戏模式：GetMinecraftEnum().GameType.*:Survival，Creative，Adventure分别为0~2 默认游戏模式发生变化时最后反映在个人游戏模式之上。
'''


OnPlayerHitBlockClientEvent = "OnPlayerHitBlockClientEvent"
'''
描述

触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。玩家着地时会触发OnGroundClientEvent，而不是该事件。客户端和服务端分别作碰撞检测，可能两个事件返回的结果略有差异。

参数

playerId	str	碰撞到方块的玩家Id
posX	int	碰撞方块x坐标
posY	int	碰撞方块y坐标
posZ	int	碰撞方块z坐标
blockId	str	碰撞方块的identifier
auxValue	int	碰撞方块的附加值
返回值

无
'''


PerspChangeClientEvent = "PerspChangeClientEvent"
'''
描述

视角切换时会触发的事件

参数

from	int	切换前的视角
to	int	切换后的视角
返回值

无

备注

视角数字代表含义 0: 第一人称 1: 第三人称背面 2: 第三人称正面
'''