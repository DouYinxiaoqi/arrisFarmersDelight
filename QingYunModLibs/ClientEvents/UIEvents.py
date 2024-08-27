# coding=utf-8
ClientChestCloseEvent = "ClientChestCloseEvent"
'''
描述

关闭箱子界面时触发，包括小箱子，合并后大箱子和末影龙箱子

参数

无

返回值

无
'''


ClientChestOpenEvent = "ClientChestOpenEvent"
'''
描述

打开箱子界面时触发，包括小箱子，合并后大箱子和末影龙箱子

参数

playerId	str	玩家实体id
x	int	箱子位置x值
y	int	箱子位置y值
z	int	箱子位置z值
返回值

无
'''


ClientPlayerInventoryCloseEvent = "ClientPlayerInventoryCloseEvent"
'''
描述

关闭物品背包界面时触发

参数

无

返回值

无
'''


ClientPlayerInventoryOpenEvent = "ClientPlayerInventoryOpenEvent"
'''
描述

打开物品背包界面时触发

参数

isCreative	bool	是否是创造模式背包界面
cancel	bool	取消打开物品背包界面
返回值

无
'''


CloseNeteaseShopEvent = "CloseNeteaseShopEvent"
'''
描述

关闭商城界面时触发，包括脚本商城和Apollo插件商城

参数

无

返回值

无
'''


GridComponentSizeChangedClientEvent = "GridComponentSizeChangedClientEvent"
'''
描述

触发时机：UI grid组件里格子数目发生变化时触发

参数

无

返回值

无
'''


OnItemSlotButtonClickedEvent = "OnItemSlotButtonClickedEvent"
'''
描述

点击快捷栏和背包栏的物品槽时触发

参数

slotIndex	int	点击的物品槽的编号
返回值

无
'''


PlayerChatButtonClickClientEvent = "PlayerChatButtonClickClientEvent"
'''
描述

玩家点击聊天按钮或回车键触发呼出聊天窗口时客户端抛出的事件

参数

无

返回值

无
'''


PopScreenAfterClientEvent = "PopScreenAfterClientEvent"
'''
描述

screen移除触发

参数

screenName	str	UI名字
返回值

无

备注

与PopScreenEvent不同，PopScreenAfterClientEvent触发时机是在完全把UI弹出后，返回的screenName是弹出后最顶层UI的Screen名
'''


PopScreenEvent = "PopScreenEvent"
'''
描述

screen移除触发

参数

screenName	str	UI名字
返回值

无

备注

screenName为正在弹出的Screen名，如果需要获取下一个Screen可使用PopScreenAfterClientEvent
'''


PushScreenEvent = "PushScreenEvent"
'''
描述

screen创建触发

参数

screenName	str	UI名字
返回值

无
'''


ScreenSizeChangedClientEvent = "ScreenSizeChangedClientEvent"
'''
描述

改变屏幕大小时会触发的事件

参数

beforeX	float	屏幕大小改变前的宽度
beforeY	float	屏幕大小改变前的高度
afterX	float	屏幕大小改变后的宽度
afterY	float	屏幕大小改变后的高度
返回值

无

备注

该事件仅支持PC
'''


UiInitFinished = "UiInitFinished"
'''
描述

UI初始化框架完成,此时可以创建UI

参数

无

返回值

无

备注

切换维度后会重新初始化UI并触发该事件
'''
