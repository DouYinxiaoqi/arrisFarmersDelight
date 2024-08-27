# coding=utf-8
ClientBlockUseEvent = "ClientBlockUseEvent"
'''
描述

触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时客户端抛出该事件（该事件tick执行，需要注意效率问题）。

参数

playerId	str	玩家Id
blockName	str	方块的identifier，包含命名空间及名称
aux	int	方块附加值
cancel	bool	设置为True可拦截与方块交互的逻辑。
x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
返回值

无

备注

有的方块是在ServerBlockUseEvent中设置cancel生效，但是有部分方块是在ClientBlockUseEvent中设置cancel才生效，如有需求建议在两个事件中同时设置cancel以保证生效。
'''


FallingBlockCauseDamageBeforeClientEvent = "FallingBlockCauseDamageBeforeClientEvent"
'''
描述

触发时机：当下落的方块开始计算砸到实体的伤害时，客户端触发该事件

参数

fallingBlockId	int	下落的方块实体id
fallingBlockX	float	下落的方块实体位置x
fallingBlockY	float	下落的方块实体位置y
fallingBlockZ	float	下落的方块实体位置z
blockName	str	重力方块的identifier，包含命名空间及名称
dimensionId	int	下落的方块实体维度id
collidingEntitys	list(str)	当前碰撞到的实体列表id（客户端只能获取到玩家），如果没有的话是None
fallTickAmount	int	下落的方块实体持续下落了多少tick
fallDistance	float	下落的方块实体持续下落了多少距离
isHarmful	bool	客户端始终为false，因为客户端不会计算伤害值
fallDamage	int	对实体的伤害
返回值

无

备注

不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义重力方块）
当该事件的参数数据（fallTickAmount，fallDistance，collidingEntitys，fallDamage）与服务端事件FallingBlockCauseDamageBeforeServerEvent数据有差异时，请以服务端事件数据为准。
'''


OnAfterFallOnBlockClientEvent = "OnAfterFallOnBlockClientEvent"
'''
描述

触发时机：当实体降落到方块后客户端触发，主要用于力的计算

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
如果需要修改实体的力，最好配合服务端事件同步修改，避免产生非预期现象
因为引擎最后一定会按照原版方块规则计算力（普通方块置0，床、粘液块等反弹），所以脚本层如果想直接修改当前力需要将calculate设为true取消原版计算，按照传回值计算
引擎在落地之后OnAfterFallOnBlockClientEvent会一直触发，因此请在脚本层中做对应的逻辑判断
'''


OnEntityInsideBlockClientEvent = "OnEntityInsideBlockClientEvent"
'''
描述

触发时机：当实体碰撞盒所在区域有方块时，客户端持续触发

参数

entityId	str	实体id
dimensionId	int	实体所在维度id
slowdownMultiX	float	实体移速X方向的减速比例
slowdownMultiY	float	实体移速Y方向的减速比例
slowdownMultiZ	float	实体移速Z方向的减速比例
blockX	int	方块位置x
blockY	int	方块位置y
blockZ	int	方块位置z
blockName	str	方块的identifier，包含命名空间及名称
cancel	bool	可由脚本层回传True给引擎，阻止触发后续原版逻辑
返回值

无

备注

不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：自定义方块JSON组件） ，原版方块需要先通过RegisterOnEntityInside接口注册才能触发
如果需要修改slowdownMulti/cancel，强烈建议与服务端事件同步修改，避免出现被服务端矫正等非预期现象。
如果要在脚本层修改slowdownMulti，回传的一定要是浮点型，例如需要赋值1.0而不是1
有任意slowdownMulti参数被传回非0值时生效减速比例
slowdownMulti参数更像是一个Buff，例如并不是立刻计算，而是先保存在实体属性里延后计算、在已经有slowdownMulti属性的情况下会取最低的值、免疫掉落伤害等，与原版蜘蛛网逻辑基本一致。
'''


OnModBlockNeteaseEffectCreatedClientEvent = "OnModBlockNeteaseEffectCreatedClientEvent"
'''
描述

自定义方块实体绑定的特效创建成功事件，在自定义方块实体中绑定的特效创建成功时触发以及使用接口CreateFrameEffectForBlockEntity或CreateParticleEffectForBlockEntity为自定义方块实体添加特效成功时触发。

参数

effectName	str	创建成功的特效的自定义键值名称
id	int	该特效的id
effectType	int	该特效的类型，0为粒子特效，1为序列帧特效
blockPos	tuple(float,float,float)	该特效绑定的自定义方块实体的世界坐标
返回值

无
'''


OnStandOnBlockClientEvent = "OnStandOnBlockClientEvent"
'''
描述

触发时机：当实体站立到方块上时客户端持续触发

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
如果要在脚本层修改motion/cancel，强烈建议配合OnStandOnBlockServerEvent服务端事件同步修改，避免出现被服务端矫正等非预期现象
如果要在脚本层修改motion，回传的一定要是浮点型，例如需要赋值0.0而不是0
'''


PlayerTryDestroyBlockClientEvent = "PlayerTryDestroyBlockClientEvent"
'''
描述

当玩家即将破坏方块时，客户端线程触发该事件。主要用于床，旗帜，箱子这些根据方块实体数据进行渲染的方块，一般情况下请使用ServerPlayerTryDestroyBlockEvent

参数

x	int	方块x坐标
y	int	方块y坐标
z	int	方块z坐标
face	int	方块被敲击的面向id，参考Facing枚举
blockName	str	方块的identifier，包含命名空间及名称
auxData	int	方块附加值
playerId	str	试图破坏方块的玩家ID
cancel	bool	默认为False，在脚本层设置为True就能取消该方块的破坏
返回值

无
'''


ShearsDestoryBlockBeforeClientEvent = "ShearsDestoryBlockBeforeClientEvent"
'''
描述

触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在客户端线程触发该事件

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

目前仅绊线会触发，需要取消剪刀效果得配合ShearsDestoryBlockBeforeServerEvent同时使用
'''


StartDestroyBlockClientEvent = "StartDestroyBlockClientEvent"
'''
描述

玩家开始挖方块时触发。创造模式下不触发。

参数

pos	tuple(float,float,float)	方块的坐标
blockName	str	方块的identifier，包含命名空间及名称
auxValue	int	方块的附加值
playerId	str	玩家id
cancel	bool	修改为True时，可阻止玩家进入挖方块的状态。需要与StartDestroyBlockServerEvent一起修改。
返回值

无

备注

如果是隔着火焰挖方块，即使将该事件cancel掉，火焰也会被扑灭。如果要阻止火焰扑灭，需要配合ExtinguishFireClientEvent使用
'''


StepOffBlockClientEvent = "StepOffBlockClientEvent"
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


StepOnBlockClientEvent = "StepOnBlockClientEvent"
'''
描述

触发时机：实体刚移动至一个新实心方块时触发。

参数

cancel	bool	是否允许触发，默认为False，若设为True，可阻止触发后续原版逻辑
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
压力板与绊线钩在过去的版本的事件是可以触发的，但在更新后这种非实心方块并不会触发，有需要的可以使用OnEntityInsideBlockClientEvent事件。
不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：自定义方块JSON组件）， 原版方块需要先通过RegisterOnStepOn接口注册才能触发。原版的红石矿默认注册了，但深层红石矿没有默认注册。
如果需要修改cancel，强烈建议配合服务端事件同步修改，避免出现被服务端矫正等非预期现象。
'''