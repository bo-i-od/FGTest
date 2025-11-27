from common.basePage import BasePage
from configs.elementsData import ElementsData

class HomeRightSettingPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.HomeRightSettingPanel.HomeRightSettingPanel)

    def click_head_mask(self):
        self.click_element_safe(element_data=ElementsData.HomeRightSettingPanel.head_mask)

    def click_fortune_hall(self):
        self.click_element_safe(element_data=ElementsData.HomeRightSettingPanel.fortune_hall)

    def click_map(self):
        self.click_element_safe(element_data=ElementsData.HomeRightSettingPanel.map)

    def click_board_report(self):
        self.click_element_safe(element_data=ElementsData.HomeRightSettingPanel.board_report)

    def click_setting(self):
        self.click_element_safe(element_data=ElementsData.HomeRightSettingPanel.setting)

    def click_btn_facebook(self):
        self.click_element_safe(element_data=ElementsData.HomeRightSettingPanel.btn_facebook)

    def click_btn_close(self):
        self.click_element_safe(element_data=ElementsData.HomeRightSettingPanel.btn_close)

    def get_name_text(self):
        return self.get_text(element_data=ElementsData.HomeRightSettingPanel.name)