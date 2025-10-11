import copy


from table_configuration.decl.FORTUNE_FLIP_DEAL import FORTUNE_FLIP_DEAL, FORTUNE_FLIP_CARD_WEIGHT
from table_configuration.decl.FORTUNE_FLIP_EVENT import FORTUNE_FLIP_ROUND, DEAL_GROUP

# 翻牌游戏卡牌配置字典
# 定义了游戏中所有可能出现的卡牌类型及其基本属性
cfg = {
    # 空白卡：不显示的卡牌
    "blank": {"cardId": 1, "name": "没随机到卡", "category": 0, "weightInPool": 0},

    # 加分类卡牌 (category: 1)
    "add_5": {"cardId": 11, "name": "加5", "displayIcon": "", "category": 1, "arg": 5, "weightInPool": 1000, "weightFlip": 1000},
    "add_25": {"cardId": 12, "name": "加25", "displayIcon": "", "category": 1, "arg": 25, "weightInPool": 1000, "weightFlip": 1000},
    "add_50": {"cardId": 13, "name": "加50", "displayIcon": "", "goldCardId": 14, "category": 1, "arg": 50, "weightInPool": 1000, "weightFlip": 1000},
    "add_150": {"cardId": 14, "name": "加150", "displayIcon": "", "isGold": 1, "category": 1, "arg": 150, "weightInPool": 1000, "weightFlip": 1000},

    # 减分类卡牌 (category: 2)
    "subtract_10": {"cardId": 21, "name": "减10", "displayIcon": "", "category": 2, "arg": 10, "weightInPool": 1000, "weightFlip": 1000},
    "subtract_15": {"cardId": 22, "name": "减15", "displayIcon": "", "category": 2, "arg": 15, "weightInPool": 1000, "weightFlip": 1000},
    "subtract_20": {"cardId": 23, "name": "减20", "displayIcon": "", "category": 2, "arg": 20, "weightInPool": 1000, "weightFlip": 1000},
    "subtract_30": {"cardId": 24, "name": "减30", "displayIcon": "", "category": 2, "arg": 30, "weightInPool": 1000, "weightFlip": 1000},

    # 乘法类卡牌 (category: 3)
    "multiply_2": {"cardId": 31, "name": "乘2", "displayIcon": "", "goldCardId": 32, "category": 3, "arg": 2, "weightInPool": 1000, "weightFlip": 1000},
    "multiply_3": {"cardId": 32, "name": "乘3", "displayIcon": "", "isGold": 1, "category": 3, "arg": 3, "weightInPool": 1000, "weightFlip": 1000},

    # 除法类卡牌 (category: 4)
    "divide_2": {"cardId": 41, "name": "除2", "displayIcon": "", "category": 4, "arg": 2, "weightInPool": 1000, "weightFlip": 1000},

    # 回合类卡牌 (category: 5) - 增加游戏回合数
    "turn_2": {"cardId": 51, "name": "加2回合", "displayIcon": "", "goldCardId": 52, "category": 5, "arg": 2, "weightInPool": 1000, "weightFlip": 1000},
    "turn_3": {"cardId": 52, "name": "加3回合", "displayIcon": "", "isGold": 1, "category": 5, "arg": 3, "weightInPool": 1000, "weightFlip": 1000},

    # 特殊功能卡牌 (category: 6-11)
    "random": {"cardId": 61, "name": "随机卡", "displayIcon": "", "category": 6, "weightInPool": 1000, "weightFlip": 1000, "isSpecial": 1},
    "card_two": {"cardId": 71, "name": "两张卡", "displayIcon": "", "category": 7, "weightInPool": 1000, "weightFlip": 1000, "isSpecial": 1},
    "gold": {"cardId": 81, "name": "黄金卡", "displayIcon": "", "category": 8, "weightInPool": 1000, "weightFlip": 1000, "isSpecial": 1},
    "double": {"cardId": 91, "name": "加倍卡", "displayIcon": "", "category": 9, "weightInPool": 1000, "weightFlip": 1000, "isSpecial": 1},
    "reveal": {"cardId": 101, "name": "揭开卡", "displayIcon": "", "category": 10, "weightInPool": 1000, "weightFlip": 1000, "isSpecial": 1},
    "remove_bad": {"cardId": 111, "name": "移除坏卡", "displayIcon": "", "category": 11, "weightInPool": 1000, "weightFlip": 1000, "isSpecial": 1},
}

