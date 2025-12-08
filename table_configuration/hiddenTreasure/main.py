import csv

from table_configuration.decl.HIDDEN_TREASURE_EVENT import HIDDEN_TREASURE_EVENT
from table_configuration.decl.HIDDEN_TREASURE_LEVEL import HIDDEN_TREASURE_LEVEL, HIDDEN_TREASURE_REWARDS

from configs.pathConfig import DEV_EXCEL_PATH
from table_configuration.minigameCommon.common_reward import get_rewards_list

from tools.decl2py import json_to_instance, json_list_to_instance_list
from tools.excelRead import ExcelToolsForActivities


def hidden_treasure_event(excel_tool: ExcelToolsForActivities, level_group):
    hidden_treasure_event_detail = excel_tool.get_table_data_detail(book_name="HIDDEN_TREASURE_EVENT.xlsm")
    key = "id"
    hidden_treasure_event_id = 300100 + level_group
    json_object_list = excel_tool.get_table_data_list_by_key_value(key=key, value=hidden_treasure_event_id, table_data_detail=hidden_treasure_event_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    instance_object = HIDDEN_TREASURE_EVENT()
    instance_object.id = hidden_treasure_event_id
    instance_object.name = f"挖沙子第{level_group}套配置"
    instance_object.levelGroup = level_group
    print(instance_object)
    if mode == 1:
        excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=hidden_treasure_event_detail,
                              instance_object=instance_object)
    else:
        excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=hidden_treasure_event_detail,
                                     instance_object=instance_object)


def hidden_treasure_level(excel_tool: ExcelToolsForActivities,level_group, level_list, rewards_list):
    # if len(group_id_list) != len(rewards_list):
    #     raise DifferError("请确保关卡轮数和奖励轮数一致")
    hidden_treasure_level_detail = excel_tool.get_table_data_detail(book_name="HIDDEN_TREASURE_LEVEL.xlsm")
    minigame_hiddentreasure_level_detail = excel_tool.get_table_data_detail(book_name="MINIGAME_HIDDENTREASURE_LEVEL.xlsm")
    key = "id"
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="levelGroup", value=level_group, table_data_detail=hidden_treasure_level_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    rewards = None
    if rewards_list:
        rewards = rewards_list[0]
    instance_list_template = json_list_to_instance_list(json_object_list=json_object_list, cls=HIDDEN_TREASURE_LEVEL)
    level_index = 0
    loop = 1
    while loop <= len(level_list):


        # if len(rewards) != len(minigame_hiddentreasure_level_list):
        #     raise DifferError(f"关卡数：{len(minigame_hiddentreasure_level_list)}，奖励数：{len(rewards)}，请确保关卡数和奖励数一致")
        cur = 0
        while cur < len(level_list[loop-1]):
            minigame_hiddentreasure_level = excel_tool.get_table_data_by_key_value(key="levelId", value=level_list[loop-1][cur], table_data_detail=minigame_hiddentreasure_level_detail)
            instance_object = HIDDEN_TREASURE_LEVEL()
            instance_object.id = level_group * 1000 + loop * 100 + cur + 1
            instance_object.name = f"第{level_group}套-{loop}轮-{cur + 1}关"
            instance_object.levelGroup = level_group
            instance_object.loop = loop
            instance_object.order = cur + 1
            instance_object.targetId = minigame_hiddentreasure_level["targetId"]
            instance_object.metaId = minigame_hiddentreasure_level["metaId"]
            instance_object.layouts = minigame_hiddentreasure_level["layouts"]
            while len(instance_object.layouts) < 150:
                instance_object.layouts.append(0)
            instance_object.itemReward = HIDDEN_TREASURE_REWARDS()
            # print(f"instance_list_template[level_index].itemReward={instance_list_template[level_index].itemReward}")
            if rewards is None or rewards[level_index] is None:
                pass
            elif rewards_list:
                instance_object.itemReward.itemId = rewards[level_index].tpId
                instance_object.itemReward.type = rewards[level_index].ioIdType
                instance_object.itemReward.count = rewards[level_index].count
            if not instance_list_template:
                pass
            else:
                r = instance_list_template[level_index].itemReward
                instance_object.itemReward.itemId = r.itemId
                instance_object.itemReward.type = r.type
                instance_object.itemReward.count = r.count


            print(instance_object)
            if mode == 1:
                excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=hidden_treasure_level_detail,
                                      instance_object=instance_object)
            else:
                excel_tool.change_object(key=key, value=instance_object.id,
                                         table_data_detail=hidden_treasure_level_detail, instance_object=instance_object)
            cur += 1
            level_index += 1
        loop += 1





def main():
    mode = 2
    level_group = 3
    token_id = 101310 + level_group
    notes = f"挖沙子第{level_group}套"

    level_dict = {
        1: [
            [14161, 14804, 16420, 15511, 31695, 36679, 21747, 19414],
            [33933, 15208, 27399, 15410, 32289, 34302, 18633, 16824, 30535, 20045, 31897, 34504]
        ],
        2: [
            [14168, 16622, 18909, 26591, 17228, 31796, 22656, 36578, 17623, 27601],
            [19313, 35265, 23262, 16016, 25076, 24975, 34012, 35568]
        ],
        3: [
            [37422, 17724, 24874, 30838, 17329, 19212, 34965, 23565, 27197, 15511, 34403, 22757, 36376, 23464, 19641, 37220, 23666, 37321]
        ]

    }
    id_2_rewards_csv_list = {1: {"csv": ["rewards_dig_2_1.csv"]}, 2: {"csv":["rewards_dig_2_2.csv"]}, 3: {"csv":["rewards_dig_2_3.csv"]}}
    rewards_csv_list = id_2_rewards_csv_list[level_group]["csv"]
    rewards_list = None
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    hidden_treasure_event(excel_tool=excel_tool, level_group=level_group)

    if mode == 1:
        rewards_list = get_rewards_list(excel_tool=excel_tool, rewards_csv_list=rewards_csv_list, token_id=token_id, notes=notes)
    hidden_treasure_level(excel_tool=excel_tool,level_group=level_group, level_list=level_dict[level_group], rewards_list=rewards_list)

if __name__ == '__main__':
    main()