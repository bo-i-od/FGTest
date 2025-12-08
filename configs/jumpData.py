from configs.elementsData import ElementsData


class JumpData:
    element_data_home = None
    panel_list = [ElementsData.Panels, ElementsData.GetCommonRewardsPanel.GetCommonRewardsPanel]
    pop_window_set = {
        "StickerCollectPopEventPanel",
        "MessageBoxPanel",
        "GetCommonRewardsPanel",
        "StickerRewardsShowPanel",
        "ChampionshipMainPanel",
        "NewbieGuideFishingLowTension",

    }

    panel_dict = {
    "ActivityBuffCashBoostPanel": {"element_data": ElementsData.ActivityBuffCashBoostPanel.ActivityBuffCashBoostPanel, "close_path": [ElementsData.ActivityBuffCashBoostPanel.btn_close]},
    "ActivityBuffBuildersBashPanel": {"element_data": ElementsData.ActivityBuffBuildersBashPanel.ActivityBuffCashBoostPanel, "close_path": [ElementsData.ActivityBuffBuildersBashPanel.btn_close]},
    "BaitShopPanel": {"element_data": ElementsData.BaitShopPanel.BuildingPanel, "close_path": [ElementsData.BaitShopPanel.btn_close]},
    "BuildingPanel": {"element_data": ElementsData.BuildingPanel.BuildingPanel, "close_path": [ElementsData.BuildingPanel.btn_close]},
    "BuildingCityListPanel": {"element_data": ElementsData.BuildingCityListPanel.BuildingCityListPanel, "close_path": [ElementsData.BuildingCityListPanel.btn_close]},
    "BuildingCityPanel": {"element_data": ElementsData.BuildingCityPanel.BuildingCityPanel, "close_path": [ElementsData.BuildingCityPanel.btn_close]},
    "BuildingCompletePanel": {"element_data": ElementsData.BuildingCompletePanel.BuildingCompletePanel, "close_path": [ElementsData.BuildingCompletePanel.btn_go]},
    "BuildingDestroyPanelChoose": {"element_data": ElementsData.BuildingDestroyPanel.BuildingDestroyPanel, "close_path": [ElementsData.BuildingDestroyPanel.panel_choose.btn_confirm]},
    "BuildingDestroyPanelChange": {"element_data": ElementsData.BuildingDestroyPanel.panel_change.panel_change, "close_path": [ElementsData.BuildingDestroyPanel.panel_change.btn_close]},
    "BuildingDestroyPanelReward": {"element_data": ElementsData.BuildingDestroyPanel.panel_reward.panel_reward, "close_path": [ElementsData.BuildingDestroyPanel.panel_reward.btn_confirm]},
    "ChampionshipMainPanel": {"element_data": ElementsData.ChampionshipMainPanel.ChampionshipMainPanel, "close_path": [ElementsData.ChampionshipMainPanel.btn_receive]},
    "ChampionshipRulesPopupPanel": {"element_data": ElementsData.ChampionshipRulesPopupPanel.ChampionshipRulesPopupPanel, "close_path": [ElementsData.ChampionshipRulesPopupPanel.btn_close]},
    "ChampionshipSeasonRankPanel": {"element_data": ElementsData.ChampionshipSeasonRankPanel.ChampionshipSeasonRankPanel, "close_path": [ElementsData.ChampionshipSeasonRankPanel.btn_close]},
    "DailyMissionMainPanel": {"element_data": ElementsData.DailyMissionMainPanel.DailyMissionMainPanel, "close_path": [ElementsData.DailyMissionMainPanel.btn_close]},
    "DisplayCaseMainPanel": {"element_data": ElementsData.DisplayCaseMainPanel.DisplayCaseMainPanel, "close_path": [ElementsData.DisplayCaseMainPanel.btn_close]},
    "DisplayCaseMainPanelTips": {"element_data": ElementsData.DisplayCaseMainPanel.tips.tips_chess, "close_path": [ElementsData.DisplayCaseMainPanel.tips.btn_close]},
    "DisplayCaseShowModelPanel": {"element_data": ElementsData.DisplayCaseShowModelPanel.DisplayCaseShowModelPanel, "close_path": [ElementsData.DisplayCaseShowModelPanel.btn_close]},
    "FindFriendsPanel": {"element_data": ElementsData.FindFriendsPanel.FindFriendsPanel, "close_path": [ElementsData.FindFriendsPanel.btn_close]},
    "FindFriendsPanelRules": {"element_data": ElementsData.FindFriendsPanel.panel_rules.panel_rules, "close_path": [ElementsData.FindFriendsPanel.panel_rules.btn_close]},
    "FishingPreparePanel": {"element_data": ElementsData.FishingPreparePanel.FishingPreparePanel, "close_path": [ElementsData.FishingPreparePanel.btn_cast]},
    "FishingPanel": {"element_data": ElementsData.FishingPanel.FishingPanel},
    "FishingResultPanel": {"element_data": ElementsData.FishingResultPanel.FishingResultPanel, "close_path": [ElementsData.FishingResultPanel.btn_confirm]},
    "FlipCardPanel": {"element_data": ElementsData.FlipCardPanel.FlipCardPanel, "close_path": [ElementsData.FlipCardPanel.btn_close]},
    "GetCommonRewardsPanel": {"element_data": ElementsData.GetCommonRewardsPanel.GetCommonRewardsPanel, "close_path": [ElementsData.GetCommonRewardsPanel.btn_confirm]},
    "HiddentreasurePanel": {"element_data": ElementsData.HiddentreasurePanel.HiddentreasurePanel, "close_path": [ElementsData.HiddentreasurePanel.btn_close]},
    "HiddentreasurePanelRules": {"element_data": ElementsData.HiddentreasurePanel.panel_rules.panel_rules, "close_path": [ElementsData.HiddentreasurePanel.panel_rules.btn_close]},
    "HiddentreasurePopUpPanel": {"element_data": ElementsData.HiddentreasurePopUpPanel.HiddentreasurePopUpPanel, "close_path": [ElementsData.HiddentreasurePopUpPanel.btn_close]},
    "HomeBottomFriendsPanel": {"element_data": ElementsData.HomeBottomFriendsPanel.HomeBottomFriendsPanel, "close_path": [ElementsData.HomeBottomFriendsPanel.btn_close]},
    "HomeRightSettingPanel": {"element_data": ElementsData.HomeRightSettingPanel.HomeRightSettingPanel, "close_path": [ElementsData.HomeRightSettingPanel.btn_close]},
    "JuggleJamMainPanel": {"element_data": ElementsData.JuggleJamMainPanel.JuggleJamMainPanel, "close_path": [ElementsData.JuggleJamMainPanel.btn_close]},
    "JuggleJamPopUpPanel": {"element_data": ElementsData.JuggleJamPopUpPanel.JuggleJamPopUpPanel, "close_path": [ElementsData.JuggleJamPopUpPanel.btn_close]},
    "LoginChessboardReportPanel": {"element_data": ElementsData.LoginChessboardReportPanel.LoginChessboardReportPanel, "close_path": [ElementsData.LoginChessboardReportPanel.btn_close]},
    "MessageBoxPanel": {"element_data": ElementsData.MessageBoxPanel.MessageBoxPanel, "close_path": [ElementsData.MessageBoxPanel.btn_confirm]},
    "MiniGameTurntablePanel": {"element_data": ElementsData.MiniGameTurntablePanel.MiniGameTurntablePanel, "close_path": [ElementsData.MiniGameTurntablePanel.btn_close]},
    "MiniGameTurntablePanelTips": {"element_data": ElementsData.MiniGameTurntablePanel.tips.tips, "close_path": [ElementsData.MiniGameTurntablePanel.tips.btn_close]},
    "NewbieGuideFishingLowTension": {"element_data": ElementsData.NewbieGuideFishingLowTension.NewbieGuideFishingLowTension, "close_path": [ElementsData.FishingPanel.btn_hook]},
    "ScratchCardPanel": {"element_data": ElementsData.ScratchCardPanel.ScratchCardPanel, "close_path": [ElementsData.ScratchCardPanel.btn_close]},
    "ScratchCardPanelTips": {"element_data": ElementsData.ScratchCardPanel.tips.tips, "close_path": [ElementsData.ScratchCardPanel.tips.btn_close]},
    "SettingsPanel": {"element_data": ElementsData.SettingsPanel.SettingsPanel, "close_path": [ElementsData.SettingsPanel.btn_close]},
    "SettingPanellegal": {"element_data": ElementsData.SettingPanellegal.SettingPanellegal, "close_path": [ElementsData.SettingPanellegal.btn_close]},
    "SettingPanelManageAccount": {"element_data": ElementsData.SettingPanelManageAccount.SettingPanelManageAccount, "close_path": [ElementsData.SettingPanelManageAccount.btn_close]},
    "SettingPanelModifyProfile": {"element_data": ElementsData.SettingPanelModifyProfile.SettingPanelModifyProfile, "close_path": [ElementsData.SettingPanelModifyProfile.btn_close]},
    "SettingPanelModifyName": {"element_data": ElementsData.SettingPanelModifyName.SettingPanelModifyName, "close_path": [ElementsData.SettingPanelModifyName.btn_close]},
    "StarGalleryPanel": {"element_data": ElementsData.StarGalleryPanel.StarGalleryPanel, "close_path": [ElementsData.StarGalleryPanel.btn_close]},
    "StarGalleryPanelPopup": {"element_data": ElementsData.StarGalleryPanel.popup.popup, "close_path": [ElementsData.StarGalleryPanel.popup.btn_close]},
    "StickerRewardsShowPanel": {"element_data": ElementsData.StickerRewardsShowPanel.StickerRewardsShowPanel, "close_path": [ElementsData.StickerRewardsShowPanel.btn_collect]},
    "StickerCollectPanel": {"element_data": ElementsData.StickerCollectPanel.StickerCollectPanel, "close_path": [ElementsData.StickerCollectPanel.btn_close]},
    "StickerCollectPanelTips": {"element_data": ElementsData.StickerCollectPanel.tips.tips, "close_path": [ElementsData.StickerCollectPanel.tips.btn_close_tips]},
    "StickerCollectPopPanel": {"element_data": ElementsData.StickerCollectPopPanel.StickerCollectPopPanel, "close_path": [ElementsData.StickerCollectPopPanel.btn_close]},
    "StickerCollectPopDetailPanel": {"element_data": ElementsData.StickerCollectPopDetailPanel.StickerCollectPopDetailPanel, "close_path": [ElementsData.StickerCollectPopDetailPanel.btn_close]},
    "StickerCollectFriendPanel": {"element_data": ElementsData.StickerCollectFriendPanel.StickerCollectFriendPanel, "close_path": [ElementsData.StickerCollectFriendPanel.btn_close]},
    "StickerExchangeMainPanel": {"element_data": ElementsData.StickerExchangeMainPanel.StickerExchangeMainPanel, "close_path": [ElementsData.StickerExchangeMainPanel.btn_close]},
    "StickerCollectPopEventPanel": {"element_data": ElementsData.StickerCollectPopEventPanel.StickerCollectPopEventPanel, "close_path": [ElementsData.StickerCollectPopEventPanel.btn_close]},
    "StorePanel": {"element_data": ElementsData.StorePanel.StorePanel, "close_path": [ElementsData.StorePanel.btn_close]},
    "TurntablePopUpPanel": {"element_data": ElementsData.TurntablePopUpPanel.TurntablePopUpPanel, "close_path": [ElementsData.TurntablePopUpPanel.btn_close]},
}

    nbg_list = [
        {"element_data": ElementsData.NewbieGuidePanel.NBG_plot_guide_1,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_plot_guide_1_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_plot_guide_2,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_plot_guide_2_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_plot_guide_3,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_plot_guide_3_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_introduce_fish,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_introduce_fish_close, }]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_first_cast_1,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_first_cast_1_close},
                        {"execute": "sleep"},
                        {"execute": "autofish"}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_first_cast_3,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_first_cast_3_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_finish_first_fishing,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_finish_first_fishing_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_first_hook_1,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_first_hook_1_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_first_hook_2,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_first_hook_2_close}]},
        # {"element_data": ElementsData.NewbieGuidePanel.NBG_first_hook_3, "close_path": [{"click_element":ElementsData.FishingPanel.btn_hook}]},

        # {"element_data": ElementsData.NewbieGuidePanel.NBG_first_ult_max, "close_path": [{"execute": "ult"}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_fishing_randomevents_events,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_fishing_randomevents_events_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_go_to_album,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_go_to_album_close}]},

        # {"element_data": ElementsData.NewbieGuidePanel.NBG_last_fishing_begin,
        #  "close_path": [{"click_element": ElementsData.FishingPreparePanel.btn_cast}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_go_to_build,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_go_to_build_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_build_1,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_build_1_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_build_2,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_build_2_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_build_3,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_build_3_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_back_to_fish,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_back_to_fish_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_fishing_randomevents_1,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_fishing_randomevents_1_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_fishing_randomevents_plane,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_fishing_randomevents_plane_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_go_to_board_1,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_go_to_board_1_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_no_bait_guide,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_no_bait_guide_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_look_board,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_look_board_close}]},

        {"element_data": ElementsData.ChoosePawnPanel.ChoosePawnPanel,
         "close_path": [{"click_element": ElementsData.ChoosePawnPanel.btn_Piece1}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_first_roll,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_first_roll_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_board_bait,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_board_bait_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_attack_1,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_attack_1_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_attack_2,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_attack_2_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_attack_3,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_attack_3_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_attack_5,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_attack_5_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_attack_7,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_attack_7_close}]},
        # {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_attack_6, "close_path": [{"click_element": ElementsData.BuildingDestroyPanel.panel_reward.btn_confirm}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_shield_generate_1,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_shield_generate_1_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_shield_generate_2,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_shield_generate_2_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_shield_introduction,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_shield_introduction_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_bank_2,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_bank_2_close}]},
        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_bank_3,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_bank_3_close}]},

        {"element_data": ElementsData.NewbieGuidePanel.NBG_rookie_back_to_build,
         "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_rookie_back_to_build_close}]},

        # {"element_data": ElementsData.NewbieGuidePanel.NBG_last_fishing_result, "close_path": [{"click_element": ElementsData.NewbieGuidePanel.NBG_last_fishing_result}]},

        # {"element_data": ElementsData.NewbieGuidePanel.NBG_plot_guide.NBG_plot_guide_3, "close_path": [ElementsData.NewbieGuidePanel.NBG_plot_guide.NBG_plot_guide_3]},
        # {"element_data": ElementsData.NewbieGuidePanel.NBG_plot_guide.NBG_plot_guide_3, "close_path": [ElementsData.NewbieGuidePanel.NBG_plot_guide.NBG_plot_guide_3]},
    ]












