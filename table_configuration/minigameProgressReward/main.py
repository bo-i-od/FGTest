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
            "progress_node_list":
                [{'point': 440, 'pointStart': 0, 'pointEnd': 2200, 'forceMoveOut': 1},
                 {'point': 1265, 'pointStart': 440, 'pointEnd': 2640, 'forceMoveOut': 1},
                 {'point': 2480, 'pointStart': 1265, 'pointEnd': 3465, 'forceMoveOut': 1},
                 {'point': 3920, 'pointStart': 2480, 'pointEnd': 4940},
                 {'point': 6400, 'pointStart': 3090, 'pointEnd': 6400, 'grandPrize': 1},
                 {'point': 8000, 'pointStart': 6400, 'pointEnd': 15240, 'forceMoveOut': 1},
                 {'point': 10800, 'pointStart': 8000, 'pointEnd': 16840, 'forceMoveOut': 1},
                 {'point': 13600, 'pointStart': 10800, 'pointEnd': 19640, 'forceMoveOut': 1},
                 {'point': 18800, 'pointStart': 13600, 'pointEnd': 22440, 'forceMoveOut': 1},
                 {'point': 23200, 'pointStart': 18800, 'pointEnd': 28610},
                 {'point': 30720, 'pointStart': 19840, 'pointEnd': 30720, 'grandPrize': 1}]
        },
        2: {
            "csv": ["rewards_drop_2_2.csv"],
            "progress_node_list":
                [{'point': 380, 'pointStart': 0, 'pointEnd': 2010, 'forceMoveOut': 1},
                 {'point': 1090, 'pointStart': 380, 'pointEnd': 2390, 'forceMoveOut': 1},
                 {'point': 2150, 'pointStart': 1090, 'pointEnd': 3100, 'forceMoveOut': 1},
                 {'point': 3390, 'pointStart': 2150, 'pointEnd': 4160, 'forceMoveOut': 1},
                 {'point': 4620, 'pointStart': 3390, 'pointEnd': 5580},
                 {'point': 6400, 'pointStart': 3740, 'pointEnd': 6400, 'grandPrize': 1},
                 {'point': 7400, 'pointStart': 6400, 'pointEnd': 14050, 'forceMoveOut': 1},
                 {'point': 9450, 'pointStart': 7400, 'pointEnd': 15050, 'forceMoveOut': 1},
                 {'point': 11360, 'pointStart': 9450, 'pointEnd': 17100, 'forceMoveOut': 1},
                 {'point': 14260, 'pointStart': 11360, 'pointEnd': 19010, 'forceMoveOut': 1},
                 {'point': 17600, 'pointStart': 14260, 'pointEnd': 21910, 'forceMoveOut': 1},
                 {'point': 22610, 'pointStart': 17600, 'pointEnd': 25780},
                 {'point': 30720, 'pointStart': 19020, 'pointEnd': 30720, 'grandPrize': 1}]
        },
        3: {
            "csv": ["rewards_drop_2_3.csv"],
            "progress_node_list":
                [{'point': 450, 'pointStart': 0, 'pointEnd': 2830, 'forceMoveOut': 1},
                 {'point': 1210, 'pointStart': 450, 'pointEnd': 3280, 'forceMoveOut': 1},
                 {'point': 2330, 'pointStart': 1210, 'pointEnd': 4040, 'forceMoveOut': 1},
                 {'point': 4250, 'pointStart': 2330, 'pointEnd': 5750},
                 {'point': 7660, 'pointStart': 3050, 'pointEnd': 7660, 'grandPrize': 1},
                 {'point': 8620, 'pointStart': 7660, 'pointEnd': 14720, 'forceMoveOut': 1},
                 {'point': 10320, 'pointStart': 8620, 'pointEnd': 15680, 'forceMoveOut': 1},
                 {'point': 12490, 'pointStart': 10320, 'pointEnd': 17380, 'forceMoveOut': 1},
                 {'point': 15320, 'pointStart': 12490, 'pointEnd': 19550, 'forceMoveOut': 1},
                 {'point': 19560, 'pointStart': 15320, 'pointEnd': 22380, 'forceMoveOut': 1},
                 {'point': 23660, 'pointStart': 19560, 'pointEnd': 26970},
                 {'point': 30720, 'pointStart': 20820, 'pointEnd': 30720, 'grandPrize': 1}]
        },
        4: {
            "csv": ["rewards_juggle_2_1.csv"],
            "progress_node_list":
                [{'point': 450, 'pointStart': 0, 'pointEnd': 3910, 'forceMoveOut': 1},
                 {'point': 1000, 'pointStart': 450, 'pointEnd': 4360, 'forceMoveOut': 1},
                 {'point': 2480, 'pointStart': 1000, 'pointEnd': 4910, 'forceMoveOut': 1},
                 {'point': 5500, 'pointStart': 2480, 'pointEnd': 6580},
                 {'point': 9000, 'pointStart': 3970, 'pointEnd': 9000, 'grandPrize': 1},
                 {'point': 10300, 'pointStart': 9000, 'pointEnd': 14940, 'forceMoveOut': 1},
                 {'point': 11690, 'pointStart': 10300, 'pointEnd': 16240, 'forceMoveOut': 1},
                 {'point': 13370, 'pointStart': 11690, 'pointEnd': 17630, 'forceMoveOut': 1},
                 {'point': 15500, 'pointStart': 13370, 'pointEnd': 19310, 'forceMoveOut': 1},
                 {'point': 18330, 'pointStart': 15500, 'pointEnd': 21440, 'forceMoveOut': 1},
                 {'point': 22260, 'pointStart': 18330, 'pointEnd': 25040},
                 {'point': 27900, 'pointStart': 20560, 'pointEnd': 27900, 'grandPrize': 1}]
        },
        5: {
            "csv": ["rewards_juggle_2_2.csv"],
            "progress_node_list":
                [{'point': 380, 'pointStart': 0, 'pointEnd': 1720, 'forceMoveOut': 1},
                 {'point': 930, 'pointStart': 380, 'pointEnd': 2100, 'forceMoveOut': 1},
                 {'point': 1680, 'pointStart': 930, 'pointEnd': 2650, 'forceMoveOut': 1},
                 {'point': 2810, 'pointStart': 1680, 'pointEnd': 3570},
                 {'point': 4650, 'pointStart': 2000, 'pointEnd': 4650, 'grandPrize': 1},
                 {'point': 5210, 'pointStart': 4650, 'pointEnd': 8020, 'forceMoveOut': 1},
                 {'point': 6030, 'pointStart': 5210, 'pointEnd': 8580, 'forceMoveOut': 1},
                 {'point': 7080, 'pointStart': 6030, 'pointEnd': 9400, 'forceMoveOut': 1},
                 {'point': 8510, 'pointStart': 7080, 'pointEnd': 10450, 'forceMoveOut': 1},
                 {'point': 10630, 'pointStart': 8510, 'pointEnd': 12140},
                 {'point': 13950, 'pointStart': 9070, 'pointEnd': 13950, 'grandPrize': 1},
                 {'point': 14950, 'pointStart': 13950, 'pointEnd': 18290, 'forceMoveOut': 1},
                 {'point': 16210, 'pointStart': 14950, 'pointEnd': 19290, 'forceMoveOut': 1},
                 {'point': 17810, 'pointStart': 16210, 'pointEnd': 20550, 'forceMoveOut': 1},
                 {'point': 19980, 'pointStart': 17810, 'pointEnd': 22150, 'forceMoveOut': 1},
                 {'point': 23120, 'pointStart': 19980, 'pointEnd': 25100},
                 {'point': 27900, 'pointStart': 21630, 'pointEnd': 27900, 'grandPrize': 1}]
        },
        6: {
            "csv": ["rewards_juggle_2_3.csv"],
            "progress_node_list":
                [{'point': 300, 'pointStart': 0, 'pointEnd': 1700, 'forceMoveOut': 1},
                 {'point': 930, 'pointStart': 300, 'pointEnd': 2000, 'forceMoveOut': 1},
                 {'point': 1700, 'pointStart': 930, 'pointEnd': 2630, 'forceMoveOut': 1},
                 {'point': 2860, 'pointStart': 1700, 'pointEnd': 3500},
                 {'point': 4700, 'pointStart': 2210, 'pointEnd': 4700, 'grandPrize': 1},
                 {'point': 5230, 'pointStart': 4700, 'pointEnd': 7670, 'forceMoveOut': 1},
                 {'point': 6000, 'pointStart': 5230, 'pointEnd': 8200, 'forceMoveOut': 1},
                 {'point': 7030, 'pointStart': 6000, 'pointEnd': 8970, 'forceMoveOut': 1},
                 {'point': 8500, 'pointStart': 7030, 'pointEnd': 10000, 'forceMoveOut': 1},
                 {'point': 10600, 'pointStart': 8500, 'pointEnd': 11910},
                 {'point': 13700, 'pointStart': 9120, 'pointEnd': 13700, 'grandPrize': 1},
                 {'point': 14660, 'pointStart': 13700, 'pointEnd': 18010, 'forceMoveOut': 1},
                 {'point': 15900, 'pointStart': 14660, 'pointEnd': 18970, 'forceMoveOut': 1},
                 {'point': 17500, 'pointStart': 15900, 'pointEnd': 20210, 'forceMoveOut': 1},
                 {'point': 19660, 'pointStart': 17500, 'pointEnd': 21810, 'forceMoveOut': 1},
                 {'point': 22860, 'pointStart': 19660, 'pointEnd': 24530},
                 {'point': 27900, 'pointStart': 20560, 'pointEnd': 27900, 'grandPrize': 1}]
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
    point_progress_reward(excel_tool=excel_tool, point_progress_reward_id=progress_reward_id, rewards_csv_list=rewards_csv_list,progress_node_list=progress_node_list, token_id=token_id, notes=notes)
    minigame_progress_reward(excel_tool=excel_tool,minigame_progress_reward_id=progress_reward_id, progress_node_list=progress_node_list, notes=notes)



if __name__ == '__main__':
    main()