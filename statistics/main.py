
from common.basePage import BasePage
from functools import wraps

from statistics import action_parser


def roll(bp, times, rate=1):
    bp.lua_console(f"AutoPerformController:Perform({times}, {rate})")


def fish(bp, fishery,times, use_limited_fish_spot):
    use_limited_fish_spot_str = "false"
    if use_limited_fish_spot:
        use_limited_fish_spot_str = "true"
    cmd = f"FishingController:Simulation({fishery}, {times}, {use_limited_fish_spot_str})"
    bp.lua_console(cmd)


def with_base_page(is_mobile_device=False, serial_number=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            bp = BasePage(is_mobile_device=is_mobile_device, serial_number=serial_number)
            try:
                # 将bp作为第一个参数传递给被装饰的函数
                return func(bp, *args, **kwargs)
            finally:
                pass
                # # 将CSValidateActionsMsg解析的简短一些
                # if bp.was_roll:
                #     action_parser.parser_roll_actions()
                #     # 直到接收到客户端打印的已执行完毕的结束标志，timeout最大保持连接时间单位s
                #     bp.receive_until_get_msg(msg_key="已执行完毕", timeout=1000)
                #     bp.sleep(10)

                bp.connect_close()
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
    times = 1
    # # # # 骰子模拟
    # roll(bp, times=times, rate=10)
    # # 保持连接次数越多sleep越久
    # bp.sleep(10)
    # # CSValidateActionsMsg解析其中的roll heist atk_building相关内容
    # action_parser.parser_roll_actions()

    # 钓鱼模拟
    fish(bp, fishery=400301, times=times, use_limited_fish_spot=False)
    # 保持连接次数越多sleep越久
    bp.sleep(3)
    # CSValidateActionsMsg解析其中的cast hook相关内容
    action_parser.parser_fish_actions()



if __name__ == '__main__':
    main()
