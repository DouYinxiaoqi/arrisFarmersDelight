# coding=utf-8
BlockDestroyByLiquidServerEvent = "BlockDestroyByLiquidServerEvent"
'''
描述

触发时机：方块被水流破坏的事件

参数

x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
liquidName	str	流体方块id
blockName	str	方块id
auxValue	int	方块附加值
返回值

无

备注

指令或者接口的设置不会触发该事件
'''


BlockLiquidStateChangeAfterServerEvent = "BlockLiquidStateChangeAfterServerEvent"
'''
描述

触发时机：方块转为含水或者脱离含水(流体)后触发

参数

blockName	str	方块的identifier，包含命名空间及名称
auxValue	int	方块附加值
dimension	int	方块维度
x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
turnLiquid	bool	是否转为含水，true则转为含水，false则脱离含水
返回值

无
'''


BlockLiquidStateChangeServerEvent = "BlockLiquidStateChangeServerEvent"
'''
描述

触发时机：方块转为含水或者脱离含水(流体)前触发

参数

blockName	str	方块的identifier，包含命名空间及名称
auxValue	int	方块附加值
dimension	int	方块维度
x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
turnLiquid	bool	是否转为含水，true则转为含水，false则脱离含水
返回值

无
'''


BlockNeighborChangedServerEvent = "BlockNeighborChangedServerEvent"
'''
描述

触发时机：自定义方块周围的方块发生变化时，需要配置netease:neighborchanged_sendto_script，详情请查阅《自定义农作物》文档

参数

dimensionId	int	维度
posX	int	方块x坐标
posY	int	方块y坐标
posZ	int	方块z坐标
blockName	str	方块的identifier，包含命名空间及名称
auxValue	int	方块附加值
neighborPosX	int	变化方块x坐标
neighborPosY	int	变化方块y坐标
neighborPosZ	int	变化方块z坐标
fromBlockName	str	方块变化前的identifier，包含命名空间及名称
fromBlockAuxValue	int	方块变化前附加值
toBlockName	str	方块变化后的identifier，包含命名空间及名称
toAuxValue	int	方块变化后附加值
返回值

无
'''


BlockRandomTickServerEvent = "BlockRandomTickServerEvent"
'''
描述

触发时机：自定义方块配置netease:random_tick随机tick时

参数

posX	int	方块x坐标
posY	int	方块y坐标
posZ	int	方块z坐标
blockName	str	方块名称
fullName	str	方块的identifier，包含命名空间及名称
auxValue	int	方块附加值
dimensionId	int	实体维度
返回值

无
'''


BlockRemoveServerEvent = "BlockRemoveServerEvent"
'''
描述

触发时机：监听该事件的方块在销毁时触发，可以通过ListenOnBlockRemoveEvent方法进行监听，或者通过json组件netease:listen_block_remove进行配置

参数

x	int	方块位置x
y	int	方块位置y
z	int	方块位置z
fullName	str	方块的identifier，包含命名空间及名称
auxValue	int	方块的附加值
dimension	int	该方块所在的维度
返回值

无
'''


BlockSnowStateChangeAfterServerEvent = "BlockSnowStateChangeAfterServerEvent"
'''
描述

触发时机：方块转为含雪或者脱离含雪后触发

参数

dimension	int	方块维度
x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
turnSnow	bool	是否转为含雪，true则转为含雪，false则脱离含雪
setBlockType	int	方块进入脱离含雪的原因，参考SetBlockType
返回值

无
'''


BlockSnowStateChangeServerEvent = "BlockSnowStateChangeServerEvent"
'''
描述

触发时机：方块转为含雪或者脱离含雪前触发

参数

dimension	int	方块维度
x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
turnSnow	bool	是否转为含雪，true则转为含雪，false则脱离含雪
setBlockType	int	方块进入脱离含雪的原因，参考SetBlockType
返回值

无
'''


