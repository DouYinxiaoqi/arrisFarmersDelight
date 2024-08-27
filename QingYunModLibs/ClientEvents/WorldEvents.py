# coding=utf-8
AddEntityClientEvent = "AddEntityClientEvent"
'''
描述

客户端侧创建新实体时触发

参数

id	str	实体id
posX	float	位置x
posY	float	位置y
posZ	float	位置z
dimensionId	int	实体维度
isBaby	bool	是否为幼儿
engineTypeStr	str	实体类型
itemName	str	物品identifier（仅当物品实体时存在该字段）
auxValue	int	物品附加值（仅当物品实体时存在该字段）

返回值
无

备注

创建玩家时不会触发该事件
'''


AddPlayerAOIClientEvent = "AddPlayerAOIClientEvent"
'''
描述

玩家加入游戏或者其余玩家进入当前玩家视野时触发的事件，替换AddPlayerEvent

参数

playerId	str	玩家id
返回值

无

备注

该事件触发只表明在服务端数据中接收到了新玩家，并不能代表此时玩家在客户端中可见，若想在玩家进入视野后立马调用玩家渲染相关接口，建议使用AddPlayerCreatedClientEvent。
'''


AddPlayerCreatedClientEvent = "AddPlayerCreatedClientEvent"
'''
描述

玩家进入当前玩家所在的区块AOI后，玩家皮肤数据异步加载完成后触发的事件

参数

playerId	str	玩家id
返回值

无

备注

由于玩家皮肤是异步加载的原因，该事件触发时机比AddPlayerAOIClientEvent晚，触发该事件后可以对该玩家调用相关玩家渲染接口。
当前客户端每加载好一个玩家的皮肤，就会触发一次该事件，比如刚进入世界时，localPlayer加载好会触发一次，周围的所有玩家加载好后也会分别触发一次。
'''


ChunkAcquireDiscardedClientEvent = "ChunkAcquireDiscardedClientEvent"
'''
描述

触发时机：客户端区块即将被卸载时

参数

dimension	int	区块所在维度
chunkPosX	int	区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15]
chunkPosZ	int	区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15]
返回值

无

备注

区块卸载：游戏只会加载玩家周围的区块，玩家移动到别的区域时，原来所在区域的区块会被卸载，参考区块介绍
'''


ChunkLoadedClientEvent = "ChunkLoadedClientEvent"
'''
描述

触发时机：客户端区块加载完成时

参数

dimension	int	区块所在维度
chunkPosX	int	区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15]
chunkPosZ	int	区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15]
返回值

无
'''


LoadClientAddonScriptsAfter = "LoadClientAddonScriptsAfter"
'''
描述

客户端加载mod完成事件

参数

无

返回值

无
'''


OnCommandOutputClientEvent = "OnCommandOutputClientEvent"
'''
描述

当command命令有成功消息输出时触发

参数

command	str	命令名称
message	str	命令返回的消息
返回值

无

备注

部分命令在返回的时候没有命令名称，SetCommand接口需要showOutput参数为True时才会有返回
'''


OnLocalPlayerStopLoading = "OnLocalPlayerStopLoading"
'''
描述

触发时机：玩家进入存档，出生点地形加载完成时触发。该事件触发时可以进行切换维度的操作。

参数

playerId	str	加载完成的玩家id
返回值

无
'''


OnScriptTickClient = "OnScriptTickClient"
'''
描述

客户端tick事件,1秒30次

参数

无

返回值

无
'''


RemoveEntityClientEvent = "RemoveEntityClientEvent"
'''
描述

客户端侧实体被移除时触发

参数

id	str	移除的实体id
返回值

无

备注

客户端接收到了服务端监测实体离开玩家视野时触发，原事件名 RemoveEntityPacketEvent
'''


RemovePlayerAOIClientEvent = "RemovePlayerAOIClientEvent"
'''
描述

玩家离开当前玩家视野时触发的事件

参数

playerId	str	玩家id
返回值

无
'''


UnLoadClientAddonScriptsBefore = "UnLoadClientAddonScriptsBefore"
'''
描述

客户端卸载mod之前触发

参数

无

返回值

无
'''