def generate_card_deal_common(keys, goodness=50, blank_weight_in_pool_factor: float = 0):
    """
    生成通用卡牌池配置

    Args:
        keys: 需要包含在卡牌池中的卡牌键名列表
        goodness: 好坏程度，范围1-100，数值越高对玩家越有利
        blank_weight_in_pool_factor: 空白卡权重因子，用于增加获得空白卡的概率

    Returns:
        card_deal: 卡牌池配置列表，包含各卡牌的权重信息
    """

    # 根据goodness参数生成权重配置
    weight = generate_weight_common_all(goodness=goodness)
    card_weight_list = []
    weight_total = 0

    # 遍历指定的卡牌键，创建卡牌权重对象
    for key in keys:
        card_weight = FORTUNE_FLIP_CARD_WEIGHT()
        card_weight.fortuneFlipCardId = weight[key]["cardId"]
        card_weight.weightInPool = weight[key]["weightInPool"]
        card_weight.weightFlip = weight[key]["weightFlip"]
        card_weight_list.append(card_weight)
        weight_total += card_weight.weightInPool

    # 如果需要添加空白卡
    if blank_weight_in_pool_factor > 0:
        key = "blank"
        card_weight = FORTUNE_FLIP_CARD_WEIGHT()
        card_weight.fortuneFlipCardId = weight[key]["cardId"]
        card_weight.weightInPool = int(blank_weight_in_pool_factor * weight_total)
        card_weight_list.append(card_weight)

    return card_weight_list


def generate_weight_common_all(goodness=50):
    """
    根据好坏程度生成卡牌权重配置

    Args:
        goodness: 好坏程度，范围1-100
                 ≤50: 对玩家较不利，坏卡权重较高
                 >50: 对玩家较有利，好卡权重较高

    Returns:
        weight: 包含所有卡牌权重信息的字典
    """
    weight = copy.deepcopy(cfg)

    # 限制goodness在有效范围内
    if goodness < 0:
        goodness = 0
    if goodness > 100:
        goodness = 100

    # goodness ≤ 50时的权重配置（较不利）
    if goodness <= 50:
        # 加分卡权重配置：goodness越低，低价值加分卡权重越高
        weight["add_5"]["weightInPool"] = 3000 - goodness*50
        weight["add_25"]["weightInPool"] = 2000 - goodness*10
        weight["add_50"]["weightInPool"] = 1000 + goodness*10
        weight["add_150"]["weightInPool"] = goodness*10
        weight["add_150"]["weightFlip"] = 1050

        # 减分卡权重配置：goodness越低，减分卡权重越高
        weight["subtract_30"]["weightInPool"] = 3000 - goodness*50
        weight["subtract_30"]["weightFlip"] = 900
        weight["subtract_20"]["weightInPool"] = 2000 - goodness*10
        weight["subtract_20"]["weightFlip"] = 850
        weight["subtract_15"]["weightInPool"] = 1000 + goodness*10
        weight["subtract_15"]["weightFlip"] = 800
        weight["subtract_10"]["weightInPool"] = goodness*10
        weight["subtract_10"]["weightFlip"] = 750

        # 乘除法卡权重配置
        weight["multiply_2"]["weightInPool"] = goodness*10
        weight["multiply_3"]["weightInPool"] = goodness
        weight["multiply_3"]["weightFlip"] = 1500
        weight["divide_2"]["weightInPool"] = 3000 - goodness*50
        weight["divide_2"]["weightFlip"] = 750

        # 回合卡权重配置
        weight["turn_2"]["weightInPool"] = goodness*5
        weight["turn_2"]["weightFlip"] = 1333
        weight["turn_3"]["weightInPool"] = goodness
        weight["turn_3"]["weightFlip"] = 1500

    # goodness > 50时的权重配置（较有利）
    else:
        # 调整加分卡权重：更倾向于高价值加分卡
        weight["add_5"]["weightInPool"] = 1000 - goodness*10
        weight["add_25"]["weightInPool"] = 2000 - goodness*10
        weight["add_50"]["weightInPool"] = 1000 + goodness*10
        weight["add_150"]["weightInPool"] = -2000 + goodness*50
        weight["add_150"]["weightFlip"] = 1050

        # 调整减分卡权重：降低减分卡出现概率
        weight["subtract_30"]["weightInPool"] = 1000 - goodness*10
        weight["subtract_30"]["weightFlip"] = 900
        weight["subtract_20"]["weightInPool"] = 2000 - goodness*10
        weight["subtract_20"]["weightFlip"] = 850
        weight["subtract_15"]["weightInPool"] = 1000 + goodness*10
        weight["subtract_15"]["weightFlip"] = 800
        weight["subtract_10"]["weightInPool"] = -2000 + goodness*50
        weight["subtract_10"]["weightFlip"] = 750

        # 乘除法卡权重调整
        weight["multiply_2"]["weightInPool"] = goodness*10
        weight["multiply_3"]["weightInPool"] = goodness
        weight["multiply_3"]["weightFlip"] = 1500
        weight["divide_2"]["weightInPool"] = 1000 - goodness*10
        weight["divide_2"]["weightFlip"] = 750

        # 回合卡权重调整
        weight["turn_2"]["weightInPool"] = goodness*5
        weight["turn_2"]["weightFlip"] = 1333
        weight["turn_3"]["weightInPool"] = goodness
        weight["turn_3"]["weightFlip"] = 1500

    return weight