BlockStrengthChangedServerEvent = "BlockStrengthChangedServerEvent"
'''
描述

触发时机：自定义机械元件方块红石信号量发生变化时触发

参数

posX	int	方块x坐标
posY	int	方块y坐标
posZ	int	方块z坐标
blockName	str	方块的identifier，包含命名空间及名称
auxValue	int	方块附加值
newStrength	int	变化后的红石信号量
dimensionId	int	维度
返回值

无
'''


ChestBlockTryPairWithServerEvent = "ChestBlockTryPairWithServerEvent"
'''
描述

触发时机：两个并排的小箱子方块准备组合为一个大箱子方块时

参数

cancel	bool	是否允许触发，默认为False，若设为True，可阻止小箱子组合成为一个大箱子
blockX	int	小箱子方块x坐标
blockY	int	小箱子方块y坐标
blockZ	int	小箱子方块z坐标
otherBlockX	int	将要与之组合的另外一个小箱子方块x坐标
otherBlockY	int	将要与之组合的另外一个小箱子方块y坐标
otherBlockZ	int	将要与之组合的另外一个小箱子方块z坐标
dimensionId	int	维度id
返回值

无
'''


CommandBlockContainerOpenEvent = "CommandBlockContainerOpenEvent"
'''
描述

触发时机：玩家点击命令方块，尝试打开命令方块的设置界面

参数

playerId	str	玩家实体id
isBlock	bool	是否以方块坐标的形式定位命令方块，当为True时下述的blockX/blockY/blockZ有意义，当为False时，下述的victimId有意义
blockX	int	命令方块位置x，当isBlock为True时有效
blockY	int	命令方块位置y，当isBlock为True时有效
blockZ	int	命令方块位置z，当isBlock为True时有效
victimId	str	命令方块对应的逻辑实体的唯一id，当isBlock为False时有效
cancel	bool	修改为True时，可以阻止玩家打开命令方块的设置界面
返回值

无
'''


CommandBlockUpdateEvent = "CommandBlockUpdateEvent"
'''
描述

触发时机：玩家尝试修改命令方块的内置命令时

参数

playerId	str	玩家实体id
playerUid	int/long	玩家的uid
command	str	企图修改的命令方块中的命令内容字符串
isBlock	bool	是否以方块坐标的形式定位命令方块，当为True时下述的blockX/blockY/blockZ有意义，当为False时，下述的victimId有意义
blockX	int	命令方块位置x，当isBlock为True时有效
blockY	int	命令方块位置y，当isBlock为True时有效
blockZ	int	命令方块位置z，当isBlock为True时有效
victimId	str	命令方块对应的逻辑实体的唯一id，当isBlock为False时有效
cancel	bool	修改为True时，可以阻止玩家修改命令方块的内置命令
返回值

无

备注

当修改的目标为命令方块矿车时（此时isBlock为False），设置cancel为True，依旧可以阻止修改命令方块矿车的内部指令，但是从客户端能够看到命令方块矿车的内部指令变化了，不过这仅仅是假象，重新登录或者其他客户端打开命令方块矿车的设置界面，就会发现其实内部指令没有变化
'''


DestroyBlockEvent = "DestroyBlockEvent"
'''
描述

触发时机：当方块已经被玩家破坏时触发该事件。

参数

x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
face	int	方块被敲击的面向id，参考Facing枚举
fullName	str	方块的identifier，包含命名空间及名称
auxData	int	方块附加值
playerId	str	破坏方块的玩家ID
dimensionId	int	维度id
返回值

无

备注

在生存模式或创造模式下都会触发
'''


DirtBlockToGrassBlockServerEvent = "DirtBlockToGrassBlockServerEvent"
'''
描述

触发时机：泥土方块变成草方块时触发

参数

dimension	int	方块维度
x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
返回值

无

备注

指令或者接口的设置不会触发该事件
'''


