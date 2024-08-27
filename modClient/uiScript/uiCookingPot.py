# -*- coding: utf-8 -*-
import mod.client.extraClientApi as clientApi
from ...QingYunModLibs.SystemApi import *
from ...modCommon.itemInfo import *
from ...modCommon.modConfig import *
import copy
import random

ScreenNode = clientApi.GetScreenNodeCls()
playerId = clientApi.GetLocalPlayerId()
levelId = clientApi.GetLevelId()
ViewBinder = clientApi.GetViewBinderCls()
compFactory = clientApi.GetEngineCompFactory()

ROOT_SCREEN = "/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel"
CLOSE = ROOT_SCREEN + "/cooking_pot_bg/cooking_pot_main/top_panel/close"
InventoryGrid = ROOT_SCREEN + "/cooking_pot_bg/cooking_pot_main/inventory_panel/inventory_grid"
HotbarGrid = ROOT_SCREEN + "/cooking_pot_bg/cooking_pot_main/inventory_panel/hotbar_grid"
inputItemGrid = ROOT_SCREEN + "/cooking_pot_bg/cooking_pot_main/cooking_pot/inputItemGrid"
vesselItemSlot = ROOT_SCREEN + "/cooking_pot_bg/cooking_pot_main/cooking_pot/vesselItem"
resultItemSlot = ROOT_SCREEN + "/cooking_pot_bg/cooking_pot_main/cooking_pot/resultItem"
heat = ROOT_SCREEN + "/cooking_pot_bg/cooking_pot_main/cooking_pot/heat/fire"
arrow = ROOT_SCREEN + "/cooking_pot_bg/cooking_pot_main/cooking_pot/arrow"
preview = ROOT_SCREEN + "/cooking_pot_bg/cooking_pot_main/cooking_pot/preview/item"
itemTips = ROOT_SCREEN + "/cooking_pot_bg/popup_tip_text/item_panel_image/item_text_label"
cookRecipePanel = ROOT_SCREEN + "/padding_bg/cookbook_bg/stack_panel"

foodRecipePath = None

