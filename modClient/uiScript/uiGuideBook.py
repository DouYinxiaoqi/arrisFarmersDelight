# -*- coding: utf-8 -*-
from ..modCommon.guideBookConfig import config
import mod.client.extraClientApi as clientApi
import copy

ScreenNode = clientApi.GetScreenNodeCls()
playerId = clientApi.GetLocalPlayerId()
levelId = clientApi.GetLevelId()

ViewBinder = clientApi.GetViewBinderCls()
compFactory = clientApi.GetEngineCompFactory()

ROOT_PATH = "/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel"
TITLE_PATH = ROOT_PATH + "/stack_panel/content/title/text"
CONTENT = None
SELECTOR = None

class guideBook(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.pag = None # 当前选中的一级分页
        self.selectorToggle = None # 当前选中的二级分页按钮控件
        self.selectorControl = None # 二级内容页滑块控件
        self.contentControl = None # 内容页控件

    def Create(self):
        global CONTENT, SELECTOR
        inputModeId = compFactory.CreatePlayerView(levelId).GetToggleOption(clientApi.GetMinecraftEnum().OptionId.INPUT_MODE)
        if inputModeId == 0: # 键鼠操作
            SELECTOR = ROOT_PATH + "/stack_panel/scroll_view/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
            CONTENT = ROOT_PATH + "/stack_panel/content/scroll_view/scroll_mouse/scroll_view/stack_panel/background_and_viewport/scrolling_view_port/scrolling_content"
        elif inputModeId == 1: # 触摸屏操作
            SELECTOR = ROOT_PATH + "/stack_panel/scroll_view/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
            CONTENT = ROOT_PATH + "/stack_panel/content/scroll_view/scroll_touch/scroll_view/panel/background_and_viewport/scrolling_view_port/scrolling_content"
        self.selectorControl = self.GetBaseUIControl(SELECTOR)
        self.contentControl = self.GetBaseUIControl(CONTENT)

        buttonControl = self.GetBaseUIControl(ROOT_PATH + "/gb_bg/close").asButton()
        buttonControl.AddTouchEventParams()
        buttonControl.SetButtonTouchUpCallback(self.CloseGuideBookScreen)

    @ViewBinder.binding_collection(ViewBinder.BF_BindString, "selectorToggle", "#toggleLabel.text")
    def OnSelectorToggleText(self, index):
        if self.pag:
            return config[self.pag][index]["title"]

    @ViewBinder.binding_collection(ViewBinder.BF_BindString, "pagToggle", "#toggleLabel.text")
    def OnPagToggleText(self, index):
        if len(config) > index:
            pag = config.keys()
            return pag[index]

    @ViewBinder.binding(ViewBinder.BF_ToggleChanged, "#selectorToggleGroup")
    def OnSelectorChecked(self, args):
        toggleIndex = args["index"]
        if self.pag:
            self.GetBaseUIControl(ROOT_PATH + "/stack_panel/content").SetVisible(True)
            introduce = config[self.pag][toggleIndex]
            self.GetBaseUIControl(TITLE_PATH).asLabel().SetText(str(introduce.get("title")))
            itemName = introduce.get("namespace")
            aux = introduce.get("auxValue")
            content = introduce.get("content")
            itemRenderer = self.contentControl.GetChildByName("item_renderer")
            contentText = self.contentControl.GetChildByName("label")
            nameSpace = itemRenderer.GetChildByName("namespace")
            itemRenderer.asItemRenderer().SetUiItem(itemName, aux, False)
            nameSpace.asLabel().SetText(itemName)
            contentText.asLabel().SetText(content)

    @ViewBinder.binding(ViewBinder.BF_ToggleChanged, "#pagToggleGroup")
    def pagToggleChecked(self, args):
        if args["state"] is True:
            self.GetBaseUIControl(ROOT_PATH + "/stack_panel/content").SetVisible(False)
            pag = config.keys()
            index = args["index"]
            self.pag = pag[index]
            self.selectorControl.SetVisible(True)

    @ViewBinder.binding(ViewBinder.BF_BindInt, "#pagToggleGrid.item_count")
    def OnPagToggleGridResize(self):
        return len(config)

    @ViewBinder.binding(ViewBinder.BF_BindInt, "#selectorToggleGrid.item_count")
    def OnSelectorToggleGridResize(self):
        if self.pag:
            return len(config[self.pag])

    def CloseGuideBookScreen(self, args):
        # 退出教程书界面
        clientApi.PopScreen()
