import math
import random

from table_configuration.decl.MINIGAME_HIDDENTREASURE_LAYOUTMETADATA import MINIGAME_HIDDENTREASURE_LAYOUTMETADATA, \
    MINIGAME_HIDDENTREASURE_LAYOUTMETADATAITEM
from table_configuration.decl.MINIGAME_HIDDENTREASURE_LEVEL import MINIGAME_HIDDENTREASURE_LEVEL
from table_configuration.hiddenTreasure.external.base_part import load_all_layouts
from table_configuration.hiddenTreasure.external.part import combin_part_column, combin_part_row
from tools.decl2py import json_list_to_instance_list
from tools.excelRead import ExcelToolsForActivities


def get_cover(cover_kind, width, height):
    if cover_kind == 0:
        return None

    if cover_kind == 1:
        return get_cover_indestructible(width=width, height=height)

    if cover_kind == 2:
        return get_cover_double(width=width, height=height)

    if cover_kind == 3:
        return get_cover_mixed(width=width, height=height)

    if cover_kind == 4:
        return get_cover_mixed_variant(width=width, height=height)


def get_cover_indestructible(width, height):
    filename = f"layouts/layouts_{height}_{width}.json"
    layouts = load_all_layouts(filename=filename)
    index_random = random.randint(0, len(layouts) - 1)
    cover = layouts[index_random]
    return cover


def get_cover_double(width, height):
    filename = f"layouts/layouts_{height}_{width}.json"
    layouts = load_all_layouts(filename=filename)
    index_random = random.randint(0, len(layouts) - 1)
    cover = layouts[index_random]
    for i in range(len(cover)):  # 遍历每一行
        for j in range(len(cover[i])):  # 遍历该行中的每一个元素
            if cover[i][j] == 1:
                cover[i][j] = 2
    return cover


def get_cover_mixed(width, height):
    filename = f"layouts/layouts_mixed_{height}_{width}.json"
    layouts = load_all_layouts(filename=filename)
    index_random = random.randint(0, len(layouts) - 1)
    cover = layouts[index_random]
    return cover


def get_cover_mixed_variant(width, height):
    filename = f"layouts/layouts_mixed_{height}_{width}.json"
    layouts = load_all_layouts(filename=filename)
    index_random_1 = random.randint(0, len(layouts) - 1)
    index_random_2 = random.randint(0, len(layouts) - 1)
    concat_list = []
    concat_list.extend(combin_part_column(layouts[index_random_1], layouts[index_random_2]))
    concat_list.extend(combin_part_row(layouts[index_random_1], layouts[index_random_2]))
    index_random = random.randint(0, len(concat_list) - 1)
    cover = concat_list[index_random]
    return cover


def get_prop_random(width, height, items, cover):
    area = width * height
    area_cost = area
    for i in range(len(cover)):  # 遍历每一行
        for j in range(len(cover[i])):  # 遍历该行中的每一个元素
            if cover[i][j] == 1:
                area_cost -= 1
                continue
            if cover[i][j] == 2:
                area_cost += 1

    area_fill = 0
    for item in items:
        item: MINIGAME_HIDDENTREASURE_LAYOUTMETADATAITEM
        area_fill += item.width * item.height

    fill_rate = area_fill / area_cost

    int(math.pow(max(0.5 - fill_rate, 0) * area, 0.5) + 0.5) + random.randint(0, 1)




def minigame_hiddentreasure_level(excel_tool: ExcelToolsForActivities):
    minigame_hiddentreasure_level_detail = excel_tool.get_table_data_detail(book_name="MINIGAME_HIDDENTREASURE_LEVEL.xlsm")
    hidden_treasure_layoutmetadata_detail = excel_tool.get_table_data_detail(book_name="MINIGAME_HIDDENTREASURE_LAYOUTMETADATA.xlsm")
    instance_object_list = json_list_to_instance_list(json_object_list=minigame_hiddentreasure_level_detail[0], cls=MINIGAME_HIDDENTREASURE_LEVEL)

    cur = 0
    seed = 0
    # 逐个关卡进行生成
    while cur < len(instance_object_list):
        instance_object = instance_object_list[cur]
        instance_object: MINIGAME_HIDDENTREASURE_LEVEL

        # 找到关卡的长宽和物件长宽
        instance_object_hidden_treasure_layoutmetadata = excel_tool.get_table_data_by_key_value(key="metaId", value=instance_object.metaId, table_data_detail=hidden_treasure_layoutmetadata_detail)
        instance_object_hidden_treasure_layoutmetadata: MINIGAME_HIDDENTREASURE_LAYOUTMETADATA
        width = instance_object_hidden_treasure_layoutmetadata.width
        height = instance_object_hidden_treasure_layoutmetadata.height
        items = instance_object_hidden_treasure_layoutmetadata.items

        random.seed(seed)
        # 定一个覆盖结构种类 0无覆盖 1不可挖掘 2两次挖掘 3不可挖掘+两次挖掘 4不可挖掘+两次挖掘两种拼接
        cover_kind = random.randint(0, 4)

        # 根据长宽和填充率随机出一个覆盖结构
        cover = get_cover(cover_kind=cover_kind, width=width, height=height)

        # 根据长宽和填充率和覆盖结构随出道具
        prop = get_prop_random(width=width, height=height, items=items, cover=cover)


        # 逐个牌面得到填充的位置,剔除互斥的牌面
        layouts = []
        for layout in instance_object.layouts:
            pass
        if not layouts:
            seed += 1
            continue
        seed += 1
        cur += 1

def main():
    cover = get_cover(cover_kind=4, width=4, height=4)
    print(cover)


if __name__ == "__main__":
    main()