def generate_card_deal_special(keys, blank_weight_in_pool_factor: float = 0):
    """
    生成特殊卡牌池配置（用于特殊回合）
    与通用卡牌池不同，特殊卡牌池使用固定的权重配置

    Args:
        keys: 需要包含的特殊卡牌键名列表
        blank_weight_in_pool_factor: 空白卡权重因子

    Returns:
        card_deal: 特殊卡牌池配置列表
    """
    weight = copy.deepcopy(cfg)
    card_weight_list = []
    weight_total = 0

    # 创建特殊卡牌权重对象
    for key in keys:
        card_weight = FORTUNE_FLIP_CARD_WEIGHT()
        card_weight.fortuneFlipCardId = weight[key]["cardId"]
        card_weight.weightInPool = weight[key]["weightInPool"]  # 使用默认权重
        card_weight.weightFlip = weight[key]["weightFlip"]
        card_weight_list.append(card_weight)
        weight_total += card_weight.weightInPool

    # 添加空白卡（如果需要）
    if blank_weight_in_pool_factor > 0:
        key = "blank"
        card_weight = FORTUNE_FLIP_CARD_WEIGHT()
        card_weight.fortuneFlipCardId = weight[key]["cardId"]
        card_weight.weightInPool = int(blank_weight_in_pool_factor * weight_total)
        card_weight_list.append(card_weight)
    return card_weight_list


# 以下是各个回合的卡牌池生成函数
# 每个函数对应游戏中的一个特定回合，定义了该回合的卡牌配置

