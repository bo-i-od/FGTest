from table_configuration.decl.MINIGAME_PROGRESS_REWARD import MINIGAME_PROGRESS_REWARD, MINIGAME_PROGRESS_REWARD_DETAIL
from common.error import DifferError
from configs.pathConfig import DEV_EXCEL_PATH
from table_configuration.decl.POINT_PROGRESS_REWARD import PROGRESS_REWARD, POINT_PROGRESS_REWARD
from table_configuration.minigameCommon.common_reward import get_rewards_list
from tools.decl2py import json_to_instance
from tools.excelRead import ExcelToolsForActivities


def point_progress_reward(excel_tool: ExcelToolsForActivities,point_progress_reward_id, rewards_csv_list,progress_node_list, token_id, notes):
    point_progress_reward_detail = excel_tool.get_table_data_detail(book_name="POINT_PROGRESS_REWARD.xlsm")
    key = "id"
    json_list = excel_tool.get_table_data_list_by_key_value(key=key, value=point_progress_reward_id, table_data_detail=point_progress_reward_detail)
    if json_list:
        mode = 2
        instance_object = json_to_instance(json_object=json_list[0], cls=POINT_PROGRESS_REWARD)
    else:
        mode = 1
        instance_object = POINT_PROGRESS_REWARD()


    instance_object.id = point_progress_reward_id
    instance_object.name = notes
    instance_object.tokenResourceId = token_id + 8000
    instance_object.progressType = 4
    instance_object.progressRewards = []
    rewards_list = get_rewards_list(excel_tool=excel_tool, rewards_csv_list=rewards_csv_list, token_id=token_id, notes=notes)
    rewards = rewards_list[0]
    if len(rewards) != len(progress_node_list):
        raise DifferError("奖励和积分长度不一致")
    cur = 0
    while cur < len(rewards):
        progress_reward = PROGRESS_REWARD()
        reward = rewards[cur]
        progress_reward.count = reward.count
        progress_reward.ioIdType = reward.ioIdType
        progress_reward.tpId = reward.tpId
        progress_reward.point = progress_node_list[cur]["point"]
        instance_object.progressRewards.append(progress_reward)
        cur += 1
    while len(instance_object.progressRewards) < 65:
        instance_object.progressRewards.append(PROGRESS_REWARD())
    print(instance_object)
    if mode == 1:
        excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=point_progress_reward_detail, instance_object=instance_object)
        return instance_object.id
    excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=point_progress_reward_detail, instance_object=instance_object)

def minigame_progress_reward(excel_tool: ExcelToolsForActivities, minigame_progress_reward_id, progress_node_list, notes):
    minigame_progress_reward_detail = excel_tool.get_table_data_detail(book_name="MINIGAME_PROGRESS_REWARD.xlsm")
    key = "id"
    json_object_list = excel_tool.get_table_data_list_by_key_value(key=key, value=minigame_progress_reward_id, table_data_detail=minigame_progress_reward_detail)
    if json_object_list:
        mode = 2
        instance_object = json_to_instance(json_object=json_object_list[0], cls=MINIGAME_PROGRESS_REWARD)
    else:
        mode = 1
        instance_object = MINIGAME_PROGRESS_REWARD()
    instance_object.id = minigame_progress_reward_id
    instance_object.name = notes
    instance_object.hideFactor = 85
    instance_object.progressRewardsDetail = []
    cur = 0
    while cur < len(progress_node_list):
        progress_reward_detail = MINIGAME_PROGRESS_REWARD_DETAIL()
        progress_reward_detail.pointStart = progress_node_list[cur]["pointStart"]
        progress_reward_detail.pointEnd = progress_node_list[cur]["pointEnd"]
        progress_reward_detail.grandPrize = 0
        progress_reward_detail.forceMoveOut = 0
        if "forceMoveOut" in progress_node_list[cur]:
            progress_reward_detail.forceMoveOut = progress_node_list[cur]["forceMoveOut"]
        if "grandPrize" in progress_node_list[cur]:
            progress_reward_detail.grandPrize = progress_node_list[cur]["grandPrize"]

        instance_object.progressRewardsDetail.append(progress_reward_detail)
        cur += 1
    while len(instance_object.progressRewardsDetail) < 20:
        instance_object.progressRewardsDetail.append(MINIGAME_PROGRESS_REWARD_DETAIL())
    print(instance_object)
    if mode == 1:
        excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=minigame_progress_reward_detail, instance_object=instance_object)
        return
    excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=minigame_progress_reward_detail, instance_object=instance_object)

