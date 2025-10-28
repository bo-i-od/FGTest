from configs.elementsData import ElementsData


class JumpData:
    element_data_home = None
    panel_list = [ElementsData.Panels]
    pop_window_set = {
        "StickerCollectPopEventPanel",
        "MessageBoxPanel"
    }

    panel_dict = {
        "StickerCollectPopEventPanel": {"element_data": ElementsData.StickerCollectPopEventPanel.StickerCollectPopEventPanel,  "close_path": [ElementsData.StickerCollectPopEventPanel.btn_close]},
        "MessageBoxPanel": {"element_data": ElementsData.MessageBoxPanel.MessageBoxPanel, "close_path": [ElementsData.MessageBoxPanel.btn_confirm]},
    }












