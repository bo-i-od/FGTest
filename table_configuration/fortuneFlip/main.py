
from table_configuration.decl.FORTUNE_FLIP_CARD import FORTUNE_FLIP_CARD, RANDOM_CARD
from table_configuration.decl.FORTUNE_FLIP_DEAL import FORTUNE_FLIP_DEAL, FORTUNE_FLIP_CARD_WEIGHT
from table_configuration.decl.FORTUNE_FLIP_EVENT import FORTUNE_FLIP_EVENT, FORTUNE_FLIP_ROUND
from configs.pathConfig import DEV_EXCEL_PATH
from fortune_flip_deal import *
from tools.excelRead import ExcelToolsForActivities



def fortune_flip_event(excel_tool: ExcelToolsForActivities, event_id, round_list):
    """
    生成翻牌游戏事件配置并写入Excel

    Args:
        excel_tool: Excel操作工具类实例
        event_id: 事件ID，用于标识不同的游戏配置套装
        special_round_list: 特殊回合列表，这些回合会被标记为特殊类型
        round_max: 最大回合数，定义游戏的总回合数

    功能：
        - 创建游戏事件的基本配置
        - 为每个回合分配对应的卡牌池ID
        - 将配置写入或更新到Excel表格中
    """
    fortune_flip_event_id = event_id
    key = "id"

    # 获取Excel表格的详细信息
    fortune_flip_event_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_EVENT.xlsm")
    # fortune_flip_deal_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_DEAL.xlsm")

    # 创建游戏事件实例并设置基本属性
    instance_object = FORTUNE_FLIP_EVENT()
    instance_object.id = fortune_flip_event_id
    instance_object.name = f"翻牌配置{fortune_flip_event_id}"
    instance_object.activityBaseCost = 30
    instance_object.activityInitialBasePoints = 10
    instance_object.minigameMultipleGroupId = 9999
    instance_object.minigameProgressRewardId = event_id // 10000 * 1000 + event_id % 1000


    # 为每个回合生成配置
    instance_object.round = round_list
    # 确保回合列表长度为11（0-10回合）
    while len(instance_object.round) <= 10:
        instance_object.round.append(FORTUNE_FLIP_ROUND())

    print(instance_object)

    # 检查配置是否已存在，如果存在则更新，否则添加新配置
    if excel_tool.get_table_data_list_by_key_value(key=key, value=fortune_flip_event_id,
                                                   table_data_detail=fortune_flip_event_detail):
        excel_tool.change_object(key=key, value=fortune_flip_event_id, table_data_detail=fortune_flip_event_detail,
                                 instance_object=instance_object)
        return
    excel_tool.add_object(key=key, value=fortune_flip_event_id, table_data_detail=fortune_flip_event_detail,
                          instance_object=instance_object)


