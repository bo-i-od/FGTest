from common.basePage import BasePage
from configs.elementsData import ElementsData

class FishingResultPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishingResultPanel.FishingResultPanel)

    def click_btn_confirm(self):
        self.click_element(element_data=ElementsData.FishingResultPanel.btn_confirm)

    def click_btn_confirm_safe(self):
        self.click_element_safe(element_data=ElementsData.FishingResultPanel.btn_confirm)

    def wait_for_result(self):
        while True:
            self.clear_popup()
            # if FlashCardReceivePanel.is_panel_active(self):
            #     self.sleep(6)
            #     img = self.get_full_screen_shot()
            #     self.save_img(img)
            #     self.clear_popup()
            #     self.cur += 1
            position_list = self.get_position_list(element_data_list=[ElementsData.FishingResultPanel.btn_confirm])
            if position_list[0]:
                return ElementsData.FishingResultPanel.btn_confirm
            # self.sleep(1)

    def settlement(self, element_btn):
        # f_flag = True
        while True:
            if not self.exist(element_data=element_btn):
                break
            # if f_flag:
            #     img = self.get_full_screen_shot()
            #     self.save_img(img)
            #     f_flag = False

            self.clear_popup()
            # self.sleep(1)
            if self.is_ray_input:
                self.ray_input(kind="click", element_data=element_btn)
                continue
            self.click_element_safe(element_data=element_btn)


    def get_fish_name(self):
        return self.get_text_list(element_data=ElementsData.FishingResultPanel.fish_name)

    def get_money(self):
        return self.get_text_list(element_data=ElementsData.FishingResultPanel.money)

    def get_digital(self):
        return self.get_text_list(element_data=ElementsData.FishingResultPanel.digital)

    def get_rank(self):
        return self.get_icon_list(element_data=ElementsData.FishingResultPanel.rank)

    def get_fish_class(self):
        return self.get_icon_list(element_data=ElementsData.FishingResultPanel.fish_class)


