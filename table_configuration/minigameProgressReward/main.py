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
    if point_progress_reward_id is None:
        mode = 1
        point_progress_reward_id = excel_tool.get_min_value_more_than_start(table_object_detail=point_progress_reward_detail, key=key, start=token_id % 1000 * 100 + 1)
    else:
        mode = 2

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
    while len(instance_object.progressRewards) < 62:
        instance_object.progressRewards.append(PROGRESS_REWARD())
    print(instance_object)
    if mode == 1:
        excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=point_progress_reward_detail, instance_object=instance_object)
        return instance_object.id
    excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=point_progress_reward_detail, instance_object=instance_object)
    return instance_object.id
def minigame_progress_reward(excel_tool: ExcelToolsForActivities,point_progress_reward_id, minigame_progress_reward_id, rewards_csv_list,progress_node_list, token_id, notes):
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
    instance_object.pointProgressRewardId = point_progress_reward_id
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
    minigame_progress_reward_id = 1
    point_progress_reward_id = None
    token_id = 101302
    notes = f"minigame进度条第{minigame_progress_reward_id}套"
    id_2_rewards_detail = {
        1: {
            "csv": ["rewards_drop_2_1.csv"],
            "progress_node_list": [
                {"point": 440, "pointStart":0, "pointEnd": 2800, "forceMoveOut": 1},
                {"point": 1264, "pointStart": 440, "pointEnd": 3240, "forceMoveOut": 1},
                {"point": 2480, "pointStart": 1264, "pointEnd": 4064, "forceMoveOut": 1},
                {"point": 3920, "pointStart": 2000, "pointEnd": 5000},
                {"point": 6400, "pointStart": 3000, "pointEnd": 6400, "grandPrize": 1},
                {"point": 8000, "pointStart": 6400, "pointEnd": 16400, "forceMoveOut": 1},
                {"point": 10800, "pointStart": 8000, "pointEnd": 18000, "forceMoveOut": 1},
                {"point": 13600, "pointStart": 10800, "pointEnd": 20800, "forceMoveOut": 1},
                {"point": 18800, "pointStart": 13600, "pointEnd": 23100, "forceMoveOut": 1},
                {"point": 23200, "pointStart": 16400, "pointEnd": 26400},
                {"point": 30720, "pointStart": 18400, "pointEnd": 30720,"grandPrize": 1}
            ]
        }
    }
    rewards_csv_list = id_2_rewards_detail[minigame_progress_reward_id]["csv"]
    progress_node_list = id_2_rewards_detail[minigame_progress_reward_id]["progress_node_list"]
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    point_progress_reward_id = point_progress_reward(excel_tool=excel_tool, point_progress_reward_id=point_progress_reward_id,rewards_csv_list=rewards_csv_list,progress_node_list=progress_node_list, token_id=token_id, notes=notes)
    minigame_progress_reward(excel_tool=excel_tool, point_progress_reward_id=point_progress_reward_id,minigame_progress_reward_id=minigame_progress_reward_id,rewards_csv_list=rewards_csv_list,progress_node_list=progress_node_list, token_id=token_id, notes=notes)



if __name__ == '__main__':
    main()