from configs.pathConfig import DEV_EXCEL_PATH
from table_configuration.decl.ITEM_PACKAGE import ITEM_PACKAGE
from table_configuration.decl.POINT_PROGRESS_REWARD import POINT_PROGRESS_REWARD
from tools.decl2py import json_to_instance, json_list_to_instance_list
from tools.excelRead import ExcelToolsForActivities


back_data_list = [
    {"cost": 3000, "dice_chess": 0.18, "dice_process": 0.2, "dice_championship_p": 0.1,"dice_championship_r": 0.03, "dice_minigame": 0.1,
     "dice_card": 0.03, "dice_build": 0.02, "dice_buff": 0.1, "money_chess": 1, "money_process": 0.2, "money_championship_p": 0.2,"money_championship_r": 0.03,
     "money_minigame": 0.08, "money_card": 0.03, "money_build": 0.05, "money_buff_1": 0.025, "money_buff_2": 0.025},
    {"cost": 10000, "dice_chess": 0.18, "dice_process": 0.2, "dice_championship_p": 0.09, "dice_championship_r": 0.03, "dice_minigame": 0.1,
     "dice_card": 0.04, "dice_build": 0.02,"dice_buff": 0.1, "money_chess": 1, "money_process": 0.15, "money_championship_p": 0.15,"money_championship_r": 0.03,
     "money_minigame": 0.08, "money_card": 0.04, "money_build": 0.05, "money_buff_1": 0.025, "money_buff_2": 0.025},
    {"cost": 50000, "dice_chess": 0.18, "dice_process": 0.16, "dice_championship_p": 0.08,"dice_championship_r": 0.02, "dice_minigame": 0.1,
    "dice_card": 0.05, "dice_build": 0.02, "dice_buff": 0.1, "money_chess": 1, "money_process": 0.1, "money_championship_p": 0.1,"money_championship_r": 0.02,
     "money_minigame": 0.08, "money_card": 0.05, "money_build": 0.05, "money_buff_1": 0.025, "money_buff_2": 0.025},
]

def get_back_rate_dice(daily_cost, system_key=None):
    back_rate_dice = 0
    if daily_cost <= 3000:
        back_data = back_data_list[0]
        for data in back_data:
            if "dice" not in data:
                continue
            if system_key and system_key not in data:
                continue
            back_rate_dice += back_data[data]
        return back_rate_dice
    if daily_cost <= 10000:
        back_data_pre = back_data_list[0]
        back_data_cur = back_data_list[1]
        progress = (daily_cost - 3000) / (10000 - 3000)
        for data in back_data_pre:
            if "dice" not in data:
                continue
            if system_key and system_key not in data:
                continue
            back_rate_dice += back_data_pre[data] * (1-progress)

        for data in back_data_cur:
            if "dice" not in data:
                continue
            if system_key and system_key not in data:
                continue
            back_rate_dice += back_data_cur[data] * progress
        return back_rate_dice
    if daily_cost <= 20000:
        back_data_pre = back_data_list[1]
        back_data_cur = back_data_list[2]
        progress = (daily_cost - 10000) / (50000 - 10000)
        for data in back_data_pre:
            if "dice" not in data:
                continue
            if system_key and system_key not in data:
                continue
            back_rate_dice += back_data_pre[data] * (1-progress)

        for data in back_data_cur:
            if "dice" not in data:
                continue
            if system_key and system_key not in data:
                continue
            back_rate_dice += back_data_cur[data] * progress
        return back_rate_dice
    if daily_cost <= 50000:
        back_data_pre = back_data_list[1]
        back_data_cur = back_data_list[2]
        progress = (daily_cost - back_data_pre["cost"]) / (back_data_cur["cost"] - back_data_pre["cost"])
        for data in back_data_pre:
            if "dice" not in data:
                continue
            if system_key and system_key not in data:
                continue
            back_rate_dice += back_data_pre[data] * (1-progress)
        if system_key in ["dice_minigame"]:
            return 0
        back_rate_dice -= back_data_pre["dice_minigame"] * (1-progress)
        return back_rate_dice
    back_data = back_data_list[2]
    for data in back_data:
        if "dice" not in data:
            continue
        if system_key and system_key not in data:
            continue
        back_rate_dice += back_data[data]
    if system_key in ["dice_minigame", "dice_championship_p", "dice_process"]:
        return 0

    back_rate_dice -= back_data["dice_minigame"]
    back_rate_dice -= back_data["dice_championship_p"]
    back_rate_dice -= back_data["dice_process"]
    return back_rate_dice

