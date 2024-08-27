# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi

playerId = clientApi.GetLocalPlayerId()
levelId = clientApi.GetLevelId()
compFactory = clientApi.GetEngineCompFactory()

""" 附魔种类枚举 """
EnchantType = {
    0: "保护",
    1: "火焰保护",
    2: "摔落保护",
    3: "爆炸保护",
    4: "弹射物保护",
    5: "荆棘",
    6: "水下呼吸",
    7: "深海探索者",
    8: "水下速掘",
    9: "锋利",
    10: "亡灵杀手",
    11: "节肢杀手",
    12: "击退",
    13: "火焰附加",
    14: "抢夺",
    15: "效率",
    16: "精准采集",
    17: "耐久",
    18: "时运",
    19: "力量",
    20: "冲击",
    21: "火矢",
    22: "无限",
    23: "海之眷顾",
    24: "饵钓",
    25: "冰霜行者",
    26: "经验修补",
    27: "绑定诅咒",
    28: "消失诅咒",
    29: "穿刺",
    30: "激流",
    31: "忠诚",
    32: "引雷",
    33: "多重射击",
    34: "穿透",
    35: "快速装填",
    36: "灵魂疾行",
    37: "迅捷潜行",
    38: "附魔种数",
    39: "无效附魔",
    255: "自定义附魔"
}
""" 罗马数字 """
RomanNumerals = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X"
}
""" 盔甲纹饰 """
TrimPattern = {
    "coast": " 海岸纹饰盔甲",
    "dune": " 沙丘纹饰盔甲",
    "eye": " 眼眸纹饰盔甲",
    "host": " 主导盔甲纹饰",
    "raiser": " 崛起盔甲纹饰",
    "rib": " 肋骨纹饰盔甲",
    "sentry": " 哨兵纹饰盔甲",
    "shaper": " 塑形盔甲纹饰",
    "silence": " 潜声盔甲纹饰",
    "snout": " 猪鼻纹饰盔甲",
    "spire": " 尖顶纹饰盔甲",
    "tide": " 潮汐纹饰盔甲",
    "vex": " 恼鬼纹饰盔甲",
    "ward": " 监守纹饰盔甲",
    "wayfinder": " 寻路盔甲纹饰",
    "wild": " 荒野纹饰盔甲",
    "bolt": " 镶铆盔甲纹饰",
    "flow": " 涡流盔甲纹饰"
}
""" 盔甲材质 """
TrimMaterial = {
    "amethyst": " 紫水晶材料",
    "copper": " 铜材料",
    "diamond": " 钻石材料",
    "emerald": " 绿宝石材料",
    "gold": " 黄金材料",
    "iron": " 铁材料",
    "lapis": " 青金石材料",
    "netherite": " 下界合金材料",
    "quartz": " 石英材料",
    "redstone": " 红石材料"
}
""" 材质颜色 """
MaterialColor = {
    "amethyst": "§5",
    "copper": "§n",
    "diamond": "§3",
    "emerald": "§2",
    "gold": "§e",
    "iron": "§7",
    "lapis": "§1",
    "netherite": "§8",
    "quartz": "§r",
    "redstone": "§4"
}

