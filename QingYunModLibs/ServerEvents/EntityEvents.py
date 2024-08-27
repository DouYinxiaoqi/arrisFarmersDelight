# coding=utf-8
ActorHurtServerEvent = "ActorHurtServerEvent"
'''
描述

触发时机：生物（包括玩家）受伤时触发

参数

entityId	str	生物Id
cause	str	伤害来源，详见Minecraft枚举值文档的ActorDamageCause
damage	int	伤害值（被伤害吸收后的值），不可修改
damage_f	float	伤害值（被伤害吸收后的值），不可修改
absorbedDamage	int	被伤害吸收效果吸收的伤害值
返回值

无
'''


ActuallyHurtServerEvent = "ActuallyHurtServerEvent"
'''
描述

实体实际受到伤害时触发，相比于DamageEvent，该伤害为经过护甲及buff计算后，实际的扣血量

参数

srcId	str	伤害源id
projectileId	str	投射物id
entityId	str	被伤害id
damage	int	伤害值（被伤害吸收后的值），允许修改，设置为0则此次造成的伤害为0，若设置数值和原来一样则视为没有修改
damage_f	float	伤害值（被伤害吸收后的值），允许修改，若修改该值，则会覆盖damage的修改效果
cause	str	伤害来源，详见Minecraft枚举值文档的ActorDamageCause
返回值

无

备注

药水与状态效果造成的伤害不触发，可以使用ActorHurtServerEvent
为了游戏运行效率请尽可能避免将火的伤害设置为0，因为这样会导致大量触发该事件。
若要修改damage或damage_f的值，请确保修改后的值与原值不同，且需要使用原来的数据类型(int/float)，否则引擎会忽略这次修改。
'''


AddEffectServerEvent = "AddEffectServerEvent"
'''
描述

触发时机：实体获得状态效果时

参数

entityId	str	实体id
effectName	str	实体获得状态效果的名字
effectDuration	int	状态效果的持续时间，单位秒
effectAmplifier	int	状态效果的放大倍数
damage	int	状态造成的伤害值（真实扣除生命值的量）。只有持续时间为0时有用
返回值

无
'''


ChangeSwimStateServerEvent = "ChangeSwimStateServerEvent"
'''
描述

触发时机：实体开始或者结束游泳时

参数

entityId	str	实体的唯一ID
formState	bool	事件触发前，实体是否在游泳状态
toState	bool	事件触发后，实体是否在游泳状态
返回值

无

备注

当实体的状态没有变化时，不会触发此事件，即formState和toState必定一真一假
'''


DamageEvent = "DamageEvent"
'''
描述

实体受到伤害时触发

参数

srcId	str	伤害源id
projectileId	str	投射物id
entityId	str	被伤害id
damage	int	伤害值（被伤害吸收前的值），允许修改，设置为0则此次造成的伤害为0
damage_f	float	伤害值（被伤害吸收前的值），不允许修改
absorption	int	受到伤害时，扣除黄心前，实体拥有的黄心血量（见AttrType枚举的ABSORPTION）
cause	str	伤害来源，详见Minecraft枚举值文档的ActorDamageCause
knock	bool	是否击退被攻击者，允许修改，设置该值为False则不产生击退
ignite	bool	是否点燃被伤害者，允许修改，设置该值为True产生点燃效果，反之亦然
返回值

无

备注

damage值会被护甲和absorption等吸收，不一定是最终扣血量。通过设置这个伤害值可以取消伤害，但不会取消由击退效果或者点燃效果带来的伤害
该事件在实体受伤之前触发，由于部分伤害是在tick中处理，因此持续触发受伤时（如站在火中）会每帧触发事件（可以使用ActorHurtServerEvent来避免）。
这里的damage是伤害源具有的攻击伤害值，并非实体真实的扣血量，如果需要获取真实伤害，可以使用ActuallyHurtServerEvent事件。
当目标无法被击退时，knock值无效
药水与状态效果造成的伤害不触发，可以使用ActorHurtServerEvent
'''


