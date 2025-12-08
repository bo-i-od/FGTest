import random

from common.basePage import BasePage
from configs.elementsData import ElementsData


class BuildingDestroyPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BuildingDestroyPanel.BuildingDestroyPanel)

    class panel_choose(BasePage):
        def click_crosshair(self, index=None):
            position_list = self.get_position_list(element_data=ElementsData.BuildingDestroyPanel.panel_choose.crosshair_list)
            if index is None:
                index = random.randint(0, len(position_list) - 1)

            self.click_position(position_list[index])

    class panel_reward(BasePage):
        def click_btn_confirm(self):
            self.click_element(element_data=ElementsData.BuildingDestroyPanel.panel_reward.btn_confirm)

        def click_btn_confirm_safe(self):
            self.click_element_safe(element_data=ElementsData.BuildingDestroyPanel.panel_reward.btn_confirm)


