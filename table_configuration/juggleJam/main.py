from table_configuration.decl.JUGGLE_JAM_PUZZLE_POOL import JUGGLE_JAM_PUZZLE_POOL
from configs.pathConfig import DEV_EXCEL_PATH
from tools.excelRead import ExcelToolsForActivities

def get_max_repeat_color_ball_count_and_max_count(puzzle):
    puzzle_split_list = puzzle.split(';')
    max_repeat_color_ball_count = 0
    max_count = 0
    for puzzle_split in puzzle_split_list:
        res = puzzle_split.split(':')
        res_0 = int(res[0])
        res_1 = int(res[1])
        if res_0 > max_repeat_color_ball_count:
            max_repeat_color_ball_count = res_0
        if res_1 > max_count:
            max_count = res_1
    return max_repeat_color_ball_count, max_count

def juggle_jam_puzzle_pool(excel_tool: ExcelToolsForActivities, puzzle_pool_group_id):
    cfg_list=[{'puzzle': '3:1', 'expect_cost': 3, 'reward_quantity': 40, 'weight': 130},
     {'puzzle': '4:1', 'expect_cost': 4, 'reward_quantity': 55, 'weight': 140},
     {'puzzle': '1:1;2:1', 'expect_cost': 4.33333, 'reward_quantity': 40, 'weight': 120},
     {'puzzle': '5:1', 'expect_cost': 5, 'reward_quantity': 70, 'weight': 150},
     {'puzzle': '1:3', 'expect_cost': 5.5, 'reward_quantity': 45, 'weight': 330},
     {'puzzle': '1:1;3:1', 'expect_cost': 5.5, 'reward_quantity': 60, 'weight': 130},
     {'puzzle': '2:2', 'expect_cost': 6, 'reward_quantity': 55, 'weight': 240},
     {'puzzle': '6:1', 'expect_cost': 6, 'reward_quantity': 85, 'weight': 160},
     {'puzzle': '1:1;4:1', 'expect_cost': 6.6, 'reward_quantity': 75, 'weight': 140},
     {'puzzle': '7:1', 'expect_cost': 7, 'reward_quantity': 100, 'weight': 170},
     {'puzzle': '1:2;2:1', 'expect_cost': 7.16667, 'reward_quantity': 65, 'weight': 240},
     {'puzzle': '2:1;3:1', 'expect_cost': 7.4, 'reward_quantity': 75, 'weight': 130},
     {'puzzle': '1:1;5:1', 'expect_cost': 7.66667, 'reward_quantity': 90, 'weight': 150},
     {'puzzle': '1:2;3:1', 'expect_cost': 8.55, 'reward_quantity': 85, 'weight': 260},
     {'puzzle': '2:1;4:1', 'expect_cost': 8.66667, 'reward_quantity': 90, 'weight': 140},
     {'puzzle': '1:1;6:1', 'expect_cost': 8.71429, 'reward_quantity': 105, 'weight': 160},
     {'puzzle': '1:4', 'expect_cost': 8.83333, 'reward_quantity': 70, 'weight': 440},
     {'puzzle': '3:2', 'expect_cost': 9, 'reward_quantity': 85, 'weight': 260},
     {'puzzle': '1:1;2:2', 'expect_cost': 9.13333, 'reward_quantity': 80, 'weight': 240},
     {'puzzle': '1:2;4:1', 'expect_cost': 9.8, 'reward_quantity': 100, 'weight': 280},
     {'puzzle': '2:1;5:1', 'expect_cost': 9.85714, 'reward_quantity': 110, 'weight': 150},
     {'puzzle': '3:1;4:1', 'expect_cost': 10.4286, 'reward_quantity': 105, 'weight': 140},
     {'puzzle': '1:1;2:1;3:1', 'expect_cost': 10.7333, 'reward_quantity': 100, 'weight': 130},
     {'puzzle': '1:3;2:1', 'expect_cost': 10.7667, 'reward_quantity': 95, 'weight': 360},
     {'puzzle': '1:2;5:1', 'expect_cost': 10.9762, 'reward_quantity': 120, 'weight': 300},
     {'puzzle': '2:3', 'expect_cost': 11.4, 'reward_quantity': 100, 'weight': 360},
     {'puzzle': '1:1;2:1;4:1', 'expect_cost': 12.1429, 'reward_quantity': 120, 'weight': 140},
     {'puzzle': '1:3;3:1', 'expect_cost': 12.3, 'reward_quantity': 115, 'weight': 390},
     {'puzzle': '1:1;3:2', 'expect_cost': 12.5143, 'reward_quantity': 115, 'weight': 260},
     {'puzzle': '1:5', 'expect_cost': 12.6333, 'reward_quantity': 100, 'weight': 550},
     {'puzzle': '1:2;2:2', 'expect_cost': 13.0444, 'reward_quantity': 110, 'weight': 240},
     {'puzzle': '2:2;3:1', 'expect_cost': 13.219, 'reward_quantity': 120, 'weight': 260},
     {'puzzle': '1:3;4:1', 'expect_cost': 13.6524, 'reward_quantity': 130, 'weight': 420},
     {'puzzle': '1:2;2:1;3:1', 'expect_cost': 14.8024, 'reward_quantity': 135, 'weight': 260},
     {'puzzle': '1:4;2:1', 'expect_cost': 14.8778, 'reward_quantity': 125, 'weight': 480},
     {'puzzle': '1:1;2:3', 'expect_cost': 15.5619, 'reward_quantity': 130, 'weight': 360},
     {'puzzle': '1:4;3:1', 'expect_cost': 16.6071, 'reward_quantity': 150, 'weight': 520},
     {'puzzle': '1:6', 'expect_cost': 17.0806, 'reward_quantity': 135, 'weight': 660},
     {'puzzle': '1:3;2:2', 'expect_cost': 17.4548, 'reward_quantity': 145, 'weight': 360},
     {'puzzle': '1:5;2:1', 'expect_cost': 19.6651, 'reward_quantity': 165, 'weight': 600},
     {'puzzle': '1:7', 'expect_cost': 22.1849, 'reward_quantity': 175, 'weight': 770}]

    key = "id"
    juggle_jam_puzzle_pool_detail = excel_tool.get_table_data_detail(book_name="JUGGLE_JAM_PUZZLE_POOL.xlsm")
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="puzzlePoolGroupId", value=puzzle_pool_group_id, table_data_detail=juggle_jam_puzzle_pool_detail)
    # id_start = excel_tool.get_max_value(key=key, table_object_detail=juggle_jam_puzzle_pool_detail) + 1
    if json_object_list:
        mode = 2
        # id_start = json_object_list[0]["id"]
    else:
        mode = 1

    cur = 0
    while cur < len(cfg_list):
        # if cur > 0:
        #     break
        cfg = cfg_list[cur]
        instance_object = JUGGLE_JAM_PUZZLE_POOL()
        instance_object.id = puzzle_pool_group_id * 100 + cur + 1
        instance_object.name = f"题面池{puzzle_pool_group_id}-{cur+1}"
        instance_object.puzzlePoolGroupId = puzzle_pool_group_id
        instance_object.puzzle = cfg['puzzle']
        instance_object.rewardQuantity = cfg['reward_quantity']
        instance_object.weight = cfg['weight']
        print(instance_object)
        if mode == 1:
            excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=juggle_jam_puzzle_pool_detail, instance_object=instance_object)
        else:
            excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=juggle_jam_puzzle_pool_detail, instance_object=instance_object)
        cur += 1



def main():
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    puzzle_pool_group_id = 2
    juggle_jam_puzzle_pool(excel_tool, puzzle_pool_group_id=puzzle_pool_group_id)

# 示例使用
if __name__ == "__main__":
    main()





