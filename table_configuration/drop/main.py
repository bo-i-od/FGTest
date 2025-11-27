from table_configuration.decl.PRIZE_DROP_EVENT import PRIZE_DROP_EVENT, PRIZE_DROP_ITEM, GOAL
from configs.pathConfig import DEV_EXCEL_PATH
from tools.excelRead import ExcelToolsForActivities

def prize_drop_event(excel_tool: ExcelToolsForActivities, event_id, minigame_progress_reward_id_list, token_id):
    bumper_progress_rewards_list = [
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=5),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=5),
        PRIZE_DROP_ITEM(type=1, itemId=token_id, count=5),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=10),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=5),
        PRIZE_DROP_ITEM(type=2, itemId=201001, count=1),
        PRIZE_DROP_ITEM(type=1, itemId=token_id, count=5),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=5),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=10),
        PRIZE_DROP_ITEM(type=2, itemId=201001, count=1),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=15),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=10),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=15),
        PRIZE_DROP_ITEM(type=1, itemId=token_id, count=5),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=10),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=15),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=15),
        PRIZE_DROP_ITEM(type=1, itemId=token_id, count=10),
        PRIZE_DROP_ITEM(type=2, itemId=201002, count=1),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=20),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=15),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=20),
        PRIZE_DROP_ITEM(type=1, itemId=token_id, count=10),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=15),
        PRIZE_DROP_ITEM(type=1, itemId=token_id, count=15),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=20),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=20),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=25),
        PRIZE_DROP_ITEM(type=2, itemId=201002, count=1),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=20),
        PRIZE_DROP_ITEM(type=1, itemId=100100, count=25),
        PRIZE_DROP_ITEM(type=1, itemId=100210, count=25),
    ]
    index = 0
    for bumper_progress_rewards in bumper_progress_rewards_list:
        bumper_progress_rewards.index = index
        index += 1
    prize_drop_event_detail = excel_tool.get_table_data_detail(book_name="PRIZE_DROP_EVENT.xlsm")
    key = "id"
    json_object_list = excel_tool.get_table_data_list_by_key_value(key=key, value=event_id, table_data_detail=prize_drop_event_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    instance_object = PRIZE_DROP_EVENT()
    instance_object.id = event_id
    instance_object.name = f"弹珠第{event_id}套配置"
    instance_object.pointId = token_id + 8000
    instance_object.minigameMultipleGroupId = 1
    instance_object.prizeDropScriptPoolGroupId = 1
    instance_object.dropPortCount = 5
    instance_object.goalPortCount = 7
    instance_object.bumperCount = 1
    instance_object.goal = [
        GOAL(point=2, weight=311, sameDirectionWeight=600),
        GOAL(point=13, weight=400, sameDirectionWeight=600),
        GOAL(point=24, weight=200, sameDirectionWeight=600),
        GOAL(point=150, weight=89, sameDirectionWeight=500),
    ]
    instance_object.dropProgressFactor = 400
    instance_object.dropProgressOffset = 200
    instance_object.pointBumper = 4
    instance_object.pointBumperProgress = 60
    instance_object.minigameProgressRewardId = []
    cur = 0
    while cur < 5:
        if cur < len(minigame_progress_reward_id_list):
            instance_object.minigameProgressRewardId.append(minigame_progress_reward_id_list[cur])
            cur += 1
            continue
        instance_object.minigameProgressRewardId.append(0)
        cur += 1
    instance_object.bumperProgressAdd = 67
    instance_object.bumperProgressRewards = bumper_progress_rewards_list

    print(instance_object)
    if mode == 1:
        excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=prize_drop_event_detail, instance_object=instance_object)
        return
    excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=prize_drop_event_detail, instance_object=instance_object)


def main():
    event_id = 1
    token_id = 101302
    minigame_progress_reward_id_list = [1, 2]
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    prize_drop_event(excel_tool=excel_tool, event_id=event_id, minigame_progress_reward_id_list=minigame_progress_reward_id_list, token_id=token_id)


if __name__ == '__main__':
    main()