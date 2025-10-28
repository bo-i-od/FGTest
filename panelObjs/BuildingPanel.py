from common.basePage import BasePage
from configs.elementsData import ElementsData


class BuildingPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.BuildingPanel.BuildingPanel)

    def click_building_1(self):
        self.click_element_safe(element_data=ElementsData.BuildingPanel.building_1)

    def click_building_2(self):
        self.click_element_safe(element_data=ElementsData.BuildingPanel.building_2)

    def click_building_3(self):
        self.click_element_safe(element_data=ElementsData.BuildingPanel.building_3)

    def click_building_4(self):
        self.click_element_safe(element_data=ElementsData.BuildingPanel.building_4)

    def click_building_5(self):
        self.click_element_safe(element_data=ElementsData.BuildingPanel.building_5)

    def get_cost1_value(self):
        cost1_value = self.convert_numeric_string(element_data=ElementsData.BuildingPanel.cost1_value)
        return cost1_value

    def get_cost2_value(self):
        cost2_value = self.convert_numeric_string(element_data=ElementsData.BuildingPanel.cost2_value)
        return cost2_value

    def get_cost3_value(self):
        cost3_value = self.convert_numeric_string(element_data=ElementsData.BuildingPanel.cost3_value)
        return cost3_value

    def get_cost4_value(self):
        cost4_value = self.convert_numeric_string(element_data=ElementsData.BuildingPanel.cost4_value)
        return cost4_value

    def get_cost5_value(self):
        cost5_value = self.convert_numeric_string(element_data=ElementsData.BuildingPanel.cost5_value)
        return cost5_value

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
