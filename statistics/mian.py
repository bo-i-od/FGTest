import math

from common.basePage import BasePage
from functools import wraps

from statistics import roll_action_parser


def roll(bp, times, rate=1):
    bp.lua_console(f"AutoPerformController:Perform({times}, {rate})")


def with_base_page(is_mobile_device=False, serial_number=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            bp = BasePage(is_mobile_device=is_mobile_device, serial_number=serial_number)
            try:
                # 将bp作为第一个参数传递给被装饰的函数
                return func(bp, *args, **kwargs)
            finally:
                # 直到接收到客户端打印的已执行完毕的结束标志，timeout最大保持连接时间单位s
                bp.receive_until_get_msg(msg_key="已执行完毕", timeout=1000)
                bp.sleep(10)
                # 将CSValidateActionsMsg解析的简短一些
                roll_action_parser.main()
        return wrapper
    return decorator


def clear_log():
    f = open(f"../statistics/cs_validate_actions_msg_log.txt", "w")
    f.close()
    f = open(f"../statistics/sc_validate_actions_msg_log.txt", "w")
    f.close()


@with_base_page()
def main(bp: BasePage):
    # 清空记录validate_actions_msg_log
    clear_log()

    times = 100
    roll(bp, times=times, rate=1)




if __name__ == '__main__':
    main()