class ItemInformationAPI:
    """ 部分获取物品信息的功能 """

    def __init__(self):
        pass

    @staticmethod
    def getCustomName(itemDict):
        """ 获取物品自定义名称 """
        userData = itemDict.get("userData", {})
        if userData:
            return userData.get("display", {}).get("Name", {}).get("__value__")  # 玩家的自定义名称
        return None

    @staticmethod
    def getEnchant(itemDict):
        """ 获取物品附魔的中文名称与等级 """
        enchantData = itemDict.get("enchantData", [])
        enchantList = [
            "§i%s %s§r" % (EnchantType.get(i[0]), RomanNumerals.get(i[1], i[1]))
            for i in enchantData
        ]
        """ 原版附魔 """

        modEnchantList = [
            compFactory.CreateGame(levelId).GetChinese("enchantment.%s.name" % i[0]) + str(i[1])
            for i in itemDict.get("modEnchantData", [])
        ]
        """ 自定义附魔 """
        return enchantList + modEnchantList

    @staticmethod
    def getDamage(itemDict):
        """ 获取物品伤害值 """
        comp = compFactory.CreateItem(levelId)
        damage = comp.GetItemBasicInfo(itemDict.get("newItemName"), itemDict.get("newAuxValue")).get("weaponDamage")
        level = next((i[1] for i in itemDict.get("enchantData", []) if i[0] == 9), 0)
        damage += int(1.25 * level)
        return damage

    @staticmethod
    def getTrimPatternAndMaterial(itemDict):
        """ 获取盔甲纹饰和材质 """
        userData = itemDict.get("userData", {})
        if userData:
            pattern = userData.get("Trim", {}).get("Pattern", {}).get("__value__")  # 盔甲纹饰
            material = userData.get("Trim", {}).get("Material", {}).get("__value__") # 盔甲材质
            if pattern and material:
                return {"pattern": pattern, "material": material}
            else:
                return None
        return None

    @staticmethod
    def getShulkerBox(itemDict):
        """ 获取潜影盒信息 """
        userData = itemDict.get("userData", {})
        if userData:
            itemList = userData.get("Items", [])
            info = []
            itemNum = len(itemList) - 5
            if itemList:
                for i in range(0, len(itemList) - 1):
                    itemDict = itemList[i]
                    itemName = itemDict.get("Name").get("__value__")
                    count = itemDict.get("Count").get("__value__")
                    itemType = compFactory.CreateItem(levelId).GetItemBasicInfo(itemName, 0)["itemType"]
                    print itemList[i]
                    if itemType == "block":
                        if itemName[0:9] == "minecraft":
                            name = compFactory.CreateGame(levelId).GetChinese("tile.{}.name".format(itemName[10:]))
                        else:
                            name = compFactory.CreateGame(levelId).GetChinese("tile.{}.name".format(itemName))
                    else:
                        if itemName[0:9] == "minecraft":
                            name = compFactory.CreateGame(levelId).GetChinese("item.{}.name".format(itemName[10:]))
                        else:
                            name = compFactory.CreateGame(levelId).GetChinese("item.{}.name".format(itemName))
                    info.append("{} x{}".format(name, str(count)))
                if itemNum > 0:
                    info.append("还有 {} 个...".format(str(itemNum)))
                return info
            else:
                return None
        return None

def updateItemMessageShow(itemDict):
    """ 更新物品信息显示 """

    def buildMessageText():
        # 构建信息文字
        messageList = [name]
        if effectName:
            messageList.append(effectName)
        if shulkerBoxInfo:
            for shulker in shulkerBoxInfo:
                messageList.append("§7" + shulker)
        if trimPatternAndMaterial:
            messageList.append(trimPatternAndMaterial)
        if enchantList:
            messageList.extend([""] + enchantList)
        if damage > 0:
            messageList.append("\n§9+%s 攻击伤害§r" % damage)
        if knockbackResistance > 0:
            messageList.append("\n§9+%s 击退抗性§r" % int(knockbackResistance * 10))
        return "\n".join(i for i in messageList if i != "")
    if itemDict:
        comp = compFactory.CreateItem(levelId)
        info = comp.GetItemBasicInfo(itemDict.get("newItemName"), itemDict.get("newAuxValue"))
        name = info.get("itemName")
        knockbackResistance = info.get("armorKnockbackResistance")
        """ 名称 """
        customName = ItemInformationAPI.getCustomName(itemDict)
        """ 自定义名称 """
        if customName:
            name = "§o" + customName + "§r"
        """ 潜影盒信息 """
        shulkerBoxInfo = ItemInformationAPI.getShulkerBox(itemDict)
        """盔甲纹饰以及材质"""
        armorDict = ItemInformationAPI.getTrimPatternAndMaterial(itemDict)
        trimPatternAndMaterial = None
        if armorDict:
            color = MaterialColor.get(armorDict.get("material", ""))
            pattern = TrimPattern.get(armorDict.get("pattern", ""))
            material = TrimMaterial.get(armorDict.get("material", ""))
            trimPatternAndMaterial = "§7升级:\n{}{}\n{}".format(color, pattern, material)
        """ 武器伤害 """
        damage = ItemInformationAPI.getDamage(itemDict)
        """ 附魔 """
        enchantList = ItemInformationAPI.getEnchant(itemDict)
        if enchantList:  # 有附魔则名称变蓝色
            name = "§b" + name + "§r"

        if itemDict.get("customTips"):
            text = itemDict.get("customTips")  # type: str
            text = text.replace("%name%", name)
            text = text.replace("%category%", "")
            text = text.replace("%enchanting%", "\n" + "\n".join(i for i in ItemInformationAPI.getEnchant(itemDict) if i != ""))
            text = text.replace("%attack_damage%", "\n§9+%s 攻击伤害§r" % damage if damage > 0 else "")
        else:
            effectName = comp.GetItemEffectName(itemDict.get("newItemName"), itemDict.get("newAuxValue"))
            """ 效果名称 """
            text = buildMessageText()
        return text
