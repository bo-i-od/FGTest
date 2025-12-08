from common.basePage import BasePage
from configs.elementsData import ElementsData
from configs.jumpData import JumpData
from panelObjs.BankHeistPanel import BankHeistPanel
from panelObjs.BuildingDestroyPanel import BuildingDestroyPanel
from panelObjs.BuildingPanel import BuildingPanel
from panelObjs.FishingPreparePanel import FishingPreparePanel
from panelObjs.FishingResultPanel import FishingResultPanel
from panelObjs.FishingResultSundriesPanel import FishingResultSundriesPanel
from panelObjs.HomePanel import HomePanel
from panelObjs.Panel_steal import Panel_steal


# def fish_once(bp: BasePage):
#     FishingPreparePanel.click_btn_cast(bp)
#     bp.custom_cmd("autofish")
#     while True:
#         bp.clear_popup()
#         position_list = bp.get_position_list(element_data_list=[ElementsData.FishingResultPanel.btn_confirm])
#         if position_list[0]:
#             element_btn = ElementsData.FishingResultPanel.btn_confirm
#             break
#
    # FishingResultPanel.settlement(bp, element_btn=element_btn)




def execute_close(bp: BasePage, close_path):
    for close in close_path:
        if "click_element" in close:
            print(f'尝试关闭引导{close["click_element"]}')
            bp.click_element_safe(element_data=close["click_element"])
            continue
        if "execute" in close:
            print(f'执行{close["execute"]}')
            close_func(bp=bp, close_func_name=close["execute"])


def close_nbg(bp: BasePage, nbg_list, element_data_nbg_list):
    # 关闭引导
    position_list = bp.get_position_list(element_data_list=element_data_nbg_list)
    cur = 0
    while cur < len(position_list):
        if not position_list[cur]:
            cur += 1
            continue
        if "close_path" not in nbg_list[cur]:
            cur += 1
            continue

        execute_close(bp=bp, close_path=nbg_list[cur]["close_path"])
        return True
    return False




def close_func(bp: BasePage, close_func_name):
    if close_func_name == "ult":
        lua_code = """local sceneMgr = GameRoot:GetSceneMgr()
---@type SceneStateFishery
local state = sceneMgr:GetCurrentState()
local fishingMatch = state:GetFishingMatch()
BATTLE_PLAYER_ACTIVE_SKILL = {
    ULT = BCN._1,
    COMMON_ATTACK = BCN._2,
    BATTLE_SKILL_1 = BCN._3, -- 策划配置预留槽位1
    DEFAULT = BCN._4 -- 这个一定是最后一个数字，自动添加的主动技能会从这个开始计数
}
fishingMatch:TriggerActiveSkill(BATTLE_PLAYER_ACTIVE_SKILL.ULT)
"""
        bp.lua_console(command=lua_code)
        return

    if close_func_name == "sleep":
        bp.sleep(1)
        return

    if close_func_name == "autofish":
        bp.custom_cmd("autofish")
        return


def main():
    bp = BasePage(is_mobile_device=True, serial_number="127.0.0.1:21513")
    bp.is_ray_input = False
    element_data_nbg_list = []
    for nbg in JumpData.nbg_list:
        element_data_nbg_list.append(nbg["element_data"])

    element_data_list = [
        ElementsData.FishingPreparePanel.btn_cast,
        ElementsData.FishingResultPanel.btn_confirm,
        ElementsData.FishingResultSundriesPanel.btn_close,
        ElementsData.HomePanel.navbar.btn_start,
        ElementsData.HomePanel.navbar.btn_start_disabled,
        ElementsData.BuildingDestroyPanel.panel_choose.crosshair_list,
        ElementsData.BuildingDestroyPanel.panel_reward.btn_confirm,
        ElementsData.Panel_steal.btn_click_list,
        ElementsData.BankHeistPanel.btn_confirm,
        ElementsData.BuildingPanel.btn_close,

    ]
    FishingPreparePanel_btn_cast_index = element_data_list.index(ElementsData.FishingPreparePanel.btn_cast)
    FishingResultPanel_btn_confirm_index = element_data_list.index(ElementsData.FishingResultPanel.btn_confirm)
    FishingResultSundriesPanel_btn_close_index = element_data_list.index(ElementsData.FishingResultSundriesPanel.btn_close)
    HomePanel_btn_start_index = element_data_list.index(ElementsData.HomePanel.navbar.btn_start)
    HomePanel_btn_start_disabled_index= element_data_list.index(ElementsData.HomePanel.navbar.btn_start_disabled)
    crosshair_list_index = element_data_list.index( ElementsData.BuildingDestroyPanel.panel_choose.crosshair_list)
    BuildingDestroyPanel_btn_confirm = element_data_list.index( ElementsData.BuildingDestroyPanel.panel_reward.btn_confirm)
    btn_click_list_index = element_data_list.index(ElementsData.Panel_steal.btn_click_list)
    BankHeistPanel_btn_confirm_index = element_data_list.index(ElementsData.BankHeistPanel.btn_confirm)
    BuildingPanel_btn_close_index = element_data_list.index(ElementsData.BuildingPanel.btn_close)
    while True:
        bp.clear_popup()
        is_nbg_closed = close_nbg(bp=bp, nbg_list=JumpData.nbg_list, element_data_nbg_list=element_data_nbg_list)
        if is_nbg_closed:
            bp.sleep(1)
            continue

        object_id_list = bp.get_object_id_list(element_data_list=element_data_list)

        if object_id_list[FishingPreparePanel_btn_cast_index]:
            print(f'点击抛竿')
            FishingPreparePanel.click_btn_cast_safe(bp)
            bp.sleep(1)
            print(f'开始自动钓鱼')
            bp.custom_cmd("autofish")

        if object_id_list[FishingResultPanel_btn_confirm_index]:
            print(f'尝试点击FishingResultPanel的btn_confirm')
            FishingResultPanel.click_btn_confirm_safe(bp)
            bp.sleep(1)

        if object_id_list[FishingResultSundriesPanel_btn_close_index]:
            print(f'点击FishingResultSundriesPanel的btn_close')
            FishingResultSundriesPanel.click_btn_close_safe(bp)
            bp.sleep(1)

        if object_id_list[HomePanel_btn_start_index] and not object_id_list[HomePanel_btn_start_disabled_index]:
            print(f'点击btn_start')
            HomePanel.navbar.click_btn_start(bp)
            bp.sleep(1)

        if object_id_list[crosshair_list_index]:
            print(f'点击crosshair')
            BuildingDestroyPanel.panel_choose.click_crosshair(bp)
            bp.sleep(1)

        if object_id_list[BuildingDestroyPanel_btn_confirm]:
            print(f'尝试点击BuildingDestroyPanel的btn_confirm')
            BuildingDestroyPanel.panel_reward.click_btn_confirm_safe(bp)
            bp.sleep(1)

        if object_id_list[btn_click_list_index]:
            print(f'点击btn_click')
            Panel_steal.click_btn_click(bp)
            bp.sleep(1)

        if object_id_list[BankHeistPanel_btn_confirm_index]:
            print(f'尝试点击BankHeistPanel的btn_confirm')
            BankHeistPanel.click_btn_confirm_safe(bp)
            bp.sleep(1)

        if object_id_list[BuildingPanel_btn_close_index]:
            print(f'点击BuildingPanel的btn_close')
            BuildingPanel.click_btn_close_safe(bp)
            bp.sleep(1)





if __name__ == '__main__':
    main()