EntityChangeDimensionServerEvent = "EntityChangeDimensionServerEvent"
'''
描述

实体维度改变时服务端抛出

参数

entityId	str	实体id
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

实体转移维度时，如果对应维度的对应位置的区块尚未加载，实体会缓存在维度自身的缓冲区中，直到对应区块被加载时才会创建对应的实体，此事件的抛出只代表实体从原维度消失，不代表必定会在对应维度出现
注意，玩家维度改变时不触发该事件，而是会触发DimensionChangeServerEvent事件
'''


EntityDefinitionsEventServerEvent = "EntityDefinitionsEventServerEvent"
'''
描述

触发时机：生物定义json文件中设置的event触发时同时触发。生物行为变更事件

参数

entityId	str	生物id
eventName	str	触发的事件名称
返回值

无
'''


EntityDieLoottableServerEvent = "EntityDieLoottableServerEvent"
'''
描述

触发时机：生物死亡掉落物品时

参数

dieEntityId	str	死亡实体的entityId
attacker	str	伤害来源的entityId
itemList	list(dict)	掉落物品列表，每个元素为一个itemDict，格式可参考物品信息字典
dirty	bool	默认为False，如果需要修改掉落列表需将该值设为True
返回值

无

备注

只有当dirty为True时才会重新读取item列表并生成对应的掉落物，如果不需要修改掉落结果的话请勿随意修改dirty值
'''


EntityDroppedItemServerEvent = "EntityDroppedItemServerEvent"
'''
描述

触发时机：生物扔出物品时触发

参数

entityId	str	生物Id
itemDict	dict	扔出的物品的物品信息字典
itemEntityId	str	物品实体Id
返回值

无
'''


EntityEffectDamageServerEvent = "EntityEffectDamageServerEvent"
'''
描述

生物受到状态伤害/回复事件。

参数

entityId	str	实体id
damage	int	伤害值（伤害吸收后实际扣血量），负数表示生命回复量
attributeBuffType	int	状态类型，参考AttributeBuffType
duration	float	状态持续时间，单位秒（s）
lifeTimer	float	状态生命时间，单位秒（s）
isInstantaneous	bool	是否为立即生效状态
返回值

无
'''


EntityLoadScriptEvent = "EntityLoadScriptEvent"
'''
描述

数据库加载实体自定义数据时触发

参数

args	list	该事件的参数为长度为2的list，而非dict，其中list的第一个元素为实体id
返回值

无

备注

只有使用过extraData组件的SetExtraData接口的实体才有此事件，触发时可以通过extraData组件的GetExtraData或GetWholeExtraData接口获取该实体的自定义数据
'''


EntityMotionStartServerEvent = "EntityMotionStartServerEvent"
'''
描述

实体运动器开始事件。实体（包含玩家）添加运动器后，运动器开始运行时触发

参数

motionId	int	运动器id
entityId	str	实体id
返回值

无
'''


EntityMotionStopServerEvent = "EntityMotionStopServerEvent"
'''
描述

实体运动器停止事件。实体（包含玩家）添加运动器并开始运行后，运动器自动停止时触发

参数

motionId	int	运动器id
entityId	str	实体id
remove	bool	是否移除该运动器，设置为False则保留，默认为True，即运动器停止后自动移除，该参数设置只对非玩家实体有效
返回值

无

备注

注意：该事件触发表示运动器播放顺利完成，手动调用的StopEntityMotion、RemoveEntityMotion以及实体被销毁导致的运动器停止不会触发该事件。
'''


EntityPickupItemServerEvent = "EntityPickupItemServerEvent"
'''
描述

有minecraft:behavior.pickup_items行为的生物拾取物品时触发该事件，例如村民拾取面包、猪灵拾取金锭

参数

entityId	str	生物Id
itemDict	dict	拾取的物品的物品信息字典
secondaryActor	str	物品给予者id（一般是玩家），如果不存在给予者的话，这里为空字符串
返回值

无
'''


