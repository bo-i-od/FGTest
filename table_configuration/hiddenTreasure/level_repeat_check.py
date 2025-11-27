from table_configuration.decl.HIDDEN_TREASURE_LEVEL import HIDDEN_TREASURE_LEVEL
from table_configuration.decl.MINIGAME_HIDDENTREASURE_LEVEL import MINIGAME_HIDDENTREASURE_LEVEL
from table_configuration.decl.MINIGAME_HIDDENTREASURE_TARGET import MINIGAME_HIDDENTREASURE_TARGET
from configs.pathConfig import DEV_EXCEL_PATH
from tools.decl2py import json_list_to_instance_list, json_to_instance
from tools.excelRead import ExcelToolsForActivities




def find_repeat(dicts):
    # 转换为frozenset来检查重复
    seen = set()
    duplicates = []

    for i, d in enumerate(dicts):
        frozen_dict = frozenset(d.items())
        if frozen_dict in seen:
            duplicates.append((i, d))
        else:
            seen.add(frozen_dict)

    if duplicates:
        print("\n重复的字典:")
        for index, duplicate_dict in duplicates:
            print(f"索引 {index}: {duplicate_dict}")


def main():
    groupId = 110
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    minigame_hiddentreasure_level_detail = excel_tool.get_table_data_detail(book_name="MINIGAME_HIDDENTREASURE_LEVEL.xlsm")
    minigame_hiddentreasure_target_detail = excel_tool.get_table_data_detail(book_name="MINIGAME_HIDDENTREASURE_TARGET.xlsm")
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="groupId", value=groupId, table_data_detail=minigame_hiddentreasure_level_detail)
    instance_object_list = json_list_to_instance_list(json_object_list=json_object_list, cls=MINIGAME_HIDDENTREASURE_LEVEL)
    dicts = []
    cur = 0
    while cur < len(instance_object_list):
        instance_object: MINIGAME_HIDDENTREASURE_LEVEL
        instance_object = instance_object_list[cur]
        target_id = instance_object.targetId
        minigame_hiddentreasure_target: MINIGAME_HIDDENTREASURE_TARGET
        minigame_hiddentreasure_target = json_to_instance(json_object=excel_tool.get_table_data_by_key_value(key="targetId", value=target_id, table_data_detail=minigame_hiddentreasure_target_detail), cls=MINIGAME_HIDDENTREASURE_TARGET)
        res = {}
        for item in minigame_hiddentreasure_target.items:
            if item.itemId in res:
                res[item.itemId] += 1
            else:
                res[item.itemId] = 1
        dicts.append(res)
        cur += 1
    print(dicts)
    find_repeat(dicts)



if __name__ == '__main__':
    main()