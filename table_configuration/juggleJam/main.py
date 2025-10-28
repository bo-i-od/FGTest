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

def juggle_jam_puzzle_pool(excel_tool: ExcelToolsForActivities, puzzle_pool_group_id, factor_press_range_common, factor_press_range, name):
    cfg_list=[{'puzzle': '3:1', 'expect_cost': 3, 'reward_quantity': 400, 'weight': 130},
     {'puzzle': '4:1', 'expect_cost': 4, 'reward_quantity': 550, 'weight': 140},
     {'puzzle': '1:1;2:1', 'expect_cost': 4.33333, 'reward_quantity': 400, 'weight': 120},
     {'puzzle': '5:1', 'expect_cost': 5, 'reward_quantity': 700, 'weight': 150},
     {'puzzle': '1:3', 'expect_cost': 5.5, 'reward_quantity': 450, 'weight': 330},
     {'puzzle': '1:1;3:1', 'expect_cost': 5.5, 'reward_quantity': 600, 'weight': 130},
     {'puzzle': '2:2', 'expect_cost': 6, 'reward_quantity': 550, 'weight': 240},
     {'puzzle': '6:1', 'expect_cost': 6, 'reward_quantity': 850, 'weight': 160},
     {'puzzle': '1:1;4:1', 'expect_cost': 6.6, 'reward_quantity': 750, 'weight': 140},
     {'puzzle': '7:1', 'expect_cost': 7, 'reward_quantity': 1000, 'weight': 170},
     {'puzzle': '1:2;2:1', 'expect_cost': 7.16667, 'reward_quantity': 650, 'weight': 240},
     {'puzzle': '2:1;3:1', 'expect_cost': 7.4, 'reward_quantity': 750, 'weight': 130},
     {'puzzle': '1:1;5:1', 'expect_cost': 7.66667, 'reward_quantity': 900, 'weight': 150},
     {'puzzle': '1:2;3:1', 'expect_cost': 8.55, 'reward_quantity': 850, 'weight': 260},
     {'puzzle': '2:1;4:1', 'expect_cost': 8.66667, 'reward_quantity': 900, 'weight': 140},
     {'puzzle': '1:1;6:1', 'expect_cost': 8.71429, 'reward_quantity': 1050, 'weight': 160},
     {'puzzle': '1:4', 'expect_cost': 8.83333, 'reward_quantity': 700, 'weight': 440},
     {'puzzle': '3:2', 'expect_cost': 9, 'reward_quantity': 850, 'weight': 260},
     {'puzzle': '1:1;2:2', 'expect_cost': 9.13333, 'reward_quantity': 800, 'weight': 240},
     {'puzzle': '1:2;4:1', 'expect_cost': 9.8, 'reward_quantity': 1000, 'weight': 280},
     {'puzzle': '2:1;5:1', 'expect_cost': 9.85714, 'reward_quantity': 1100, 'weight': 150},
     {'puzzle': '3:1;4:1', 'expect_cost': 10.4286, 'reward_quantity': 1050, 'weight': 140},
     {'puzzle': '1:1;2:1;3:1', 'expect_cost': 10.7333, 'reward_quantity': 1000, 'weight': 130},
     {'puzzle': '1:3;2:1', 'expect_cost': 10.7667, 'reward_quantity': 950, 'weight': 360},
     {'puzzle': '1:2;5:1', 'expect_cost': 10.9762, 'reward_quantity': 1200, 'weight': 300},
     {'puzzle': '2:3', 'expect_cost': 11.4, 'reward_quantity': 1000, 'weight': 360},
     {'puzzle': '1:1;2:1;4:1', 'expect_cost': 12.1429, 'reward_quantity': 1200, 'weight': 140},
     {'puzzle': '1:3;3:1', 'expect_cost': 12.3, 'reward_quantity': 1150, 'weight': 390},
     {'puzzle': '1:1;3:2', 'expect_cost': 12.5143, 'reward_quantity': 1150, 'weight': 260},
     {'puzzle': '1:5', 'expect_cost': 12.6333, 'reward_quantity': 1000, 'weight': 550},
     {'puzzle': '1:2;2:2', 'expect_cost': 13.0444, 'reward_quantity': 1100, 'weight': 240},
     {'puzzle': '2:2;3:1', 'expect_cost': 13.219, 'reward_quantity': 1200, 'weight': 260},
     {'puzzle': '1:3;4:1', 'expect_cost': 13.6524, 'reward_quantity': 1300, 'weight': 420},
     {'puzzle': '1:2;2:1;3:1', 'expect_cost': 14.8024, 'reward_quantity': 1350, 'weight': 260},
     {'puzzle': '1:4;2:1', 'expect_cost': 14.8778, 'reward_quantity': 1250, 'weight': 480},
     {'puzzle': '1:1;2:3', 'expect_cost': 15.5619, 'reward_quantity': 1300, 'weight': 360},
     {'puzzle': '1:4;3:1', 'expect_cost': 16.6071, 'reward_quantity': 1500, 'weight': 520},
     {'puzzle': '1:6', 'expect_cost': 17.0806, 'reward_quantity': 1350, 'weight': 660},
     {'puzzle': '1:3;2:2', 'expect_cost': 17.4548, 'reward_quantity': 1450, 'weight': 360},
     {'puzzle': '1:5;2:1', 'expect_cost': 19.6651, 'reward_quantity': 1650, 'weight': 600},
     {'puzzle': '1:7', 'expect_cost': 22.1849, 'reward_quantity': 1750, 'weight': 770}]
    key = "id"
    juggle_jam_puzzle_pool_detail = excel_tool.get_table_data_detail(book_name="JUGGLE_JAM_PUZZLE_POOL.xlsm")
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="puzzlePoolGroupId", value=puzzle_pool_group_id, table_data_detail=juggle_jam_puzzle_pool_detail)
    # id_start = excel_tool.get_max_value(key=key, table_object_detail=juggle_jam_puzzle_pool_detail) + 1
    if json_object_list:
        mode = 2
        # id_start = json_object_list[0]["id"]
    else:
        mode = 1
    res = {1:0, 2:0, 3:0}
    weight_total = 0
    cur = 0
    for cfg in cfg_list:

        # if cur > 0:
        #     break
        ball_count = 0
        puzzle_split = cfg['puzzle'].split(";")
        for p in puzzle_split:
            m, n = p.split(":")
            ball_count += int(m) * int(n)
        factor_pressure = cfg['expect_cost'] / ball_count
        print(factor_pressure)
        if factor_pressure <= factor_press_range[0]:
            continue
        elif factor_pressure >= factor_press_range[1]:
            continue

        cur += 1
        instance_object = JUGGLE_JAM_PUZZLE_POOL()
        instance_object.id = puzzle_pool_group_id * 100 + cur
        instance_object.name = f"{name}题面池{puzzle_pool_group_id}-{cur}"
        instance_object.puzzlePoolGroupId = puzzle_pool_group_id
        instance_object.puzzle = cfg['puzzle']
        instance_object.rewardQuantity = cfg['reward_quantity']
        instance_object.weight = cfg['weight']

        if factor_pressure < factor_press_range_common[0]:
            instance_object.pressureLevel = 1
        elif factor_pressure > factor_press_range_common[1]:
            instance_object.pressureLevel = 3
        else:
            instance_object.pressureLevel = 2
        res[instance_object.pressureLevel] += instance_object.weight
        weight_total += instance_object.weight

        print(instance_object)
        if mode == 1:
            excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=juggle_jam_puzzle_pool_detail, instance_object=instance_object)
        else:
            excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=juggle_jam_puzzle_pool_detail, instance_object=instance_object)
    for r in res:
        print(f"{r}:{res[r]/weight_total:.1%}")



def main():
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    puzzle_pool_group_id = 4
    # 压力系数 = 期望次数 / 球数
    factor_press_range_common = [1.55, 2.25]
    factor_press_range = [2.25, 100]
    name = "困难"
    juggle_jam_puzzle_pool(excel_tool, puzzle_pool_group_id=puzzle_pool_group_id, factor_press_range_common=factor_press_range_common, factor_press_range=factor_press_range, name=name)

# 示例使用
if __name__ == "__main__":
    main()