def get_back_dice(daily_cost, system_key=None):
    """
    通过日耗得到骰子返还数量
    :param daily_cost:
    :param system_key:
    :return:
    """
    if daily_cost <= 20000:
        return get_back_rate_dice(daily_cost, system_key=system_key) * daily_cost
    if daily_cost <= 50000:
        return get_back_dice(20000, system_key=system_key) + get_back_rate_dice(daily_cost, system_key=system_key) * (daily_cost - 20000)
    return get_back_dice(50000, system_key=system_key) + get_back_rate_dice(daily_cost, system_key=system_key) * (daily_cost - 50000)

# def get_back_dice_by_key(daily_cost):
#     get_back_rate_dice()

def get_net_loss(daily_cost):
    """
    通过日耗反推净消耗
    :param daily_cost: 日耗
    :return:
    """
    net_loss = daily_cost - get_back_dice(daily_cost)
    return net_loss

def get_net_net_loss(daily_cost, daily_output):
    """
    通过日耗反推净净消耗
    :param daily_cost: 日耗
    :param daily_output: 每日固定获得骰子
    :return:
    """
    net_loss = get_net_loss(daily_cost)
    net_net_loss = net_loss - daily_output
    return net_net_loss


def find_daily_cost_by_net_net_loss(target_net_net_loss, daily_output, low=0, high=200000, tolerance=1e-6):
    """
    通过二分查找，根据目标净净亏损反向求解每日消费。

    :param target_net_net_loss: 目标净净亏损值。
    :param daily_output: 每日产出（固定值）。
    :param low: 搜索范围的下限。
    :param high: 搜索范围的上限。
    :param tolerance: 求解的精度。
    :return: 计算得出的每日消费 (daily_cost)。
    """

    # 检查目标值是否在搜索范围内
    min_loss = get_net_net_loss(low, daily_output=daily_output)
    if target_net_net_loss < min_loss:
        print(f"警告: 目标亏损 {target_net_net_loss} 低于搜索下限 {low} 对应的亏损 {min_loss}。可能无解或解为 {low}。")
        return low

    max_loss = get_net_net_loss(high, daily_output=daily_output)
    if target_net_net_loss > max_loss:
        print(
            f"警告: 目标亏损 {target_net_net_loss} 高于搜索上限 {high} 对应的亏损 {max_loss}。请尝试提高搜索上限 'high'。")
        return high

    # 二分查找
    while high - low > tolerance:
        mid = (low + high) / 2
        # 如果中间值是0，避免无限循环
        if mid == low or mid == high:
            break

        current_loss = get_net_net_loss(mid, daily_output=daily_output)

        if current_loss < target_net_net_loss:
            # 当前猜测的cost太小，亏损不够，需要增加cost
            low = mid
        else:
            # 当前猜测的cost太大或正好，亏损超了，需要减小cost
            high = mid

    return (low + high) / 2

