from configs.pathConfig import DEV_EXCEL_PATH
from table_configuration.decl.HIDDEN_TREASURE_EVENT import HIDDEN_TREASURE_EVENT
from table_configuration.decl.HIDDEN_TREASURE_LEVEL import HIDDEN_TREASURE_LEVEL
from table_configuration.decl.MINIGAME_HIDDENTREASURE_LAYOUT import MINIGAME_HIDDENTREASURE_LAYOUT
from table_configuration.decl.MINIGAME_HIDDENTREASURE_LAYOUTMETADATA import MINIGAME_HIDDENTREASURE_LAYOUTMETADATA
from table_configuration.decl.MINIGAME_HIDDENTREASURE_LEVEL import MINIGAME_HIDDENTREASURE_LEVEL
from table_configuration.decl.MINIGAME_HIDDENTREASURE_TARGET import MINIGAME_HIDDENTREASURE_TARGET
from tools.decl2py import json_list_to_instance_list, instance_to_json
from tools.excelRead import ExcelToolsForActivities


def hidden_treasure_event(excel_tool: ExcelToolsForActivities):
    hidden_treasure_event_detail = excel_tool.get_table_data_detail(book_name="HIDDEN_TREASURE_EVENT.xlsm")
    instance_object_list = json_list_to_instance_list(json_object_list=hidden_treasure_event_detail[0],
                                                      cls=HIDDEN_TREASURE_EVENT)
    levelGroup_list = []
    for instance_object in instance_object_list:
        levelGroup_list.append(instance_object.levelGroup)
    return levelGroup_list


def hidden_treasure_level(excel_tool: ExcelToolsForActivities, levelGroup_list):
    book_name = "HIDDEN_TREASURE_LEVEL.xlsm"
    detail = excel_tool.get_table_data_detail(book_name=book_name)
    # 获取原始 json 列表，方便后续重写
    original_json_list, _, prefix = detail

    instance_object_list = json_list_to_instance_list(json_object_list=original_json_list, cls=HIDDEN_TREASURE_LEVEL)

    targetId_list = []
    metaId_list = []
    layouts_list = []

    # 用于存储最终要保留的 json 对象
    keep_json_list = []

    for instance_object in instance_object_list:
        if instance_object.levelGroup in levelGroup_list:
            targetId_list.append(instance_object.targetId)
            metaId_list.append(instance_object.metaId)
            layouts_list.extend(instance_object.layouts)

            # 将保留的对象转回 json (或者直接从 original_json_list 里找，但转回json更通用)
            keep_json_list.append(instance_to_json(instance_object))

    # 【关键优化】：如果列表长度有变化，说明有删除，仅执行一次写入
    if len(keep_json_list) != len(original_json_list):
        excel_tool.write_data_txt(name=prefix, json_object_list=keep_json_list)

    return targetId_list, metaId_list, layouts_list


def minigame_hiddentreasure_target(excel_tool: ExcelToolsForActivities, targetId_list):
    book_name = "MINIGAME_HIDDENTREASURE_TARGET.xlsm"
    detail = excel_tool.get_table_data_detail(book_name=book_name)
    original_json_list, _, prefix = detail

    instance_object_list = json_list_to_instance_list(json_object_list=original_json_list,
                                                      cls=MINIGAME_HIDDENTREASURE_TARGET)
    keep_json_list = []

    # 为了加快查找速度，将 targetId_list 转为 set
    targetId_set = set(targetId_list)

    for instance_object in instance_object_list:
        if instance_object.targetId in targetId_set:
            keep_json_list.append(instance_to_json(instance_object))

    if len(keep_json_list) != len(original_json_list):
        print(f"Saving {prefix}... Removed {len(original_json_list) - len(keep_json_list)} items.")
        excel_tool.write_data_txt(name=prefix, json_object_list=keep_json_list)


def minigame_hiddentreasure_layoutmetadata(excel_tool: ExcelToolsForActivities, metaId_list):
    book_name = "MINIGAME_HIDDENTREASURE_LAYOUTMETADATA.xlsm"
    detail = excel_tool.get_table_data_detail(book_name=book_name)
    original_json_list, _, prefix = detail

    instance_object_list = json_list_to_instance_list(json_object_list=original_json_list,
                                                      cls=MINIGAME_HIDDENTREASURE_LAYOUTMETADATA)
    keep_json_list = []
    metaId_set = set(metaId_list)  # Set 优化查找

    for instance_object in instance_object_list:
        if instance_object.metaId in metaId_set:
            keep_json_list.append(instance_to_json(instance_object))

    if len(keep_json_list) != len(original_json_list):
        print(f"Saving {prefix}... Removed {len(original_json_list) - len(keep_json_list)} items.")
        excel_tool.write_data_txt(name=prefix, json_object_list=keep_json_list)


def minigame_hiddentreasure_layout(excel_tool: ExcelToolsForActivities, layouts_list):
    book_name = "MINIGAME_HIDDENTREASURE_LAYOUT.xlsm"
    detail = excel_tool.get_table_data_detail(book_name=book_name)
    original_json_list, _, prefix = detail

    instance_object_list = json_list_to_instance_list(json_object_list=original_json_list,
                                                      cls=MINIGAME_HIDDENTREASURE_LAYOUT)
    keep_json_list = []
    layouts_set = set(layouts_list)

    for instance_object in instance_object_list:
        if instance_object.layoutId in layouts_set:
            keep_json_list.append(instance_to_json(instance_object))
        else:
            pass

    if len(keep_json_list) != len(original_json_list):
        print(f"Saving {prefix}... Removed {len(original_json_list) - len(keep_json_list)} items.")
        excel_tool.write_data_txt(name=prefix, json_object_list=keep_json_list)


def minigame_hiddentreasure_level(excel_tool: ExcelToolsForActivities):
    book_name = "MINIGAME_HIDDENTREASURE_LEVEL.xlsm"
    # 正确获取表详情
    table_data_detail = excel_tool.get_table_data_detail(book_name=book_name)
    # 从详情中获取 prefix
    _, _, prefix = table_data_detail

    print(f"Clearing {prefix}...")
    excel_tool.write_data_txt(name=prefix, blocks="")




def main():
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    levelGroup_list = hidden_treasure_event(excel_tool=excel_tool)

    targetId_list, metaId_list, layouts_list = hidden_treasure_level(excel_tool=excel_tool, levelGroup_list=levelGroup_list)

    minigame_hiddentreasure_target(excel_tool=excel_tool,targetId_list=targetId_list)

    minigame_hiddentreasure_layoutmetadata(excel_tool=excel_tool, metaId_list=metaId_list)

    minigame_hiddentreasure_layout(excel_tool=excel_tool, layouts_list=layouts_list)

    minigame_hiddentreasure_level(excel_tool=excel_tool)



if __name__ == '__main__':
    main()