def fortune_flip_card(excel_tool: ExcelToolsForActivities):
    """
    生成翻牌游戏卡牌配置并写入Excel

    Args:
        excel_tool: Excel操作工具类实例

    功能：
        - 遍历所有卡牌配置（cfg字典）
        - 为每张卡牌创建对应的数据库记录
        - 将卡牌配置写入或更新到Excel表格中
    """
    fortune_flip_card_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_CARD.xlsm")
    key = "id"

    # 遍历cfg配置字典中的所有卡牌
    for card in cfg:
        card_detail = cfg[card]
        instance_object = FORTUNE_FLIP_CARD()

        # 设置卡牌的基本属性
        instance_object.id = card_detail["cardId"]
        instance_object.name = card_detail["name"]
        instance_object.category = card_detail["category"]

        # 设置可选属性（如果存在的话）
        if "arg" in card_detail:
            instance_object.arg = card_detail["arg"]  # 卡牌效果参数
        if "isGold" in card_detail:
            instance_object.isGold = card_detail["isGold"]  # 是否为黄金卡
        if "isSpecial" in card_detail:
            instance_object.isGold = card_detail["isSpecial"]  # 是否为黄金卡
        if "goldCardId" in card_detail:
            instance_object.goldCardId = card_detail["goldCardId"]  # 对应的黄金卡ID
        if "displayIcon" in card_detail:
            instance_object.displayIcon = card_detail["displayIcon"]  # 显示图标
        if instance_object.id == 61:
            instance_object.randomCard = []
            instance_object.randomCard.append(RANDOM_CARD(cardId=11, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=12, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=13, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=14, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=31, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=51, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=71, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=81, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=91, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=101, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD(cardId=111, weight=1000))
            instance_object.randomCard.append(RANDOM_CARD())
            instance_object.randomCard.append(RANDOM_CARD())
            instance_object.randomCard.append(RANDOM_CARD())
            instance_object.randomCard.append(RANDOM_CARD())

        print(instance_object)

        # 检查卡牌是否已存在，如果存在则更新，否则添加新卡牌
        if excel_tool.get_table_data_list_by_key_value(key=key, value=instance_object.id,
                                                       table_data_detail=fortune_flip_card_detail):
            excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=fortune_flip_card_detail,
                                     instance_object=instance_object)
            continue
        excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=fortune_flip_card_detail,
                              instance_object=instance_object)

def deal_once_round(excel_tool:ExcelToolsForActivities, fortune_flip_deal_detail, deal_id_list):
    """
    处理单个回合的卡牌池配置并写入Excel

    Args:
        excel_tool: Excel操作工具类实例
        event_id: 事件ID
        fortune_flip_deal_detail: 卡牌池表格的详细信息
        deal_id_list: 回合详细配置，包含dealId和roundId

    功能：
        - 为指定回合的每个卡牌位置创建卡牌池配置
        - 生成唯一的卡牌池ID
        - 将配置写入Excel表格
    """
    key = "id"
    # deal = deal_id_list["dealId"]
    # round_id = deal_id_list["roundId"]
    cur = 0

    # 遍历回合中的每个卡牌位置
    while cur < len(deal_id_list):
        instance_object = deal_id_list[cur]

        # # 生成唯一的卡牌池ID：事件ID * 1000 + 回合ID * 10 + 位置编号
        # instance_object.id = event_id * 10000 + round_id * 100 + cur
        # instance_object.name = f"第{event_id}套-剩{round_id}回合-第{cur}张牌的随机"
        # instance_object.cardWeight = deal[cur]  # 设置卡牌权重配置

        # 确保卡牌权重列表长度为15（填充空的权重对象）
        while len(instance_object.cardWeight) < 15:
            instance_object.cardWeight.append(FORTUNE_FLIP_CARD_WEIGHT())
        print(instance_object)

        # 检查配置是否已存在，如果存在则更新，否则添加新配置
        if excel_tool.get_table_data_list_by_key_value(key=key, value=instance_object.id,
                                                       table_data_detail=fortune_flip_deal_detail):
            excel_tool.change_object(key=key, value=instance_object.id, table_data_detail=fortune_flip_deal_detail,
                                     instance_object=instance_object)
            cur += 1
            continue
        excel_tool.add_object(key=key, value=instance_object.id, table_data_detail=fortune_flip_deal_detail,
                              instance_object=instance_object)
        cur += 1

