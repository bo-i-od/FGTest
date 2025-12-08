from common.basePage import BasePage
from panelObjs.HomePanel import HomePanel
from panelObjs.Panel_steal import Panel_steal


def main():
    bp = BasePage(is_mobile_device=False, serial_number="b6h65hd64p5pxcyh")
    # circulate_fish(bp=bp, is_quick=True, fishery_id=400301)
    # fish_once(bp=bp, is_quick=True)
    # bp.cmd("add 1 101341 1000")
    while True:
        bp.cmd("mode 5 5")
        HomePanel.navbar.click_btn_start(bp)

        if Panel_steal.is_panel_active(bp):
            Panel_steal.steal(bp)
            continue



    # bp.connect_close()


if __name__ == '__main__':
    main()