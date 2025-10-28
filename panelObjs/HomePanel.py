from common.basePage import BasePage
from configs.elementsData import ElementsData

class HomePanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.HomePanel.HomePanel)

    def click_btn_start(self):
        self.click_element_safe(element_data=ElementsData.HomePanel.btn_start)

    def get_dice_value_own(self):
        dice_value = self.get_text(element_data=ElementsData.HomePanel.dice_value)
        dice_value_own = dice_value.split('/')[0]
        dice_value_own = int(dice_value_own)
        return dice_value_own

    def get_dice_value_max(self):
        dice_value = self.get_text(element_data=ElementsData.HomePanel.dice_value)
        dice_value_max = dice_value.split('/')[1]
        dice_value_max = int(dice_value_max)
        return dice_value_max

    def click_btn_multiple(self):
        self.click_element_safe(element_data=ElementsData.HomePanel.btn_multiple)

    def get_multiple_value(self):
        multiple_value = self.get_text(element_data=ElementsData.HomePanel.multiple_value)
        multiple_value = multiple_value.split('×')[1]
        multiple_value = int(multiple_value)
        return multiple_value

    def click_btn_fishing(self):
        self.click_element_safe(element_data=ElementsData.HomePanel.btn_fishing)

    def click_btn_building(self):
        self.click_element_safe(element_data=ElementsData.HomePanel.btn_building)

    def click_btn_cards(self):
        self.click_element_safe(element_data=ElementsData.HomePanel.btn_cards)

    def click_btn_friends(self):
        self.click_element_safe(element_data=ElementsData.HomePanel.btn_friends)

    def click_btn_shop(self):
        self.click_element_safe(element_data=ElementsData.HomePanel.btn_shop)

    def click_btn_bank(self):
        self.click_element_safe(element_data=ElementsData.HomePanel.btn_bank)

    def get_right_name(self):
        right_name = self.get_text(element_data=ElementsData.HomePanel.right_name)
        return right_name

    def get_money_value(self):
        money_value = self.convert_numeric_string(element_data=ElementsData.HomePanel.money_value)
        return money_value

    def get_right_multiple_value(self):
        right_multiple_value = self.get_text(element_data=ElementsData.HomePanel.right_multiple)
        return right_multiple_value

    def click_btn_tournaments(self):
        self.click_element_safe(element_data=ElementsData.HomePanel.btn_tournaments)

    def get_tournaments_time(self):
        tournaments_time = self.get_text(element_data=ElementsData.HomePanel.tournaments_time)
        return tournaments_time

    def get_ranking_value(self):
        ranking_value = self.get_text(element_data=ElementsData.HomePanel.ranking_value)
        ranking_value = int(ranking_value)
        return ranking_value

    def get_progress_value(self):
        progress_value = self.get_text(element_data=ElementsData.HomePanel.progress_value)
        progress_value = int(progress_value)
        return progress_value

    def get_progress_value_max(self):
        progress_value_max = self.get_text(element_data=ElementsData.HomePanel.progress_value_max)
        progress_value_max =progress_value_max.split('/')[1]
        progress_value_max = int(progress_value_max)
        return progress_value_max

    def get_reward_value(self):
        reward_value = self.get_text(element_data=ElementsData.HomePanel.reward_value)
        return reward_value

    def get_progress_time(self):
        progress_time = self.get_text(element_data=ElementsData.HomePanel.progress_time)
        return progress_time

if __name__ == "__main__":
    bp = BasePage()

    print(HomePanel.get_dice_value_max(bp))