def get_minigame_coin_count(excel_tool: ExcelToolsForActivities,value_multil, id_progress_progress, id_championship_progress, progress_progress, championship_progress,day_progress, day_championship):
    point_progress_reward_detail = excel_tool.get_table_data_detail(book_name="POINT_PROGRESS_REWARD.xlsm")
    key = "id"
    progress_progress_object: POINT_PROGRESS_REWARD
    championship_progress_object: POINT_PROGRESS_REWARD
    progress_progress_object = json_to_instance(json_object=excel_tool.get_table_data_by_key_value(key=key, value=id_progress_progress, table_data_detail=point_progress_reward_detail), cls=POINT_PROGRESS_REWARD)
    championship_progress_object = json_to_instance(json_object=excel_tool.get_table_data_by_key_value(key=key, value=id_championship_progress, table_data_detail=point_progress_reward_detail), cls=POINT_PROGRESS_REWARD)
    minigame_coin_count_progress = 0
    point_max_progress = 0
    cur = 0
    while cur < len(progress_progress_object.progressRewards):
        if progress_progress_object.progressRewards[cur].point is None:
            break
        point_max_progress = progress_progress_object.progressRewards[cur].point
        cur += 1
    cur = 0
    while cur < len(progress_progress_object.progressRewards):
        reward = progress_progress_object.progressRewards[cur]
        if reward.tpId != 9700001:
            cur += 1
            continue

        if progress_progress < reward.point/ point_max_progress:
            break
        # minigame_coin_count_progress += int(reward.count * value_multil + 1)
        minigame_coin_count_progress += reward.count * value_multil
        cur += 1

    point_max_championship = 0
    cur = 0
    while cur < len(championship_progress_object.progressRewards):
        if championship_progress_object.progressRewards[cur].point is None:
            break
        point_max_championship = int(championship_progress_object.progressRewards[cur].point + 1)
        cur += 1
    minigame_coin_count_championship = 0

    cur = 0
    while cur < len(championship_progress_object.progressRewards):
        reward = championship_progress_object.progressRewards[cur]
        if reward.tpId != 9700001:
            cur += 1
            continue
        if championship_progress < reward.point / point_max_championship:
            break
        # minigame_coin_count_championship += int(reward.count * value_multil + 1)
        minigame_coin_count_championship += int(reward.count * value_multil + 1)
        cur += 1
    return minigame_coin_count_progress/day_progress + minigame_coin_count_championship/day_championship

def get_task_output_minigame_coin(excel_tool: ExcelToolsForActivities, value_multil):
    item_package_detail = excel_tool.get_table_data_detail(book_name="ITEM_PACKAGE.xlsm")
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="name", value="每日任务礼盒", table_data_detail=item_package_detail)
    instance_list = json_list_to_instance_list(json_object_list=json_object_list, cls=ITEM_PACKAGE)
    minigame_coin = 0
    for instance_object in instance_list:
        instance_object: ITEM_PACKAGE
        for packageItem in instance_object.packageItem:
            if packageItem.rewardid != 9700001:
                continue
            minigame_coin += int(packageItem.count * value_multil + 1)
    return minigame_coin


