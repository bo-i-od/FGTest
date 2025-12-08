from common.basePage import BasePage
from configs.elementsData import ElementsData

class FishingResultSundriesPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishingResultSundriesPanel.FishingResultSundriesPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.FishingResultSundriesPanel.btn_close)

    def click_btn_close_safe(self):
        self.click_element_safe(element_data=ElementsData.FishingResultSundriesPanel.btn_close)