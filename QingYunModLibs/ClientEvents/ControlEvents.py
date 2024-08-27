# coding=utf-8
ClientJumpButtonPressDownEvent = "ClientJumpButtonPressDownEvent"
'''
描述

跳跃按钮按下事件，返回值设置参数只对当次按下事件起作用

参数

continueJump	bool	设置是否执行跳跃逻辑
返回值

无
'''


ClientJumpButtonReleaseEvent = "ClientJumpButtonReleaseEvent"
'''
描述

跳跃按钮按下释放事件

参数

无

返回值

无
'''


GetEntityByCoordEvent = "GetEntityByCoordEvent"
'''
描述

玩家点击屏幕时触发，多个手指点在屏幕上时，只有第一个会触发。

参数

无

返回值

无
'''


GetEntityByCoordReleaseClientEvent = "GetEntityByCoordReleaseClientEvent"
'''
描述

玩家点击屏幕后松开时触发，多个手指点在屏幕上时，只有最后一个手指松开时触发。

参数

无

返回值

无
'''


HoldBeforeClientEvent = "HoldBeforeClientEvent"
'''
描述

玩家长按屏幕，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用RightClickBeforeClientEvent事件监听鼠标右键

参数

cancel	bool	设置为True可拦截原版的挖方块/使用物品/与实体交互响应
返回值

无

备注

玩家长按屏幕的处理顺序为：
玩家点击屏幕，在长按判定时间内（默认为400毫秒，可通过SetHoldTimeThreshold接口修改）一直没有进行拖动或松手
触发该事件
若事件没有cancel，则根据主手上的物品，准心处的物体类型以及与玩家的距离，进行挖方块/使用物品/与实体交互等操作 即该事件只会在到达长按判定时间的瞬间触发一次，后面一直按住不会连续触发，可以使用TapOrHoldReleaseClientEvent监听长按后松手
与TapBeforeClientEvent事件类似，被ui层捕获，没有穿透到世界的点击不会触发该事件
'''


LeftClickBeforeClientEvent = "LeftClickBeforeClientEvent"
'''
描述

玩家按下鼠标左键时触发。仅在pc的普通控制模式（即非F11模式）下触发。

参数

cancel	bool	设置为True可拦截原版的挖方块或攻击响应
返回值

无
'''


LeftClickReleaseClientEvent = "LeftClickReleaseClientEvent"
'''
描述

玩家松开鼠标左键时触发。仅在pc的普通控制模式（即非F11模式）下触发。

参数

无

返回值

无
'''


MouseWheelClientEvent = "MouseWheelClientEvent"
'''
描述

鼠标滚轮滚动时触发

参数

direction	int	1为向上滚动，0为向下滚动
返回值

无
'''


OnBackButtonReleaseClientEvent = "OnBackButtonReleaseClientEvent"
'''
描述

返回按钮（目前特指安卓系统导航中的返回按钮）松开时触发

参数

无

返回值

无

备注

目前仅安卓平台可用
'''


OnClientPlayerStartMove = "OnClientPlayerStartMove"
'''
描述

移动按钮按下触发事件，在按住一个方向键的同时，去按另外一个方向键，不会触发第二次

参数

无

返回值

无
'''


OnClientPlayerStopMove = "OnClientPlayerStopMove"
'''
描述

移动按钮按下释放时触发事件，同时按下多个方向键，需要释放所有的方向键才会触发事件

参数

无

返回值

无
'''


OnKeyPressInGame = "OnKeyPressInGame"
'''
描述

按键按下或按键释放时触发

参数

screenName	str	当前screenName
key	str	键码（注：这里的int型被转成了str型，比如"1"对应的就是枚举值文档中的1），详见KeyBoardType枚举
isDown	str	是否按下，按下为1，弹起为0
返回值

无
'''


OnMouseMiddleDownClientEvent = "OnMouseMiddleDownClientEvent"
'''
描述

鼠标按下中键时触发

参数

isDown	int	1为按下，0为弹起
mousePositionX	float	按下时的x坐标
mousePositionY	float	按下时的y坐标
返回值

无

备注

仅通过PushScreen创建的界面能够正常返回坐标，开启F11模式的时候，返回最后点击屏幕时的坐标
'''


RightClickBeforeClientEvent = "RightClickBeforeClientEvent"
'''
描述

玩家按下鼠标右键时触发。仅在pc下触发（普通控制模式及F11模式都会触发）。

参数

cancel	bool	设置为True可拦截原版的物品使用/实体交互响应
返回值

无
'''


RightClickReleaseClientEvent = "RightClickReleaseClientEvent"
'''
描述

玩家松开鼠标右键时触发。仅在pc的普通控制模式（即非F11模式）下触发。在F11下右键，按下会触发RightClickBeforeClientEvent，松开时会触发TapOrHoldReleaseClientEvent

参数

无

返回值

无

备注

pc的普通控制模式下的鼠标点击流程见TapOrHoldReleaseClientEvent备注中的配图
'''


TapBeforeClientEvent = "TapBeforeClientEvent"
'''
描述

玩家点击屏幕并松手，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用LeftClickBeforeClientEvent事件监听鼠标左键

参数

参数名	
数据类型
说明
cancel	bool	设置为True可拦截原版的攻击或放置响应
返回值

无

备注

玩家点击屏幕的处理顺序为：
1.玩家点击屏幕，没有进行拖动，并在短按判定时间（250毫秒）内松手
2.触发该事件
3.若事件没有cancel，则根据准心处的物体类型以及与玩家的距离，进行攻击或放置等操作
与GetEntityByCoordEvent事件不同的是，被ui层捕获，没有穿透到世界的点击不会触发该事件，例如：
1.点击原版的移动/跳跃等按钮，
2.通过SetIsHud(0)屏蔽了游戏操作
3.对按钮使用AddTouchEventHandler接口时isSwallow参数设置为True
'''


TapOrHoldReleaseClientEvent = "TapOrHoldReleaseClientEvent"
'''
描述

玩家点击屏幕后松手时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用LeftClickReleaseClientEvent与RightClickReleaseClientEvent事件监听鼠标松开

参数

无

返回值

无

备注

短按及长按后松手都会触发该事件
移动端及pc的F11模式下点触流程见下图
https://mc.163.com/dev/mcmanual/mc-dev/assets/img/pe_touch_event.4e2b39b0.png
'''


OnGamepadKeyPressClientEvent = "OnGamepadKeyPressClientEvent"
'''
描述

游戏手柄按键事件

参数

screenName	str	当前screenName
key	int	键码，详见GamepadKeyType枚举
isDown	str	是否按下，按下为1，弹起为0

返回值

无
'''


OnGamepadStickClientEvent = "OnGamepadStickClientEvent"
'''
描述

游戏手柄摇杆事件

参数

key	int	键码，详见GamepadKeyType枚举
x	float	摇杆水平方向的值，从左到右取值为 -1.0 ~ 1.0
y	float	摇杆竖直方向的值，从下到上取值为 -1.0 ~ 1.0

返回值

无

备注

触发时机：当摇杆摇动位置发生改变时
'''


OnGamepadTriggerClientEvent = "OnGamepadTriggerClientEvent"
'''
描述

游戏手柄扳机事件

参数

key	int	键码，详见GamepadKeyType枚举
magnitude	float	扣动扳机的力度，取值为 0 ~ 1.0

返回值

无

备注

触发时机：当扣动扳机的力度发生改变时
'''