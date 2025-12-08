import random

from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.BankHeistPanel import BankHeistPanel


class Panel_steal(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.Panel_steal.Panel_steal)


    def click_btn_click(self, index=None):
        position_list = self.get_position_list(element_data=ElementsData.Panel_steal.btn_click_list)
        if index is None:
            index = random.randint(0, len(position_list) - 1)
        self.click_position(position_list[index])

    def steal(self):
        while True:
            if BankHeistPanel.is_panel_active(self):
                break
            Panel_steal.click_btn_click(self)
            self.sleep(0.1)



if __name__ == "__main__":
    bp = BasePage()
    Panel_steal.steal(bp)
    bp.connect_close()