EntityStartRidingEvent = "EntityStartRidingEvent"
'''
描述

当实体骑乘上另一个实体时触发

参数

id	str	乘骑者实体id
rideId	str	被乘骑者实体id
返回值

无
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
cancel	bool	设置为True可以取消（需要与客户端事件一同取消）
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
'''


EntityTickServerEvent = "EntityTickServerEvent"
'''
描述

实体tick时触发。该事件为20帧每秒。需要使用AddEntityTickEventWhiteList添加触发该事件的实体类型白名单。

参数

entityId	str	实体id
identifier	str	实体identifier
返回值

无
'''


HealthChangeBeforeServerEvent = "HealthChangeBeforeServerEvent"
'''
描述

生物生命值发生变化之前触发

参数

entityId	str	实体id
from	float	变化前的生命值
to	float	将要变化到的生命值，cancel设置为True时可以取消该变化，但是此参数不变
byScript	bool	是否通过SetAttrValue或SetAttrMaxValue调用产生的变化
cancel	bool	是否取消该变化
返回值

无
'''


HealthChangeServerEvent = "HealthChangeServerEvent"
'''
描述

生物生命值发生变化时触发

参数

entityId	str	实体id
from	float	变化前的生命值
to	float	变化后的生命值
byScript	bool	是否通过SetAttrValue或SetAttrMaxValue调用产生的变化
返回值

无
'''


MobDieEvent = "MobDieEvent"
'''
描述

实体被玩家杀死时触发

参数

id	str	实体id
attacker	str	伤害来源id
返回值

无

备注

注意：不能在该事件回调中对此玩家手持物品进行修改，如SpawnItemToPlayerCarried、ChangePlayerItemTipsAndExtraId等接口
'''


MobGriefingBlockServerEvent = "MobGriefingBlockServerEvent"
'''
描述

环境生物改变方块时触发，触发的时机与mobgriefing游戏规则影响的行为相同

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

触发的时机包括：生物踩踏耕地、破坏单个方块、破门、火矢点燃方块、凋灵boss破坏方块、末影龙破坏方块、末影人捡起方块、蠹虫破坏被虫蚀的方块、蠹虫把方块变成被虫蚀的方块、凋零杀死生物生成凋零玫瑰、生物踩坏海龟蛋。
'''


OnFireHurtEvent = "OnFireHurtEvent"
'''
描述

生物受到火焰伤害时触发

参数

victim	str	受伤实体id
src	str	火焰创建者id
fireTime	float	着火时间，单位秒
cancel	bool	是否取消此处火焰伤害
返回值

无


'''


OnGroundServerEvent = "OnGroundServerEvent"
'''
描述

实体着地事件。实体，掉落的物品，点燃的TNT掉落地面时触发

参数

id	str	实体id
返回值

无
'''


OnKnockBackServerEvent = "OnKnockBackServerEvent"
'''
描述

实体被击退时触发

参数

id	str	实体id
返回值

无
'''


OnMobHitBlockServerEvent = "OnMobHitBlockServerEvent"
'''
描述

触发时机：通过OpenMobHitBlockDetection打开方块碰撞检测后，当生物（不包括玩家）碰撞到方块时触发该事件。

参数

entityId	str	碰撞到方块的生物Id
posX	int	碰撞方块x坐标
posY	int	碰撞方块y坐标
posZ	int	碰撞方块z坐标
blockId	str	碰撞方块的identifier
auxValue	int	碰撞方块的附加值
dimensionId	int	维度id
返回值

无
'''


OnMobHitMobServerEvent = "OnMobHitMobServerEvent"
'''
描述

触发时机：通过OpenPlayerHitMobDetection打开生物碰撞检测后，当生物间（包含玩家）碰撞时触发该事件。注：客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。

参数

mobId	str	当前生物的id
hittedMobList	list[str]	当前生物碰撞到的其他所有生物id的list
返回值

无

备注

本事件代替原有的OnPlayerHitMobServerEvent事件
'''


ProjectileCritHitEvent = "ProjectileCritHitEvent"
'''
描述

触发时机：当抛射物与头部碰撞时触发该事件。注：需调用OpenPlayerCritBox开启玩家爆头后才能触发。

参数

id	str	抛射物id
targetId	str	碰撞目标id
返回值

无
'''


