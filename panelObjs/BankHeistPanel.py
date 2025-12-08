from common.basePage import BasePage
from configs.elementsData import ElementsData


class BankHeistPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BankHeistPanel.BankHeistPanel)


    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.BankHeistPanel.btn_confirm)


    def click_btn_confirm_safe(self):
        self.click_element_safe(element_data=ElementsData.BankHeistPanel.btn_confirm)