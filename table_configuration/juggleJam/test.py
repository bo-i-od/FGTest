import json

from table_configuration.decl.JUGGLE_JAM_PUZZLE_POOL import JUGGLE_JAM_PUZZLE_POOL
from configs.pathConfig import DEV_EXCEL_PATH
from tools.decl2py import json_list_to_instance_list
from tools.excelRead import ExcelToolsForActivities


def main():
    path = "cost_cfg.json"
    cost_cfg = json.load(open(path, "r"))
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    puzzle_pool_group_id = 2
    juggle_jam_puzzle_pool_detail = excel_tool.get_table_data_detail(book_name="JUGGLE_JAM_PUZZLE_POOL.xlsm")
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="puzzlePoolGroupId", value=puzzle_pool_group_id, table_data_detail=juggle_jam_puzzle_pool_detail)
    instance_object_list = json_list_to_instance_list(json_object_list=json_object_list, cls=JUGGLE_JAM_PUZZLE_POOL)
    weight_total = 0
    value_total = 0
    for instance_object in instance_object_list:
        instance_object: JUGGLE_JAM_PUZZLE_POOL
        value_total += instance_object.weight * instance_object.rewardQuantity / cost_cfg[instance_object.puzzle]
        weight_total += instance_object.weight
    print(value_total / weight_total)

# 示例使用
if __name__ == "__main__":
    main()