def main():
    index = 1
    bias = 6
    progress_reward_id = 30300 + index
    token_id = 101330 + index
    notes = f"minigame翻牌-进度条-第{index}套"
    id_2_rewards_detail = {
        1: {
            "csv": ["rewards_drop_2_1.csv"],
            "progress_node_list": [
                {"point": 440, "pointStart":0, "pointEnd": 2800, "forceMoveOut": 1},
                {"point": 1265, "pointStart": 440, "pointEnd": 3240, "forceMoveOut": 1},
                {"point": 2480, "pointStart": 1265, "pointEnd": 4065, "forceMoveOut": 1},
                {"point": 3920, "pointStart": 2000, "pointEnd": 5000},
                {"point": 6400, "pointStart": 3000, "pointEnd": 6400, "grandPrize": 1},
                {"point": 8000, "pointStart": 6400, "pointEnd": 16400, "forceMoveOut": 1},
                {"point": 10800, "pointStart": 8000, "pointEnd": 18000, "forceMoveOut": 1},
                {"point": 13600, "pointStart": 10800, "pointEnd": 20800, "forceMoveOut": 1},
                {"point": 18800, "pointStart": 13600, "pointEnd": 23100, "forceMoveOut": 1},
                {"point": 23200, "pointStart": 16400, "pointEnd": 26400},
                {"point": 30720, "pointStart": 18400, "pointEnd": 30720,"grandPrize": 1}
            ]
        },
        2: {
            "csv": ["rewards_drop_3_1.csv"],
            "progress_node_list": [
                {"point": 570, "pointStart": 0, "pointEnd": 4000, "forceMoveOut": 1},
                {"point": 1645, "pointStart": 570, "pointEnd": 4570, "forceMoveOut": 1},
                {"point": 3220, "pointStart": 1645, "pointEnd": 5645, "forceMoveOut": 1},
                {"point": 5090, "pointStart": 3220, "pointEnd": 7220, "forceMoveOut": 1},
                {"point": 6935, "pointStart": 5090, "pointEnd": 9600},
                {"point": 9600, "pointStart": 5090, "pointEnd": 9600, "grandPrize": 1},
                {"point": 11100, "pointStart": 9600, "pointEnd": 19600, "forceMoveOut": 1},
                {"point": 14185, "pointStart": 11100, "pointEnd": 21100, "forceMoveOut": 1},
                {"point": 17040, "pointStart": 14185, "pointEnd": 24185, "forceMoveOut": 1},
                {"point": 21400, "pointStart": 17040, "pointEnd": 27040, "forceMoveOut": 1},
                {"point": 26400, "pointStart": 21400, "pointEnd": 31400, "forceMoveOut": 1},
                {"point": 33920, "pointStart": 23400, "pointEnd": 39000},
                {"point": 46080, "pointStart": 27000, "pointEnd": 46080, "grandPrize": 1},
            ]
        },
        3: {
            "csv": ["rewards_drop_3_2.csv"],
            "progress_node_list": [
                {"point": 680, "pointStart": 0, "pointEnd": 4000, "forceMoveOut": 1},
                {"point": 1825, "pointStart": 680, "pointEnd": 4680, "forceMoveOut": 1},
                {"point": 3500, "pointStart": 1825, "pointEnd": 5825, "forceMoveOut": 1},
                {"point": 6380, "pointStart": 3500, "pointEnd": 7500, "forceMoveOut": 1},
                {"point": 11500, "pointStart": 5000, "pointEnd": 11500, "grandPrize": 1},
                {"point": 12950, "pointStart": 11500, "pointEnd": 19500, "forceMoveOut": 1},
                {"point": 15500, "pointStart": 12950, "pointEnd": 20950, "forceMoveOut": 1},
                {"point": 18750, "pointStart": 15500, "pointEnd": 23500, "forceMoveOut": 1},
                {"point": 23000, "pointStart": 18750, "pointEnd": 26750, "forceMoveOut": 1},
                {"point": 29350, "pointStart": 23000, "pointEnd": 33000, "forceMoveOut": 1},
                {"point": 35500, "pointStart": 29350, "pointEnd": 41000},
                {"point": 46080, "pointStart": 32000, "pointEnd": 46080, "grandPrize": 1},
            ]
        },
        4: {
            "csv": ["rewards_juggle_2_1.csv"],
            "progress_node_list":
                [{'point': 450, 'pointStart': 0, 'pointEnd': 3600, 'forceMoveOut': 1},
                 {'point': 1000, 'pointStart': 450, 'pointEnd': 4050, 'forceMoveOut': 1},
                 {'point': 2480, 'pointStart': 1000, 'pointEnd': 4600, 'forceMoveOut': 1},
                 {'point': 5500, 'pointStart': 2480, 'pointEnd': 6260},
                 {'point': 9000, 'pointStart': 4360, 'pointEnd': 9000, 'grandPrize': 1},
                 {'point': 10300, 'pointStart': 9000, 'pointEnd': 15340, 'forceMoveOut': 1},
                 {'point': 11690, 'pointStart': 10300, 'pointEnd': 16640, 'forceMoveOut': 1},
                 {'point': 13370, 'pointStart': 11690, 'pointEnd': 18030, 'forceMoveOut': 1},
                 {'point': 15500, 'pointStart': 13370, 'pointEnd': 19710, 'forceMoveOut': 1},
                 {'point': 18330, 'pointStart': 15500, 'pointEnd': 21840, 'forceMoveOut': 1},
                 {'point': 22260, 'pointStart': 18330, 'pointEnd': 25430},
                 {'point': 27900, 'pointStart': 19720, 'pointEnd': 27900, 'grandPrize': 1}]
        },
        5: {
            "csv": ["rewards_juggle_3_1.csv"],
            "progress_node_list":
                [{'point': 570, 'pointStart': 0, 'pointEnd': 2570, 'forceMoveOut': 1},
                 {'point': 1400, 'pointStart': 570, 'pointEnd': 3140, 'forceMoveOut': 1},
                 {'point': 2530, 'pointStart': 1400, 'pointEnd': 3970, 'forceMoveOut': 1},
                 {'point': 4220, 'pointStart': 2530, 'pointEnd': 5300},
                 {'point': 6975, 'pointStart': 2905, 'pointEnd': 6975, 'grandPrize': 1},
                 {'point': 7825, 'pointStart': 6975, 'pointEnd': 11715, 'forceMoveOut': 1},
                 {'point': 9055, 'pointStart': 7825, 'pointEnd': 12565, 'forceMoveOut': 1},
                 {'point': 10625, 'pointStart': 9055, 'pointEnd': 13795, 'forceMoveOut': 1},
                 {'point': 12775, 'pointStart': 10625, 'pointEnd': 15365, 'forceMoveOut': 1},
                 {'point': 15955, 'pointStart': 12775, 'pointEnd': 17845},
                 {'point': 20925, 'pointStart': 14255, 'pointEnd': 20925, 'grandPrize': 1},
                 {'point': 22425, 'pointStart': 20925, 'pointEnd': 27315, 'forceMoveOut': 1},
                 {'point': 24325, 'pointStart': 22425, 'pointEnd': 28815, 'forceMoveOut': 1},
                 {'point': 26725, 'pointStart': 24325, 'pointEnd': 30715, 'forceMoveOut': 1},
                 {'point': 29975, 'pointStart': 26725, 'pointEnd': 33115, 'forceMoveOut': 1},
                 {'point': 34685, 'pointStart': 29975, 'pointEnd': 37895},
                 {'point': 41850, 'pointStart': 31170, 'pointEnd': 41850, 'grandPrize': 1}]
        },
        6: {
            "csv": ["rewards_juggle_3_2.csv"],
            "progress_node_list":
                [{'point': 450, 'pointStart': 0, 'pointEnd': 2500, 'forceMoveOut': 1},
                 {'point': 1400, 'pointStart': 450, 'pointEnd': 2950, 'forceMoveOut': 1},
                 {'point': 2550, 'pointStart': 1400, 'pointEnd': 3900, 'forceMoveOut': 1},
                 {'point': 4300, 'pointStart': 2550, 'pointEnd': 5600},
                 {'point': 7050, 'pointStart': 3360, 'pointEnd': 7050, 'grandPrize': 1},
                 {'point': 7850, 'pointStart': 7050, 'pointEnd': 12070, 'forceMoveOut': 1},
                 {'point': 9000, 'pointStart': 7850, 'pointEnd': 12870, 'forceMoveOut': 1},
                 {'point': 10550, 'pointStart': 9000, 'pointEnd': 14020, 'forceMoveOut': 1},
                 {'point': 12750, 'pointStart': 10550, 'pointEnd': 15570, 'forceMoveOut': 1},
                 {'point': 15900, 'pointStart': 12750, 'pointEnd': 18520},
                 {'point': 20550, 'pointStart': 14470, 'pointEnd': 20550, 'grandPrize': 1},
                 {'point': 22000, 'pointStart': 20550, 'pointEnd': 27500, 'forceMoveOut': 1},
                 {'point': 23850, 'pointStart': 22000, 'pointEnd': 28950, 'forceMoveOut': 1},
                 {'point': 26250, 'pointStart': 23850, 'pointEnd': 30800, 'forceMoveOut': 1},
                 {'point': 29500, 'pointStart': 26250, 'pointEnd': 33200, 'forceMoveOut': 1},
                 {'point': 34300, 'pointStart': 29500, 'pointEnd': 36790},
                 {'point': 41850, 'pointStart': 31120, 'pointEnd': 41850, 'grandPrize': 1}]
        },
        7:{
            "csv": ["rewards_flip_2_1.csv"],
            "progress_node_list":
                [{'point': 1420, 'pointStart': 0, 'pointEnd': 16990, 'forceMoveOut': 1},
                 {'point': 3210, 'pointStart': 1420, 'pointEnd': 18410, 'forceMoveOut': 1},
                 {'point': 7890, 'pointStart': 3210, 'pointEnd': 20200, 'forceMoveOut': 1},
                 {'point': 17490, 'pointStart': 7890, 'pointEnd': 24880, 'forceMoveOut': 1},
                 {'point': 28640, 'pointStart': 17490, 'pointEnd': 34480, 'forceMoveOut': 1},
                 {'point': 32820, 'pointStart': 28640, 'pointEnd': 45630, 'forceMoveOut': 1},
                 {'point': 37230, 'pointStart': 32820, 'pointEnd': 49810, 'forceMoveOut': 1},
                 {'point': 42560, 'pointStart': 37230, 'pointEnd': 54220, 'forceMoveOut': 1},
                 {'point': 49350, 'pointStart': 42560, 'pointEnd': 59550, 'forceMoveOut': 1},
                 {'point': 58420, 'pointStart': 49350, 'pointEnd': 66340, 'forceMoveOut': 1},
                 {'point': 70320, 'pointStart': 58420, 'pointEnd': 76590},
                 {'point': 84000, 'pointStart': 65360, 'pointEnd': 84000, 'grandPrize': 1}]
        },

    }
    rewards_csv_list = id_2_rewards_detail[index + bias]["csv"]
    progress_node_list = id_2_rewards_detail[index + bias]["progress_node_list"]
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    # point_progress_reward(excel_tool=excel_tool, point_progress_reward_id=progress_reward_id, rewards_csv_list=rewards_csv_list,progress_node_list=progress_node_list, token_id=token_id, notes=notes)
    minigame_progress_reward(excel_tool=excel_tool,minigame_progress_reward_id=progress_reward_id, progress_node_list=progress_node_list, notes=notes)



if __name__ == '__main__':
    main()