EntityPlaceBlockAfterServerEvent = "EntityPlaceBlockAfterServerEvent"
'''
描述

触发时机：当生物成功放置方块后触发

参数

x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
fullName	str	方块的identifier，包含命名空间及名称
auxData	int	方块附加值
entityId	str	试图放置方块的生物ID
dimensionId	int	维度id
face	int	点击方块的面，参考Facing枚举
返回值

无

备注

部分放置后会产生实体的方块、可操作的方块、带有特殊逻辑的方块，不会触发该事件，包括但不限于床、门、告示牌、花盆、红石中继器、船、炼药锅、头部模型、蛋糕、酿造台、盔甲架等。
'''


FallingBlockBreakServerEvent = "FallingBlockBreakServerEvent"
'''
描述

触发时机：当下落的方块实体被破坏时，服务端触发该事件

参数

fallingBlockId	str	下落的方块实体id
fallingBlockX	float	下落的方块实体位置x
fallingBlockY	float	下落的方块实体位置y
fallingBlockZ	float	下落的方块实体位置z
blockName	str	重力方块的identifier，包含命名空间及名称
fallTickAmount	int	下落的方块实体持续下落了多少tick
dimensionId	int	下落的方块实体维度id
cancelDrop	bool	是否取消方块物品掉落，可以在脚本层中设置
返回值

无

备注

不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）
'''


FallingBlockCauseDamageBeforeServerEvent = "FallingBlockCauseDamageBeforeServerEvent"
'''
描述

触发时机：当下落的方块开始计算砸到实体的伤害时，服务端触发该事件

参数

fallingBlockId	str	下落的方块实体id
fallingBlockX	float	下落的方块实体位置x
fallingBlockY	float	下落的方块实体位置y
fallingBlockZ	float	下落的方块实体位置z
blockName	str	重力方块的identifier，包含命名空间及名称
dimensionId	int	下落的方块实体维度id
collidingEntitys	list(str)	当前碰撞到的实体列表id，如果没有的话是None
fallTickAmount	int	下落的方块实体持续下落了多少tick
fallDistance	float	下落的方块实体持续下落了多少距离
isHarmful	bool	是否计算对实体的伤害，引擎传来的值由json配置和伤害是否大于0决定，可在脚本层修改传回引擎
fallDamage	int	对实体的伤害，引擎传来的值距离和json配置决定，可在脚本层修改传回引擎
返回值

无

备注

不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）
服务端通常触发在客户端之后，而且有时会相差一个tick，这就意味着可能发生以下现象:服务端fallTickAmount比配置强制破坏时间多1tick，下落的距离、下落的伤害计算出来比客户端时间多1tick的误差。
'''


FallingBlockReturnHeavyBlockServerEvent = "FallingBlockReturnHeavyBlockServerEvent"
'''
描述

触发时机：当下落的方块实体变回普通重力方块时，服务端触发该事件

参数

fallingBlockId	int	下落的方块实体id
blockX	int	方块位置x
blockY	int	方块位置y
blockZ	int	方块位置z
heavyBlockName	str	重力方块的identifier，包含命名空间及名称
prevHereBlockName	str	变回重力方块时，原本方块位置的identifier，包含命名空间及名称
dimensionId	int	下落的方块实体维度id
fallTickAmount	int	下落的方块实体持续下落了多少tick
返回值

无

备注

不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）
'''


FarmBlockToDirtBlockServerEvent = "FarmBlockToDirtBlockServerEvent"
'''
描述

触发时机：耕地退化为泥土时触发

参数

dimension	int	方块维度
x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
setBlockType	int	耕地退化为泥土的原因，参考SetBlockType
返回值

无

备注

指令或者接口的设置不会触发该事件
'''


GrassBlockToDirtBlockServerEvent = "GrassBlockToDirtBlockServerEvent"
'''
描述

触发时机：草方块变成泥土方块时触发

参数

dimension	int	方块维度
x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
返回值

无

备注

指令或者接口的设置不会触发该事件
'''


