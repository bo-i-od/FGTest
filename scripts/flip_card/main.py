from common.basePage import BasePage
from panelObjs.FlipCardPanel import FlipCardPanel


def main():
    times = 10000
    bp = BasePage()
    cur = 0
    while cur < times:
        # bp.lua_console("FlipCardMiniGameController:DbgNext()")
        # bp.clear_popup()
        # cur += 1
        bp.clear_popup()
        bp.sleep(1)
        FlipCardPanel.click_go_or_card(bp)


    bp.connect_close()


if __name__ == '__main__':
    main()