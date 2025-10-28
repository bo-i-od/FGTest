import itertools
import random

from common.basePage import BasePage
from configs.pathConfig import DEV_EXCEL_PATH
from netMsg.csMsgAll import get_CSCharaRenameMsg, get_CSCharaSetIconMsg
from table_configuration.decl.MAP_LEVEL import MAP_LEVEL
import tools.createUsers
from tools.decl2py import json_to_instance
from tools.excelRead import ExcelToolsForActivities


def gm_map_level(level):
    return f"build 1 {level}"


def gm_building_level(level, index=-1):
    return f"build 2 {index} {level}"


def gm_building_status(status, index=-1):
    return f"build 3 {index} {status}"


def gm_refresh_db():
    return f"build 4"

def change_name(bp: BasePage, name):
    msg = get_CSCharaRenameMsg(newName=name)
    bp.lua_console(command=msg)

def change_icon(bp: BasePage, icon):
    msg = get_CSCharaSetIconMsg(icon=icon)
    bp.lua_console(command=msg)

# def set_name_random(bp: BasePage):
#     name_pool = get_name_pool(bp=bp)
#     index = random.randint(0, len(name_pool) - 1)
#     name = name_pool[index]
#     change_name(bp=bp, name=name)

def get_name_pool(bp: BasePage):
    names = bp.excelTools.get_table_data_by_key_value(key="id",value=1, book_name="ROBOT_MAIN.xlsm")["extArgs"][0]
    return names.split("&")


def set_building(bp: BasePage, map_level, map_level_detail):
    map_level_object: MAP_LEVEL
    map_level_object = json_to_instance(json_object=bp.excelTools.get_table_data_by_key_value(key="id", value=map_level, table_data_detail=map_level_detail), cls=MAP_LEVEL)
    build_max_level = map_level_object.buildingMaxLevel
    cmd_list = []
    cur = 0
    while cur < 5:
        build_level = random.randint(0, build_max_level)
        if build_level == 0:
            cur += 1
            continue

        # 等级
        cmd = gm_building_level(level=build_level, index=cur)
        cmd_list.append(cmd)

        # 被锤状态
        is_damaged = random.randint(0, 1)
        cmd = gm_building_status(status=is_damaged, index=cur)
        cmd_list.append(cmd)

        cur += 1
    # print(cmd_list)
    bp.cmd_list(command_list=cmd_list)


def main():
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21503")
    tools.createUsers.init(bp)
    map_level_detail = bp.excelTools.get_table_data_detail(book_name="MAP_LEVEL.xlsm")
    name_pool = get_name_pool(bp)
    random.shuffle(name_pool)

    cur = 31
    while cur < 2000:
        map_level = cur // 10 % 200 + 1
        name_login = f"lv_{map_level}_{cur}"
        tools.createUsers.login(bp, name=name_login)
        # 护盾
        shield_count = cur % 2
        if shield_count == 1:
            shield_count += random.randint(0, 2)
        bp.set_item_count(item_tpid="100300", target_count=shield_count)

        # 图标
        icon = random.randint(1, 30)
        change_icon(bp=bp, icon=icon)

        # 名称
        name = name_pool[cur % len(name_pool)]
        change_name(bp, name=name)

        # 建筑等级

        print(f"地图等级{map_level}, 名称{name}，头像{icon}，护盾{shield_count}个")
        # 建筑状态
        set_building(bp=bp, map_level=map_level, map_level_detail=map_level_detail)
        bp.cmd(command=gm_refresh_db())
        tools.createUsers.logout(bp)
        bp.sleep(1)
        cur += 1





if __name__ == '__main__':
    main()