HeavyBlockStartFallingServerEvent = "HeavyBlockStartFallingServerEvent"
'''
描述

触发时机：当重力方块变为下落的方块实体后，服务端触发该事件

参数

fallingBlockId	str	下落的方块实体id
blockX	int	方块位置x
blockY	int	方块位置y
blockZ	int	方块位置z
blockName	str	重力方块的identifier，包含命名空间及名称
dimensionId	int	下落的方块实体维度id
返回值

无

备注

不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）
'''


HopperTryPullInServerEvent = "HopperTryPullInServerEvent"
'''
描述

触发时机：当漏斗上方连接容器后，容器往漏斗开始输入物品时触发，事件仅触发一次

参数

x	int	漏斗位置x
y	int	漏斗位置y
z	int	漏斗位置z
abovePosX	int	交互的容器位置x
abovePosY	int	交互的容器位置y
abovePosZ	int	交互的容器位置z
dimensionId	int	维度id
canHopper	bool	是否允许容器往漏斗加东西(要关闭此交互，需先监听此事件再放置容器)
返回值

无
'''


HopperTryPullOutServerEvent = "HopperTryPullOutServerEvent"
'''
描述

触发时机：当漏斗以毗邻的方式连接容器时，即从旁边连接容器时，漏斗向容器开始输出物品时触发，事件仅触发一次

参数

x	int	漏斗位置x
y	int	漏斗位置y
z	int	漏斗位置z
attachedPosX	int	交互的容器位置x
attachedPosY	int	交互的容器位置y
attachedPosZ	int	交互的容器位置z
dimensionId	int	维度id
canHopper	bool	是否允许漏斗往容器加东西(要关闭此交互，需先监听此事件再放置容器)
返回值

无
'''


OnAfterFallOnBlockServerEvent = "OnAfterFallOnBlockServerEvent"
'''
描述

触发时机：当实体降落到方块后服务端触发，主要用于力的计算

参数

entityId	str	实体id
posX	float	实体位置x
posY	float	实体位置y
posZ	float	实体位置z
motionX	float	瞬时移动X方向的力
motionY	float	瞬时移动Y方向的力
motionZ	float	瞬时移动Z方向的力
blockName	str	方块的identifier，包含命名空间及名称
calculate	bool	是否按脚本层传值计算力
返回值

无

备注

不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件）
如果要在脚本层修改motion，回传的需要是浮点型，例如需要赋值0.0而不是0
如果需要修改实体的力，最好配合客户端事件同步修改，避免产生非预期现象
因为引擎最后一定会按照原版方块规则计算力（普通方块置0，床、粘液块等反弹），所以脚本层如果想直接修改当前力需要将calculate设为true取消原版计算，按照传回值计算
引擎在落地之后，OnAfterFallOnBlockServerEvent会一直触发，因此请在脚本层中做对应的逻辑判断
'''


OnBeforeFallOnBlockServerEvent = "OnBeforeFallOnBlockServerEvent"
'''
描述

触发时机：当实体刚降落到方块上时服务端触发，主要用于伤害计算

参数

entityId	str	实体id
blockX	int	方块位置x
blockY	int	方块位置y
blockZ	int	方块位置z
blockName	str	方块的identifier，包含命名空间及名称
fallDistance	float	实体下降距离，可在脚本层传给引擎
cancel	bool	是否取消引擎对实体下降伤害的计算
返回值

无

备注

不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件）
如果要在脚本层修改fallDistance，回传的一定要是浮点型，例如需要赋值0.0而不是0
可能会因为轻微的反弹触发多次，可在脚本层针对fallDistance的值进行判断
'''


