from configs.elementsData import ElementsData


class JumpData:
    element_data_home = None
    panel_list = [ElementsData.Panels, ElementsData.GetCommonRewardsPanel.GetCommonRewardsPanel]
    pop_window_set = {
        "StickerCollectPopEventPanel",
        "MessageBoxPanel",
        "GetCommonRewardsPanel",
        "StickerRewardsShowPanel"
    }

    panel_dict = {
        "StickerCollectPopEventPanel": {"element_data": ElementsData.StickerCollectPopEventPanel.StickerCollectPopEventPanel,  "close_path": [ElementsData.StickerCollectPopEventPanel.btn_close]},
        "MessageBoxPanel": {"element_data": ElementsData.MessageBoxPanel.MessageBoxPanel, "close_path": [ElementsData.MessageBoxPanel.btn_confirm]},
        "GetCommonRewardsPanel": {"element_data": ElementsData.GetCommonRewardsPanel.GetCommonRewardsPanel, "close_path": [ElementsData.GetCommonRewardsPanel.btn_confirm]},
        "StickerRewardsShowPanel":{"element_data": ElementsData.StickerRewardsShowPanel.StickerRewardsShowPanel, "close_path": [ElementsData.StickerRewardsShowPanel.btn_collect]},
    }












