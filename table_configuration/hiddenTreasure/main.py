import csv

from table_configuration.decl.HIDDEN_TREASURE_EVENT import HIDDEN_TREASURE_EVENT
from table_configuration.decl.HIDDEN_TREASURE_LEVEL import HIDDEN_TREASURE_LEVEL

from configs.pathConfig import DEV_EXCEL_PATH
from table_configuration.commonReward.common_reward import get_rewards_list
from tools.decl2py import json_to_instance
from tools.excelRead import ExcelToolsForActivities


def hidden_treasure_event(excel_tool: ExcelToolsForActivities, hidden_treasure_event_id):
    hidden_treasure_event_detail = excel_tool.get_table_data_detail(book_name="HIDDEN_TREASURE_EVENT.xlsm")
    key = "id"
    json_object_list = excel_tool.get_table_data_list_by_key_value(key=key, value=hidden_treasure_event_id, table_data_detail=hidden_treasure_event_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    instance_object = HIDDEN_TREASURE_EVENT()
    instance_object.id = hidden_treasure_event_id
    instance_object.name = f"挖沙子第{hidden_treasure_event_id}套配置"
    instance_object.levelGroup = hidden_treasure_event_id
    instance_object.tokenRecycleId = 210100
    print(instance_object)
    if mode == 1:
        excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=hidden_treasure_event_detail,
                              instance_object=instance_object)
    else:
        excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=hidden_treasure_event_detail,
                                     instance_object=instance_object)


def hidden_treasure_level(excel_tool: ExcelToolsForActivities, hidden_treasure_event_id, group_id_list, rewards_list):
    # if len(group_id_list) != len(rewards_list):
    #     raise DifferError("请确保关卡轮数和奖励轮数一致")
    hidden_treasure_level_detail = excel_tool.get_table_data_detail(book_name="HIDDEN_TREASURE_LEVEL.xlsm")
    minigame_hiddentreasure_level_detail = excel_tool.get_table_data_detail(book_name="MINIGAME_HIDDENTREASURE_LEVEL.xlsm")
    key = "id"
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="levelGroup", value=hidden_treasure_event_id, table_data_detail=hidden_treasure_level_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    loop = 1
    while loop <= len(group_id_list):
        group_id = group_id_list[loop - 1]
        minigame_hiddentreasure_level_list = excel_tool.get_table_data_list_by_key_value(key="groupId", value=group_id, table_data_detail=minigame_hiddentreasure_level_detail)
        rewards = None
        if rewards_list:
            rewards = rewards_list[loop - 1]
        # if len(rewards) != len(minigame_hiddentreasure_level_list):
        #     raise DifferError(f"关卡数：{len(minigame_hiddentreasure_level_list)}，奖励数：{len(rewards)}，请确保关卡数和奖励数一致")
        cur = 0
        while cur < len(minigame_hiddentreasure_level_list):
            instance_object = HIDDEN_TREASURE_LEVEL()
            instance_object.id = hidden_treasure_event_id * 1000 + loop * 100 + cur + 1
            instance_object.name = f"第{hidden_treasure_event_id}套-{loop}轮-{cur + 1}关"
            instance_object.levelGroup = hidden_treasure_event_id
            instance_object.loop = loop
            instance_object.order = cur + 1
            instance_object.targetId = minigame_hiddentreasure_level_list[cur]["targetId"]
            instance_object.metaId = minigame_hiddentreasure_level_list[cur]["metaId"]
            instance_object.layouts = minigame_hiddentreasure_level_list[cur]["layouts"]
            while len(instance_object.layouts) < 150:
                instance_object.layouts.append(0)

            if rewards_list:
                instance_object.itemReward = rewards[cur]
            else:
                instance_object.itemReward = json_to_instance(json_object_list[cur], cls=HIDDEN_TREASURE_LEVEL).itemReward

            print(instance_object)
            if mode == 1:
                excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=hidden_treasure_level_detail,
                                      instance_object=instance_object)
            else:
                excel_tool.change_object(key=key, value=instance_object.id,
                                         table_data_detail=hidden_treasure_level_detail, instance_object=instance_object)
            cur += 1
            if loop > 1 and cur > 9:
                break
        loop += 1





def main():
    mode = 2
    hidden_treasure_event_id = 4
    token_id = 101301
    notes = f"挖沙子第{hidden_treasure_event_id}套"
    group_id_list = [104 + hidden_treasure_event_id]
    id_2_rewards_csv_list = {2: {"csv": ["rewards_dig_2_1.csv"]}, 3: {"csv":["rewards_dig_3_1.csv"]}, 4: {"csv":["rewards_dig_3_2.csv"]}}
    rewards_csv_list = id_2_rewards_csv_list[hidden_treasure_event_id]["csv"]
    rewards_list = None
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    hidden_treasure_event(excel_tool=excel_tool, hidden_treasure_event_id=hidden_treasure_event_id)

    if mode == 1:
        rewards_list = get_rewards_list(excel_tool=excel_tool, rewards_csv_list=rewards_csv_list, token_id=token_id, notes=notes)
    hidden_treasure_level(excel_tool=excel_tool, hidden_treasure_event_id=hidden_treasure_event_id, group_id_list=group_id_list, rewards_list=rewards_list)

if __name__ == '__main__':
    main()