OnEntityInsideBlockServerEvent = "OnEntityInsideBlockServerEvent"
'''
描述

触发时机：当实体碰撞盒所在区域有方块时，服务端持续触发

参数

entityId	str	实体id
slowdownMultiX	float	实体移速X方向的减速比例，可在脚本层被修改
slowdownMultiY	float	实体移速Y方向的减速比例，可在脚本层被修改
slowdownMultiZ	float	实体移速Z方向的减速比例，可在脚本层被修改
blockX	int	方块位置x
blockY	int	方块位置y
blockZ	int	方块位置z
blockName	str	方块的identifier，包含命名空间及名称
cancel	bool	可由脚本层回传True给引擎，阻止触发后续原版逻辑
返回值

无

备注

不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件） ，原版方块需要先通过RegisterOnEntityInside接口注册才能触发
如果需要修改slowdownMulti/cancel，强烈建议与客户端事件同步修改，避免出现客户端表现不一致等非预期现象。
如果要在脚本层修改slowdownMulti，回传的一定要是浮点型，例如需要赋值1.0而不是1
有任意slowdownMulti参数被传回非0值时生效减速比例
slowdownMulti参数更像是一个Buff，例如并不是立刻计算，而是先保存在实体属性里延后计算、在已经有slowdownMulti属性的情况下会取最低的值、免疫掉落伤害等，与原版蜘蛛网逻辑基本一致。
'''


OnStandOnBlockServerEvent = "OnStandOnBlockServerEvent"
'''
描述

触发时机：当实体站立到方块上时服务端持续触发

参数

entityId	str	实体id
dimensionId	int	实体所在维度id
posX	float	实体位置x
posY	float	实体位置y
posZ	float	实体位置z
motionX	float	瞬时移动X方向的力
motionY	float	瞬时移动Y方向的力
motionZ	float	瞬时移动Z方向的力
blockX	int	方块位置x
blockY	int	方块位置y
blockZ	int	方块位置z
blockName	str	方块的identifier，包含命名空间及名称
cancel	bool	可由脚本层回传True给引擎，阻止触发后续原版逻辑
返回值

无

备注

不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件） ，原版方块需要先通过RegisterOnStandOn接口注册才能触发
如果需要修改motion/cancel，强烈建议配合客户端事件同步修改，避免出现客户端表现不一致等现象
如果要在脚本层修改motion，回传的一定要是浮点型，例如需要赋值0.0而不是0
'''


PistonActionServerEvent = "PistonActionServerEvent"
'''
描述

触发时机：活塞或者粘性活塞推送/缩回影响附近方块时

参数

cancel	bool	是否允许触发，默认为False，若设为True，可阻止触发后续的事件
action	str	推送时=expanding；缩回时=retracting
pistonFacing	int	活塞的朝向，参考Facing枚举
pistonMoveFacing	int	活塞的运动方向，参考Facing枚举
dimensionId	int	活塞方块所在的维度
pistonX	int	活塞方块的x坐标
pistonY	int	活塞方块的y坐标
pistonZ	int	活塞方块的z坐标
blockList	list[(x,y,z),...]	活塞运动影响到产生被移动效果的方块坐标(x,y,z)，均为int类型
breakBlockList	list[(x,y,z),...]	活塞运动影响到产生被破坏效果的方块坐标(x,y,z)，均为int类型
entityList	list[string,...]	活塞运动影响到产生被移动或被破坏效果的实体的ID列表
返回值

无
'''


ServerBlockEntityTickEvent = "ServerBlockEntityTickEvent"
'''
描述

触发时机：自定义方块配置了netease:block_entity组件并设tick为true，方块在玩家的模拟距离（新建存档时可以设置，默认为4个区块）内，或者在tickingarea内的时候触发

参数

blockName	str	该方块名称
dimension	int	该方块所在的维度
posX	int	该方块的x坐标
posY	int	该方块的y坐标
posZ	int	该方块的z坐标
返回值

无

备注

方块实体的tick事件频率为每秒钟20次
触发本事件时，若正在退出游戏，将无法获取到抛出本事件的方块实体数据（GetBlockEntityData函数返回None），也无法对其进行操作
'''


