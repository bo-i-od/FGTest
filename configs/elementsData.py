class ElementsData:
    Panels = {"locator": "UICanvas>>"}
    Panels_Default = {"locator": "UICanvas>Default>"}

    class ActivityBuffCashBoostPanel:
        ActivityBuffCashBoostPanel = {"locator": "UICanvas>Default>ActivityBuffCashBoostPanel"}
        btn_close = {"locator": "UICanvas>Default>ActivityBuffCashBoostPanel>panel>btn_close"}
        btn_continue = {"locator": "UICanvas>Default>ActivityBuffCashBoostPanel>panel>btn_continue"}

    class ActivityBuffBuildersBashPanel:
        ActivityBuffCashBoostPanel = {"locator": "UICanvas>Default>ActivityBuffCashBoostPanel"}
        btn_close = {"locator": "UICanvas>Default>ActivityBuffCashBoostPanel>panel>btn_close"}
        btn_continue = {"locator": "UICanvas>Default>ActivityBuffCashBoostPanel>panel>btn_continue"}

    class BaitShopPanel:
        BuildingPanel = {"locator": "UICanvas>Default>BaitShopPanel"}
        btn_close = {"locator": "UICanvas>Default>BaitShopPanel>panel>btn_close"}
        btn_i = {"locator": "UICanvas>Default>BaitShopPanel>panel>rules>rule_2>btn_i"}


    class BankHeistPanel:
        BankHeistPanel = {"locator": "UICanvas>Default>BankHeistPanel"}
        btn_confirm = {"locator": "UICanvas>Default>BankHeistPanel>panel_popups>panel_bottom>btn_confirm"}

    class BuildingPanel:
        BuildingPanel = {"locator": "UICanvas>Default>BuildingPanel"}
        building_list = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>"}
        cost_value_list = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>>cost>value"}
        progress_value = {"locator": "UICanvas>Default>BuildingPanel>panel>panel_bottom>value"}
        btn_close = {"locator": "UICanvas>Default>BuildingPanel>panel>panel_bottom>btn_close"}


    class BuildingCityListPanel:
        BuildingCityListPanel = {"locator": "UICanvas>Default>BuildingCityListPanel"}
        btn_close = {"locator": "UICanvas>Default>BuildingCityListPanel>panel>panel_bottom>btn_close"}
        Viewport = {"locator": "UICanvas>Default>BuildingCityListPanel>panel>city_list>Viewport"}
        btn_go_list = {"locator": "UICanvas>Default>BuildingCityListPanel>panel>city_list>Viewport>Content>>btn_go"}

    class BuildingCityPanel:
        BuildingCityPanel = {"locator": "UICanvas>Default>BuildingCityPanel"}
        btn_close = {"locator": "UICanvas>Default>BuildingCityPanel>panel>panel_bottom>btn_close"}
        btn_arrow_right = {"locator": "UICanvas>Default>BuildingCityPanel>panel>panel_bottom>btn_arrow_right"}
        btn_arrow_left = {"locator": "UICanvas>Default>BuildingCityPanel>panel>panel_bottom>btn_arrow_left"}


    class BuildingCompletePanel:
        BuildingCompletePanel = {"locator": "UICanvas>Default>BuildingCompletePanel"}
        btn_go = {"locator": "UICanvas>Default>BuildingCompletePanel>panel>down>btn_go"}

    class BuildingDestroyPanel:
        BuildingDestroyPanel = {"locator": "UICanvas>Default>BuildingDestroyPanel"}

        class panel_choose:
            btn_confirm = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>panel_bottom>btn_confirm"}
            opponent_head_mask = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>opponent_Info>head>head_mask>head_img"}
            opponent_name = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>opponent_Info>name"}
            multiple = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>opponent_Info>multiple>multiples_modle>text"}
            crosshair_list = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>Crosshair>>crosshair"}

        class panel_change:
            panel_change = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change"}
            btn_close = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change>panel_bottom>btn_close>icon"}
            btn_revenge = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change>panel_list>tab>1>text"}
            btn_friend = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change>panel_list>tab>2>text"}
            btn_go = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change>panel_list>list>Viewport>Content>1>list_item_model>panel_revenge>btn_go"}

        class panel_reward:
            panel_reward = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward"}
            money_value = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward>reward>money>value"}
            opponent_head_mask = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward>opponent_Info>head>head_mask>head_img"}
            opponent_name = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward>opponent_Info>name"}
            btn_confirm = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward>panel_bottom>btn_confirm"}

    class ChampionshipMainPanel:
        ChampionshipMainPanel = {"locator": "UICanvas>Default>ChampionshipMainPanel"}
        btn_close = {"locator": "UICanvas>Default>ChampionshipMainPanel>activity_popup_201>btn_close"}
        btn_receive = {"locator": "UICanvas>Default>ChampionshipMainPanel>activity_popup_201>panel>btn_receive"}
        btn_tips = {"locator": "UICanvas>Default>ChampionshipMainPanel>activity_popup_201>panel>btn_tips"}
        btn_ranking = {"locator": "UICanvas>Default>ChampionshipMainPanel>activity_popup_201>panel>btn_ranking"}
        icon_cost = {"locator": "UICanvas>Default>ChampionshipMainPanel>activity_popup_201>panel>progress>icon_cost"}

    class ChampionshipRulesPopupPanel:
        ChampionshipRulesPopupPanel = {"locator": "UICanvas>Default>ChampionshipRulesPopupPanel"}
        btn_close = {"locator": "UICanvas>Default>ChampionshipRulesPopupPanel>btn_close"}

    class ChampionshipSeasonRankPanel:
        ChampionshipSeasonRankPanel = {"locator": "UICanvas>Default>ChampionshipSeasonRankPanel"}
        btn_close = {"locator": "UICanvas>Default>ChampionshipSeasonRankPanel>activity_popup_201>btn_close"}
        Viewport = {"locator": "UICanvas>Default>ChampionshipSeasonRankPanel>activity_popup_201>panel>ranking_list>Viewport"}
        btn_player_list = {"locator": "UICanvas>Default>ChampionshipSeasonRankPanel>activity_popup_201>panel>ranking_list>Viewport>Content>>btn_player"}


    class ChoosePawnPanel:
        ChoosePawnPanel = {"locator": "UICanvas>Default>ChoosePawnPanel"}
        btn_Piece1 = {"locator": "UICanvas>Default>ChoosePawnPanel>btn_Piece1"}
        btn_Piece2 = {"locator": "UICanvas>Default>ChoosePawnPanel>btn_Piece2"}
        btn_Piece3 = {"locator": "UICanvas>Default>ChoosePawnPanel>btn_Piece3"}

    class DailyMissionMainPanel:
        DailyMissionMainPanel = {"locator": "UICanvas>Default>DailyMissionMainPanel"}
        btn_close = {"locator": "UICanvas>Default>DailyMissionMainPanel>panel>panel_bottom>btn_close"}
        btn_receive_list = {"locator": "UICanvas>Default>DailyMissionMainPanel>panel>task_list>>receive>btn_receive"}


    class DisplayCaseMainPanel:
        DisplayCaseMainPanel = {"locator": "UICanvas>Default>DisplayCaseMainPanel"}
        btn_close = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>panel_bottom>btn_close"}
        btn_i_list = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>Scroll View>Viewport>Content>>top>btn_i"}
        btn_chess = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>page_btn>btns>btn_chess"}
        btn_shield = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>page_btn>btns>btn_shield"}
        btn_bomb = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>page_btn>btns>btn_bomb"}
        btn_dice = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>page_btn>btns>btn_dice"}
        btn_list = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>Scroll View>Viewport>Content>>list>Viewport>Content>>items>>btn"}
        box_list = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>Scroll View>Viewport>Content>>list>Viewport>Content>>box"}
        Viewport_list = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>Scroll View>Viewport>Content>>list>Viewport"}

        class tips:
            tips_chess = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>tips_chess"}
            tips_shield = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>tips_shield"}
            tips_bomb = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>tips_bomb"}
            tips_dice = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>tips_dice"}
            btn_close = {"locator": "UICanvas>Default>DisplayCaseMainPanel>panel>>btn_close"}

    class DisplayCaseShowModelPanel:
        DisplayCaseShowModelPanel = {"locator": "3DUI>DisplayCaseShowModelPanel"}
        btn_close = {"locator": "3DUI>DisplayCaseShowModelPanel>UI>panel>panel_bottom>btn_close", "camera": "UICamera"}
        btn_continue = {"locator": "3DUI>DisplayCaseShowModelPanel>UI>panel>panel_bottom>btn_continue", "camera": "UICamera"}
        btn_arrow_right = {"locator": "3DUI>DisplayCaseShowModelPanel>UI>panel>panel_bottom>btn_arrow_right", "camera": "UICamera"}
        btn_arrow_left = {"locator": "3DUI>DisplayCaseShowModelPanel>UI>panel>panel_bottom>btn_arrow_left", "camera": "UICamera"}

    class FindFriendsPanel:
        FindFriendsPanel = {"locator": "UICanvas>Default>FindFriendsPanel"}
        btn_close = {"locator": "UICanvas>Default>FindFriendsPanel>panel>btn_close"}
        btn_search = {"locator": "UICanvas>Default>FindFriendsPanel>panel>panel>btn_search"}
        input_field = {"locator": "UICanvas>Default>FindFriendsPanel>panel>panel>enter_bg>input_field"}
        btn_tips = {"locator": "UICanvas>Default>FindFriendsPanel>panel>panel>btn_tips"}

        class panel_rules:
            panel_rules = {"locator": "UICanvas>Default>FindFriendsPanel>panel_rules"}
            btn_close = {"locator": "UICanvas>Default>FindFriendsPanel>panel_rules>btn_close"}

    class FishingPreparePanel:
        FishingPreparePanel = {"locator": "UICanvas>Default>FishingPreparePanel"}
        btn_cast = {"locator": "UICanvas>Default>FishingPreparePanel>panel>bottom>table>fishing reel>btn_cast"}

    class FishingPanel:
        FishingPanel = {"locator": "UICanvas>Default>FishingPanel"}
        btn_hook = {"locator": "UICanvas>Default>FishingPanel>panel>fishing reel>btn_hook"}


    class FishingResultPanel:
        FishingResultPanel = {"locator": "UICanvas>Default>FishingResultPanel"}
        btn_confirm = {"locator": "UICanvas>Default>FishingResultPanel>panel>panel_bottom>btn_confirm"}
        fish_name = {"locator":"UICanvas>Default>FishingResultPanel>panel>fish_name>text"}
        digital = {"locator":"UICanvas>Default>FishingResultPanel>panel>reward>weight>digital>value"}
        rank = {"locator":"UICanvas>Default>FishingResultPanel>panel>reward>weight>rank"}
        money = {"locator":"UICanvas>Default>FishingResultPanel>panel>reward>money>value"}
        fish_class = {"locator":"UICanvas>Default>FishingResultPanel>panel>fish_name>icon"}


    class FishingResultSundriesPanel:
        FishingResultSundriesPanel = {"locator": "UICanvas>Default>FishingResultSundriesPanel"}
        btn_close = {"locator":"UICanvas>Default>FishingResultSundriesPanel>panel>btn_close"}

    class FlipCardPanel:
        FlipCardPanel = {"locator":"UICanvas>Default>FlipCardPanel"}
        btn_close = {"locator":"UICanvas>Default>FlipCardPanel>panel>panel_bottom>btn_close>icon"}
        text_multiples = {"locator":"UICanvas>Default>FlipCardPanel>panel>panel_info>panel_desk>bg_desk>bg>bg_locked>bg_multiples>multiples_modle>text"}
        btn_go = {"locator":"UICanvas>Default>FlipCardPanel>panel>panel_info>panel_desk>bg_desk>bg>bg_locked>bg_hole1>btn_go>num"}
        text_cost = {"locator":"UICanvas>Default>FlipCardPanel>panel>panel_info>panel_desk>bg_desk>bg>bg_locked>bg_hole1>btn_go>num>text"}
        text_own = {"locator":"UICanvas>Default>FlipCardPanel>panel>panel_info>panel_desk>bg_desk>bg>bg_locked>bg_hole2>bg_hole2>cost>value"}
        text_bout = {"locator":"UICanvas>Default>FlipCardPanel>panel>panel_info>panel_body>panel_body>panel_bout>value"}
        card_list = {"locator":"UICanvas>Default>FlipCardPanel>panel>panel_info>panel_card>bg_desk>bg>card_list>Viewport>Content>>card_model>card>FlopCard_card_model>btn"}
        panel_card = {"locator":"UICanvas>Default>FlipCardPanel>panel>panel_info>panel_card"}

    class GetCommonRewardsPanel:
        GetCommonRewardsPanel = {"locator": "3DUI>GetCommonRewardsPanel"}
        btn_confirm = {"locator": "3DUI>GetCommonRewardsPanel>UI>panel>down>btn_confirm", "camera": "UICamera"}

    class HiddentreasurePanel:
        HiddentreasurePanel = {"locator":"UICanvas>Default>HiddentreasurePanel"}
        btn_close = {"locator": "UICanvas>Default>HiddentreasurePanel>panel>panel_info>btn_close"}
        btn_tips = {"locator": "UICanvas>Default>HiddentreasurePanel>panel>panel_info>btn_tips"}
        class panel_rules:
            panel_rules = {"locator": "UICanvas>Default>HiddentreasurePanel>panel>panel_rules"}
            btn_close = {"locator": "UICanvas>Default>HiddentreasurePanel>panel>panel_rules>btn_close"}

    class HiddentreasurePopUpPanel:
        HiddentreasurePopUpPanel = {"locator":"UICanvas>Default>HiddentreasurePopUpPanel"}
        btn_close = {"locator": "UICanvas>Default>HiddentreasurePopUpPanel>panel>panel>btn_close"}
        btn_go = {"locator": "UICanvas>Default>HiddentreasurePopUpPanel>panel>panel>btn_go"}

    class HomePanel:
        HomePanel = {"locator": "UICanvas>Default>HomePanel"}
        class navbar:
            btn_start = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_start"}
            btn_start_disabled = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_start>btn_pressed2"}
            dice_value = {"locator": "UICanvas>Default>HomePanel>panel>navbar>progress_dice>value"}
            btn_multiple = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_multiple"}
            multiple_value = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_multiple>text"}
            btn_fishing = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_navbar_1"}
            btn_building = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_navbar_2"}
            btn_cards = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_navbar_3"}
            btn_friends = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_navbar_4"}

        class panel_left:
            btn_shop = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>btn_shop"}

        class panel_right:
            btn_bank = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank"}
            right_name = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank>btn>name"}
            right_head = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank>btn>head>head_mask>head_img"}
            money_value = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank>btn>money>value"}
            right_multiple = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank>btn>multiple>multiples_modle>text"}
            btn_tournaments = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_tournaments"}
            tournaments_time = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_tournaments>btn>time>text"}
            ranking_value = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_tournaments>btn>ranking>value"}

        class panel_progress_com:
            progress_value = {"locator": "UICanvas>Default>HomePanel>panel>panel_progress_com>panel>progress>value>value"}
            progress_value_max = {"locator": "UICanvas>Default>HomePanel>panel>panel_progress_com>panel>progress>value>value_max"}
            reward_value = {"locator": "UICanvas>Default>HomePanel>panel>panel_progress_com>panel>progress>reward>value"}
            progress_time = {"locator": "UICanvas>Default>HomePanel>panel>panel_progress_com>panel>time>text"}

    class HomeBottomFriendsPanel:
        HomeBottomFriendsPanel = {"locator": "UICanvas>Default>HomeBottomFriendsPanel"}
        btn_close = {"locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel_bottom>btn_close"}
        tab_list = {"locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>tab"}
        class page_1:
            btn_copy ={"locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_1>top>btn_copy"}
            btn_search = {"locator": "btn_search"}
            btn_share_list = {"locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_1>rank>ScrollRect>Viewport>Content>>bottom>btn_share"}
            btn_search_list = { "locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_1>rank>ScrollRect>Viewport>Content>>bottom>btn_search"}
            Viewport = { "locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_1>rank>ScrollRect>Viewport"}
            btn_player_list = { "locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_1>rank>ScrollRect>Viewport>Content>>top>btn_player"}

        class page_2:
            btn_receive = {"locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_2>btn_receive"}
            Viewport = { "locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_2>rank>ScrollRect>Viewport"}
            btn_player_list = { "locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_2>rank>ScrollRect>Viewport>Content>model>>btn_player"}

        class page_3:
            btn_switch_list = {"locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_3>top>>btn_switch>"}
            Viewport = { "locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_3>rank>ScrollRect>Viewport"}
            btn_player_list = { "locator": "UICanvas>Default>HomeBottomFriendsPanel>panel>panel>page_3>rank>ScrollRect>Viewport>Content>model>>btn_player"}






    class HomeRightSettingPanel:
        HomeRightSettingPanel = {"locator": "UICanvas>Default>HomeRightSettingPanel"}
        btn_close = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel_bottom>btn_close"}
        head = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>top>head"}
        name = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>top>name"}
        btn_fortune_hall = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>button_2"}
        btn_my_showroom = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>button_3"}
        btn_map = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>button_5"}
        btn_board_report = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>button_6"}
        btn_settings = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>button_8"}
        btn_facebook = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>btn1>btn_facebook"}


    class JuggleJamMainPanel:
        JuggleJamMainPanel = {"locator": "UICanvas>Default>JuggleJamMainPanel"}
        btn_close = {"locator": "UICanvas>Default>JuggleJamMainPanel>Panel>panel_bottom>btn_close"}
        btn_tips = {"locator": "UICanvas>Default>JuggleJamMainPanel>Panel>panel_top>panel>btn_tips"}


    class JuggleJamPopUpPanel:
        JuggleJamPopUpPanel = {"locator": "UICanvas>Default>JuggleJamPopUpPanel"}
        btn_close = {"locator": "UICanvas>Default>JuggleJamPopUpPanel>panel>btn_close"}
        btn_go = {"locator": "UICanvas>Default>JuggleJamPopUpPanel>panel>panel>btn_go"}

    class LoginChessboardReportPanel:
        LoginChessboardReportPanel = {"locator": "UICanvas>Default>LoginChessboardReportPanel"}
        btn_close = {"locator": "UICanvas>Default>LoginChessboardReportPanel>btn_close"}

    class LoginPanel:
        LoginPanel = {"locator": "UICanvas>Default>LoginPanel"}
        btn_login = {"locator": "UICanvas>Default>LoginPanel>panel_internal>btn_login"}
        Dropdown = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_ServerList"}
        Dropdown_list = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_ServerList>Template>Viewport>Content"}
        InputField_UserName = {"locator": "UICanvas>Default>LoginPanel>panel_internal>InputField_UserName"}
        Dropdown_HistoryAccount = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_HistoryAccount"}
        Dropdown_HistoryAccount_List = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_HistoryAccount>Template>Viewport>Content"}

    class MessageBoxPanel:
        MessageBoxPanel = {"locator": "UICanvas>Default>MessageBoxPanel"}
        btn_confirm = {"locator": "UICanvas>Important>MessageBoxPanel>panel>btn_confirm"}

    class MiniGameTurntablePanel:
        MiniGameTurntablePanel = {"locator": "UICanvas>Default>MiniGameTurntablePanel"}
        btn_close = {"locator": "UICanvas>Default>MiniGameTurntablePanel>Panel>panel_bottom>btn_close"}
        btn_i = {"locator": "UICanvas>Default>MiniGameTurntablePanel>Panel>Panel_top>btn_i"}
        class tips:
            tips = {"locator": "UICanvas>Default>MiniGameTurntablePanel>tips"}
            btn_close = {"locator": "UICanvas>Default>MiniGameTurntablePanel>tips>btn_close"}

    class NewbieGuidePanel:
        NewbieGuidePanel = {"locator": "UICanvas>Important>NewbieGuidePanel"}

        NBG_plot_guide_1 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_plot_guide_1(Clone)"}
        NBG_plot_guide_2 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_plot_guide_2(Clone)"}
        NBG_plot_guide_3 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_plot_guide_3(Clone)"}
        NBG_plot_guide_1_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_plot_guide_1(Clone)>Guide_VirtualBtn"}
        NBG_plot_guide_2_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_plot_guide_2(Clone)>Guide_VirtualBtn"}
        NBG_plot_guide_3_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_plot_guide_3(Clone)>Guide_VirtualBtn"}


        NBG_introduce_fish = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_introduce_fish(Clone)"}
        NBG_introduce_fish_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_introduce_fish(Clone)>Guide_VirtualBtn"}


        NBG_first_cast_1 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_cast_1(Clone)"}
        NBG_first_cast_3 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_cast_3(Clone)"}
        NBG_first_cast_1_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_cast_1(Clone)>Guide_VirtualBtn"}
        NBG_first_cast_3_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_cast_3(Clone)>Guide_VirtualBtn"}


        NBG_finish_first_fishing = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_finish_first_fishing(Clone)"}
        NBG_finish_first_fishing_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_finish_first_fishing(Clone)>Guide_VirtualBtn"}


        NBG_first_hook_1 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_hook_1(Clone)"}
        NBG_first_hook_2 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_hook_2(Clone)"}
        NBG_first_hook_3 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_hook_3(Clone)"}
        NBG_first_hook_1_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_hook_1(Clone)>Guide_VirtualBtn"}
        NBG_first_hook_2_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_hook_2(Clone)>Guide_VirtualBtn"}

        NBG_first_ult_max = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_first_ult_max(Clone)"}

        NBG_fishing_randomevents_events = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_fishing_randomevents_events(Clone)"}
        NBG_fishing_randomevents_events_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_fishing_randomevents_events(Clone)>Guide_VirtualBtn"}

        NBG_go_to_album = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_go_to_album(Clone)"}
        NBG_go_to_album_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_go_to_album(Clone)>Guide_VirtualBtn"}

        NBG_last_fishing_begin = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_last_fishing_begin(Clone)"}

        # NBG_last_fishing_result = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_last_fishing_result(Clone)"}

        NBG_go_to_build = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_go_to_build(Clone)"}
        NBG_go_to_build_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_go_to_build(Clone)>Guide_VirtualBtn"}

        NBG_rookie_build_1 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_build_1(Clone)"}
        NBG_rookie_build_2 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_build_2(Clone)"}
        NBG_rookie_build_3 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_build_3(Clone)"}
        NBG_rookie_build_1_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_build_1(Clone)>Guide_VirtualBtn"}
        NBG_rookie_build_2_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_build_2(Clone)>Guide_VirtualBtn"}
        NBG_rookie_build_3_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_build_3(Clone)>Guide_VirtualBtn"}

        NBG_rookie_back_to_fish = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_back_to_fish(Clone)"}
        NBG_rookie_back_to_fish_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_back_to_fish(Clone)>Guide_VirtualBtn"}

        NBG_fishing_randomevents_1 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_fishing_randomevents_1(Clone)"}
        NBG_fishing_randomevents_1_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_fishing_randomevents_1(Clone)>Guide_VirtualBtn"}

        NBG_fishing_randomevents_plane ={"locator": "UICanvas>Important>NewbieGuidePanel>NBG_fishing_randomevents_plane(Clone)"}
        NBG_fishing_randomevents_plane_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_fishing_randomevents_plane(Clone)>Guide_VirtualBtn"}

        NBG_go_to_board_1 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_go_to_board_1(Clone)"}
        NBG_go_to_board_1_close= {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_go_to_board_1(Clone)>Guide_VirtualBtn"}

        NBG_no_bait_guide = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_no_bait_guide(Clone)"}
        NBG_no_bait_guide_close= {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_no_bait_guide(Clone)>Guide_VirtualBtn"}

        NBG_rookie_look_board = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_look_board(Clone)"}
        NBG_rookie_look_board_close= {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_look_board(Clone)>Guide_VirtualBtn"}

        NBG_rookie_first_roll = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_first_roll(Clone)"}
        NBG_rookie_first_roll_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_first_roll(Clone)>Guide_VirtualBtn", "focus": (0.5, 1)}

        NBG_rookie_board_bait = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_board_bait(Clone)"}
        NBG_rookie_board_bait_close= {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_board_bait(Clone)>Guide_VirtualBtn"}

        NBG_rookie_attack_1 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_1(Clone)"}
        NBG_rookie_attack_2 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_2(Clone)"}
        NBG_rookie_attack_3 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_3(Clone)"}
        NBG_rookie_attack_4 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_4(Clone)"}
        NBG_rookie_attack_5 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_5(Clone)"}
        NBG_rookie_attack_6 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_6(Clone)"}
        NBG_rookie_attack_7 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_7(Clone)"}
        NBG_rookie_attack_1_close= {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_1(Clone)>Guide_VirtualBtn"}
        NBG_rookie_attack_2_close= {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_2(Clone)>Guide_VirtualBtn"}
        NBG_rookie_attack_3_close= {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_3(Clone)>Guide_VirtualBtn"}
        NBG_rookie_attack_5_close= {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_5(Clone)>Guide_VirtualBtn"}
        NBG_rookie_attack_7_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_attack_7(Clone)>Guide_VirtualBtn"}

        NBG_rookie_shield_generate_1 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_shield_generate_1(Clone)"}
        NBG_rookie_shield_generate_2 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_shield_generate_2(Clone)"}
        NBG_rookie_shield_introduction = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_shield_introduction(Clone)"}
        NBG_rookie_shield_generate_1_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_shield_generate_1(Clone)>Guide_VirtualBtn"}
        NBG_rookie_shield_generate_2_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_shield_generate_2(Clone)>Guide_VirtualBtn"}
        NBG_rookie_shield_introduction_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_shield_introduction(Clone)>Guide_Mask>maskCtrl"}

        NBG_rookie_bank_2 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_bank_2(Clone)"}
        NBG_rookie_bank_3 = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_bank_3(Clone)"}
        NBG_rookie_bank_2_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_bank_2(Clone)>Guide_VirtualBtn"}
        NBG_rookie_bank_3_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_bank_3(Clone)>Guide_VirtualBtn"}

        NBG_rookie_back_to_build = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_back_to_build(Clone)"}
        NBG_rookie_back_to_build_close = {"locator": "UICanvas>Important>NewbieGuidePanel>NBG_rookie_back_to_build(Clone)>Guide_VirtualBtn", "focus": (0.5, 1)}







    class NewbieGuideFishingLowTension:
        NewbieGuideFishingLowTension = {"locator": "UICanvas>Default>NewbieGuideFishingLowTension"}


    class Panel_steal:
        Panel_steal = {"locator": "SceneRoot>Canvas>Panel_steal"}
        btn_click_list = {"locator": "SceneRoot>Canvas>Panel_steal>panel_main>treasure_chest>>btn_click", "camera": "Camera3D"}


    class ResourcesBarPanel:
        ResourcesBarPanel = {"locator": "UICanvas>Default>ResourcesBarPanel"}
        money_value = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>res_01>value"}
        player_exp_value = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>player_exp>value"}
        player_exp = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>player_exp"}
        btn_menu = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>btn_menu"}
        shield_total = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>panel_shield>icon(Clone)"}
        shield = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>panel_shield>icon(Clone)>icon"}

    class ScratchCardPanel:
        ScratchCardPanel = {"locator": "UICanvas>Default>ScratchCardPanel"}
        btn_close = {"locator": "UICanvas>Default>ScratchCardPanel>Panel>panel_bottom>btn_close"}
        btn_i = {"locator": "UICanvas>Default>ScratchCardPanel>Panel>Panel_top>btn_i"}
        class tips:
            tips = {"locator": "UICanvas>Default>ScratchCardPanel>tips"}
            btn_close = {"locator": "UICanvas>Default>ScratchCardPanel>tips>btn_close"}

    class SettingsPanel:
        SettingsPanel = {"locator": "UICanvas>Default>SettingsPanel"}
        btn_close = {"locator": "UICanvas>Default>SettingsPanel>btn_close"}
        btn_switch_list = {"locator": "UICanvas>Default>SettingsPanel>panel>top>>btn_switch"}
        btn_language = {"locator": "UICanvas>Default>SettingsPanel>panel>center>btn_language"}
        btn_notice = {"locator": "UICanvas>Default>SettingsPanel>panel>down>btn_notice"}
        btn_legal = {"locator": "UICanvas>Default>SettingsPanel>panel>down>btn_legal"}
        btn_account = {"locator": "UICanvas>Default>SettingsPanel>panel>btn_account"}

    class SettingPanellegal:
        SettingPanellegal = {"locator": "UICanvas>Default>SettingPanellegal"}
        btn_close = {"locator": "UICanvas>Default>SettingPanellegal>btn_close"}

    class SettingPanelManageAccount:
        SettingPanelManageAccount = {"locator": "UICanvas>Default>SettingPanelManageAccount"}
        btn_close = {"locator":"UICanvas>Default>SettingPanelManageAccount>btn_close"}


    class SettingPanelModifyProfile:
        SettingPanelModifyProfile = {"locator": "UICanvas>Default>SettingPanelModifyProfile"}
        btn_close = {"locator":"UICanvas>Default>SettingPanelModifyProfile>btn_close"}
        btn_save = {"locator":"UICanvas>Default>SettingPanelModifyProfile>panel>btn_save"}
        Viewport = {"locator":"UICanvas>Default>SettingPanelModifyProfile>panel>head_list>Viewport"}
        head_list = {"locator":"UICanvas>Default>SettingPanelModifyProfile>panel>head_list>Viewport>Content>>head"}
        head = {"locator":"UICanvas>Default>SettingPanelModifyProfile>panel>top>head"}
        name = {"locator":"UICanvas>Default>SettingPanelModifyProfile>panel>top>name"}

    class SettingPanelModifyName:
        SettingPanelModifyName = {"locator": "UICanvas>Default>SettingPanelModifyName"}
        btn_close = {"locator": "UICanvas>Default>SettingPanelModifyName>btn_close"}
        input_name = {"locator": "UICanvas>Default>SettingPanelModifyName>panel>input_name"}
        btn_submit = {"locator": "UICanvas>Default>SettingPanelModifyName>panel>btn_submit"}

    class StarGalleryPanel:
        StarGalleryPanel = {"locator": "UICanvas>Default>StarGalleryPanel"}
        btn_close = {"locator": "UICanvas>Default>StarGalleryPanel>panel>panel_bottom>btn_close"}
        property_model_list = {"locator": "UICanvas>Default>StarGalleryPanel>panel>property_list>list>Viewport>Content>>>property_model_new"}

        class popup:
            popup = {"locator": "UICanvas>Default>StarGalleryPanel>panel>popup"}
            btn_close = {"locator": "UICanvas>Default>StarGalleryPanel>panel>popup>btn_close"}


    class ShowRewardsPanel:
        ShowRewardsPanel = {"locator": "UICanvas>Default>UICanvas>Default>ShowRewardsPanel"}

    class StickerRewardsShowPanel:
        StickerRewardsShowPanel = {"locator": "UICanvas>Default>UICanvas>Default>StickerRewardsShowPanel"}
        btn_collect = {"locator": "UICanvas>Default>StickerRewardsShowPanel>panel_bottom>btn_collect"}

    class StickerCollectPanel:
        StickerCollectPanel = {"locator": "UICanvas>Default>UICanvas>Default>StickerCollectPanel"}
        btn_close = {"locator": "UICanvas>Default>StickerCollectPanel>panel>panel_bottom>btn_close"}
        btn_tips = {"locator": "UICanvas>Default>StickerCollectPanel>panel>time>btn_tips"}
        btn_exchange = {"locator": "UICanvas>Default>StickerCollectPanel>panel>panel_top>btn_exchange"}
        class tips:
            tips = {"locator": "UICanvas>Default>StickerCollectPanel>panel>tips"}
            btn_close_tips = {"locator": "UICanvas>Default>StickerCollectPanel>panel>tips>btn_close"}

    class StickerCollectPopPanel:
        StickerCollectPopPanel = {"locator": "UICanvas>Default>UICanvas>Default>StickerCollectPopPanel"}
        btn_close = {"locator": "UICanvas>Default>StickerCollectPopPanel>Panel>panel_bottom>btn_close"}
        btn_left = {"locator": "UICanvas>Default>StickerCollectPopPanel>Panel>panel_bottom>btn_lift"}
        btn_right = {"locator": "UICanvas>Default>StickerCollectPopPanel>Panel>panel_bottom>btn_right"}
        Page_list = {"locator": "UICanvas>Default>StickerCollectPopPanel>Panel>LoopPage>Viewport>Content>Page(Clone)"}
        btn_list = {"locator": "UICanvas>Default>StickerCollectPopPanel>Panel>LoopPage>Viewport>Content>>panel_list>Viewport>Content>>root>Com_card_model>btn"}

    class StickerCollectPopDetailPanel:
        StickerCollectPopDetailPanel = {"locator": "UICanvas>Default>UICanvas>Default>StickerCollectPopPanel"}
        btn_close = {"locator": "UICanvas>Default>StickerCollectPopDetailPanel>panel_bottom>btn_close"}
        btn_arrow_left = {"locator": "UICanvas>Default>StickerCollectPopDetailPanel>panel_bottom>btn_arrow_left"}
        btn_arrow_right = {"locator": "UICanvas>Default>StickerCollectPopDetailPanel>panel_bottom>btn_arrow_right"}
        btn_friends = {"locator": "UICanvas>Default>StickerCollectPopDetailPanel>panel_bottom>>btn_friends"}

    class StickerCollectFriendPanel:
        StickerCollectFriendPanel = {"locator": "UICanvas>Default>UICanvas>Default>StickerCollectFriendPanel"}
        btn_close = {"locator": "UICanvas>Default>StickerCollectFriendPanel>panel_choose>btn_close"}
        btn_continue = {"locator": "UICanvas>Default>StickerCollectFriendPanel>panel_choose>panel>btn_continue"}
        tab_list = {"locator": "UICanvas>Default>StickerCollectFriendPanel>panel_choose>panel>changecards>btn_switch>"}
        InputField = {"locator": "UICanvas>Default>StickerCollectFriendPanel>panel_choose>panel>search>InputField"}


    class StickerExchangeMainPanel:
        StickerExchangeMainPanel = {"locator": "UICanvas>Default>StickerExchangeMainPanel"}
        btn_close = {"locator": "UICanvas>Default>StickerExchangeMainPanel>panel>panel_bottom>btn_close"}
        btn_list = {"locator": "UICanvas>Default>StickerExchangeMainPanel>panel>list>>btn"}


    class StickerCollectPopEventPanel:
        StickerCollectPopEventPanel = {"locator": "UICanvas>Default>StickerCollectPopEventPanel"}
        btn_close = {"locator": "UICanvas>Default>StickerCollectPopEventPanel>panel>btn_close"}


    class StorePanel:
        StorePanel = {"locator": "UICanvas>Default>StorePanel"}
        btn_close = {"locator": "UICanvas>Default>StorePanel>panel>panel_bottom>btn_close"}
        btn_confirm = {"locator": "UICanvas>Default>StorePanel>panel>gift_pack>ScrollView>Viewport>Content>Page(Clone)>btn_confirm"}


    class TurntablePopUpPanel:
        TurntablePopUpPanel = {"locator": "UICanvas>Default>TurntablePopUpPanel"}
        btn_close = {"locator": "UICanvas>Default>TurntablePopUpPanel>panel>btn_close"}

