import json
import random

from table_configuration.decl.JUGGLE_JAM_PUZZLE_POOL import JUGGLE_JAM_PUZZLE_POOL
from configs.pathConfig import DEV_EXCEL_PATH
from tools.decl2py import json_list_to_instance_list
from tools.excelRead import ExcelToolsForActivities


def get_convert_rate(excel_tool: ExcelToolsForActivities,juggle_jam_puzzle_pool_detail, puzzle_pool_group_id):
    path = "cost_cfg.json"
    cost_cfg = json.load(open(path, "r"))
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="puzzlePoolGroupId", value=puzzle_pool_group_id, table_data_detail=juggle_jam_puzzle_pool_detail)
    instance_object_list = json_list_to_instance_list(json_object_list=json_object_list, cls=JUGGLE_JAM_PUZZLE_POOL)
    weight_total = 0
    value_total = 0
    cost_total = 0
    for instance_object in instance_object_list:
        instance_object: JUGGLE_JAM_PUZZLE_POOL
        value_total += instance_object.weight * instance_object.rewardQuantity / cost_cfg[instance_object.puzzle]
        weight_total += instance_object.weight
        cost_total += instance_object.weight * cost_cfg[instance_object.puzzle]
    convert_rate = value_total / weight_total
    ave_cost = cost_total / weight_total
    print(ave_cost)
    return convert_rate



def serve_once(serve_dict, weight_total):

    target = random.randint(1, weight_total)
    for weight_end in serve_dict:
        if weight_end < target:
            continue
        return serve_dict[weight_end]
    raise Exception("没有随机到合适的权重")


def serve_test(excel_tool: ExcelToolsForActivities,juggle_jam_puzzle_pool_detail, puzzle_pool_group_id):
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="puzzlePoolGroupId", value=puzzle_pool_group_id, table_data_detail=juggle_jam_puzzle_pool_detail)
    instance_object_list = json_list_to_instance_list(json_object_list=json_object_list, cls=JUGGLE_JAM_PUZZLE_POOL)
    serve_dict = {}
    weight_total = 0
    for instance_object in instance_object_list:
        instance_object: JUGGLE_JAM_PUZZLE_POOL
        if instance_object.weight is None:
            continue
        if instance_object.weight == 0:
            continue
        weight_total += instance_object.weight
        serve_dict[weight_total] = instance_object
    cur = 0
    while cur < 1000:
        res = serve_once(serve_dict, weight_total)
        print(f"{res.pressureLevel} 题面{res.puzzle}")
        cur += 1




def main():
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    puzzle_pool_group_id = 2
    juggle_jam_puzzle_pool_detail = excel_tool.get_table_data_detail(book_name="JUGGLE_JAM_PUZZLE_POOL.xlsm")
    serve_test(excel_tool=excel_tool, juggle_jam_puzzle_pool_detail=juggle_jam_puzzle_pool_detail, puzzle_pool_group_id=puzzle_pool_group_id)
    convert_rate = get_convert_rate(excel_tool=excel_tool,juggle_jam_puzzle_pool_detail=juggle_jam_puzzle_pool_detail, puzzle_pool_group_id=puzzle_pool_group_id)
    print(convert_rate)


# 示例使用
if __name__ == "__main__":
    main()