ProjectileDoHitEffectEvent = "ProjectileDoHitEffectEvent"
'''
描述

触发时机：当抛射物碰撞时触发该事件

参数

id	str	抛射物id
hitTargetType	str	碰撞目标类型,'ENTITY'或是'BLOCK'
targetId	str	碰撞目标id
hitFace	int	撞击在方块上的面id，参考Facing枚举
x	float	碰撞x坐标
y	float	碰撞y坐标
z	float	碰撞z坐标
blockPosX	int	碰撞是方块时，方块x坐标
blockPosY	int	碰撞是方块时，方块y坐标
blockPosZ	int	碰撞是方块时，方块z坐标
srcId	str	创建者id
cancel	bool	是否取消这个碰撞事件，若取消可以设置为True
返回值

无
'''


RefreshEffectServerEvent = "RefreshEffectServerEvent"
'''
描述

触发时机：实体身上状态效果更新时触发，更新条件1、新增状态等级较高，更新状态等级及时间；2、新增状态等级不变，时间较长，更新状态持续时间

参数

entityId	str	实体id
effectName	str	更新状态效果的名字
effectDuration	int	更新后状态效果剩余持续时间，单位秒
effectAmplifier	int	更新后的状态效果放大倍数
damage	int	状态造成的伤害值，如药水
返回值

无
'''


RemoveEffectServerEvent = "RemoveEffectServerEvent"
'''
描述

触发时机：实体身上状态效果被移除时

参数

entityId	str	实体id
effectName	str	被移除状态效果的名字
effectDuration	int	被移除状态效果的剩余持续时间，单位秒
effectAmplifier	int	被移除状态效果的放大倍数
返回值

无
'''


SpawnProjectileServerEvent = "SpawnProjectileServerEvent"
'''
描述

触发时机：抛射物生成时触发

参数

projectileId	str	抛射物的实体id
projectileIdentifier	str	抛射物的identifier
spawnerId	str	发射者的实体id，没有发射者时为-1
返回值

无

备注

该事件里无法获取弹射物实体的auxvalue。如有需要可以延迟一帧获取，或者在ProjectileDoHitEffectEvent获取
'''


StartRidingServerEvent = "StartRidingServerEvent"
'''
描述

触发时机：一个实体即将骑乘另外一个实体

参数

cancel	bool	是否允许触发，默认为False，若设为True，可阻止触发后续的实体交互事件
actorId	str	骑乘者的唯一ID
victimId	str	被骑乘实体的唯一ID
返回值

无
'''


WillAddEffectServerEvent = "WillAddEffectServerEvent"
'''
描述

触发时机：实体即将获得状态效果前

参数

entityId	str	实体id
effectName	str	实体获得状态效果的名字
effectDuration	int	状态效果的持续时间，单位秒
effectAmplifier	int	状态效果的放大倍数
cancel	bool	设置为True可以取消
damage	int	状态将会造成的伤害值，如药水；需要注意，该值不一定是最终的伤害值，例如被伤害吸收效果扣除。只有持续时间为0时有用
返回值

无
'''


WillTeleportToServerEvent = "WillTeleportToServerEvent"
'''
描述

实体即将传送或切换维度

参数

cancel	bool	是否允许触发，默认为False，若设为True，可阻止触发后续的传送
entityId	str	实体的唯一ID
fromDimensionId	int	传送前所在的维度
toDimensionId	int	传送后的目标维度
fromX	int	传送前所在的x坐标
fromY	int	传送前所在的y坐标
fromZ	int	传送前所在的z坐标
toX	int	传送目标地点的x坐标
toY	int	传送目标地点的y坐标
toZ	int	传送目标地点的z坐标
cause	str	传送理由，详情见MinecraftEnum.EntityTeleportCause
返回值

无

备注

假如目标维度尚未在内存中创建（即服务器启动之后，到传送之前，没有玩家进入过这个维度），那么此时事件中返回的目标地点坐标是算法生成的，不能保证正确。
'''