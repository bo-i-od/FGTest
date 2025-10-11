from table_configuration.decl.FORTUNE_FLIP_DEAL import FORTUNE_FLIP_DEAL
from table_configuration.decl.FORTUNE_FLIP_EVENT import FORTUNE_FLIP_EVENT
from configs.pathConfig import DEV_EXCEL_PATH
from tools.decl2py import json_to_instance
from tools.excelRead import ExcelToolsForActivities
import itertools

class Blackboard:
    """
    黑板类：用于存储翻牌游戏期望值计算过程中的数据

    Attributes:
        expected_value_delta_list: 每回合代币收益期望值列表
        expected_value_accumulated_list: 累计代币期望值列表
    """
    expected_value_delta_list = []
    expected_value_accumulated_list = []

def get_value(bb: Blackboard, card_id):
    """
    根据卡牌ID计算卡牌的期望价值

    Args:
        bb: 黑板对象，包含当前游戏状态的期望值信息
        card_id: 卡牌ID

    Returns:
        float: 卡牌的期望价值

    功能：
        - 固定数值卡牌：直接返回对应的数值
        - 乘法卡牌：基于当前累计期望值计算
        - 除法卡牌：基于当前累计期望值的负面影响
        - 回合卡牌：基于历史回合期望值计算额外收益
    """
    # 固定数值卡牌的价值映射表
    value_by_id = {
        # 必须覆盖到会被抽到的所有 id
        # 例：
        1: 0,
        11: 5,
        12: 25,
        13: 50,
        14: 150,
        21: -10,
        22: -15,
        23: -20,
        24: -30,
    }
    # 乘法卡牌的价值计算（基于当前累计期望值）
    if card_id == 31:  # 乘2卡
        return bb.expected_value_accumulated_list[-1]
    if card_id == 32:    # 乘3卡
        return bb.expected_value_accumulated_list[-1] * 2

    # 除法卡牌的价值计算（负面影响）
    if card_id == 41:  # 除2卡
        return -0.5 * bb.expected_value_accumulated_list[-1]

    # 回合卡牌的价值计算（基于历史回合期望收益）
    if card_id == 51:  # 加2回合卡
        # 价值 = 最近两回合的期望收益之和
        return bb.expected_value_delta_list[-1] + bb.expected_value_delta_list[-2]
    if card_id == 52:  # 加3回合卡
        # 价值 = 最近三回合的期望收益之和
        return bb.expected_value_delta_list[-1] + bb.expected_value_delta_list[-2] + bb.expected_value_delta_list[-3]

    # 返回固定数值卡牌的价值
    return value_by_id[card_id]

def expected_value_one_round(bb, positions):
    """
    计算单个回合的期望值

    Args:
        bb: 黑板对象，包含当前游戏状态信息
        positions: 卡牌位置列表，每个位置包含可能的卡牌及其权重

    Returns:
        float: 该回合的期望收益值

    算法原理：
        1. 遍历所有可能的卡牌组合（笛卡尔积）
        2. 计算每种组合的概率
        3. 计算每种组合的加权期望值（基于翻牌权重）
        4. 汇总得到整体期望值
    """
    supports = []      # 每个位置支持的卡牌ID列表
    probs = []         # 每个位置每张卡牌的抽取概率
    flips = []         # 每个位置每张卡牌的翻牌权重
    active_indices = []  # 记录哪些位置是非空的（有有效卡牌）

    # 预处理：提取每个位置的有效卡牌信息
    for idx, pos in enumerate(positions):
        # 过滤出权重大于0的卡牌
        sup = {cid: w for cid, w in pos.items() if w.get('weightInPool', 0) > 0}
        if not sup:
            # 该位置无有效牌，跳过
            continue
        active_indices.append(idx)  # 记录活跃位置
        total_in = sum(c['weightInPool'] for c in sup.values())

        # 计算每张卡牌的抽取概率
        supports.append(list(sup.keys()))
        probs.append({cid: sup[cid]['weightInPool'] / total_in for cid in sup})
        flips.append({cid: sup[cid].get('weightFlip', 0) for cid in sup})

    if len(active_indices) == 0:
        return 0.0  # 完全无牌，返回0

    ev = 0.0  # 期望值累加器

    # 只对非空位置做笛卡尔积
    for combo in itertools.product(*supports):
        # combo 是非空位置的卡牌组合，例如 (c0, c2) 如果只有位置0和2有牌
        p_combo = 1.0           # 当前组合的概率
        weighted_value_sum = 0.0  # 加权价值总和
        w_sum = 0.0             # 权重总和

        for i, card_id in enumerate(combo):
            pos_idx = active_indices[i]  # 映射回原始位置索引
            p_combo *= probs[i][card_id]  # 累乘概率

            w = flips[i][card_id]  # 翻牌权重
            v = get_value(bb, card_id)  # 卡牌价值
            weighted_value_sum += w * v  # 累加加权价值
            w_sum += w  # 累加权重

        if w_sum == 0:
            continue  # 权重全0，跳过

        # 计算该组合的平均价值
        round_value = weighted_value_sum / w_sum

        # 累加到总期望值（乘以组合概率）
        ev += p_combo * round_value

    return ev

