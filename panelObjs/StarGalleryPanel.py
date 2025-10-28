from common.basePage import BasePage
from configs.elementsData import ElementsData

class StarGGalleryPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.StarGalleryPanel.StarGalleryPanel)

    def click_btn_close(self):
        return self.click_element_safe(element_data=ElementsData.StarGalleryPanel.btn_close)