def fortune_flip_deal_protect(excel_tool, event_id):
    """
    生成保护模式的翻牌游戏卡牌池配置

    Args:
        excel_tool: Excel操作工具类实例
        event_id: 事件ID

    功能：
        - 生成所有回合的保护模式配置（0-8回合）
        - 保护模式对玩家更有利，风险更低
        - 按照从高回合到低回合的顺序处理配置
    """

    # 生成所有保护模式回合的配置
    fortune_flip_deal_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_DEAL.xlsm")
    round_0, deal_id_list_0 = generate_fortune_flip_round_protect_0(event_id)
    round_1, deal_id_list_1 = generate_fortune_flip_round_protect_1(event_id)
    round_2, deal_id_list_2 = generate_fortune_flip_round_protect_2(event_id)
    round_3, deal_id_list_3 = generate_fortune_flip_round_protect_3(event_id)
    round_4, deal_id_list_4 = generate_fortune_flip_round_protect_4(event_id)
    round_5, deal_id_list_5 = generate_fortune_flip_round_protect_5(event_id)
    round_6, deal_id_list_6 = generate_fortune_flip_round_protect_6(event_id)
    round_7, deal_id_list_7 = generate_fortune_flip_round_protect_7(event_id)
    round_8, deal_id_list_8 = generate_fortune_flip_round_protect_8(event_id)


    # 按照从高回合到低回合的顺序处理配置
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_0)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_1)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_2)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_3)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_4)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_5)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_6)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_7)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_8)

    round_list = [round_0, round_1, round_2, round_3, round_4, round_5, round_6, round_7, round_8]
    return round_list

def fortune_flip_deal(excel_tool, event_id):
    """
    生成标准模式的翻牌游戏卡牌池配置

    Args:
        excel_tool: Excel操作工具类实例
        event_id: 事件ID

    功能：
        - 生成所有回合的标准模式配置（0-10回合）
        - 标准模式提供正常的游戏难度和风险
        - 包含更多的回合和更复杂的卡牌配置
    """
    # 生成所有标准模式回合的配置
    fortune_flip_deal_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_DEAL.xlsm")
    round_0, deal_id_list_0 = generate_fortune_flip_round_0(event_id)
    round_1, deal_id_list_1 = generate_fortune_flip_round_1(event_id)
    round_2, deal_id_list_2 = generate_fortune_flip_round_2(event_id)
    round_3, deal_id_list_3 = generate_fortune_flip_round_3(event_id)
    round_4, deal_id_list_4 = generate_fortune_flip_round_4(event_id)
    round_5, deal_id_list_5 = generate_fortune_flip_round_5(event_id)
    round_6, deal_id_list_6 = generate_fortune_flip_round_6(event_id)
    round_7, deal_id_list_7 = generate_fortune_flip_round_7(event_id)
    round_8, deal_id_list_8 = generate_fortune_flip_round_8(event_id)
    round_9, deal_id_list_9 = generate_fortune_flip_round_9(event_id)
    round_10, deal_id_list_10 = generate_fortune_flip_round_10(event_id)

    # 按照从低回合到高回合的顺序处理配置
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_0)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_1)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_2)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_3)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_4)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_5)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_6)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_7)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_8)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_9)
    deal_once_round(excel_tool=excel_tool, fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id_list=deal_id_list_10)

    round_list = [round_0, round_1, round_2, round_3, round_4, round_5, round_6, round_7, round_8, round_9, round_10]
    return round_list






def main():
    """
    主函数：执行翻牌游戏配置生成流程

    功能：
        - 初始化Excel操作工具
        - 设置游戏配置参数
        - 执行配置生成和数据写入
    """
    # 初始化Excel操作工具，指定Excel文件的根路径
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)

    # 游戏配置参数
    event_id = 300301                      # 事件ID，标识这是第2套配置


    # 执行配置生成（可以选择性启用不同的模式）

    # 生成保护模式配置（已注释，可根据需要启用）
    # round_list = fortune_flip_deal_protect(excel_tool=excel_tool, event_id=event_id)

    # # 生成标准模式的卡牌池配置
    round_list = fortune_flip_deal(excel_tool=excel_tool, event_id=event_id)
    #
    # # 生成游戏事件的主配置
    fortune_flip_event(excel_tool=excel_tool, event_id=event_id, round_list=round_list)

    # 生成卡牌基础配置（已注释，可根据需要启用）
    # fortune_flip_card(excel_tool=excel_tool)

if __name__ == '__main__':
    main()
