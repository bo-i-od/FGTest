class ElementsData:
    Panels = {"locator": "UICanvas>>"}
    Panels_Default = {"locator": "UICanvas>Default>"}

    class LoginPanel:
        LoginPanel = {"locator": "UICanvas>Default>LoginPanel"}
        btn_login = {"locator": "UICanvas>Default>LoginPanel>panel_internal>btn_login>text"}
        Dropdown = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_ServerList"}
        Dropdown_list = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_ServerList>Template>Viewport>Content"}
        InputField_UserName = {"locator": "UICanvas>Default>LoginPanel>panel_internal>InputField_UserName"}
        Dropdown_HistoryAccount = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_HistoryAccount"}
        Dropdown_HistoryAccount_List = {"locator": "UICanvas>Default>LoginPanel>panel_internal>Dropdown_HistoryAccount>Template>Viewport>Content"}

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

    class ResourcesBarPanel:
        ResourcesBarPanel = {"locator": "UICanvas>Default>ResourcesBarPanel"}
        money_value = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>res_01>value"}
        player_exp_value = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>player_exp>value"}
        btn_menu = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>btn_menu>btn_normal"}
        shield = {"locator": "UICanvas>Default>ResourcesBarPanel>panel>panel_shield>icon(Clone)"}

