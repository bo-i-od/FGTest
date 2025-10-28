from common.basePage import BasePage
from configs.elementsData import ElementsData


class ResourceBarPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ResourcesBarPanel.ResourcesBarPanel)

    def get_money_value(self):
        money_value = self.convert_numeric_string(element_data=ElementsData.ResourcesBarPanel.money_value)
        return money_value

    def get_player_exp_value(self):
        player_exp_value = self.convert_numeric_string(element_data=ElementsData.ResourcesBarPanel.player_exp_value)
        return player_exp_value

    def click_btn_menu(self):
        self.click_element_safe(element_data=ElementsData.ResourcesBarPanel.btn_menu)

    def get_shield_total_num(self):
        # 盾牌总数
        shield_total_num_list = self.get_object_id_list(element_data=ElementsData.ResourcesBarPanel.shield_total)
        shield_total_num = len(shield_total_num_list)
        return shield_total_num

    def get_shield_num(self):
        # 生效的盾牌总数
        shield_num_list = self.get_object_id_list(element_data=ElementsData.ResourcesBarPanel.shield)
        shield_num = len(shield_num_list)
        return shield_num