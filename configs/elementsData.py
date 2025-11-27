class ElementsData:
    Panels = {"locator": "UICanvas>>"}
    Panels_Default = {"locator": "UICanvas>Default>"}


    class FishingPreparePanel:
        FishingPreparePanel = {"locator": "UICanvas>Default>FishingPreparePanel"}
        btn_cast = {"locator": "UICanvas>Default>FishingPreparePanel>panel>bottom>table>fishing reel>btn_cast"}

    class FishingPanel:
        FishingPanel = {"locator": "UICanvas>Default>FishingPanel"}

    class FishingResultPanel:
        FishingResultPanel = {"locator": "UICanvas>Default>FishingResultPanel"}
        btn_confirm = {"locator": "UICanvas>Default>FishingResultPanel>panel>panel_bottom>btn_confirm"}
        fish_name = {"locator":"UICanvas>Default>FishingResultPanel>panel>fish_name>text"}
        digital = {"locator":"UICanvas>Default>FishingResultPanel>panel>reward>weight>digital>value"}
        rank = {"locator":"UICanvas>Default>FishingResultPanel>panel>reward>weight>rank"}
        money = {"locator":"UICanvas>Default>FishingResultPanel>panel>reward>money>value"}
        fish_class = {"locator":"UICanvas>Default>FishingResultPanel>panel>fish_name>icon"}

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




    class HomePanel:
        HomePanel = {"locator": "UICanvas>Default>HomePanel"}
        btn_start = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_start>btn_normal"}
        dice_value = {"locator": "UICanvas>Default>HomePanel>panel>navbar>progress_dice>value"}
        btn_multiple = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_multiple>btn_normal"}
        multiple_value = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_multiple>text"}
        btn_fishing = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_navbar_1>btn_normal"}
        btn_building = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_navbar_2>btn_normal"}
        btn_cards = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_navbar_3>btn_normal"}
        btn_friends = {"locator": "UICanvas>Default>HomePanel>panel>navbar>btn_navbar_4>btn_normal"}
        btn_shop = {"locator": "UICanvas>Default>HomePanel>panel>panel_left>btn_shop>btn>icon"}
        btn_bank = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank>btn"}
        right_name = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank>btn>name"}
        right_head = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank>btn>head>head_mask>head_img"}
        money_value = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank>btn>money>value"}
        right_multiple = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_bank>btn>multiple>multiples_modle>text"}
        btn_tournaments = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_tournaments>btn"}
        tournaments_time = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_tournaments>btn>time>text"}
        ranking_value = {"locator": "UICanvas>Default>HomePanel>panel>panel_right>btn_tournaments>btn>ranking>value"}
        progress_value = {"locator": "UICanvas>Default>HomePanel>panel>panel_progress_com>panel>progress>value>value"}
        progress_value_max = {"locator": "UICanvas>Default>HomePanel>panel>panel_progress_com>panel>progress>value>value_max"}
        reward_value = {"locator": "UICanvas>Default>HomePanel>panel>panel_progress_com>panel>progress>reward>value"}
        progress_time = {"locator": "UICanvas>Default>HomePanel>panel>panel_progress_com>panel>time>text"}

    class GetCommonRewardsPanel:
        GetCommonRewardsPanel = {"locator": "3DUI>GetCommonRewardsPanel"}
        btn_confirm = {"locator": "3DUI>GetCommonRewardsPanel>UI>panel>down>btn_confirm", "camera": "UICamera"}

    class LoginPanel:
        LoginPanel = {"locator": "UICanvas>Default>LoginPanel"}
        btn_login = {"locator": "UICanvas>Default>LoginPanel>panel_internal>btn_login>text"}
        Dropdown = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_ServerList"}
        Dropdown_list = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_ServerList>Template>Viewport>Content"}
        InputField_UserName = {"locator": "UICanvas>Default>LoginPanel>panel_internal>InputField_UserName"}
        Dropdown_HistoryAccount = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_HistoryAccount"}
        Dropdown_HistoryAccount_List = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_HistoryAccount>Template>Viewport>Content"}

    class MessageBoxPanel:
        MessageBoxPanel = {"locator": "UICanvas>Default>MessageBoxPanel"}
        btn_confirm = {"locator": "UICanvas>Important>MessageBoxPanel>panel>btn_confirm"}

    class ResourcesBarPanel:
        ResourcesBarPanel = {"locator": "UICanvas>Default>ResourcesBarPanel"}
        money_value = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>res_01>value"}
        player_exp_value = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>player_exp>value"}
        btn_menu = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>btn_menu>btn_normal"}
        shield_total = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>panel_shield>icon(Clone)"}
        shield = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>panel_shield>icon(Clone)>icon"}

    class BuildingPanel:
        BuildingPanel = {"locator": "UICanvas>Default>BuildingPanel"}
        building_1 = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_1>icon"}
        building_2 = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_2>icon"}
        building_3 = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_3>icon"}
        building_4 = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_4>icon"}
        building_5 = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_5>icon"}
        cost1_value = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_1>cost>value"}
        cost2_value = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_2>cost>value"}
        cost3_value = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_3>cost>value"}
        cost4_value = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_4>cost>value"}
        cost5_value = {"locator": "UICanvas>Default>BuildingPanel>panel>building_list>building_5>cost>value"}
        progress_value = {"locator": "UICanvas>Default>BuildingPanel>panel>panel_bottom>value"}
        btn_close = {"locator": "UICanvas>Default>BuildingPanel>panel>panel_bottom>btn_close"}

    class BuildingCompletePanel:
        BuildingCompletePanel = {"locator": "UICanvas>Default>BuildingCompletePanel"}
        btn_go = {"locator": "UICanvas>Default>BuildingCompletePanel>panel>down>btn_go>btn_normal"}

    class StarGalleryPanel:
        StarGalleryPanel = {"locator": "UICanvas>Default>StarGalleryPanel"}
        btn_close = {"locator": "UICanvas>Default>StarGalleryPanel>panel>panel_bottom>btn_close>icon"}

    class BuildingDestroyPanel:
        BuildingDestroyPanel = {"locator": "UICanvas>Default>BuildingDestroyPanel"}

        class Choose:
            panel_choose = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose"}
            btn_confirm = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>panel_bottom>btn_confirm>btn_normal"}
            opponent_head_mask = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>opponent_Info>head>head_mask>head_img"}
            opponent_name = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>opponent_Info>name"}
            multiple = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>opponent_Info>multiple>multiples_modle>text"}
            crosshair = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_choose>Crosshair>model(Clone)>crosshair"}

        class Change:
            panel_change = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change"}
            btn_close = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change>panel_bottom>btn_close>icon"}
            btn_revenge = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change>panel_list>tab>1>text"}
            btn_friend = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change>panel_list>tab>2>text"}
            btn_go_list = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_change>panel_list>list>Viewport>Content>>list_item_model>panel_revenge>btn_go>btn_normal"}

        class Reward:
            panel_reward = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward"}
            money_value = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward>reward>money>value"}
            opponent_head_mask = {
                "locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward>opponent_Info>head>head_mask>head_img"}
            opponent_name = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward>opponent_Info>name"}
            btn_confirm = {"locator": "UICanvas>Default>BuildingDestroyPanel>panel_reward>panel_bottom>btn_confirm>btn_normal"}

    class HomeRightSettingPanel:
        HomeRightSettingPanel = {"locator": "UICanvas>Default>HomeRightSettingPanel"}
        head_mask = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>top>head>head_mask>head_img"}
        name = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>top>name"}
        fortune_hall = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>button_2>text"}
        map = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>button_5>text"}
        board_report = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>button_6>text"}
        setting = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>button_8>text"}
        btn_facebook = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel>center>btn1>btn_facebook>btn_normal"}
        btn_close = {"locator": "UICanvas>Default>HomeRightSettingPanel>panel_bottom>btn_close>icon"}





    class ShowRewardsPanel:
        ShowRewardsPanel = {"locator": "UICanvas>Default>UICanvas>Default>ShowRewardsPanel"}

    class StickerRewardsShowPanel:
        StickerRewardsShowPanel = {"locator": "UICanvas>Default>UICanvas>Default>StickerRewardsShowPanel"}
        btn_collect = {"locator": "UICanvas>Default>StickerRewardsShowPanel>panel_bottom>btn_collect"}

    class StickerCollectPopEventPanel:
        StickerCollectPopEventPanel = {"locator": "UICanvas>Default>StickerCollectPopEventPanel"}
        btn_close = {"locator": "UICanvas>Default>StickerCollectPopEventPanel>panel>btn_close>icon"}