ServerBlockUseEvent = "ServerBlockUseEvent"
'''
描述

触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时服务端抛出该事件（该事件tick执行，需要注意效率问题）。

参数

playerId	str	玩家Id
blockName	str	方块的identifier，包含命名空间及名称
aux	int	方块附加值
cancel	bool	设置为True可拦截与方块交互的逻辑。
x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
dimensionId	int	维度id
返回值

无

备注

当对原生方块进行使用时，如堆肥桶等类似有 使用 功能的方块使用物品时，会触发该事件，而ServerItemUseOnEvent则不会被触发。当需要获取触发时使用的物品时，可以通过item组件（例如GetPlayerItem接口）获取手上有的物品。对应的客户端事件同理。
有的方块是在ServerBlockUseEvent中设置cancel生效，但是有部分方块是在ClientBlockUseEvent中设置cancel才生效，如有需求建议在两个事件中同时设置cancel以保证生效。
'''


ServerEntityTryPlaceBlockEvent = "ServerEntityTryPlaceBlockEvent"
'''
描述

触发时机：当生物试图放置方块时触发该事件。

参数

x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
fullName	str	方块的identifier，包含命名空间及名称
auxData	int	方块附加值
entityId	str	试图放置方块的生物ID
dimensionId	int	维度id
face	int	点击方块的面，参考Facing枚举
cancel	bool	默认为False，在脚本层设置为True就能取消该方块的放置
返回值

无

备注

部分放置后会产生实体的方块、可操作的方块、带有特殊逻辑的方块，不会触发该事件，包括但不限于床、门、告示牌、花盆、红石中继器、船、炼药锅、头部模型、蛋糕、酿造台、盔甲架等。
'''


ServerPlaceBlockEntityEvent = "ServerPlaceBlockEntityEvent"
'''
描述

触发时机：手动放置或通过接口创建含自定义方块实体的方块时触发，此时可向该方块实体中存放数据

参数

blockName	str	该方块名称
dimension	int	该方块所在的维度
posX	int	该方块的x坐标
posY	int	该方块的y坐标
posZ	int	该方块的z坐标
返回值

无
'''


ServerPlayerTryDestroyBlockEvent = "ServerPlayerTryDestroyBlockEvent"
'''
描述

当玩家即将破坏方块时，服务端线程触发该事件。

参数

x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
face	int	方块被敲击的面向id，参考Facing枚举
fullName	str	方块的identifier，包含命名空间及名称
auxData	int	方块附加值
playerId	str	试图破坏方块的玩家ID
dimensionId	int	维度id
cancel	bool	默认为False，在脚本层设置为True就能取消该方块的破坏
spawnResources	bool	是否生成掉落物，默认为True，在脚本层设置为False就能取消生成掉落物
返回值

无

备注

若需要禁止某些特殊方块的破坏，需要配合PlayerTryDestroyBlockClientEvent一起使用，例如床，旗帜，箱子这些根据方块实体数据进行渲染的方块
该服务端事件触发于玩家破坏方块时，当方块为秒破方块时（破坏方块所需时间为0或未设置破坏时间），本事件触发在StartDestroyBlockServerEvent事件之前;当方块为非秒破方块时，本事件触发在StartDestroyBlockServerEvent事件之后。
可通过minecraft:destroy_time方块组件来修改方块的破坏时间
'''


