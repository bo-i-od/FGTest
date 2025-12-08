from common.basePage import BasePage


def main():
    bp = BasePage(serial_number="127.0.0.1:21513", is_mobile_device=False)
    # bp.lua_console("DebugLog=true")
    # chess_position = bp.get_chess_position()
    # print(chess_position)
    res = bp.get_chess_position()
    bp.connect_close()





if __name__ == '__main__':
    main()
