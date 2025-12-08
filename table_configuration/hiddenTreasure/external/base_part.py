import json
from itertools import combinations
from enum import Enum
import copy


class JointDirection(Enum):
    COLUMN = 1
    ROW = 2


class BasePart:
    def __init__(self, part_content):

        self.part_content = part_content
        self.block_count = self.get_block_count()

    def get_flip(self, flip_x=False,  flip_y=False):
        part_content_temp = copy.deepcopy(self.part_content)
        if not flip_x and not flip_y:  # 如果没有翻转操作，直接返回副本
            return BasePart(part_content=part_content_temp)

        if flip_x:
            # 水平翻转
            for row in part_content_temp:
                row.reverse()  # 直接反转每行更简洁

        if flip_y:
            # 垂直翻转（翻转行顺序）
            part_content_temp.reverse()

        return BasePart(part_content=part_content_temp)

    def get_transpose(self):
        """
        --- 新增方法：转置 ---
        将BasePart进行转置 (行列互换)，这对于将一个3x1的边条变成1x3的顶/底条至关重要
        """
        if self.height == 0 or self.width == 0:
            return BasePart(part_content=[[]])
        transposed_content = [list(row) for row in zip(*self.part_content)]
        return BasePart(part_content=transposed_content)


    def get_quadrant(self, quadrant):
        part_content_temp = copy.deepcopy(self.part_content)
        if quadrant == 1:
            return BasePart(part_content=part_content_temp)
        if quadrant == 2:
            for row in part_content_temp:
                row.reverse()  # 直接反转每行更简洁
            return BasePart(part_content=part_content_temp)
        if quadrant == 3:
            for row in part_content_temp:
                row.reverse()  # 直接反转每行更简洁
            part_content_temp.reverse()
            return BasePart(part_content=part_content_temp)
        if quadrant == 4:
            part_content_temp.reverse()
            return BasePart(part_content=part_content_temp)
        raise Exception("quadrant范围为1~4")

    def get_all_transformations(self):
        """
        生成一个部件的所有8种独特变换（4次旋转 + 4次翻转旋转）
        返回一个列表，其中包含去重后的所有 BasePart 变换形态。
        """
        # 使用元组形式的内容和尺寸作为key来去重
        unique_transforms = {}

        part = self
        # 4次旋转
        for _ in range(4):
            # 添加当前形态
            key = (tuple(map(tuple, part.part_content)), part.width, part.height)
            if key not in unique_transforms:
                unique_transforms[key] = part

            # 添加水平翻转后的形态
            flipped_part = part.get_flip(flip_x=True)
            key = (tuple(map(tuple, flipped_part.part_content)), flipped_part.width, flipped_part.height)
            if key not in unique_transforms:
                unique_transforms[key] = flipped_part

            # 旋转90度
            part = part.get_quadrant(4)

        return list(unique_transforms.values())

    def get_block_count(self):
        block_count = 0
        for row in self.part_content:
            block_count += row.count(1)
        return block_count

    def show(self):
        for row in self.part_content:
            print(row)

    @property
    def height(self):
        return len(self.part_content)

    @property
    def width(self):
        return len(self.part_content[0]) if self.part_content else 0

    @property
    def area(self):
        """计算BasePart的面积"""
        return self.height * self.width


def merge_part(part_list: list, joint_direction: JointDirection = JointDirection.COLUMN):
    if joint_direction == JointDirection.COLUMN:
        part0: BasePart = part_list[0]
        cur = 0
        while cur < len(part_list):
            part: BasePart = part_list[cur]
            if part.height != part0.height:
                raise Exception("长度不一致，无法拼接")
            cur += 1
        part_content = []
        cur = 0
        while cur < part0.height:
            part_joint = []
            i = 0
            while i < len(part_list):
                part: BasePart = part_list[i]
                part_joint += part.part_content[cur]
                i += 1
            part_content.append(part_joint)
            cur += 1
        return BasePart(part_content=part_content)
    part_content = []
    part0: BasePart = part_list[0]
    cur = 0
    while cur < len(part_list):
        part: BasePart = part_list[cur]
        if part.width != part0.width:
            raise Exception("长度不一致，无法拼接")
        part_content += part.part_content
        cur += 1
    return BasePart(part_content=part_content)


def generate_all_mine_layouts(m, n, k):
    """生成所有可能的埋k个雷的布局"""
    total = m * n
    board_list = []

    for mine_positions in combinations(range(total), k):
        board = [[0] * n for _ in range(m)]
        for pos in mine_positions:
            i = pos // n
            j = pos % n
            board[i][j] = 1
        board_list.append(board)

    return board_list


def save_all_layouts(m, n, max_mines):
    """生成并保存所有布局到一个JSON文件"""
    filename = f"layouts/layouts_{m}_{n}.json"
    all_boards = []
    for k in range(0, max_mines + 1):
        layouts = generate_all_mine_layouts(m, n, k)
        all_boards.extend(layouts)
        print(f"✓ 生成雷数={k}的布局: {len(layouts)}种")

    # 保存到JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_boards, f, indent=2)

    print(f"\n✅ 总共 {len(all_boards)} 种布局已保存到: {filename}")
    return all_boards


def load_all_layouts(filename):
    """从JSON文件读取所有布局"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_random_layout(layouts):
    """随机获取一个布局"""
    import random
    return random.choice(layouts)


# 生成1*1 至 3*3的base_part
def main():
    m = 3
    n = 3
    max_mines = (m * n) // 2
    # max_mines=3

    # ========== 保存 ==========
    print(f"📦 生成 {m}x{n} 扫雷盘所有布局\n")
    save_all_layouts(m, n, max_mines)

    # ========== 读取和使用 ==========
    print("\n" + "=" * 50)
    print("📖 读取示例：\n")

    filename = f"layouts/layouts_{m}_{n}.json"
    layouts = load_all_layouts(filename=filename)
    print(f"总共加载了 {len(layouts)} 种布局\n")

    # 随机获取
    board = get_random_layout(layouts)
    print("随机获取的布局:")
    for row in board:
        print(row)

    # 按索引获取
    print("\n第0个布局:")
    for row in layouts[0]:
        print(row)


if __name__ == "__main__":
    main()
    # part_content = [[1, 0, 0], [0, 1, 0], [1, 0, 0]]
    # bp1 = BasePart(part_content=part_content)
    # print(bp1.part_content)
    # bp2 = BasePart(part_content=part_content)
    # print(bp2.part_content)
    # bp3 = BasePart(part_content=part_content)
    # print(bp3.part_content)
    # bp4 = BasePart(part_content=part_content)
    # print(bp4.part_content)
    #
    # bp1_bp2 = merge_part(part_list=[bp1,bp2],joint_direction=JointDirection.COLUMN)
    # print(bp1_bp2.part_content)
    # bp3_bp4 = merge_part(part_list=[bp3, bp4], joint_direction=JointDirection.COLUMN)
    # print(bp3_bp4.part_content)
    # a = merge_part(part_list=[bp1_bp2, bp3_bp4], joint_direction=JointDirection.ROW)
    # print(a.part_content)
    # a.show()
    # print(a.part_content)
    #
    # print(b.part_content)
    # print(merge_part(part_list=[a,b],joint_direction=JointDirection.COLUMN).part_content)
    # print(bp.get_flip(flip_x=False, flip_y=False).part_content)
    # print(bp.get_flip(flip_x=True, flip_y=True).part_content)
    # bp.show()