ShearsDestoryBlockBeforeServerEvent = "ShearsDestoryBlockBeforeServerEvent"
'''
描述

触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在服务端线程触发该事件

参数

blockX	int	方块位置x
blockY	int	方块位置y
blockZ	int	方块位置z
blockName	str	方块的identifier，包含命名空间及名称
auxData	int	方块附加值
dropName	str	触发剪刀效果的掉落物identifier，包含命名空间及名称
dropCount	int	触发剪刀效果的掉落物数量
playerId	str	触发剪刀效果的玩家id
dimensionId	int	玩家触发时的维度id
cancelShears	bool	是否取消剪刀效果
返回值

无

备注

该事件触发在ServerPlayerTryDestroyBlockEvent之后，如果在ServerPlayerTryDestroyBlockEvent事件中设置了取消Destory或取消掉落物会导致该事件不触发
取消剪刀效果后不掉落任何东西的方块类型：蜘蛛网、枯萎的灌木、草丛、下界苗、树叶、海草、藤蔓
绊线取消剪刀效果需要配合ShearsDestoryBlockBeforeClientEvent同时使用，否则在表现上可能展现出来的还是剪刀剪断后的效果。绊线取消剪刀效果后依然会掉落成线。
'''


StartDestroyBlockServerEvent = "StartDestroyBlockServerEvent"
'''
描述

玩家开始挖方块时触发。创造模式下不触发。

参数

pos	tuple(float,float,float)	方块的坐标
blockName	str	方块的identifier，包含命名空间及名称
auxValue	int	方块的附加值
playerId	str	玩家id
dimensionId	int	维度id
cancel	bool	修改为True时，可阻止玩家进入挖方块的状态。需要与StartDestroyBlockClientEvent一起修改。
返回值

无

备注

如果是隔着火焰挖方块，即使将该事件cancel掉，火焰也会被扑灭。如果要阻止火焰扑灭，需要配合ExtinguishFireServerEvent使用
该服务端事件触发于服务端收到玩家破坏操作时，当方块为秒破方块时（破坏方块所需时间为0或未设置破坏时间），ServerPlayerTryDestroyBlockEvent事件触发在本事件之前;当方块为非秒破方块时，ServerPlayerTryDestroyBlockEvent事件触发在本事件之后。
秒破方块在本事件触发前已经被服务端删除，此时本事件获取到的blockName为minecraft:air，且无法通过本事件进行取消操作,以下是两个解决方法： （1）用ServerPlayerTryDestroyBlockEvent获取到正确的方块信息或取消操作。 （2）通过minecraft:destroy_time方块组件来修改方块的破坏时间。
'''


StepOffBlockServerEvent = "StepOffBlockServerEvent"
'''
描述

触发时机：实体移动离开一个实心方块时触发

参数

blockX	int	方块x坐标
blockY	int	方块y坐标
blockZ	int	方块z坐标
entityId	str	触发的entity的唯一ID
blockName	str	方块的identifier，包含命名空间及名称
dimensionId	int	维度id
返回值

无

备注

不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：自定义方块JSON组件）， 原版方块需要先通过RegisterOnStepOff接口注册才能触发
压力板与绊线钩这种非实心方块不会触发
'''


StepOnBlockServerEvent = "StepOnBlockServerEvent"
'''
描述

触发时机：实体刚移动至一个新实心方块时触发。

参数

cancel	bool	是否允许触发，默认为False，若设为True，可阻止触发后续物理交互事件
blockX	int	方块x坐标
blockY	int	方块y坐标
blockZ	int	方块z坐标
entityId	str	触发的entity的唯一ID
blockName	str	方块的identifier，包含命名空间及名称
dimensionId	int	维度id
返回值

无

备注

在合并微软更新之后，本事件触发时机与微软molang实验性玩法组件"minecraft:on_step_on"一致
压力板与绊线钩在过去的版本的事件是可以触发的，但在更新后这种非实心方块并不会触发，有需要的可以使用OnEntityInsideBlockServerEvent事件。
不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：自定义方块JSON组件）， 原版方块需要先通过RegisterOnStepOn接口注册才能触发。原版的红石矿默认注册了，但深层红石矿没有默认注册。
如果需要修改cancel，强烈建议配合客户端事件同步修改，避免出现客户端表现不一致等非预期现象。
'''