import csv
from dataclasses import dataclass
from typing import Optional

from table_configuration.decl.ITEM_MAIN import ITEM_MAIN
from table_configuration.decl.ITEM_PACKAGE import ITEM_PACKAGE, PACKAGE_CONTENTS
from tools.excelRead import ExcelToolsForActivities

@dataclass
class CommonReward:
    ioIdType: Optional[int] = None
    tpId: Optional[int] = None
    count: Optional[int] = None


def get_rewards(csv_path):
    rewards = []
    # 读取 CSV 文件
    with open(csv_path, newline='', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter='\t')  # 注意你举例的是“序号<TAB>路径”，所以 delimiter 用 \t
        header = next(reader)  # 第一行表头
        for row in reader:
            if len(row) < 4:
                continue
            rewards.append(row)
    return rewards


def item_package(excel_tool: ExcelToolsForActivities, reward_level_formal_list, notes):
    item_package_detail = excel_tool.get_table_data_detail(book_name="ITEM_PACKAGE.xlsm")
    start_id = excel_tool.get_min_value_more_than_start(table_object_detail=item_package_detail, start=291001, key="id")
    key = "id"
    instance_object = ITEM_PACKAGE()
    instance_object.id = start_id
    instance_object.name = f"{notes}礼盒"
    instance_object.packageItem = []
    for reward_level_formal in reward_level_formal_list:
        package = PACKAGE_CONTENTS()
        package.type = reward_level_formal.ioIdType
        package.rewardid = reward_level_formal.tpId
        package.count = reward_level_formal.count
        instance_object.packageItem.append(package)
    while len(instance_object.packageItem) < 3:
        instance_object.packageItem.append(PACKAGE_CONTENTS())
    print(instance_object)
    excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=item_package_detail, instance_object=instance_object)
    return instance_object.id
        # 291000

def item_main(excel_tool: ExcelToolsForActivities, item_package_id, notes):
    key = "id"
    item_main_detail = excel_tool.get_table_data_detail(book_name="ITEM_MAIN.xlsm")
    instance_object = ITEM_MAIN()
    instance_object.id = item_package_id
    instance_object.name = f"{notes}礼盒"
    instance_object.stype = 4
    instance_object.iconName = "icon_box_02"
    instance_object.values = [0, 0]
    instance_object.useType = 103
    instance_object.useArgs = [item_package_id, 0]
    instance_object.autoUse = 1
    instance_object.model = "rewardModel_treasureBox"
    print(instance_object)
    excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=item_main_detail, instance_object=instance_object)

def get_rewards_list(excel_tool: ExcelToolsForActivities, rewards_csv_list, token_id,notes):
    rewards_list = []
    for rewards_csv in rewards_csv_list:
        rewards = get_rewards(csv_path=rewards_csv)
        rewards_level_formal = []
        for reward_level in rewards:
            # 给
            reward_level_formal_list = []
            i = 0
            if reward_level[i] != "0":
                reward_level_formal = CommonReward()
                reward_level_formal.count = int(reward_level[i])
                reward_level_formal.ioIdType = 1
                reward_level_formal.tpId = 100100
                reward_level_formal_list.append(reward_level_formal)
            i = 1
            if reward_level[i] != "0":
                reward_level_formal = CommonReward()
                reward_level_formal.count = int(reward_level[i])
                reward_level_formal.ioIdType = 1
                reward_level_formal.tpId = 100210
                reward_level_formal_list.append(reward_level_formal)
            i = 2
            if reward_level[i] != "0":
                reward_level_formal = CommonReward()
                reward_level_formal.count = int(reward_level[i])
                reward_level_formal.ioIdType = 2
                reward_level_formal.tpId = 201001
                reward_level_formal_list.append(reward_level_formal)
            i = 3
            if reward_level[i] != "0":
                reward_level_formal = CommonReward()
                reward_level_formal.count = int(reward_level[i])
                reward_level_formal.ioIdType = 1
                reward_level_formal.tpId = token_id
                reward_level_formal_list.append(reward_level_formal)
            if len(reward_level_formal_list) > 1:
                reward_level_formal = CommonReward()
                item_package_id = item_package(excel_tool, reward_level_formal_list, notes)
                item_main(excel_tool, item_package_id, notes)
                reward_level_formal.ioIdType = 2
                reward_level_formal.tpId = item_package_id
                reward_level_formal.count = 1
                rewards_level_formal.append(reward_level_formal)
            else:
                rewards_level_formal.append(reward_level_formal_list[0])
            # print(reward_level_formal_list)
        rewards_list.append(rewards_level_formal)

    return rewards_list