def generate_fortune_flip_round_10(event_id):
    """生成剩余10回合的卡牌配置 - 特殊回合"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=1, roundId=10, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])
    # 只包含特殊功能卡牌
    keys = ["random", "card_two", "double", "reveal", "remove_bad"]

    # 前两个卡牌位置：无空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 后两个卡牌位置：增加空白卡概率
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys, blank_weight_in_pool_factor=1.5)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys, blank_weight_in_pool_factor=1.5)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_9(event_id):
    """生成剩余9回合的卡牌配置"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=9, dealGroup=[])

    index = 0

    # 默认发牌
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：加分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：减分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 黄金卡发牌
    deal_group = DEAL_GROUP(dealId=[], specialCardId=81)

    # 第一个位置：加分卡（中等好坏程度）
    keys = ["add_50", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：减分卡（中等好坏程度）
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 移除坏牌发牌 固定有坏牌
    deal_group = DEAL_GROUP(dealId=[], specialCardId=111)

    # 第一个位置：减分卡（中等好坏程度）
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：加分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 抽两张发牌 最少三张
    deal_group = DEAL_GROUP(dealId=[], specialCardId=71)

    # 第一个位置：加分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：较好配置
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=75)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 揭开一张 最少三张
    deal_group = DEAL_GROUP(dealId=[], specialCardId=101)

    # 第一个位置：减分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：中等配置
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=100)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_8(event_id):
    """生成剩余8回合的卡牌配置"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=8, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 所有位置都是加分卡，但使用最差的好坏程度（goodness=0）
    keys = ["add_5", "add_25", "add_50", "add_150"]

    # 前两个位置：纯加分卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 后两个位置：加分卡 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_7(event_id):
    """生成剩余7回合的卡牌配置"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=7, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]

    # 第一个位置：加分卡和乘法卡（较差配置）
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二到四个位置：混合卡牌（中等配置）
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "multiply_3", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 后两个位置增加空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_6(event_id):
    """生成剩余6回合的卡牌配置 - 特殊回合"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=1, roundId=6, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 包含黄金卡的特殊功能卡牌
    keys = ["random", "card_two", "gold", "double", "reveal", "remove_bad"]

    # 前两个位置：纯特殊卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 后两个位置：特殊卡 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys, blank_weight_in_pool_factor=1.5)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys, blank_weight_in_pool_factor=1.5)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_5(event_id):
    """生成剩余5回合的卡牌配置"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=5, dealGroup=[])

    index = 0
    # 默认发牌
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：加分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：减分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 黄金卡发牌
    deal_group = DEAL_GROUP(dealId=[], specialCardId=81)

    # 第一个位置：加分卡（中等好坏程度）
    keys = ["add_50", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：减分卡（中等好坏程度）
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 移除坏牌发牌 固定有坏牌
    deal_group = DEAL_GROUP(dealId=[], specialCardId=111)

    # 第一个位置：减分卡（中等好坏程度）
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：加分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 抽两张发牌 最少三张
    deal_group = DEAL_GROUP(dealId=[], specialCardId=71)

    # 第一个位置：加分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：较好配置
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=75)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 揭开一张 最少三张
    deal_group = DEAL_GROUP(dealId=[], specialCardId=101)

    # 第一个位置：减分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：中等配置
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=100)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_4(event_id):
    """生成剩余4回合的卡牌配置"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=4, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：纯加分卡
    keys = ["add_5", "add_25", "add_50", "add_150"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：全卡牌（较差配置）
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "multiply_3", "divide_2", "turn_2", "turn_3"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：全卡牌（中等配置）+ 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=75, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_3(event_id):
    """生成剩余3回合的卡牌配置 - 特殊回合"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=1, roundId=3, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 特殊功能卡牌配置
    keys = ["random", "card_two", "gold", "double", "reveal", "remove_bad"]

    # 前两个位置：纯特殊卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 后两个位置：特殊卡 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys, blank_weight_in_pool_factor=1.5)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys, blank_weight_in_pool_factor=1.5)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_2(event_id):
    """生成剩余2回合的卡牌配置"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=2, dealGroup=[])

    index = 0
    # 默认发牌
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：加分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：减分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 黄金卡发牌
    deal_group = DEAL_GROUP(dealId=[], specialCardId=81)

    # 第一个位置：加分卡（中等好坏程度）
    keys = ["add_50", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：减分卡（中等好坏程度）
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 移除坏牌发牌 固定有坏牌
    deal_group = DEAL_GROUP(dealId=[], specialCardId=111)

    # 第一个位置：减分卡（中等好坏程度）
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：加分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 抽两张发牌 最少三张
    deal_group = DEAL_GROUP(dealId=[], specialCardId=71)

    # 第一个位置：加分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：较好配置
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=75)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    # 揭开一张 最少三张
    deal_group = DEAL_GROUP(dealId=[], specialCardId=101)

    # 第一个位置：减分卡（中等好坏程度）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：中等配置
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=100)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：较差配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：中等配置 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id % 1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)

    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_1(event_id):
    """生成剩余1回合的卡牌配置"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=1, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：加分卡（最好配置）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=100)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：减分卡（最差配置）
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三、四个位置：全卡牌 + 空白卡
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "multiply_3", "divide_2", "turn_2", "turn_3"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=75, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_0(event_id):
    """生成剩余0回合的卡牌配置"""
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=0, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：黄金卡
    keys = ["multiply_3", "turn_3", "add_150"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：全卡牌（最差配置）
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2", "turn_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三、四个位置：全卡牌 + 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=67, blank_weight_in_pool_factor=2)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=100, blank_weight_in_pool_factor=2)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    
    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())

    return fortune_flip_round, fortune_flip_deal_list

