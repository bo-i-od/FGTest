from common.basePage import BasePage
from configs.elementsData import ElementsData
from panelObjs.FishingResultPanel import FishingResultPanel


class FishingPanel(BasePage):
    def is_panel_active(self):
        return self.exist(element_data=ElementsData.FishingPanel.FishingPanel)

    def reel_quick(self):
        while not FishingResultPanel.is_panel_active(self):
            self.clear_popup()
            cmd = """if _G.GMDoKillFish ~= nil then
    local success, result = pcall(_G.GMDoKillFish)
    if not success then
        print("GMDoKillFish call failed:", result)
    end
else
    print("GMDoKillFish not available")
end
"""
            # 国内
            self.lua_console(command=cmd)
            # # 海外
            # self.lua_console(command="GameRoot:GetFishingMatch().fsm:NotifyEvent(FishingMatch_FSM_EVENT.AIRTEST_G)")
            self.sleep(0.5)


    def qte(self):
        element_data_list = [
            ElementsData.FishingResultPanel.btn_confirm,
        ]
        btn_confirm_index = element_data_list.index(ElementsData.FishingResultPanel.btn_confirm)
        while True:
            object_id_list = self.get_object_id_list(element_data_list=element_data_list)
            if object_id_list[btn_confirm_index]:
                FishingResultPanel.settlement(self, element_btn=ElementsData.FishingResultPanel.btn_confirm)
                break