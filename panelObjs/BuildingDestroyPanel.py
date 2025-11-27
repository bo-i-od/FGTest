import random

from common.basePage import BasePage
from configs.elementsData import ElementsData

class BuildingDestroyPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BuildingDestroyPanel.BuildingDestroyPanel)

    def is_panel_choose_active(self):
        return self.exist(element_data=ElementsData.BuildingDestroyPanel.Choose.panel_choose)

    def click_btn_switch(self):
        self.click_element_safe(element_data=ElementsData.BuildingDestroyPanel.Choose.btn_confirm)

    def get_opponent_name(self):
        return self.get_text(element_data=ElementsData.BuildingDestroyPanel.Choose.opponent_name)

    def get_multiple(self):
        multiple = self.get_text(element_data=ElementsData.BuildingDestroyPanel.Choose.multiple)
        multiple = multiple.replace("×",'')
        int(multiple)
        return multiple

    def click_crosshair(self):
        self.click_element_safe(element_data=ElementsData.BuildingDestroyPanel.Choose.crosshair)

    def is_panel_reward_active(self):
        return self.exist(element_data=ElementsData.BuildingDestroyPanel.Reward.panel_reward)

    def get_money_value(self):
        money_value = self.convert_numeric_string(element_data=ElementsData.BuildingDestroyPanel.Reward.money_value)
        return money_value

    def get_opponent_reward_name(self):
        return self.get_text(element_data=ElementsData.BuildingDestroyPanel.Reward.opponent_name)

    def click_reward_btn_confirm(self):
        self.click_element_safe(element_data=ElementsData.BuildingDestroyPanel.Reward.btn_confirm)

    def is_panel_change_active(self):
        return self.exist(element_data=ElementsData.BuildingDestroyPanel.Change.panel_change)

    def click_btn_close(self):
        self.click_element_safe(element_data=ElementsData.BuildingDestroyPanel.Change.btn_close)

    def click_btn_revenge(self):
        self.click_element_safe(element_data=ElementsData.BuildingDestroyPanel.Change.btn_revenge)

    def click_btn_friend(self):
        self.click_element_safe(element_data=ElementsData.BuildingDestroyPanel.Change.btn_friend)

    def click_btn_go(self):
        self.click_element_safe(element_data=ElementsData.BuildingDestroyPanel.Change.btn_go_list)






if __name__ == "__main__":
    bp = BasePage()
    # multiple = BuildingDestroyPanel.get_multiple(bp)
    # print(multiple)
    # BuildingDestroyPanel.click_crosshair(bp)
    # money =BuildingDestroyPanel.get_money_value(bp)
    # print(money)
    # BuildingDestroyPanel.click_reward_btn_confirm(bp)
