from common.basePage import BasePage
from configs.elementsData import ElementsData

class BuildingCompletePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BuildingCompletePanel.BuildingCompletePanel)

    def click_btn_go(self):
        self.click_element_safe(element_data=ElementsData.BuildingCompletePanel.btn_go)