def generate_fortune_flip_round_protect_8(event_id):
    """
    生成剩余8回合的卡牌配置 - 保护模式
    保护模式下的配置通常对玩家更有利，减少风险

    Returns:
        fortune_flip_round: 包含回合ID和4个卡牌位置配置的字典
    """
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=8, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 所有4个位置都使用纯加分卡，且使用最差的好坏程度（goodness=0）
    # 这样确保即使是最差情况也不会有负面效果
    keys = ["add_5", "add_25", "add_50", "add_150"]

    # 第一二个位置：纯加分卡（最差配置，但仍然是正收益）
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第一二个位置：纯加分卡+空白卡（最差配置，但仍然是正收益）
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_protect_7(event_id):
    """
    生成剩余7回合的卡牌配置 - 保护模式
    提供一定的风险控制，第一个位置相对安全

    Returns:
        fortune_flip_round: 包含回合ID和4个卡牌位置配置的字典
    """
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=7, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：纯加分卡（较差配置，但安全）
    keys = ["add_5", "add_25", "add_50", "add_150"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25)
    # for card in fortune_flip_deal.cardWeight:
    #     card.weightFlip = 0
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：纯减分卡（中等配置）
    # 虽然是减分卡，但配置相对温和
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三四个位置：混合卡牌（中等配置）+ 空白卡
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_protect_6(event_id):
    """
    生成剩余6回合的卡牌配置 - 保护模式
    特殊回合，只提供有限的特殊功能卡牌，移除了可能有风险的卡牌

    Returns:
        fortune_flip_round: 包含回合ID和3个卡牌位置配置的字典
    """
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=1, roundId=6, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])
    
    # "double", "card_two", "remove_bad"
    keys = ["random", "reveal", "gold"]

    # 让三张牌都发出来
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_protect_5(event_id):
    """
    生成剩余5回合的卡牌配置 - 保护模式
    特殊的保护机制：确保玩家必定翻到有利的乘法卡

    Returns:
        fortune_flip_round: 包含回合ID和2个卡牌位置配置的字典
    """
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=5, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：乘法卡（有利）
    keys = ["multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：除法卡（不利）
    keys = ["divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    # 本回合给玩家保护 必翻开x2
    # 保护机制：设置weightFlip=0，使除法卡不会被自动翻开
    fortune_flip_deal.cardWeight[0].weightFlip = 0
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    # keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
    #         "multiply_2", "multiply_3", "divide_2", "turn_2", "turn_3"]
    # fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0, blank_weight_in_pool_factor=1)
    # fortune_flip_deal_list.append(card_deal)
    # fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    # fortune_flip_deal_list.append(card_deal)

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_protect_4(event_id):
    """
    生成剩余4回合的卡牌配置 - 保护模式
    提供渐进式的风险管理，从安全到稍有挑战

    Returns:
        fortune_flip_round: 包含回合ID和4个卡牌位置配置的字典
    """
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=4, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：纯加分卡（中等配置，相对安全）
    keys = ["add_5", "add_25", "add_50", "add_150"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：混合卡牌（较差配置，增加少量风险）
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：混合卡牌（中等配置）+ 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：混合卡牌（较好配置）+ 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=75, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())

    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_protect_3(event_id):
    """
    生成剩余3回合的卡牌配置 - 保护模式
    特殊回合，只提供对玩家有利的特殊功能卡牌

    Returns:
        fortune_flip_round: 包含回合ID和3个卡牌位置配置的字典
    """
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=1, roundId=3, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 让三张牌都发出来
    keys = ["double", "card_two", "remove_bad"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
    
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_special(keys=keys)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())

    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_protect_2(event_id):
    """
    生成剩余2回合的卡牌配置 - 保护模式
    强化保护机制：后两个位置的卡牌不会自动翻开，完全由玩家控制

    Returns:
        fortune_flip_round: 包含回合ID和4个卡牌位置配置的字典
    """
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=2, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：纯加分卡（中等配置，安全选择）
    keys = ["add_5", "add_25", "add_50", "add_150"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：高价值卡牌（中等配置）
    keys = ["add_50", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第三个位置：减分卡（较差配置）+ 完全保护
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=25)
    # 设置所有卡牌的weightFlip=0，确保这些不利卡牌不会自动翻开
    for card in fortune_flip_deal.cardWeight:
        card.weightFlip = 0
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：混合卡牌（较好配置）+ 空白卡 + 完全保护
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=75, blank_weight_in_pool_factor=1)
    # 设置所有卡牌的weightFlip=0，确保这些卡牌不会自动翻开
    for card in fortune_flip_deal.cardWeight:
        card.weightFlip = 0
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1
        
    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())

    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_protect_1(event_id):
    """
    生成剩余1回合的卡牌配置 - 保护模式
    接近游戏结束，提供明确的风险和收益选择

    Returns:
        fortune_flip_round: 包含回合ID和4个卡牌位置配置的字典
    """
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=1, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：加分卡和乘法卡（最好配置）
    keys = ["add_5", "add_25", "add_50", "add_150", "multiply_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=100)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：减分卡和除法卡（最差配置）
    keys = ["subtract_10", "subtract_15", "subtract_20", "subtract_30", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1


    # 第三个位置：混合卡牌（中等配置）+ 空白卡
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：混合卡牌（较好配置）+ 空白卡
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=75, blank_weight_in_pool_factor=1)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())
    return fortune_flip_round, fortune_flip_deal_list


def generate_fortune_flip_round_protect_0(event_id):
    """
    生成剩余0回合的卡牌配置 - 保护模式（最后一回合）
    最终回合的强化保护：确保高价值奖励，其它卡牌不会自动翻开

    Returns:
        fortune_flip_round: 包含回合ID和4个卡牌位置配置的字典
    """
    fortune_flip_deal_list = []

    fortune_flip_round = FORTUNE_FLIP_ROUND(roundType=0, roundId=0, dealGroup=[])

    index = 0    
    deal_group = DEAL_GROUP(dealId=[])

    # 第一个位置：最高价值加分卡
    keys = ["add_150"]

    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50)
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第二个位置：减分卡（最差配置）+ 完全保护
    keys = [ "subtract_10", "subtract_15", "subtract_20", "subtract_30",  "divide_2"]
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=0)
    # 确保这些不利卡牌不会自动翻开
    for card in fortune_flip_deal.cardWeight:
        card.weightFlip = 0
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1


    # 第三个位置：混合卡牌（中等配置）+ 高空白卡保护 + 完全控制
    keys = ["add_5", "add_25", "add_50", "add_150", "subtract_10", "subtract_15", "subtract_20", "subtract_30",
            "multiply_2", "divide_2"]

    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=50, blank_weight_in_pool_factor=2)
    for card in fortune_flip_deal.cardWeight:
        card.weightFlip = 0
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    # 第四个位置：混合卡牌（最好配置）+ 高空白卡保护 + 完全控制
    fortune_flip_deal = FORTUNE_FLIP_DEAL()  # 创建新对象
    fortune_flip_deal.cardWeight = generate_card_deal_common(keys=keys, goodness=100, blank_weight_in_pool_factor=2)
    for card in fortune_flip_deal.cardWeight:
        card.weightFlip = 0
    fortune_flip_deal.id = event_id%1000 * 10000 + fortune_flip_round.roundId * 100 + index
    deal_group.dealId.append(fortune_flip_deal.id)
    fortune_flip_deal.name = f"{event_id}卡组-剩余{fortune_flip_round.roundId}回合-第{index}个发牌池"
    fortune_flip_deal_list.append(fortune_flip_deal)
    index += 1

    while len(deal_group.dealId) < 4:
        deal_group.dealId.append(0)

    fortune_flip_round.dealGroup.append(deal_group)
    while len(fortune_flip_round.dealGroup) < 5:
        fortune_flip_round.dealGroup.append(DEAL_GROUP())

    return fortune_flip_round, fortune_flip_deal_list
