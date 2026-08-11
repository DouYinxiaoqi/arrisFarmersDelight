# 棱花 Arris 农夫乐事联动接口文档

作者：Lovely\_小柒丫

## 功能描述

本接口主要用于副包或其他模组与农夫乐事主包之间的联动，支持：

- 修改或添加新的厨锅配方
- 添加新的砧板配方
- 添加新的煎锅、炉灶烹饪食材

## 使用前的准备

调用接口前，请监听 `LoadServerAddonScriptsAfter` 事件。假设事件回调函数为
`FarmersDelight`，可以使用 ModAPI 的 `GetAttr` 接口获取主包预留的接口：

```python
def FarmersDelight(self, args):
	factory = serverApi.GetEngineCompFactory()
	mod_attr = factory.CreateModAttr("arris")
	interface = mod_attr.GetAttr("ArrisFarmersDelightInterface")
	obtain = mod_attr.GetAttr("ArrisFarmersDelightObtain")
	addRecipe = mod_attr.GetAttr("ArrisAddCookingPotRecipe")
	# 建议后续使用 if 判断是否获取成功
```

## 联动接口

### 添加小刀

将自定义物品配置为小刀，
在自定义物品的components中添加`arris:knife`标签

示例：
```
"minecraft:tags": {
    "tags": ["arris:knife"]
}
```

### ArrisFarmersDelightInterface

向农夫乐事主包配置文件 `modConfig.py` 中的字典或列表添加元素。

| 参数名    | 数据类型                | 说明                             |
| --------- | ----------------------- | -------------------------------- |
| `target`  | `str`                   | 需要调用的变量名称               |
| `element` | `str`、`list` 或 `dict` | 要添加的元素，类型取决于目标对象 |

示例：

```python
testRecipe = {
	"Recipe": [
		[
			("minecraft:stick", 0),
			("minecraft:stick", 0)
		],
		[
			("minecraft:stone", 0),
			("minecraft:stone", 0),
			("minecraft:stone", 0)
		]
	],
	"CookResult": ("minecraft:diamond", 0),
	"Vessel": ("minecraft:bowl", 0),
	"PushItem": [
		("minecraft:apple", 0)
	],
	"text": "钻石"
}

# testRecipe 作为示例配方。
# 物品 ID 后面的 0 代表 AuxValue。
# 此处添加两种钻石配方：2 个木棍或 3 个石头合成 1 个钻石。
# 配方请勿超过 6 个物品。
# Vessel 表示容器为碗，PushItem 表示烹饪完成后吐出一个苹果。

def FarmersDelight(self, args):
	factory = serverApi.GetEngineCompFactory()
	mod_attr = factory.CreateModAttr("arris")
	interface = mod_attr.GetAttr("ArrisFarmersDelightInterface")
	if interface:
		interface("CookingPotRecipeList", testRecipe)
		# 添加自定义厨锅配方
```

备注：

- 本示例仅演示添加厨锅烹饪配方。
- 还可以向其他变量添加元素，详细格式请查看 `modConfig.py`。

### ArrisFarmersDelightObtain

获取 `modConfig.py` 中的配置字典或列表。

| 参数名   | 数据类型 | 说明               |
| -------- | -------- | ------------------ |
| `target` | `str`    | 需要获取的变量名称 |

示例：

```python
def FarmersDelight(self, args):
	factory = serverApi.GetEngineCompFactory()
	mod_attr = factory.CreateModAttr("arris")
	obtain = mod_attr.GetAttr("ArrisFarmersDelightObtain")
	if obtain:
		canProvideHeatBlockList = obtain("CanProvideHeatBlockList")
		# 获取可以提供火源的方块列表
```

### AddCookingPotRecipe

在已有厨锅配方的基础上添加新配方。获取该接口时使用的属性名为
`ArrisAddCookingPotRecipe`。

| 参数名   | 数据类型 | 说明              |
| -------- | -------- | ----------------- |
| `name`   | `str`    | 对应烹饪食品的 ID |
| `recipe` | `list`   | 需要添加的配方    |

示例：

```python
testRecipe = [
	("minecraft:apple", 0),
	("minecraft:apple", 0),
	("minecraft:apple", 0),
	("minecraft:stick", 0),
	("minecraft:stick", 0)
]

# testRecipe 作为示例配方。
# 物品 ID 后面的 0 代表 AuxValue。
# 此处为蘑菇煲额外添加一种配方：
# 使用 3 个苹果和 2 个木棍合成 1 个蘑菇煲。
# 配方请勿超过 6 个物品。

def FarmersDelight(self, args):
	factory = serverApi.GetEngineCompFactory()
	mod_attr = factory.CreateModAttr("arris")
	addRecipe = mod_attr.GetAttr("ArrisAddCookingPotRecipe")
	if addRecipe:
		addRecipe("minecraft:mushroom_stew", testRecipe)
		# 在原有蘑菇煲配方上新增配方
```

## 联动配置

以下变量支持通过 `ArrisFarmersDelightInterface` 添加内容，或通过
`ArrisFarmersDelightObtain` 获取内容：

| 参数名                    | 数据类型 | 说明                                   |
| ------------------------- | -------- | -------------------------------------- |
| `CanCookedFoodDict`       | `dict`   | 可烹饪的物品 ID 及输出物品 ID          |
| `CanProvideHeatBlockList` | `list`   | 可以提供火源的方块列表                 |
| `CuttingBoardDict`        | `dict`   | 可在砧板上切的物品、输出物品及工具列表 |
| `ComposterItemDict`       | `dict`   | 可堆肥的物品和堆肥成功概率             |
| `CookingPotRecipeList`    | `list`   | 厨锅配方                               |

各配置项的详细格式请查看 `modConfig.py`。
