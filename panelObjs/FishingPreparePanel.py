from common.basePage import BasePage
from configs.elementsData import ElementsData

class FishingPreparePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishingPreparePanel.FishingPreparePanel)

    def click_btn_cast(self):
        element_data_list = [ElementsData.FishingPreparePanel.btn_cast]
        position_list = self.wait_for_appear(element_data_list=element_data_list, is_click=False)
        cur = 0
        while cur < len(position_list):
            position = position_list[cur]
            # print(position)
            if not position:
                cur += 1
                continue
            element_data = element_data_list[cur]
            print(self.is_ray_input)
            if self.is_ray_input:
                self.ray_input(kind="click", element_data=element_data)

            else:
                self.click_element(element_data=element_data)
            self.sleep(1)
            if self.exist(element_data=ElementsData.FishingPanel.FishingPanel):
                return
            cur += 1
        FishingPreparePanel.click_btn_cast(self)