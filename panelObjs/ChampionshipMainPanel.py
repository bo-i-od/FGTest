from common.basePage import BasePage
from configs.elementsData import ElementsData


class ChampionshipMainPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.ChampionshipMainPanel.ChampionshipMainPanel)

    def click_btn_close(self):
        self.click_element(element_data=ElementsData.ChampionshipMainPanel.btn_close)



if __name__ == "__main__":
    bp = BasePage()

    ChampionshipMainPanel.click_btn_close(bp)

    bp.connect_close()