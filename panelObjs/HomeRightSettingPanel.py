from common.basePage import BasePage
from configs.elementsData import ElementsData


class HomeRightSettingPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.HomeRightSettingPanel.HomeRightSettingPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.HomeRightSettingPanel.btn_close)

    def click_head(self):
        self.click_element(element_data=ElementsData.HomeRightSettingPanel.head)

    def click_name(self):
        self.click_element(element_data=ElementsData.HomeRightSettingPanel.name)

    def click_btn_fortune_hall(self):
        self.click_element(element_data=ElementsData.HomeRightSettingPanel.btn_fortune_hall)

    def click_btn_my_showroom(self):
        self.click_element(element_data=ElementsData.HomeRightSettingPanel.btn_my_showroom)

    def click_btn_map(self):
        self.click_element(element_data=ElementsData.HomeRightSettingPanel.btn_map)

    def click_btn_board_report(self):
        self.click_element(element_data=ElementsData.HomeRightSettingPanel.btn_board_report)

    def click_btn_settings(self):
        self.click_element(element_data=ElementsData.HomeRightSettingPanel.btn_settings)

    def click_btn_facebook(self):
        self.click_element(element_data=ElementsData.HomeRightSettingPanel.btn_facebook)



if __name__ == "__main__":
    bp = BasePage()

    # HomeRightSettingPanel.click_head(bp)

    # HomeRightSettingPanel.click_name(bp)

    # HomeRightSettingPanel.click_btn_fortune_hall(bp)

    HomeRightSettingPanel.click_btn_close(bp)

    bp.connect_close()