def get_positions_of_deal(excel_tool: ExcelToolsForActivities, deal_id_list, fortune_flip_deal_detail):
    """
    从Excel中获取指定卡牌池的位置信息

    Args:
        excel_tool: Excel操作工具
        deal_id_list: 卡牌池ID列表
        fortune_flip_deal_detail: 卡牌池表格详细信息

    Returns:
        list: 位置信息列表，每个位置包含卡牌ID到权重信息的映射

    功能：
        - 根据卡牌池ID从Excel中读取配置
        - 解析卡牌权重信息
        - 构建便于计算的数据结构
    """
    positions = []
    if deal_id_list is None:
        return positions
    cur = 0
    while cur < len(deal_id_list):
        deal_id = deal_id_list[cur]

        # 从Excel中查询卡牌池配置
        json_object_list = excel_tool.get_table_data_list_by_key_value(key="id", value=deal_id, table_data_detail=fortune_flip_deal_detail)
        if not json_object_list:
            cur += 1
            continue

        # 将JSON数据转换为对象实例
        json_object = json_object_list[0]
        instance_object: FORTUNE_FLIP_DEAL
        instance_object = json_to_instance(json_object=json_object, cls=FORTUNE_FLIP_DEAL)

        # 统计权重信息并构建卡牌字典
        weight_in_pool_total = 0
        weight_flip_total = 0
        card_dict = {}
        for card_weight in instance_object.cardWeight:
            if card_weight.fortuneFlipCardId is None:
                continue
            card_dict[card_weight.fortuneFlipCardId] = {}

            # 记录抽取权重
            if card_weight.weightInPool:
                weight_in_pool_total += card_weight.weightInPool
                card_dict[card_weight.fortuneFlipCardId]["weightInPool"] = card_weight.weightInPool

            # 记录翻牌权重
            if card_weight.weightFlip:
                weight_flip_total += card_weight.weightFlip
                card_dict[card_weight.fortuneFlipCardId]["weightFlip"] = card_weight.weightFlip

        positions.append(card_dict)
        cur += 1
    return positions


def main():
    """
    主函数：执行翻牌游戏期望值分析

    功能：
        1. 从Excel中读取游戏配置
        2. 初始化计算环境
        3. 按回合逆序计算期望值
        4. 输出分析结果

    计算逻辑：
        - 从最后一回合开始向前计算
        - 特殊回合有特殊处理逻辑
        - 回合8之后应用倍数因子
        - 累计期望值用于后续回合的乘法/除法卡牌计算
    """
    # 配置参数
    fortune_flip_event_id = 2  # 要分析的事件ID

    # 初始化Excel操作工具和数据访问
    excel_tool = ExcelToolsForActivities(root_path=DEV_EXCEL_PATH)
    fortune_flip_event_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_EVENT.xlsm")
    fortune_flip_deal_detail = excel_tool.get_table_data_detail(book_name="FORTUNE_FLIP_DEAL.xlsm")

    # 读取游戏事件配置
    json_object = excel_tool.get_table_data_by_key_value(key="id", value=fortune_flip_event_id, table_data_detail=fortune_flip_event_detail)
    instance_object: FORTUNE_FLIP_EVENT
    instance_object = json_to_instance(json_object=json_object, cls=FORTUNE_FLIP_EVENT)

    # 初始化计算环境
    bb = Blackboard()
    bb.expected_value_accumulated_list.append(10)  # 初始代币数量
    factor = 1  # 倍数因子
    cur = 0

    # 按回合逆序计算期望值（从最后一回合开始）
    while cur < len(instance_object.round):
        # 获取当前回合配置（逆序遍历）
        fortune_flip_round = instance_object.round[len(instance_object.round) - cur - 1]

        # 获取该回合的卡牌位置信息
        positions = get_positions_of_deal(excel_tool=excel_tool, deal_id_list=fortune_flip_round.dealId, fortune_flip_deal_detail=fortune_flip_deal_detail)

        # 特殊回合处理逻辑
        if fortune_flip_round.roundType == 1:
            bb.expected_value_delta_list.append(0)  # 特殊回合收益为0

            # 回合8之后的特殊回合应用倍数因子
            if fortune_flip_round.roundId > 8:
                factor = 2
                cur += 1
                continue

            # 累计期望值不变（特殊回合不影响累计值）
            if len(bb.expected_value_accumulated_list) > 0:
                bb.expected_value_accumulated_list.append(bb.expected_value_accumulated_list[-1])
            else:
                bb.expected_value_accumulated_list.append(0)
            factor = 2
            cur += 1
            continue

        # 普通回合：计算期望收益
        expect = expected_value_one_round(bb=bb, positions=positions) * factor
        bb.expected_value_delta_list.append(expect)

        # 回合8之后重置倍数因子
        if fortune_flip_round.roundId and fortune_flip_round.roundId > 8:
            factor = 1
            cur += 1
            continue

        # 更新累计期望值
        if len(bb.expected_value_accumulated_list) > 0:
            bb.expected_value_accumulated_list.append(bb.expected_value_accumulated_list[-1] + expect)
        else:
            bb.expected_value_accumulated_list.append(expect)
        factor = 1
        cur += 1

    # 输出分析结果
    print("累计代币变化期望：", bb.expected_value_accumulated_list)
    print("每回合代币收益期望：",bb.expected_value_delta_list)





if __name__ == '__main__':
    """
    程序入口点：执行期望值分析

    用途：
        - 游戏平衡性分析
        - 验证配置的合理性
        - 优化游戏体验
    """
    main()
