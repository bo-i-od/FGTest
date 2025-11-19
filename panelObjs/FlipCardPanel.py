import random

from common.basePage import BasePage
from configs.elementsData import ElementsData

class FlipCardPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FlipCardPanel.FlipCardPanel)

    def get_multiples(self):
        multiples = self.get_text(element_data=ElementsData.FlipCardPanel.text_multiples)
        return int(multiples)

    def get_cost(self):
        cost = self.get_text(element_data=ElementsData.FlipCardPanel.text_cost)
        return int(cost)

    def get_own(self):
        own = self.get_text(element_data=ElementsData.FlipCardPanel.text_own)
        return int(own)

    def get_bout(self):
        bout = self.get_text(element_data=ElementsData.FlipCardPanel.text_bout)
        return int(bout)

    def is_panel_card_active(self):
        return self.exist(element_data=ElementsData.FlipCardPanel.panel_card)

    def click_btn_go(self):
        if self.is_ray_input:
            self.ray_input(element_data=ElementsData.FlipCardPanel.btn_go, kind="click")
            return
        self.click_element(element_data=ElementsData.FlipCardPanel.btn_go)

    def click_card(self, index=None):
        object_id_list = self.get_object_id_list(element_data=ElementsData.FlipCardPanel.card_list)
        if index is None:
            index = random.randint(0, len(object_id_list) - 1)
        object_id = object_id_list[index]
        if self.is_ray_input:
            self.ray_input(object_id=object_id, kind="click")
            return
        self.click_element(object_id=object_id)

    def click_go_or_card(self):
        object_id_list = self.get_object_id_list(element_data_list=[ElementsData.FlipCardPanel.card_list, ElementsData.FlipCardPanel.btn_go])
        if object_id_list[0]:
            index = random.randint(0, len(object_id_list) - 1)
            object_id = object_id_list[0][index]
        elif object_id_list[1]:
            object_id = object_id_list[1][0]
        else:
            return
        if self.is_ray_input:
            self.ray_input(object_id=object_id, kind="click")
            return
        self.click_element(object_id=object_id)



    def wait_for_disappear_panel_card(self, timeout=3):
        cur = 0
        while True:
            sleep_time = 0.5
            cur += sleep_time
            self.sleep(sleep_time)
            if cur > timeout:
                break
            if not self.exist(element_data=ElementsData.FlipCardPanel.panel_card):
                break

    def wait_for_appear_panel_card(self, timeout=3):
        self.wait_for_appear(element_data=ElementsData.FlipCardPanel.panel_card, interval=0.5,timeout=timeout)



if __name__ == "__main__":
    bp = BasePage()
    # FlipCardPanel.click_btn_go(bp)
    # 加代币
    bp.cmd("add 1 100100 100")
    bp.sleep(1)
    # 开建造界面
    bp.lua_console('PanelMgr:OpenPanel("BuildingPanel")')
    bp.sleep(1)
    # 关建造界面
    bp.lua_console('PanelMgr:ClosePanel("BuildingPanel")')
    bp.sleep(1)
    # 关奖励界面
    bp.lua_console('PanelMgr:ClosePanel("GetCommonRewardsPanel")')

    # print(a)


    bp.connect_close()