def main():
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)

    value_multil = 0.4
    minigame_coin_cost_per_day = 500

    daily_output = 360

    daily_output_minigame_coin = get_task_output_minigame_coin(excel_tool=excel_tool, value_multil=value_multil) + 50 * value_multil

    # net_net_loss_list = [0,500,750,2000,6690,10000,14865,30000,34640]
    net_net_loss_list = [0,100, 200, 300, 500,750,1000,1500,2000,3000,4690,5000,7500,10000,12500,15000,20000,30000]


    print(f"骰子每日充值获取：{net_net_loss_list}")
    res = {}
    daily_cost_progress_complete = 50000
    daily_cost_championship_complete = 50000
    # daily_cost_minigame_complete = 20000

    for net_net_loss in net_net_loss_list:
        res[net_net_loss] = {}
        daily_cost = find_daily_cost_by_net_net_loss(target_net_net_loss=net_net_loss, daily_output=daily_output)
        daily_cost = int(daily_cost)

        progress_progress = min(daily_cost/daily_cost_progress_complete, 1)
        championship_progress = min(daily_cost/daily_cost_championship_complete, 1)
        # minigame_progress = min(daily_cost/daily_cost_minigame_complete, 1)
        # minigame_dice_back = get_back_dice(daily_cost=daily_cost, system_key="dice_minigame")
        # minigame_dice_back = int(minigame_dice_back)
        # minigame_dice_back_rate = minigame_dice_back / daily_cost

        res[net_net_loss]["日常产出"] = daily_output
        res[net_net_loss]["骰子日耗"] = daily_cost
        res[net_net_loss]["进度条进度"] = progress_progress
        res[net_net_loss]["锦标赛进度"] = championship_progress
        if res[net_net_loss]["骰子日耗"] == 20000:
            print(f"进度条进度:{progress_progress}, 锦标赛进度:{championship_progress}")

        # res[net_net_loss]["minigame进度"] = minigame_progress
        # res[net_net_loss]["minigame每日返还骰子"] = minigame_dice_back
        # res[net_net_loss]["minigame两日返还骰子"] = minigame_dice_back * 2
        # res[net_net_loss]["minigame三日返还骰子"] = minigame_dice_back * 3
        # res[net_net_loss]["minigame返还骰子比例"] = minigame_dice_back_rate

    # print(res)

    # 根据进度条进度和锦标赛进度得到每日获取minigame代币
    # 然后根据日耗可以求得minigame每日返还骰子和minigame返还骰子比例

    for item in res:
        progress_progress = res[item]["进度条进度"]
        championship_progress = res[item]["锦标赛进度"]
        # minigame_coin_count_list = get_minigame_coin_count(bb=bb, progress_progress=progress_progress, championship_progress=championship_progress)
        # 加权算个平均获得
        # minigame_coin_count = 0.5 * minigame_coin_count_list[0] + 0.5 * minigame_coin_count_list[1] + 0.5 * minigame_coin_count_list[2]+ 0.5 * minigame_coin_count_list[3]
        # minigame_coin_count = minigame_coin_count_list[0] +  minigame_coin_count_list[3]
        minigame_coin_count = get_minigame_coin_count(excel_tool=excel_tool, value_multil=value_multil,
                                                      id_progress_progress=101, id_championship_progress=201,
                                                      progress_progress=progress_progress,
                                                      championship_progress=championship_progress,
                                                      day_progress=2, day_championship=1)


        # 加上日常获取
        minigame_coin_count += daily_output_minigame_coin
        print(minigame_coin_count)

        # 加上minigame自身返还
        minigame_coin_count *= 1.1
        res[item]["每日获取minigame代币"] = int(minigame_coin_count + 0.5)
        res[item]["两日获取minigame代币"] = res[item]["每日获取minigame代币"] * 2
        res[item]["三日获取minigame代币"] = res[item]["每日获取minigame代币"] * 3
        res[item]["minigame进度"] = res[item]["每日获取minigame代币"] / minigame_coin_cost_per_day
        minigame_dice_back = int(get_back_dice(daily_cost=res[item]["骰子日耗"], system_key="dice_minigame"))
        res[item]["minigame每日返还骰子"] = minigame_dice_back
        res[item]["minigame两日返还骰子"] = minigame_dice_back * 2
        res[item]["minigame三日返还骰子"] = minigame_dice_back * 3
        res[item]["minigame返还骰子比例"] = minigame_dice_back / res[item]["骰子日耗"]
        print(f'骰子日耗：{res[item]["骰子日耗"]} minigame进度：{res[item]["minigame进度"]} minigame两日返还骰子：{res[item]["minigame两日返还骰子"]}')

    # print(res)

    # net_net_loss = 30000

    # daily_cost = find_daily_cost_by_net_net_loss(target_net_net_loss=net_net_loss, daily_output=daily_output)
    # print(daily_cost)
    # back_dice = get_back_dice(daily_cost=1000, system_key="dice_minigame")
    # print(back_dice)
    # a = get_net_net_loss(daily_output=daily_output,daily_cost=50000)
    # print(a)

    # cur = 0
    # while cur < len(back_data_list):
    #
    #     cur += 1


if __name__ == "__main__":

    main()