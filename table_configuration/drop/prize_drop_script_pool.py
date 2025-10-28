import random
import struct
import os
from typing import Optional

from configs.pathConfig import DEV_EXCEL_PATH
from table_configuration.decl.PRIZE_DROP_SCRIPT_POOL import PRIZE_DROP_SCRIPT_POOL, PRIZE_DROP_SCRIPT
from table_configuration.drop.script_screening.main import get_bumper_sequence, read_bytes_file, copy_file_to_target
from tools.excelRead import ExcelToolsForActivities
import shutil
import glob
import matplotlib.pyplot as plt
import numpy as np



# def print_data_summary(data):
#     """打印数据摘要"""
#     if data is None:
#         return
#
#     # print("=== 文件数据摘要 ===")
#     # print(f"场景ID: {data['scene_id']}")
#     # print(f"出生索引: {data['born_index']}")
#     # print(f"死亡索引: {data['dead_index']}")
#     # print(f"生命时间: {data['life_time']:.2f}")
#     # print(f"速度: {data['velocity']:.2f}")
#     # print(f"全局触发次数: {data['global_trigger_count']}")
#     # print(f"地面触发次数: {data['ground_trigger_count']}")
#     # print(f"统计数据条数: {len(data['statistics'])}")
#     # print(f"事件数据条数: {len(data['events'])}")
#     # print(f"轨迹点数: {len(data['track_positions'])}")
#     return data['born_index'], data['dead_index']








def show_data(numbers):

    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 4. 直方图
    plt.subplot(1, 1, 1)
    plt.hist(numbers, bins=8, color='green', alpha=0.7)
    plt.title('直方图')
    plt.xlabel('数值区间')
    plt.ylabel('频率')

    plt.tight_layout()
    plt.show()

def process_all_bytes_files(folder_path,target_path, excel_tool: ExcelToolsForActivities, group_id):
    """处理文件夹中所有的.bytes文件"""
    prize_drop_script_pool_detail = excel_tool.get_table_data_detail(book_name="PRIZE_DROP_SCRIPT_POOL.xlsm")
    key = "id"
    # count = 40
    pattern = os.path.join(folder_path, "*.bytes")
    files = glob.glob(pattern)

    json_object_list = excel_tool.get_table_data_list_by_key_value(key="groupId", value=group_id, table_data_detail=prize_drop_script_pool_detail)
    if json_object_list:
        mode = 2
    else:
        mode = 1
    instance_objects = []
    drop_index = 0
    while drop_index < 5:
        instance_objects.append([])
        goal_index = 0
        while goal_index < 7:
            instance_object= PRIZE_DROP_SCRIPT_POOL()
            instance_object.id = group_id * 100 + drop_index * 7 + goal_index + 1
            instance_object.name = f"第{group_id}组-{drop_index}入{goal_index}出"
            instance_object.groupId = group_id
            instance_object.dropPort = drop_index
            instance_object.goalPort = goal_index
            instance_object.script = []
            instance_objects[drop_index].append(instance_object)
            # print(instance_object)
            goal_index += 1
        drop_index += 1

    # print(instance_objects[3])

    # def
    # life_time_list = []
    # res = {}

    for file_path in files:
        # print(f"\n处理文件: {os.path.basename(file_path)}")
        # print(file_path)
        data = read_bytes_file(file_path)
        # print(data)
        # # 记录生存时间和碰撞次数
        # trigger_count_str = f"trigger_count{int(data['global_trigger_count'])}"
        # if trigger_count_str in res:
        #     res[trigger_count_str] += 1
        # else:
        #     res[trigger_count_str] = 1
        # life_time_str = f"life_time{int(data['life_time'])}"
        # if life_time_str in res:
        #     res[life_time_str] += 1
        # else:
        #     res[life_time_str] = 1
        # if data["global_trigger_count"] < 6:
        #
        #     # print("小于6次碰撞")
        #     continue
        # if data["life_time"] < 4.5:
        #     # print("生存时间小于4.5")
        #     continue
        # if data["global_trigger_count"] < 8 and data["life_time"] < 5:
        #
        #     continue

        # life_time_list.append(data['global_trigger_count'])
    # show_data(life_time_list)

        drop_index, goal_index = data['born_index'], data['dead_index']
        # index = drop_index * 7 + goal_index
        file_name = os.path.basename(file_path).split(".")[0]
        bumper_sequence = get_bumper_sequence(folder_path=folder_path, file_name=file_name)

        # cfg[index][]

        # if index not in res:
        #     res[index] = 1
        #     instance_object = instance_objects[drop_index][goal_index]
        #     script = PRIZE_DROP_SCRIPT()
        #     file_name = os.path.basename(file_path).split(".")[0]
        #     script.scriptName = file_name
        #     script.bumperSequence = get_bumper_sequence(folder_path=folder_path, file_name=file_name)
        #     instance_object.script.append(script)
        #     copy_file_to_target(file_path, target_path)
        #     continue


        # bumper_attack_count = bumper_sequence.count("0")
        # count_limit = 0
        # if bumper_attack_count in cfg[index]:
        #     count_limit = cfg[index][bumper_attack_count]
        # if count_limit <= 0:
        #     continue
        # cfg[index][bumper_attack_count] -= 1
        instance_object = instance_objects[drop_index][goal_index]
        script = PRIZE_DROP_SCRIPT()
        # file_name = os.path.basename(file_path).split(".")[0]
        script.scriptName = file_name
        script.bumperSequence = bumper_sequence
        instance_object.script.append(script)
        copy_file_to_target(file_path, target_path)
    # print("instance_objects:", len(instance_objects))
    # print(cfg)
    for i in instance_objects:
        # print("i:", len(i))
        for j in i:
            # pass
            # print("j:", len(j))
            # print(j)
            if mode == 1:
                excel_tool.add_object(key=key, value=j.id, table_data_detail=prize_drop_script_pool_detail,
                                      instance_object=j)
            else:

                excel_tool.change_object(key=key, value=j.id, table_data_detail=prize_drop_script_pool_detail,
                                         instance_object=j)



        # res[tag] += 1

    # for i in instance_objects:
    #     for j in i:
    #         print(len(j.script))



def main():

    folder_path = "script_screening/arranged_data"  # 替换为你的文件路径
    target_path = r"C:\ProjectMG\trunk\client\MainProject\Assets\InBundle\UI\ActivityPrizeDrop\Glass\FrameData"
    group_id = 1
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    # 读取文件
    process_all_bytes_files(folder_path=folder_path,target_path=target_path, excel_tool=excel_tool, group_id=group_id)


# 使用示例
if __name__ == "__main__":
    main()


    # # 打印摘要
    # print_data_summary(data)

    # # 访问具体数据
    # if data:
    #     # 访问轨迹数据
    #     if data['track_positions']:
    #         print("\n前5个轨迹点:")
    #         for i, pos in enumerate(data['track_positions'][:-1]):
    #             print(f"  点{i}: x={pos['x']:.1f}, y={pos['y']:.1f}, rot={pos['rotation_z']}")
    #
    #     # 访问事件数据
    #     if data['events']:
    #         print("\n前5个事件:")
    #         for i, event in enumerate(data['events'][:-1]):
    #             print(f"  事件{i}: 球类型={event['ball_type']}, 球索引={event['ball_index']}, 帧={event['frame']}")