# -*- coding: utf-8 -*-
uiGuideBookPath = "arrisFarmersDelightScripts.modClient.uiScript.uiGuideBook.guideBook"
uiGuideBookScreen = "guideBook.main"

# 可以烹饪的食物及输出结果字典
CanCookedFoodDict = {
    "minecraft:beef": "minecraft:cooked_beef",
    "minecraft:chicken": "minecraft:cooked_chicken",
    "minecraft:cod": "minecraft:cooked_cod",
    "minecraft:mutton": "minecraft:cooked_mutton",
    "minecraft:porkchop": "minecraft:cooked_porkchop",
    "minecraft:potato": "minecraft:baked_potato",
    "minecraft:rabbit": "minecraft:cooked_rabbit",
    "minecraft:salmon": "minecraft:cooked_salmon",
    "minecraft:egg": "arris:fried_egg",
    "arris:cod_slice": "arris:cooked_cod_slice",
    "arris:salmon_slice": "arris:cooked_salmon_slice",
    "arris:chicken_cuts": "arris:cooked_chicken_cuts",
    "arris:minced_beef": "arris:beef_patty",
    "arris:bacon": "arris:cooked_bacon",
    "arris:mutton_chops": "arris:cooked_mutton_chops"
}
# 可以提供火源的方块列表
CanProvideHeatBlockList = [
    "minecraft:fire",
    "minecraft:soul_fire",
    "minecraft:campfire",
    "minecraft:soul_campfire",
    "minecraft:lava",
    "minecraft:flowing_lava",
    "minecraft:magma",
    "arris:stove"
]
# 刀列表
knifeList = [
    "arris:flint_knife",
    "arris:golden_knife",
    "arris:iron_knife",
    "arris:diamond_knife",
    "arris:netherite_knife",
    "ends_delight:end_stone_knife",
    "ends_delight:purpur_knife",
    "ends_delight:dragon_egg_shell_knife",
    "ends_delight:dragon_tooth_knife"
]
# 斧头列表
axeList = [
    "minecraft:wooden_axe",
    "minecraft:stone_axe",
    "minecraft:copper_axe",
    "minecraft:iron_axe",
    "minecraft:golden_axe",
    "minecraft:diamond_axe",
    "minecraft:netherite_axe"
]
# 可以在砧板上切的食物及输出字典和使用工具
CuttingBoardDict = {
    ("minecraft:beef", 0): {"itemList": [{"itemName": "arris:minced_beef", "count": 2}], "tool": knifeList},
    ("minecraft:cooked_beef", 0): {"itemList": [{"itemName": "arris:beef_patty", "count": 2}], "tool": knifeList},
    ("minecraft:chicken", 0): {"itemList": [{"itemName": "arris:chicken_cuts", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:cooked_chicken", 0): {"itemList": [{"itemName": "arris:cooked_chicken_cuts", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:porkchop", 0): {"itemList": [{"itemName": "arris:bacon", "count": 2}], "tool": knifeList},
    ("minecraft:cooked_porkchop", 0): {"itemList": [{"itemName": "arris:cooked_bacon", "count": 2}], "tool": knifeList},
    ("minecraft:mutton", 0): {"itemList": [{"itemName": "arris:mutton_chops", "count": 2}], "tool": knifeList},
    ("minecraft:muttonraw", 0): {"itemList": [{"itemName": "arris:mutton_chops", "count": 2}], "tool": knifeList},
    ("minecraft:cooked_mutton", 0): {"itemList": [{"itemName": "arris:cooked_mutton_chops", "count": 2}], "tool": knifeList},
    ("minecraft:cod", 0): {"itemList": [{"itemName": "arris:cod_slice", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:cooked_cod", 0): {"itemList": [{"itemName": "arris:cooked_cod_slice", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:salmon", 0): {"itemList": [{"itemName": "arris:salmon_slice", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:cooked_salmon", 0): {"itemList": [{"itemName": "arris:cooked_salmon_slice", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:pumpkin", 0): {"itemList": [{"itemName": "arris:pumpkin_slice", "count": 4}], "tool": knifeList},
    ("minecraft:cake", 0): {"itemList": [{"itemName": "arris:cake_slice", "count": 7}], "tool": knifeList},
    ("arris:ham", 0): {"itemList": [{"itemName": "minecraft:porkchop", "count": 2}, {"itemName": "minecraft:bone", "count": 1}], "tool": knifeList},
    ("arris:smoked_ham", 0): {"itemList": [{"itemName": "minecraft:cooked_porkchop", "count": 2}, {"itemName": "minecraft:bone", "count": 1}], "tool": knifeList},
    ("arris:cabbage", 0): {"itemList": [{"itemName": "arris:cabbage_leaf", "count": 2}], "tool": knifeList},
    ("arris:wheat_dough", 0): {"itemList": [{"itemName": "arris:raw_pasta", "count": 1}], "tool": knifeList},
    ("arris:apple_pie_item", 0): {"itemList": [{"itemName": "arris:apple_pie_slice", "count": 4}], "tool": knifeList},
    ("arris:chocolate_pie_item", 0): {"itemList": [{"itemName": "arris:chocolate_pie_slice", "count": 4}], "tool": knifeList},
    ("arris:kelp_roll", 0): {"itemList": [{"itemName": "arris:kelp_roll_slice", "count": 3}], "tool": knifeList},
    ("arris:sweet_berry_cheesecake_item", 0): {"itemList": [{"itemName": "arris:sweet_berry_cheesecake_slice", "count": 4}], "tool": knifeList},
    ("arris:rice_panicle", 0): {"itemList": [{"itemName": "arris:rice", "count": 1}, {"itemName": "arris:straw", "count": 1}], "tool": knifeList},
    ("minecraft:oak_log", 0): {"itemList": [{"itemName": "minecraft:stripped_oak_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:spruce_log", 0): {"itemList": [{"itemName": "minecraft:stripped_spruce_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:acacia_log", 0): {"itemList": [{"itemName": "minecraft:stripped_acacia_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:birch_log", 0): {"itemList": [{"itemName": "minecraft:stripped_birch_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:cherry_log", 0): {"itemList": [{"itemName": "minecraft:stripped_cherry_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:dark_oak_log", 0): {"itemList": [{"itemName": "minecraft:stripped_dark_oak_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:jungle_log", 0): {"itemList": [{"itemName": "minecraft:stripped_jungle_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:mangrove_log", 0): {"itemList": [{"itemName": "minecraft:stripped_mangrove_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:crimson_stem", 0): {"itemList": [{"itemName": "minecraft:stripped_crimson_stem", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:crimson_hyphae", 0): {"itemList": [{"itemName": "minecraft:stripped_crimson_hyphae", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:warped_stem", 0): {"itemList": [{"itemName": "minecraft:stripped_warped_stem", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"},
    ("minecraft:warped_hyphae", 0): {"itemList": [{"itemName": "minecraft:stripped_warped_hyphae", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList, "item_type": "axe"}
}
# 可堆肥的物品
ComposterItemDict = {
    ("arris:cabbage_seeds", 0): 50,
    ("arris:tomato_seeds", 0): 50,
    ("arris:rotten_tomato", 0): 40,
    ("arris:cabbage_leaf", 0): 50,
    ("arris:rice", 0): 50,
    ("arris:tree_bark", 0): 50,
    ("arris:straw", 0): 50,
    ("arris:cabbage", 0): 70,
    ("arris:rice_panicle", 0): 60,
    ("arris:tomato", 0): 70,
    ("arris:onion", 0): 70
}
# 炉灶列表
StoveList = [
    "arris:stove"
]
# 物品转变为方块字典
itemChangeBlockDict = {
    "arris:skillet_item": "arris:skillet",
    "arris:apple_pie_item": "arris:apple_pie",
    "arris:sweet_berry_cheesecake_item": "arris:sweet_berry_cheesecake",
    "arris:chocolate_pie_item": "arris:chocolate_pie",
}
# "合成后还给玩家的空容器"映射：获得 key 物品时 → 返还 value 空容器
# 服务端 PlayerShapedRecipe 的白名单：客户端不能再指定任意 itemDict
shapedRecipeContainerDict = {
    "arris:wheat_dough": {"itemName": "minecraft:bucket", "count": 1, "auxValue": 0},
    "arris:milk_bottle": {"itemName": "minecraft:bucket", "count": 1, "auxValue": 0},
    "arris:honey_cookie": {"itemName": "minecraft:glass_bottle", "count": 1, "auxValue": 0},
    "arris:stuffed_potato": {"itemName": "minecraft:glass_bottle", "count": 1, "auxValue": 0},
    "arris:salmon_roll": {"itemName": "minecraft:bowl", "count": 1, "auxValue": 0},
    "arris:cod_roll": {"itemName": "minecraft:bowl", "count": 1, "auxValue": 0},
}
# 派列表
pieList = [
    "arris:apple_pie",
    "arris:sweet_berry_cheesecake",
    "arris:chocolate_pie"
]
# 可攀爬的方块列表
canClimbList = [
    "arris:rope",
    "arris:tomatoes_vine_stage0",
    "arris:tomatoes_vine_stage1",
    "arris:tomatoes_vine_stage2",
    "arris:tomatoes_vine_stage3"
]
# 橱柜列表
cabinetList = [
    "arris:oak_cabinet",
    "arris:spruce_cabinet",
    "arris:birch_cabinet",
    "arris:jungle_cabinet",
    "arris:acacia_cabinet",
    "arris:dark_oak_cabinet",
    "arris:mangrove_cabinet",
    "arris:cherry_cabinet",
    "arris:bamboo_cabinet",
    "arris:crimson_cabinet",
    "arris:warped_cabinet"
]
# 野生作物方块且允许种植在其方块上的列表字典
WildCropDict = {
    "arris:sandy_shrub": ["minecraft:sand", "minecraft:grass_block", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_beetroots": ["minecraft:sand", "minecraft:grass_block", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_carrots": ["minecraft:sand", "minecraft:grass_block", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_cabbages": ["minecraft:sand", "minecraft:grass_block", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_onions": ["minecraft:sand", "minecraft:grass_block", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_rice": ["minecraft:sand", "minecraft:grass_block", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_tomatoes": ["minecraft:sand", "minecraft:grass_block", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_potatoes": ["minecraft:sand", "minecraft:grass_block", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"]
}
# 原版所有负面效果 (frozenset for O(1) lookup — 本 mod 内部使用，不对外暴露于扩展接口)
negativeEffect = frozenset([
    "slowness",
    "mining_fatigue",
    "instant_damage",
    "nausea",
    "blindness",
    "hunger",
    "weakness",
    "wither",
    "poison",
    "fatal_poison",
    "wither",
    "levitation",
    "darkness",
    "wind_charged",
    "weaving",
    "oozing",
    "infested"
])
# 盘装食物
platePackagedFoodDict = {
    "arris:roast_chicken_block_stage0": {"target": "arris:roast_chicken_block_stage1", "item": "arris:roast_chicken"},
    "arris:roast_chicken_block_stage1": {"target": "arris:roast_chicken_block_stage2", "item": "arris:roast_chicken"},
    "arris:roast_chicken_block_stage2": {"target": "arris:roast_chicken_block_stage3", "item": "arris:roast_chicken"},
    "arris:roast_chicken_block_stage3": {"target": "arris:roast_chicken_block_leftover", "item": "arris:roast_chicken"},
    "arris:roast_chicken_block_leftover": {"target": None, "item": None},
    "arris:stuffed_pumpkin_block_stage0": {"target": "arris:stuffed_pumpkin_block_stage1", "item": "arris:stuffed_pumpkin"},
    "arris:stuffed_pumpkin_block_stage1": {"target": "arris:stuffed_pumpkin_block_stage2", "item": "arris:stuffed_pumpkin"},
    "arris:stuffed_pumpkin_block_stage2": {"target": "arris:stuffed_pumpkin_block_stage3", "item": "arris:stuffed_pumpkin"},
    "arris:stuffed_pumpkin_block_stage3": {"target": None, "item": None},
    "arris:honey_glazed_ham_block_stage0": {"target": "arris:honey_glazed_ham_block_stage1", "item": "arris:honey_glazed_ham"},
    "arris:honey_glazed_ham_block_stage1": {"target": "arris:honey_glazed_ham_block_stage2", "item": "arris:honey_glazed_ham"},
    "arris:honey_glazed_ham_block_stage2": {"target": "arris:honey_glazed_ham_block_stage3", "item": "arris:honey_glazed_ham"},
    "arris:honey_glazed_ham_block_stage3": {"target": "arris:honey_glazed_ham_block_leftover", "item": "arris:honey_glazed_ham"},
    "arris:honey_glazed_ham_block_leftover": {"target": None, "item": None},
    "arris:shepherds_pie_block_stage0": {"target": "arris:shepherds_pie_block_stage1", "item": "arris:shepherds_pie"},
    "arris:shepherds_pie_block_stage1": {"target": "arris:shepherds_pie_block_stage2", "item": "arris:shepherds_pie"},
    "arris:shepherds_pie_block_stage2": {"target": "arris:shepherds_pie_block_stage3", "item": "arris:shepherds_pie"},
    "arris:shepherds_pie_block_stage3": {"target": "arris:shepherds_pie_block_leftover", "item": "arris:shepherds_pie"},
    "arris:shepherds_pie_block_leftover": {"target": None, "item": None},
    "arris:rice_roll_medley_block_stage0": {"target": "arris:rice_roll_medley_block_stage1", "item": "arris:kelp_roll_slice"},
    "arris:rice_roll_medley_block_stage1": {"target": "arris:rice_roll_medley_block_stage2", "item": "arris:kelp_roll_slice"},
    "arris:rice_roll_medley_block_stage2": {"target": "arris:rice_roll_medley_block_stage3", "item": "arris:kelp_roll_slice"},
    "arris:rice_roll_medley_block_stage3": {"target": "arris:rice_roll_medley_block_stage4", "item": "arris:salmon_roll"},
    "arris:rice_roll_medley_block_stage4": {"target": "arris:rice_roll_medley_block_stage5", "item": "arris:salmon_roll"},
    "arris:rice_roll_medley_block_stage5": {"target": "arris:rice_roll_medley_block_stage6", "item": "arris:salmon_roll"},
    "arris:rice_roll_medley_block_stage6": {"target": "arris:rice_roll_medley_block_stage7", "item": "arris:cod_roll"},
    "arris:rice_roll_medley_block_stage7": {"target": "arris:rice_roll_medley_block_leftover", "item": "arris:cod_roll"},
    "arris:rice_roll_medley_block_leftover": {"target": None, "item": None},
}
# 农作物下一阶段字典
cropsDict = {
    "arris:cabbages_stage0": "arris:cabbages_stage1",
    "arris:cabbages_stage1": "arris:cabbages_stage2",
    "arris:cabbages_stage2": "arris:cabbages_stage3",
    "arris:cabbages_stage3": "arris:cabbages_stage4",
    "arris:cabbages_stage4": "arris:cabbages_stage5",
    "arris:cabbages_stage5": "arris:cabbages_stage6",
    "arris:cabbages_stage6": "arris:cabbages_stage7",
    "arris:cabbages_stage7": "",
    "arris:budding_tomatoes_stage0": "arris:budding_tomatoes_stage1",
    "arris:budding_tomatoes_stage1": "arris:budding_tomatoes_stage2",
    "arris:budding_tomatoes_stage2": "arris:budding_tomatoes_stage3",
    "arris:budding_tomatoes_stage3": "arris:budding_tomatoes_stage4",
    "arris:budding_tomatoes_stage4": "arris:budding_tomatoes_stage5",
    "arris:budding_tomatoes_stage5": "arris:budding_tomatoes_stage6",
    "arris:budding_tomatoes_stage6": "",
    "arris:tomatoes_vine_stage0": "arris:tomatoes_vine_stage1",
    "arris:tomatoes_vine_stage1": "arris:tomatoes_vine_stage2",
    "arris:tomatoes_vine_stage2": "arris:tomatoes_vine_stage3",
    "arris:tomatoes_vine_stage3": "",
    "arris:onions_stage0": "arris:onions_stage1",
    "arris:onions_stage1": "arris:onions_stage2",
    "arris:onions_stage2": "arris:onions_stage3",
    "arris:onions_stage3": "",
    "arris:organic_compost_stage0": "arris:organic_compost_stage1",
    "arris:organic_compost_stage1": "arris:organic_compost_stage2",
    "arris:organic_compost_stage2": "arris:organic_compost_stage3",
    "arris:organic_compost_stage3": "arris:rich_soil",
    "arris:rich_soil": "",
    "arris:rich_soil_wheat0": "arris:rich_soil_wheat1",
    "arris:rich_soil_wheat1": "arris:rich_soil_wheat2",
    "arris:rich_soil_wheat2": "arris:rich_soil_wheat3",
    "arris:rich_soil_wheat3": "arris:rich_soil_wheat4",
    "arris:rich_soil_wheat4": "arris:rich_soil_wheat5",
    "arris:rich_soil_wheat5": "arris:rich_soil_wheat6",
    "arris:rich_soil_wheat6": "arris:rich_soil_wheat7",
    "arris:rich_soil_wheat7": "",
    "arris:rich_soil_beetroot0": "arris:rich_soil_beetroot1",
    "arris:rich_soil_beetroot1": "arris:rich_soil_beetroot2",
    "arris:rich_soil_beetroot2": "arris:rich_soil_beetroot3",
    "arris:rich_soil_beetroot3": "",
    "arris:rich_soil_carrots0": "arris:rich_soil_carrots1",
    "arris:rich_soil_carrots1": "arris:rich_soil_carrots2",
    "arris:rich_soil_carrots2": "arris:rich_soil_carrots3",
    "arris:rich_soil_carrots3": "",
    "arris:rich_soil_potatoes0": "arris:rich_soil_potatoes1",
    "arris:rich_soil_potatoes1": "arris:rich_soil_potatoes2",
    "arris:rich_soil_potatoes2": "arris:rich_soil_potatoes3",
    "arris:rich_soil_potatoes3": "",
    "arris:rice_stage0": "arris:rice_stage1",
    "arris:rice_stage1": "arris:rice_stage2",
    "arris:rice_stage2": "arris:rice_stage3",
    "arris:rice_stage3": "",
    "arris:rice_upper_crop_stage0": "arris:rice_upper_crop_stage1",
    "arris:rice_upper_crop_stage1": "arris:rice_upper_crop_stage2",
    "arris:rice_upper_crop_stage2": "arris:rice_upper_crop_stage3",
    "arris:rice_upper_crop_stage3": "",
}
# 厨锅配方
CookingPotRecipeList = [
    {
        "Recipe": [
            [
                ("minecraft:red_mushroom", 0),
                ("minecraft:red_mushroom", 0)
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:brown_mushroom", 0)
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("minecraft:brown_mushroom", 0)
            ]
        ],
        "CookResult": ("minecraft:mushroom_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蘑菇煲"
    },
    {
        "Recipe": [
            [
                ("minecraft:beetroot", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:beetroot", 0)
            ]
        ],
        "CookResult": ("minecraft:beetroot_soup", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "甜菜汤"
    },
    {
        "Recipe": [
            [
                ("minecraft:rabbit", 0),
                ("minecraft:red_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:carrot", 0)
            ],
            [
                ("minecraft:rabbit", 0),
                ("minecraft:brown_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:carrot", 0)
            ]
        ],
        "CookResult": ("minecraft:rabbit_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "兔肉煲"
    },
    {
        "Recipe": [
            [
                ("arris:tomato", 0),
                ("arris:tomato", 0)
            ]
        ],
        "CookResult": ("arris:tomato_sauce", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "番茄酱"
    },
    {
        "Recipe": [
            [
                ("arris:rice", 0)
            ]
        ],
        "CookResult": ("arris:cooked_rice", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "米饭"
    },
    {
        "Recipe": [
            [
                ("arris:rice", 0),
                ("minecraft:egg", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0),
            ]
        ],
        "CookResult": ("arris:fried_rice", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "炒饭"
    },
    {
        "Recipe": [
            [
                ("arris:wheat_dough", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:onion", 0),
                ("arris:bacon", 0)
            ],
            [
                ("arris:wheat_dough", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:onion", 0),
                ("arris:minced_beef", 0)
            ],
            [
                ("arris:wheat_dough", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:onion", 0),
                ("arris:cod_slice", 0)
            ],
            [
                ("arris:wheat_dough", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:onion", 0),
                ("arris:salmon_slice", 0)
            ]
        ],
        "CookResult": ("arris:dumplings", 0),
        "Vessel": ("arris:cabbage_leaf", 0),
        "PushItem": [
        ],
        "text": "饺子"
    },
    {
        "Recipe": [
            [
                ("arris:minced_beef", 0),
                ("arris:raw_pasta", 0),
                ("arris:tomato", 0)
            ]
        ],
        "CookResult": ("arris:pasta_with_meatballs", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "肉丸意面"
    },
    {
        "Recipe": [
            [
                ("arris:mutton_chops", 0),
                ("arris:raw_pasta", 0),
                ("arris:tomato", 0)
            ]
        ],
        "CookResult": ("arris:pasta_with_mutton_chop", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "羊排意面"
    },
    {
        "Recipe": [
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:red_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:brown_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("minecraft:red_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:red_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:carrot", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:brown_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:carrot", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("minecraft:red_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:carrot", 0),
            ]
        ],
        "CookResult": ("arris:mushroom_rice", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蘑菇饭"
    },
    {
        "Recipe": [
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:carrot", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:carrot", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:beetroot", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:beetroot", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:tomato", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:tomato", 0),
            ]
        ],
        "CookResult": ("arris:vegetable_noodles", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蔬菜面"
    },
    {
        "Recipe": [
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:carrot", 0)
            ],
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:beetroot", 0)
            ],
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:potato", 0)
            ],
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("arris:tomato", 0)
            ]
        ],
        "CookResult": ("arris:ratatouille", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蔬菜杂烩"
    },
    {
        "Recipe": [
            [
                ("arris:cod_slice", 0),
                ("arris:raw_pasta", 0),
                ("arris:tomato", 0),
                ("minecraft:ink_sac", 0)
            ],
            [
                ("arris:salmon_slice", 0),
                ("arris:raw_pasta", 0),
                ("arris:tomato", 0),
                ("minecraft:ink_sac", 0)
            ]
        ],
        "CookResult": ("arris:squid_ink_pasta", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "鱿鱼墨面"
    },
    {
        "Recipe": [
            [
                ("arris:rice", 0),
                ("minecraft:brown_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:sweet_berries", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:red_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:sweet_berries", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:brown_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:glow_berries", 0),
                ("minecraft:beetroot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:red_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:glow_berries", 0),
                ("minecraft:beetroot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:brown_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:sweet_berries", 0),
                ("arris:onion", 0),
                ("arris:tomato", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:red_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:sweet_berries", 0),
                ("arris:onion", 0),
                ("arris:tomato", 0)
            ],
        ],
        "CookResult": ("arris:stuffed_pumpkin_block_stage0", 0),
        "Vessel": ("minecraft:pumpkin", 0),
        "PushItem": [
        ],
        "text": "填馅南瓜"
    },
    {
        "Recipe": [
            [
                ("arris:bacon", 0),
                ("arris:bacon", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:minced_beef", 0),
                ("arris:minced_beef", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:mutton_chops", 0),
                ("arris:mutton_chops", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:cod_slice", 0),
                ("arris:cod_slice", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:salmon_slice", 0),
                ("arris:salmon_slice", 0),
                ("arris:cabbage_leaf", 0)
            ]
        ],
        "CookResult": ("arris:cabbage_rolls", 0),
        "Vessel": ("arris:cabbage_leaf", 0),
        "PushItem": [
        ],
        "text": "卷心菜卷"
    },
    {
        "Recipe": [
            [
                ("minecraft:bone", 0),
                ("minecraft:brown_mushroom", 0)
            ],
            [
                ("minecraft:bone", 0),
                ("minecraft:red_mushroom", 0)
            ],
            [
                ("minecraft:bone", 0),
                ("minecraft:sweet_berries", 0)
            ],
            [
                ("minecraft:bone", 0),
                ("minecraft:glow_berries", 0)
            ]
        ],
        "CookResult": ("arris:bone_broth", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "大骨汤"
    },
    {
        "Recipe": [
            [
                ("arris:minced_beef", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0)
            ]
        ],
        "CookResult": ("arris:cookbeef_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "牛肉炖"
    },
    {
        "Recipe": [
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:beetroot", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:tomato", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:pumpkin_slice", 0)
            ]
        ],
        "CookResult": ("arris:chicken_soup", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "鸡肉汤"
    },
    {
        "Recipe": [
            [
                ("arris:cabbage_leaf", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0)
            ],
            [
                ("arris:cabbage_leaf", 0),
                ("arris:pumpkin_slice", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0)
            ]
        ],
        "CookResult": ("arris:vegetable_soup", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蔬菜汤"
    },
    {
        "Recipe": [
            [
                ("arris:cod_slice", 0),
                ("arris:tomato", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:salmon_slice", 0),
                ("arris:tomato", 0),
                ("arris:onion", 0)
            ]
        ],
        "CookResult": ("arris:fish_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "鱼肉炖"
    },
    {
        "Recipe": [
            [
                ("arris:pumpkin_slice", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:bacon", 0),
                ("arris:milk_bottle", 0)
            ]
        ],
        "CookResult": ("arris:pumpkin_soup", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
            ("minecraft:glass_bottle", 0)
        ],
        "text": "南瓜汤"
    },
    {
        "Recipe": [
            [
                ("arris:cod_slice", 0),
                ("minecraft:egg", 0),
                ("arris:tomato", 0),
                ("minecraft:potato", 0)
            ],
            [
                ("arris:cod_slice", 0),
                ("minecraft:egg", 0),
                ("arris:pumpkin_slice", 0),
                ("minecraft:potato", 0)
            ]
        ],
        "CookResult": ("arris:baked_cod_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "烘焙鳕鱼炖"
    },
    {
        "Recipe": [
            [
                ("arris:raw_pasta", 0),
                ("minecraft:dried_kelp", 0),
                ("arris:fried_egg", 0),
                ("arris:bacon", 0)
            ],
            [
                ("arris:raw_pasta", 0),
                ("minecraft:dried_kelp", 0),
                ("arris:fried_egg", 0),
                ("arris:minced_beef", 0)
            ],
            [
                ("arris:raw_pasta", 0),
                ("minecraft:dried_kelp", 0),
                ("arris:fried_egg", 0),
                ("arris:cod_slice", 0)
            ],
            [
                ("arris:raw_pasta", 0),
                ("minecraft:dried_kelp", 0),
                ("arris:fried_egg", 0),
                ("arris:salmon_slice", 0)
            ]
        ],
        "CookResult": ("arris:noodle_soup", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "面条汤"
    },
    {
        "Recipe": [
            [
                ("arris:milk_bottle", 0),
                ("minecraft:cocoa_beans", 0),
                ("minecraft:cocoa_beans", 0),
                ("minecraft:sugar", 0)
            ]
        ],
        "CookResult": ("arris:hot_cocoa", 0),
        "Vessel": ("minecraft:glass_bottle", 0),
        "PushItem": [
            ("minecraft:glass_bottle", 0)
        ],
        "text": "热可可"
    },
    {
        "Recipe": [
            [
                ("minecraft:apple", 0),
                ("minecraft:apple", 0),
                ("minecraft:sugar", 0)
            ]
        ],
        "CookResult": ("arris:apple_cider", 0),
        "Vessel": ("minecraft:glass_bottle", 0),
        "PushItem": [
        ],
        "text": "苹果酒"
    },
    {
        "Recipe": [
            [
                ("minecraft:glow_berries", 0),
                ("minecraft:egg", 0),
                ("minecraft:sugar", 0),
                ("arris:milk_bottle", 0)
            ]
        ],
        "CookResult": ("arris:glow_berry_custard", 0),
        "Vessel": ("minecraft:glass_bottle", 0),
        "PushItem": [
            ("minecraft:glass_bottle", 0)
        ],
        "text": "发光浆果蛋奶沙司"
    },
    {
        "Recipe": [
            [
                ("minecraft:rotten_flesh", 0),
                ("minecraft:bone_meal", 0),
                ("arris:rice", 0),
                ("minecraft:chicken", 0)
            ]
        ],
        "CookResult": ("arris:dog_food", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "狗粮"
    }
]

horseComponentsDict = {
    "minecraft:behavior.tempt": '{"priority": 5,"speed_multiplier": 1.2,"items": ["arris:horse_feed","golden_apple","appleEnchanted","golden_carrot"]}',
    "minecraft:healable": '{"items":[{"item":"wheat","heal_amount":2},{"item":"sugar","heal_amount":1},{"item":"hay_block","heal_amount":20},{"item":"apple","heal_amount":3},{"item":"golden_carrot","heal_amount":4},{"item":"arris:horse_feed","heal_amount":6},{"item":"golden_apple","heal_amount":10},{"item":"appleEnchanted","heal_amount":10}]}',
    "minecraft:tamemount": '{"min_temper":0,"max_temper":100,"feed_text":"action.interact.feed","ride_text":"action.interact.mount","feed_items":[{"item":"wheat","temper_mod":3},{"item":"arris:horse_feed","temper_mod":7},{"item":"sugar","temper_mod":3},{"item":"apple","temper_mod":3},{"item":"golden_carrot","temper_mod":5},{"item":"golden_apple","temper_mod":10},{"item":"appleEnchanted","temper_mod":10}],"auto_reject_items":[{"item":"horsearmorleather"},{"item":"horsearmoriron"},{"item":"horsearmorgold"},{"item":"horsearmordiamond"},{"item":"saddle"}],"tame_event":{"event":"minecraft:on_tame","target":"self"}}',
    "minecraft:breedable": '{"parent_centric_attribute_blending":["minecraft:health","minecraft:movement","minecraft:horse.jump_strength"],"require_tame":true,"inherit_tamed":false,"breeds_with":[{"mate_type":"minecraft:horse","baby_type":"minecraft:horse","breed_event":{"event":"minecraft:entity_born","target":"baby"}},{"mate_type":"minecraft:donkey","baby_type":"minecraft:mule","breed_event":{"event":"minecraft:entity_born","target":"baby"}}],"breed_items":["arris:horse_feed","golden_carrot","golden_apple","appleEnchanted"],"mutation_factor":{"extra_variant":0.2,"variant":0.111},"mutation_strategy":"random","random_variant_mutation_interval":[0,7],"random_extra_variant_mutation_interval":[0,5]}'
}

wolfComponentsDict = {
    "minecraft:breedable": '{"require_tame":true,"require_full_health":true,"breeds_with":{"mate_type":"minecraft:wolf","baby_type":"minecraft:wolf","breed_event":{"event":"minecraft:entity_born","target":"baby"}},"breed_items":["arris:dog_food","chicken","cooked_chicken","beef","cooked_beef","muttonRaw","muttonCooked","porkchop","cooked_porkchop","rabbit","cooked_rabbit","rotten_flesh"]}',
    "minecraft:healable": '{"items":[{"item":"porkchop","heal_amount":3},{"item":"cooked_porkchop","heal_amount":8},{"item":"fish","heal_amount":2},{"item":"salmon","heal_amount":2},{"item":"clownfish","heal_amount":1},{"item":"pufferfish","heal_amount":1},{"item":"cooked_fish","heal_amount":5},{"item":"cooked_salmon","heal_amount":6},{"item":"beef","heal_amount":3},{"item":"cooked_beef","heal_amount":8},{"item":"chicken","heal_amount":2},{"item":"cooked_chicken","heal_amount":6},{"item":"muttonRaw","heal_amount":2},{"item":"muttonCooked","heal_amount":6},{"item":"rotten_flesh","heal_amount":4},{"item":"rabbit","heal_amount":3},{"item":"cooked_rabbit","heal_amount":5},{"item":"arris:dog_food","heal_amount":7},{"item":"rabbit_stew","heal_amount":10}]}',
    "minecraft:behavior.beg": '{"priority":9,"look_distance":8,"look_time":[2,4],"items":["arris:dog_food","bone","porkchop","cooked_porkchop","chicken","cooked_chicken","beef","cooked_beef","rotten_flesh","muttonraw","muttoncooked","rabbit","cooked_rabbit"]}',
}

# ---------------- 厨锅配方索引 ----------------
# 为 CheckCookingPotRecipe 提供 O(1) 查找，避免每 tick 遍历 CookingPotRecipeList × variants 做 Counter 比较。
# key: tuple(sorted((itemName, auxValue), ...)) —— 将一组输入排序成可哈希的唯一键
# value: (cookResultTuple, pushItemList)
_cookingPotRecipeIndex = {}

def BuildCookingPotRecipeIndex():
    """
    重建厨锅配方索引。每次 CookingPotRecipeList 被修改后调用。
    遇到键冲突时保留先插入的那条，以维持与原 O(n) 实现"首个匹配获胜"一致的语义。
    """
    _cookingPotRecipeIndex.clear()
    for recipeDict in CookingPotRecipeList:
        cookResult = recipeDict["CookResult"]
        pushItemList = recipeDict.get("PushItem", [])
        for variant in recipeDict["Recipe"]:
            key = tuple(sorted(variant))
            if key not in _cookingPotRecipeIndex:
                _cookingPotRecipeIndex[key] = (cookResult, pushItemList)

def LookupCookingPotRecipe(inputKey):
    """
    根据排序后的输入键查找配方。inputKey: tuple(sorted([(name, aux), ...])).
    返回 (cookResultTuple, pushItemList) 或 None。
    """
    return _cookingPotRecipeIndex.get(inputKey)

# 首次构建（在模块加载时）
BuildCookingPotRecipeIndex()


def ArrisFarmersDelightInterface(target, element=None):
    """
    向配置字典或列表内添加元素
    :param target: 需要调用的变量名称 (str)
    :param element: 需要添加进去的元素(如果目标是list,则支持str或list,如果目标是dict,则仅支持dict)
    :return 修改结果
    """
    globalVar = globals()
    if not target:
        return False
    if not globalVar[target]:
        return False
    if target == "CookingPotRecipeList":
        for recipe in element["Recipe"]:
            if len(recipe) > 6:
                return False

    targetType = type(globalVar[target]).__name__
    elementType = type(element).__name__
    if targetType == "list":
        if elementType != "list":
            globalVar[target].append(element)
        else:
            globalVar[target] += element
    elif targetType == "dict" and elementType == "dict":
        globalVar[target].update(element)
    # 若外部修改的是厨锅配方表，则同步重建索引
    if target == "CookingPotRecipeList":
        BuildCookingPotRecipeIndex()
    return globalVar[target]

def ArrisFarmersDelightObtain(target):
    """
    获取配置字典或列表
    :param target: 需要获取的变量名称 (str)
    :return 结果
    """
    globalVar = globals()
    if not target:
        return False
    if not globalVar[target]:
        return False
    else:
        return globalVar[target]

def AddCookingPotRecipe(name, recipe):
    """
    在厨锅原有的配方上，新增额外配方
    :param name: 对应食物id (str)
    :param recipe: 对应需要添加上去的配方 (list)
    :return 结果
    """
    if not name:
        return False
    if len(recipe) > 6:
        return False
    for recipeDict in CookingPotRecipeList:
        if recipeDict["CookResult"][0] == name:
            recipeDict["Recipe"].append(recipe)
            BuildCookingPotRecipeIndex()
            return recipeDict["Recipe"]
    return False
