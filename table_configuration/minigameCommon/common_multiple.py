from configs.pathConfig import DEV_EXCEL_PATH
from tools.excelRead import ExcelToolsForActivities

def minigame_multiple(excel_tool: ExcelToolsForActivities, group_id):
    minigame_multiple_detail = excel_tool.get_table_data_detail(book_name="MINIGAME_MULTIPLE.xlsm")
    json_object_list = excel_tool.get_table_data_list_by_key_value(key="groupId", value=group_id, table_data_detail=minigame_multiple_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1


def main():
    cfg = [{"countMax": 1, }]
    io_id_type = 1
    tp_id = 101302
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    group_id = 1
    minigame_multiple(excel_tool=excel_tool, group_id=group_id)

# 示例使用
if __name__ == "__main__":
    main()