class uiCookingPot(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.heatEnable = param.get("heatEnable") # 火源
        self.inputItemSlot = param.get("inputItemSlot") # 厨锅输入槽 (6个)
        self.vesselItemSlot = param.get("vesselItemSlot") # 厨锅容器槽 (1个)
        self.resultItemSlot = param.get("resultItemSlot") # 厨锅输出槽 (1个)
        self.previewItemSlot = param.get("previewItemSlot") # 厨锅预览槽 (1个)
        self.blockPos = param.get("blockPos")
        self.dimensionId = param.get("dimensionId")

        self.tempIndex = None # index缓存
        self.tempGroup = None # 按钮集合缓存
        self.tempButton = None # 上一个UI控件实例缓存
        self.flyAnimationPos = []
        self.flyAnimationPos2 = []
        self.flyItem = None
        self.flyItem2 = None
        self.itemTips = None # 物品信息显示
        self.nowSelect = None # 当前选中的槽位
        self.touchButtonPath = None # 点击的slot按钮路径
        self.heatIcon = None # 火源图标实例
        self.foodRecipe = None # 配方面板UI实例
        self.foodRecipeList = None # 选择的食谱列表
        self.foodRecipeIndex = 0 # 选择的食谱索引
        self.RecipeList = CookingPotRecipeList
        self.foodRecipeTimer = None
        self.foodRecipeSearchDict = None
        self.allItemList = compFactory.CreateItem(playerId).GetPlayerAllItems(clientApi.GetMinecraftEnum().ItemPosType.INVENTORY, True)

    def Create(self):
        global foodRecipePath
        inputModeId = compFactory.CreatePlayerView(levelId).GetToggleOption(clientApi.GetMinecraftEnum().OptionId.INPUT_MODE)
        if inputModeId == 0: # 键鼠操作
            foodRecipePath = ROOT_SCREEN + "/padding_bg/option_bg/scroll_view/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
        elif inputModeId == 1: # 触摸屏操作
            foodRecipePath = ROOT_SCREEN + "/padding_bg/option_bg/scroll_view/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"

        self.foodRecipe = self.GetBaseUIControl(foodRecipePath)
        self.nowSelect = None
        self.flyItem = self.GetBaseUIControl(ROOT_SCREEN + "/cooking_pot_bg/flyItem")
        self.flyItem2 = self.GetBaseUIControl(ROOT_SCREEN + "/cooking_pot_bg/flyItem2")
        self.itemTips = self.GetBaseUIControl(ROOT_SCREEN + "/cooking_pot_bg/popup_tip_text")
        self.heatIcon = self.GetBaseUIControl(heat)
        closeButton = self.GetBaseUIControl(CLOSE).asButton()
        closeButton.AddTouchEventParams({"isSwallow": True})
        closeButton.SetButtonTouchUpCallback(self.CloseCrabTrap)
        compFactory.CreateGame(levelId).AddTimer(0.1, self.GetInventoryGrid)

    def SetGlobalPosition(self, path, pos):
        """
        设置某一控件的绝对全局屏幕坐标
        :param str path: 需要设置坐标的控件路径
        :param tuple pos: 控件绝对坐标
        """
        Pos_X, Pos_Y = pos
        ParentPath = str(path).split("/")
        for i in range(1, len(str(path).split("/"))):
            ParentPath.pop(-1)
            newComp = ""
            for Comp in ParentPath:
                if Comp == "":
                    continue
                newComp = newComp + "/" + Comp
            control = self.GetBaseUIControl(newComp)
            if control:
                X, Y = self.GetBaseUIControl(newComp).GetPosition()
                Pos_X -= X
                Pos_Y -= Y
        return Pos_X, Pos_Y

    def intermediates(self, p1, p2, nb_points=7):
        """
        获取两点之间的坐标
        :param p1: 坐标1
        :param p2: 坐标2
        :param nb_points: 步长(默认为10)
        """
        x_spacing = (p2[0] - p1[0]) / (nb_points + 1)
        y_spacing = (p2[1] - p1[1]) / (nb_points + 1)
        return [(p1[0] + i * x_spacing, p1[1] + i * y_spacing) for i in range(1, nb_points + 1)]

    def GetItemDict(self, collection, index):
        self.allItemList = compFactory.CreateItem(playerId).GetPlayerAllItems(clientApi.GetMinecraftEnum().ItemPosType.INVENTORY, True)
        if collection == "hotbarButton" or collection == "inventoryButton":
            itemDict = self.allItemList[index]
        elif collection == "inputItemButton":
            itemDict = self.inputItemSlot[index]
        elif collection == "vesselButton":
            itemDict = self.vesselItemSlot[index]
        elif collection == "resultButton":
            itemDict = self.resultItemSlot[index]
        else:
            itemDict = None
        return itemDict

    def GetItemLocked(self, itemDict, slot):
        itemLock = slot.GetChildByName("item_lock_overlay")
        if itemDict:
            userData = itemDict.get("userData")
            if userData:
                lock = userData.get("minecraft:item_lock")
                if lock:
                    mode = lock["__value__"]
                    itemLock.GetChildByName("cell_lock").SetVisible(True)
                    if mode == 1:
                        itemLock.GetChildByName("item_lock_red").SetVisible(True)
                        slot.SetTouchEnable(False)
                    elif mode == 2:
                        itemLock.GetChildByName("item_lock_yellow").SetVisible(True)
            else:
                itemLock.GetChildByName("cell_lock").SetVisible(False)
                itemLock.GetChildByName("item_lock_yellow").SetVisible(False)

    def RenderGridSlotItem(self, itemList, interval, maxCount, path, gridName):
        for index in range(1, maxCount):
            itemDict = itemList[index + interval]
            slotPath = path + "/{}{}".format(gridName, index)
            slot = self.GetBaseUIControl(slotPath)
            if itemDict == {}:
                slot.GetChildByName("item_renderer").SetVisible(False)
                slot.GetChildByName("stack_count_label").asLabel().SetText("")
                slot.GetChildByName("slot_select").SetVisible(False)
                slot.GetChildByName("cell_hint").SetVisible(False)
            self.GetItemLocked(itemDict, slot)
            itemRenderer = slot.GetChildByName("item_renderer")
            countLabel = slot.GetChildByName("stack_count_label")
            if itemDict:
                if itemDict["enchantData"]:
                    isEnchanted = True
                else:
                    isEnchanted = False
                itemRenderer.asItemRenderer().SetUiItem(itemDict["newItemName"], itemDict["newAuxValue"], isEnchanted, itemDict.get("userData", {}))
                itemRenderer.SetVisible(True)
                if itemDict["count"] == 1:
                    countLabel.asLabel().SetText("")
                else:
                    countLabel.asLabel().SetText(str(itemDict["count"]))

    def GetInventoryGrid(self):
        self.allItemList = compFactory.CreateItem(playerId).GetPlayerAllItems(clientApi.GetMinecraftEnum().ItemPosType.INVENTORY, True)
        self.RenderGridSlotItem(self.allItemList, 8, 28, InventoryGrid, "inventorySlot")
        self.RenderGridSlotItem(self.allItemList, -1, 10, HotbarGrid, "hotbarSlot")
        self.RenderGridSlotItem(self.inputItemSlot, -1, 7, inputItemGrid, "inputItemSlot")
        self.SetArrowProgress(10.0)

        if self.heatEnable is False:
            self.heatIcon.SetVisible(False)
        else:
            self.heatIcon.SetVisible(True)
        self.SetPreviewItemSlot(self.previewItemSlot[0])

        slot = self.GetBaseUIControl(vesselItemSlot)
        itemRenderer = slot.GetChildByName("item_renderer")
        countLabel = slot.GetChildByName("stack_count_label")
        itemDict = self.vesselItemSlot[0]
        if itemDict and itemDict["count"] > 0:
            if itemDict["enchantData"]:
                isEnchanted = True
            else:
                isEnchanted = False
            itemRenderer.asItemRenderer().SetUiItem(itemDict["newItemName"], itemDict["newAuxValue"], isEnchanted, itemDict.get("userData", {}))
            itemRenderer.SetVisible(True)
            if itemDict["count"] == 1:
                countLabel.asLabel().SetText("")
            else:
                countLabel.asLabel().SetText(str(itemDict["count"]))
        else:
            slot.GetChildByName("item_renderer").SetVisible(False)
            slot.GetChildByName("stack_count_label").asLabel().SetText("")
            slot.GetChildByName("slot_select").SetVisible(False)
            slot.GetChildByName("cell_hint").SetVisible(False)

        slot = self.GetBaseUIControl(resultItemSlot)
        itemRenderer = slot.GetChildByName("item_renderer")
        countLabel = slot.GetChildByName("stack_count_label")
        itemDict = self.resultItemSlot[0]
        if itemDict and itemDict["count"] > 0:
            if itemDict["enchantData"]:
                isEnchanted = True
            else:
                isEnchanted = False
            itemRenderer.asItemRenderer().SetUiItem(itemDict["newItemName"], itemDict["newAuxValue"], isEnchanted, itemDict.get("userData", {}))
            itemRenderer.SetVisible(True)
            if itemDict["count"] == 1:
                countLabel.asLabel().SetText("")
            else:
                countLabel.asLabel().SetText(str(itemDict["count"]))
        self.UpdateScreen(True)

    def ExchangeSlotItem(self, index, collection):
        """
        交换两个槽位的物品
        """
        itemsDictMap = dict()
        self.allItemList = compFactory.CreateItem(playerId).GetPlayerAllItems(clientApi.GetMinecraftEnum().ItemPosType.INVENTORY, True)
        if self.tempGroup == "hotbarButton" or self.tempGroup == "inventoryButton":
            if collection == "hotbarButton" or collection == "inventoryButton":
                self.allItemList[index], self.allItemList[self.tempIndex] = self.allItemList[self.tempIndex], self.allItemList[index]
            elif collection == "inputItemButton":
                self.inputItemSlot[index], self.allItemList[self.tempIndex] = self.allItemList[self.tempIndex], self.inputItemSlot[index]
            elif collection == "vesselButton":
                self.vesselItemSlot[index], self.allItemList[self.tempIndex] = self.allItemList[self.tempIndex], self.vesselItemSlot[index]
            elif collection == "resultButton":
                self.resultItemSlot[index], self.allItemList[self.tempIndex] = self.allItemList[self.tempIndex], self.resultItemSlot[index]
        elif self.tempGroup == "inputItemButton":
            if collection == "hotbarButton" or collection == "inventoryButton":
                self.allItemList[index], self.inputItemSlot[self.tempIndex] = self.inputItemSlot[self.tempIndex], self.allItemList[index]
            elif collection == "inputItemButton":
                self.inputItemSlot[index], self.inputItemSlot[self.tempIndex] = self.inputItemSlot[self.tempIndex], self.inputItemSlot[index]
            elif collection == "vesselButton":
                self.vesselItemSlot[index], self.inputItemSlot[self.tempIndex] = self.inputItemSlot[self.tempIndex], self.vesselItemSlot[index]
            elif collection == "resultButton":
                self.resultItemSlot[index], self.inputItemSlot[self.tempIndex] = self.inputItemSlot[self.tempIndex], self.resultItemSlot[index]
        elif self.tempGroup == "vesselButton":
            if collection == "hotbarButton" or collection == "inventoryButton":
                self.allItemList[index], self.vesselItemSlot[self.tempIndex] = self.vesselItemSlot[self.tempIndex], self.allItemList[index]
            elif collection == "inputItemButton":
                self.inputItemSlot[index], self.vesselItemSlot[self.tempIndex] = self.vesselItemSlot[self.tempIndex], self.inputItemSlot[index]
            elif collection == "resultButton":
                self.resultItemSlot[index], self.vesselItemSlot[self.tempIndex] = self.vesselItemSlot[self.tempIndex], self.resultItemSlot[index]
        elif self.tempGroup == "resultButton":
            if collection == "hotbarButton" or collection == "inventoryButton":
                self.allItemList[index], self.resultItemSlot[self.tempIndex] = self.resultItemSlot[self.tempIndex], self.allItemList[index]
            elif collection == "inputItemButton":
                self.inputItemSlot[index], self.resultItemSlot[self.tempIndex] = self.resultItemSlot[self.tempIndex], self.inputItemSlot[index]
            elif collection == "vesselButton":
                self.vesselItemSlot[index], self.resultItemSlot[self.tempIndex] = self.resultItemSlot[self.tempIndex], self.vesselItemSlot[index]

        for index in range(0, len(self.allItemList)):
            itemsDictMap[(clientApi.GetMinecraftEnum().ItemPosType.INVENTORY, index)] = self.allItemList[index]
        data = {
            "itemsDictMap": itemsDictMap,
            "playerId": playerId,
            "inputItemSlot": self.inputItemSlot,
            "vesselItemSlot": self.vesselItemSlot,
            "resultItemSlot": self.resultItemSlot,
            "previewItemSlot": self.previewItemSlot,
            "blockPos": self.blockPos,
            "dimensionId": self.dimensionId
        }
        CallServer("SetInventory", data)
        self.UpdateScreen(True)

    def SetSlotItem(self, button, count, flyItemName, itemDict):
        """
        设置槽位物品
        """
        itemName = itemDict["newItemName"]
        auxValue = itemDict["newAuxValue"]
        if itemDict["enchantData"]:
            isEnchanted = True
        else:
            isEnchanted = False
        if count == "1":
            count = ""
        itemRender = button.GetChildByName("item_renderer").asItemRenderer()
        countLabel = button.GetChildByName("stack_count_label").asLabel()
        button.GetChildByName("item_renderer").SetVisible(True)
        itemRender.SetUiItem(itemName, auxValue, isEnchanted, itemDict.get("userData", {}))
        countLabel.SetText(count)
        # 移动动画
        if flyItemName == "flyItem":
            slotGlobalPos = self.nowSelect.GetGlobalPosition()
            self.flyItem.asItemRenderer().SetUiItem(itemName, auxValue, isEnchanted, itemDict.get("userData", {}))
            toPos = self.SetGlobalPosition(ROOT_SCREEN + "/cooking_pot_bg/{}".format(flyItemName), slotGlobalPos)
            fromPos = self.SetGlobalPosition(ROOT_SCREEN + "/cooking_pot_bg/{}".format(flyItemName), button.GetGlobalPosition())
            self.flyAnimationPos = self.intermediates(toPos, fromPos)
        elif flyItemName == "flyItem2":
            self.flyItem2.asItemRenderer().SetUiItem(itemName, auxValue, isEnchanted, itemDict.get("userData", {}))
            self.flyAnimationPos2 = list(reversed(self.flyAnimationPos))

    def SetPreviewItemSlot(self, itemDict):
        previewControl = self.GetBaseUIControl(preview)
        if not itemDict:
            previewControl.GetChildByName("item_renderer").SetVisible(False)
            previewControl.GetChildByName("stack_count_label").asLabel().SetText("")
            return
        itemName = itemDict["newItemName"]
        auxValue = itemDict["newAuxValue"]
        count = itemDict["count"]
        itemRenderer = previewControl.GetChildByName("item_renderer").asItemRenderer()
        countLabel = previewControl.GetChildByName("stack_count_label").asLabel()
        if count == 1:
            count = ""
        countLabel.SetText(str(count))
        itemRenderer.SetVisible(True)
        itemRenderer.SetUiItem(itemName, auxValue, False, itemDict.get("userData", {}))
        self.previewItemSlot[0] = itemDict

    @ViewBinder.binding(ViewBinder.BF_ButtonClick)
    def clickSlotButton(self, args):
        touchEvent = args["TouchEvent"]
        buttonGroup = args["#collection_name"]
        index = args["#collection_index"]
        if buttonGroup == "inventoryButton":
            index += 9
        buttonPath = args["ButtonPath"][4:]
        self.touchButtonPath = buttonPath
        slotControl = self.GetBaseUIControl(buttonPath)
        itemRenderer = slotControl.GetChildByName("item_renderer")
        if self.nowSelect:
            itemLock = self.nowSelect.GetChildByName("item_lock_overlay")
            if itemLock.GetChildByName("cell_lock").GetVisible() is True:
                if buttonGroup not in ["hotbarButton", "inventoryButton"]:
                    return
        if slotControl and self.tempGroup:
            itemLock = slotControl.GetChildByName("item_lock_overlay")
            if itemLock.GetChildByName("cell_lock").GetVisible() is True:
                if self.tempGroup not in ["hotbarButton", "inventoryButton"]:
                    return
        if touchEvent == 0:
            if itemRenderer.GetVisible() is True:
                text = updateItemMessageShow(self.GetItemDict(buttonGroup, index))
                self.GetBaseUIControl(itemTips).asLabel().SetText(text)
                self.itemTips.resetAnimation()
                if self.nowSelect is None:
                    self.nowSelect = slotControl
                    self.nowSelect.GetChildByName("slot_select").SetVisible(True)
                    self.nowSelect.GetChildByName("cell_hint").SetVisible(True)
                else:
                    # 两个物品交换
                    newCount = slotControl.GetChildByName("stack_count_label").asLabel().GetText()
                    newItemDict = self.GetItemDict(buttonGroup, index)
                    count = self.nowSelect.GetChildByName("stack_count_label").asLabel().GetText()
                    itemDict = self.GetItemDict(self.tempGroup, self.tempIndex)
                    self.SetSlotItem(slotControl, count, "flyItem", itemDict)
                    self.SetSlotItem(self.nowSelect, newCount, "flyItem2", newItemDict)
                    self.ExchangeSlotItem(index, buttonGroup)
                    self.GetItemLocked(itemDict, slotControl)
                    self.GetItemLocked(newItemDict, self.nowSelect)
                    # 交换完成取消选中
                    self.nowSelect.GetChildByName("slot_select").SetVisible(False)
                    self.nowSelect.GetChildByName("cell_hint").SetVisible(False)
                    slotControl.GetChildByName("slot_select").SetVisible(False)
                    slotControl.GetChildByName("cell_hint").SetVisible(False)
                    self.nowSelect = None
            else:
                if self.nowSelect is not None:
                    self.nowSelect.GetChildByName("split_item").SetVisible(False)
                    # 物品移动到空格子
                    count = self.nowSelect.GetChildByName("stack_count_label").asLabel().GetText()
                    itemDict = self.GetItemDict(self.tempGroup, self.tempIndex)
                    self.SetSlotItem(slotControl, count, "flyItem", itemDict)
                    self.ExchangeSlotItem(index, buttonGroup)
                    self.GetItemLocked(itemDict, slotControl)
                    # 取消选中
                    itemLock = self.nowSelect.GetChildByName("item_lock_overlay")
                    itemLock.GetChildByName("cell_lock").SetVisible(False)
                    itemLock.GetChildByName("item_lock_yellow").SetVisible(False)
                    self.nowSelect.GetChildByName("item_renderer").SetVisible(False)
                    self.nowSelect.GetChildByName("stack_count_label").asLabel().SetText("")
                    self.nowSelect.GetChildByName("slot_select").SetVisible(False)
                    self.nowSelect.GetChildByName("cell_hint").SetVisible(False)
                    self.nowSelect = None
            self.tempIndex = index
            self.tempButton = slotControl
            self.tempGroup = buttonGroup

    @ViewBinder.binding_collection(ViewBinder.BF_BindInt, "hotbarButton", "#item_durability_total_amount")
    def hotbarTotalDurability(self, index):
        itemDict = self.allItemList[index]
        if itemDict:
            itemInfo = ClientComp.CreateItem(levelId).GetItemBasicInfo(itemDict.get("newItemName"), itemDict.get("newAuxValue"))
            maxDurability = itemInfo.get("maxDurability")
            if maxDurability:
                return maxDurability

    @ViewBinder.binding_collection(ViewBinder.BF_BindInt, "hotbarButton", "#item_durability_current_amount")
    def hotbarCurrentDurability(self, index):
        itemDict = self.allItemList[index]
        if itemDict:
            if itemDict.get("durability") != 0:
                return itemDict.get("durability")

    @ViewBinder.binding_collection(ViewBinder.BF_BindBool, "hotbarButton", "#item_durability_visible")
    def hotbarVisibleDurability(self, index):
        itemDict = self.allItemList[index]
        if itemDict:
            itemInfo = ClientComp.CreateItem(levelId).GetItemBasicInfo(itemDict.get("newItemName"), itemDict.get("newAuxValue"))
            maxDurability = itemInfo.get("maxDurability")
            durability = itemDict.get("durability")
            if durability is None:
                return False
            if durability != 0:
                if durability == maxDurability:
                    return False
                else:
                    return True
            else:
                return False

    @ViewBinder.binding_collection(ViewBinder.BF_BindInt, "inventoryButton", "#item_durability_total_amount")
    def inventoryTotalDurability(self, index):
        itemDict = self.allItemList[index + 9]
        if itemDict:
            itemInfo = ClientComp.CreateItem(levelId).GetItemBasicInfo(itemDict.get("newItemName"), itemDict.get("newAuxValue"))
            maxDurability = itemInfo.get("maxDurability")
            if maxDurability:
                return maxDurability

    @ViewBinder.binding_collection(ViewBinder.BF_BindInt, "inventoryButton", "#item_durability_current_amount")
    def inventoryCurrentDurability(self, index):
        itemDict = self.allItemList[index + 9]
        if itemDict:
            if itemDict.get("durability") != 0:
                return itemDict.get("durability")

    @ViewBinder.binding_collection(ViewBinder.BF_BindBool, "inventoryButton", "#item_durability_visible")
    def inventoryVisibleDurability(self, index):
        itemDict = self.allItemList[index + 9]
        if itemDict:
            itemInfo = ClientComp.CreateItem(levelId).GetItemBasicInfo(itemDict.get("newItemName"), itemDict.get("newAuxValue"))
            maxDurability = itemInfo.get("maxDurability")
            durability = itemDict.get("durability")
            if durability is None:
                return False
            if durability != 0:
                if durability == maxDurability:
                    return False
                else:
                    return True
            else:
                return False

    @ViewBinder.binding_collection(ViewBinder.BF_BindInt, "inputItemButton", "#item_durability_total_amount")
    def inputItemTotalDurability(self, index):
        itemDict = self.inputItemSlot[index]
        if itemDict:
            itemInfo = ClientComp.CreateItem(levelId).GetItemBasicInfo(itemDict.get("newItemName"), itemDict.get("newAuxValue"))
            maxDurability = itemInfo.get("maxDurability")
            if maxDurability:
                return maxDurability

    @ViewBinder.binding_collection(ViewBinder.BF_BindInt, "inputItemButton", "#item_durability_current_amount")
    def inputItemCurrentDurability(self, index):
        itemDict = self.inputItemSlot[index]
        if itemDict:
            if itemDict.get("durability") != 0:
                return itemDict.get("durability")

    @ViewBinder.binding_collection(ViewBinder.BF_BindBool, "inputItemButton", "#item_durability_visible")
    def inputItemVisibleDurability(self, index):
        itemDict = self.inputItemSlot[index]
        if itemDict:
            itemInfo = ClientComp.CreateItem(levelId).GetItemBasicInfo(itemDict.get("newItemName"), itemDict.get("newAuxValue"))
            maxDurability = itemInfo.get("maxDurability")
            durability = itemDict.get("durability")
            if durability is None:
                return False
            if durability != 0:
                if durability == maxDurability:
                    return False
                else:
                    return True
            else:
                return False

    @ViewBinder.binding_collection(ViewBinder.BF_BindInt, "food_recipe_book", "#recipe_book_total_items")
    def FoodRecipeBook(self, args):
        for index in range(0, len(self.RecipeList)):
            recipeDict = self.RecipeList[index]
            cookResult = recipeDict["CookResult"]
            foodRecipeButton = self.foodRecipe.GetChildByName("foodRecipe{}".format(index + 1))
            if foodRecipeButton:
                itemRenderer = foodRecipeButton.GetChildByName("item_renderer")
                itemRenderer.SetVisible(True)
                itemRenderer.asItemRenderer().SetUiItem(cookResult[0], cookResult[1])
        return len(self.RecipeList)

    @ViewBinder.binding(ViewBinder.BF_BindString, "#main.gametick")
    def GameTick(self):
        if self.flyAnimationPos:
            self.flyItem.SetVisible(True)
            pos = self.flyAnimationPos[0]
            self.flyItem.SetPosition(pos)
            del self.flyAnimationPos[0]
        else:
            self.flyItem.SetVisible(False)
        if self.flyAnimationPos2:
            self.flyItem2.SetVisible(True)
            pos = self.flyAnimationPos2[0]
            self.flyItem2.SetPosition(pos)
            del self.flyAnimationPos2[0]
        else:
            self.flyItem2.SetVisible(False)

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp)
    def ClickRecipeButton(self, args):
        index = args["#collection_index"]
        recipeDict = self.RecipeList[index]
        recipeList = recipeDict["Recipe"]
        recipeText = recipeDict["text"]
        self.foodRecipeList = recipeList
        self.foodRecipeIndex = 0
        if self.foodRecipeTimer:
            ClientComp.CreateGame(levelId).CancelTimer(self.foodRecipeTimer)
        self.foodRecipeTimer = ClientComp.CreateGame(levelId).AddRepeatedTimer(1.0, self.FoodRecipeTimerSwitch)

        recipe = self.foodRecipeList[self.foodRecipeIndex]
        for index in range(0, 6):
            recipeItem = self.GetBaseUIControl(cookRecipePanel + "/cook_recipe/grid/recipeItem{}".format(index + 1)).GetChildByName("item_renderer")
            recipeItem.SetVisible(False)
        for index in range(0, len(recipe)):
            recipeItem = self.GetBaseUIControl(cookRecipePanel + "/cook_recipe/grid/recipeItem{}".format(index + 1))
            itemRenderer = recipeItem.GetChildByName("item_renderer")
            itemRenderer.SetVisible(True)
            itemRenderer.asItemRenderer().SetUiItem(recipe[index][0], recipe[index][1])

        previewItem = self.GetBaseUIControl(cookRecipePanel + "/cook_recipe/preview/item/item_renderer")
        previewItem.asItemRenderer().SetUiItem(recipeDict["CookResult"][0], recipeDict["CookResult"][1])
        previewItem.SetVisible(True)
        vesselItem = self.GetBaseUIControl(cookRecipePanel + "/cook_recipe/vessel/item_renderer")
        vesselItem.asItemRenderer().SetUiItem(recipeDict["Vessel"][0], recipeDict["Vessel"][1])
        vesselItem.SetVisible(True)
        self.GetBaseUIControl(cookRecipePanel + "/food_title/title").asLabel().SetText(recipeText)

    @ViewBinder.binding(ViewBinder.BF_EditFinished)
    def EditBoxFinished(self, args):
        text = args["Text"]
        recipeList = []
        for index in range(0, len(CookingPotRecipeList)):
            recipeDict = CookingPotRecipeList[index]
            recipeText = recipeDict["text"]
            if text in recipeText:
                recipeList.append(recipeDict)
        self.RecipeList = recipeList
        self.UpdateScreen(True)

    def FoodRecipeTimerSwitch(self):
        if self.foodRecipeList:
            self.foodRecipeIndex += 1
            if self.foodRecipeIndex >= len(self.foodRecipeList):
                self.foodRecipeIndex = 0
            recipe = self.foodRecipeList[self.foodRecipeIndex]
            for index in range(0, len(recipe)):
                recipeItem = self.GetBaseUIControl(cookRecipePanel + "/cook_recipe/grid/recipeItem{}".format(index + 1))
                itemRenderer = recipeItem.GetChildByName("item_renderer")
                itemRenderer.SetVisible(True)
                itemRenderer.asItemRenderer().SetUiItem(recipe[index][0], recipe[index][1])
            for i in range(len(recipe), 6):
                recipeItem = self.GetBaseUIControl(cookRecipePanel + "/cook_recipe/grid/recipeItem{}".format(i + 1))
                itemRenderer = recipeItem.GetChildByName("item_renderer")
                itemRenderer.SetVisible(False)

    def CloseCrabTrap(self, args):
        clientApi.PopScreen()
        data = {"blockPos": self.blockPos, "dimensionId": self.dimensionId}
        CallServer("PlayerCloseCrabTrap", data)

    def SetArrowProgress(self, clip):
        arrowControl = self.GetBaseUIControl(arrow)
        if clip and arrowControl:
            progress = arrowControl.GetChildByName("progress")
            progress.asImage().SetSpriteClipRatio(clip / 10.0)

    def UpdateCookingPot(self, data):
        self.heatEnable = data["heatEnable"]
        self.inputItemSlot = data["inputItemSlot"]
        self.vesselItemSlot = data["vesselItemSlot"]
        self.resultItemSlot = data["resultItemSlot"]
        self.previewItemSlot = data["previewItemSlot"]
        self.GetInventoryGrid()
        self.SetPreviewItemSlot(self.previewItemSlot[0])
        self.UpdateScreen(True)
        data = {
            "playerId": playerId,
            "inputItemSlot": self.inputItemSlot,
            "vesselItemSlot": self.vesselItemSlot,
            "resultItemSlot": self.resultItemSlot,
            "previewItemSlot": self.previewItemSlot,
            "blockPos": self.blockPos,
            "dimensionId": self.dimensionId
        }
        CallServer("SetInventory", data)

    def Destroy(self):
        if self.foodRecipeTimer:
            ClientComp.CreateGame(levelId).CancelTimer(self.foodRecipeTimer)
