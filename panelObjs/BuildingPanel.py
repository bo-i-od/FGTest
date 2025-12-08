from common.basePage import BasePage
from configs.elementsData import ElementsData


class BuildingPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BuildingPanel.BuildingPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.BuildingPanel.btn_close)

    def click_btn_close_safe(self):
        self.click_element_safe(element_data=ElementsData.BuildingPanel.btn_close)

    def click_building(self, index):
        position_list = self.get_position_list(element_data=ElementsData.BuildingPanel.building_list)
        self.click_position(position=position_list[index])

    def get_cost_value(self, index):
        cost_value_str = self.get_text_list(element_data=ElementsData.BuildingPanel.cost_value_list)[index]
        cost_value = self.convert_numeric_string(num_str=cost_value_str)
        return cost_value

    def get_progress_value_completed(self):
        progress_value = self.get_text(element_data=ElementsData.BuildingPanel.progress_value)
        progress_value_completed = progress_value.split('/')[0]
        progress_value_completed = int(progress_value_completed)
        return progress_value_completed

    def get_progress_value_all(self):
        progress_value = self.get_text(element_data=ElementsData.BuildingPanel.progress_value)
        progress_value_all = progress_value.split('/')[1]
        progress_value_all = int(progress_value_all)
        return progress_value_all
