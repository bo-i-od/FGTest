import random

from configs.pathConfig import DEV_EXCEL_PATH
from table_configuration.decl.FORTUNE_FLIP_DEAL import FORTUNE_FLIP_DEAL, FORTUNE_FLIP_CARD_WEIGHT
from table_configuration.decl.FORTUNE_FLIP_EVENT import FORTUNE_FLIP_EVENT
from tools.decl2py import json_to_instance
from tools.excelRead import ExcelToolsForActivities


def serve_once(serve_dict, weight_total):

    target = random.randint(1, weight_total)
    for weight_end in serve_dict:
        if weight_end < target:
            continue
        return serve_dict[weight_end]
    raise Exception("没有随机到合适的权重")

def deal_one_card(excel_tool:ExcelToolsForActivities,fortune_flip_deal_detail, deal_id):
    json_object = excel_tool.get_table_data_by_key_value(key="id", value=deal_id, table_data_detail=fortune_flip_deal_detail)
    instance_object: FORTUNE_FLIP_DEAL
    instance_object = json_to_instance(json_object=json_object, cls=FORTUNE_FLIP_DEAL)
    serve_dict = {}
    weight_total = 0
    for card_weight in instance_object.cardWeight:
        if card_weight.weightInPool is None:
            continue
        if card_weight.weightInPool == 0:
            continue
        weight_total += card_weight.weightInPool
        serve_dict[weight_total] = card_weight

    serve_result = serve_once(serve_dict=serve_dict, weight_total=weight_total)
    return serve_result


def deal_one_round(excel_tool:ExcelToolsForActivities, fortune_flip_event_id, round_id, special_card_id, fortune_flip_event_detail=None, fortune_flip_deal_detail=None):
    if fortune_flip_event_detail is None:
        fortune_flip_event_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_EVENT.xlsm")
    if fortune_flip_deal_detail is None:
        fortune_flip_deal_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_DEAL.xlsm")

    json_object = excel_tool.get_table_data_by_key_value(key="id", value=fortune_flip_event_id, table_data_detail=fortune_flip_event_detail)
    instance_object: FORTUNE_FLIP_EVENT
    instance_object = json_to_instance(json_object=json_object, cls=FORTUNE_FLIP_EVENT)

    # 找到目标回合
    round_target = instance_object.round[0]
    for r in instance_object.round:
        if r.roundId != round_id:
            continue
        round_target = r
        break

    deal_group_target = round_target.dealGroup[0]
    for d in round_target.dealGroup:
        if d.specialCardId != special_card_id:
            continue
        deal_group_target = d
        break

    deal_result = []
    for deal_id in deal_group_target.dealId:
        deal_result.append(deal_one_card(excel_tool=excel_tool,fortune_flip_deal_detail=fortune_flip_deal_detail, deal_id=deal_id))

    return deal_result

def translate_deal_result(excel_tool: ExcelToolsForActivities, deal_result, fortune_flip_card_detail=None):
    if fortune_flip_card_detail is None:
        fortune_flip_card_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_CARD.xlsm")
    translated_deal_result = []
    for card in deal_result:
        card: FORTUNE_FLIP_CARD_WEIGHT
        json_object = excel_tool.get_table_data_by_key_value(key="id", value=card.fortuneFlipCardId, table_data_detail=fortune_flip_card_detail)
        translated_deal_result.append(json_object["name"])
    return translated_deal_result





def main():
    fortune_flip_event_id = 300301  # 要分析的事件ID
    round_id = 0
    special_card_id = None
    # 初始化Excel操作工具和数据访问
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    fortune_flip_card_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_CARD.xlsm")
    fortune_flip_event_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_EVENT.xlsm")
    fortune_flip_deal_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_DEAL.xlsm")
    cur = 0
    while cur < 100:
        deal_result = deal_one_round(excel_tool=excel_tool, fortune_flip_event_id=fortune_flip_event_id, round_id=round_id, special_card_id=special_card_id, fortune_flip_event_detail=fortune_flip_event_detail, fortune_flip_deal_detail=fortune_flip_deal_detail)
        # print(deal_result)
        translated_deal_result = translate_deal_result(excel_tool=excel_tool, deal_result=deal_result, fortune_flip_card_detail=fortune_flip_card_detail)
        print(translated_deal_result)
        cur += 1











if __name__ == '__main__':
    """
    程序入口点：执行期望值分析

    用途：
        - 游戏平衡性分析
        - 验证配置的合理性
        - 优化游戏体验
    """
    main()