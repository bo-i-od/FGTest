import json
import random

from table_configuration.hiddenTreasure.external.base_part import BasePart, load_all_layouts
from table_configuration.hiddenTreasure.external.placement import create_part_from_base_parts
from itertools import product


def get_part_all(height, width):
    filename = f"layouts/layouts_{height}_{width}.json"
    layouts = load_all_layouts(filename=filename)
    return layouts


def generate_part_77():
    all_boards = []
    base_part_all_3x3 = get_part_all(height=3, width=3)
    base_part_all_1x3 = get_part_all(height=1, width=3)
    base_part_all_1x1 = get_part_all(height=1, width=1)

    part_combos = list(product(base_part_all_3x3, base_part_all_1x3, base_part_all_1x1))

    for part_combo in part_combos:
        # print(part_combo)
        base_part_3x3 = BasePart(part_content=part_combo[0])
        base_part_1x3 = BasePart(part_content=part_combo[1])
        base_part_1x1 = BasePart(part_content=part_combo[2])
        part = create_part_from_base_parts(
            base_part_3x3, base_part_3x3.get_quadrant(2), base_part_3x3.get_quadrant(3), base_part_3x3.get_quadrant(4),
            base_part_1x3, base_part_1x3.get_quadrant(2), base_part_1x3.get_quadrant(2), base_part_1x3,
            base_part_1x1
        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards


def generate_part_76():
    all_boards = []
    base_part_all_3x3 = get_part_all(height=3, width=3)
    base_part_all_1x3 = get_part_all(height=1, width=3)

    part_combos = list(product(base_part_all_3x3, base_part_all_1x3))

    for part_combo in part_combos:
        # print(part_combo)
        base_part_3x3 = BasePart(part_content=part_combo[0])
        base_part_1x3 = BasePart(part_content=part_combo[1])
        part = create_part_from_base_parts(
            base_part_3x3, base_part_3x3.get_quadrant(2), base_part_3x3.get_quadrant(3), base_part_3x3.get_quadrant(4),
            base_part_1x3, base_part_1x3.get_quadrant(2)
        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards


def generate_part_75():
    all_boards = []
    base_part_all_2x3 = get_part_all(height=2, width=3)
    base_part_all_1x3 = get_part_all(height=1, width=3)
    base_part_all_1x2 = get_part_all(height=1, width=2)
    base_part_all_1x1 = get_part_all(height=1, width=1)

    part_combos = list(product(base_part_all_2x3, base_part_all_1x3, base_part_all_1x2, base_part_all_1x1))
    for part_combo in part_combos:
        # print(part_combo)
        base_part_2x3 = BasePart(part_content=part_combo[0])
        base_part_1x3 = BasePart(part_content=part_combo[1])
        base_part_1x2 = BasePart(part_content=part_combo[2])
        base_part_1x1 = BasePart(part_content=part_combo[3])
        part = create_part_from_base_parts(
            base_part_2x3, base_part_2x3.get_quadrant(4), base_part_2x3.get_quadrant(3), base_part_2x3.get_quadrant(2),
            base_part_1x3, base_part_1x3.get_quadrant(2),
            base_part_1x2, base_part_1x2.get_quadrant(2),
            base_part_1x1,
        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards


def generate_part_74():
    all_boards = []
    base_part_all_2x3 = get_part_all(height=2, width=3)
    base_part_all_1x2 = get_part_all(height=1, width=2)

    part_combos = list(product(base_part_all_2x3, base_part_all_1x2))
    for part_combo in part_combos:
        # print(part_combo)
        base_part_2x3 = BasePart(part_content=part_combo[0])
        base_part_1x2 = BasePart(part_content=part_combo[1])
        part = create_part_from_base_parts(
            base_part_2x3, base_part_2x3.get_quadrant(4), base_part_2x3.get_quadrant(3), base_part_2x3.get_quadrant(2),
            base_part_1x2, base_part_1x2.get_quadrant(2),
        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards


def generate_part_66():
    all_boards = []
    base_part_all_3x3 = get_part_all(height=3, width=3)

    part_combos = list(product(base_part_all_3x3))
    for part_combo in part_combos:
        # print(part_combo)
        base_part_3x3 = BasePart(part_content=part_combo[0])
        part = create_part_from_base_parts(
            base_part_3x3, base_part_3x3.get_quadrant(2), base_part_3x3.get_quadrant(3), base_part_3x3.get_quadrant(4),
        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards


def generate_part_65():
    all_boards = []
    base_part_all_2x3 = get_part_all(height=2, width=3)
    base_part_all_1x3 = get_part_all(height=1, width=3)

    part_combos = list(product(base_part_all_2x3, base_part_all_1x3))
    for part_combo in part_combos:
        # print(part_combo)
        base_part_2x3 = BasePart(part_content=part_combo[0])
        base_part_1x3 = BasePart(part_content=part_combo[1])
        part = create_part_from_base_parts(
            base_part_2x3, base_part_2x3.get_quadrant(4), base_part_2x3.get_quadrant(3), base_part_2x3.get_quadrant(2),
            base_part_1x3, base_part_1x3.get_quadrant(2)
        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards


def generate_part_64():
    all_boards = []
    base_part_all_2x3 = get_part_all(height=2, width=3)

    part_combos = list(product(base_part_all_2x3))
    for part_combo in part_combos:
        # print(part_combo)
        base_part_2x3 = BasePart(part_content=part_combo[0])
        part = create_part_from_base_parts(
            base_part_2x3, base_part_2x3.get_quadrant(4), base_part_2x3.get_quadrant(3), base_part_2x3.get_quadrant(2),
        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards



def generate_part_55():
    all_boards = []
    base_part_all_2x2 = get_part_all(height=2, width=2)
    base_part_all_1x2 = get_part_all(height=1, width=2)
    base_part_all_1x1 = get_part_all(height=1, width=1)

    part_combos = list(product(base_part_all_2x2, base_part_all_1x2, base_part_all_1x1))
    for part_combo in part_combos:
        # print(part_combo)
        base_part_2x2 = BasePart(part_content=part_combo[0])
        base_part_1x2 = BasePart(part_content=part_combo[1])
        base_part_1x1 = BasePart(part_content=part_combo[2])

        part = create_part_from_base_parts(
            base_part_2x2, base_part_2x2.get_quadrant(2), base_part_2x2.get_quadrant(3), base_part_2x2.get_quadrant(4),
            base_part_1x2, base_part_1x2.get_quadrant(2), base_part_1x2, base_part_1x2.get_quadrant(2),
            base_part_1x1,
        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards


def generate_part_54():
    all_boards = []
    base_part_all_2x2 = get_part_all(height=2, width=2)
    base_part_all_1x2 = get_part_all(height=1, width=2)

    part_combos = list(product(base_part_all_2x2, base_part_all_1x2))
    for part_combo in part_combos:
        # print(part_combo)
        base_part_2x2 = BasePart(part_content=part_combo[0])
        base_part_1x2 = BasePart(part_content=part_combo[1])

        part = create_part_from_base_parts(
            base_part_2x2, base_part_2x2.get_quadrant(2), base_part_2x2.get_quadrant(3), base_part_2x2.get_quadrant(4),
            base_part_1x2, base_part_1x2.get_quadrant(2)

        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards


def generate_part_44():
    all_boards = []
    base_part_all_2x2 = get_part_all(height=2, width=2)

    part_combos = list(product(base_part_all_2x2))
    for part_combo in part_combos:
        base_part_2x2 = BasePart(part_content=part_combo[0])

        part = create_part_from_base_parts(
            base_part_2x2, base_part_2x2.get_quadrant(2), base_part_2x2.get_quadrant(3), base_part_2x2.get_quadrant(4)
        )
        part.show()
        all_boards.append(part.part_content)
        print("\n")
    return all_boards


def generate_part(height, width):
    print("=" * 60)
    print(f"{height}x{width}框架布局")
    print("=" * 60)
    filename = f"layouts/layouts_{height}_{width}.json"
    generate_part_dict = {
        (7, 7): generate_part_77,
        (7, 6): generate_part_76,
        (7, 5): generate_part_75,
        (7, 4): generate_part_74,
        (6, 6): generate_part_66,
        (6, 5): generate_part_65,
        (6, 4): generate_part_64,
        (5, 5): generate_part_55,
        (5, 4): generate_part_54,
        (4, 4): generate_part_44,
    }

    all_boards = generate_part_dict[(height, width)]()

    # 保存到JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(all_boards, f, indent=2)


def generate_part_all():
    height = 4
    while height < 8:
        width = 4
        while width < 8:
            if width > height:
                width += 1
                continue
            generate_part(height=height, width=width)
            width += 1
        height += 1


def generate_part_mixed_variant_all():
    height = 4
    while height < 8:
        width = 4
        while width < 8:
            if width > height:
                width += 1
                continue
            generate_part_mixed_variant(height=height, width=width)
            width += 1
        height += 1

def combin_part_column(part1, part2):
    concat_list = []
    width = len(part1[0])
    width_half = width // 2
    part_content_left = [row[:width_half] for row in part1]
    part_content_right = [row[:width_half] for row in part2]

    # 没有中间列
    if width % 2 == 0:
        divided_part_combos = list(product([part_content_left], [part_content_right]))

        # 组合出新局矩阵
        for divided_part_combo in divided_part_combos:
            concat = [left + right for left, right in zip(divided_part_combo[0], divided_part_combo[1])]
            concat_list.append(concat)
        return concat_list

    # 有中间列
    part_content_middle_1 = []
    part_content_middle_2 = []
    part_content_middle_list = []
    for row in part1:
        part_content_middle = row[width_half]
        part_content_middle_1.append([part_content_middle])
    for row in part2:
        part_content_middle = row[width_half]
        part_content_middle_2.append([part_content_middle])

    # part_content_middle_list有1至2个列
    part_content_middle_list.append(part_content_middle_1)
    if part_content_middle_1 != part_content_middle_2:
        part_content_middle_list.append(part_content_middle_2)

    # 组合出新的矩阵
    divided_part_combos = list(product([part_content_left], part_content_middle_list, [part_content_right]))
    for divided_part_combo in divided_part_combos:
        concat = [left + middle + right for left, middle, right in
                  zip(divided_part_combo[0], divided_part_combo[1], divided_part_combo[2])]
        concat_list.append(concat)
    return concat_list

def combin_part_row(part1, part2):
    concat_list = []
    height = len(part1)
    height_half = height // 2
    part_content_up = part1[:height_half]
    part_content_down = part2[:height_half]
    if height % 2 == 0:
        concat = []
        concat.extend(part_content_up)
        concat.extend(part_content_down)
        concat_list.append(concat)
        return concat_list

    part_content_middle_list = []
    part_content_middle_1 = part1[height_half]
    part_content_middle_2 = part2[height_half]

    part_content_middle_list.append(part_content_middle_1)
    # 相同就只用一个
    if part_content_middle_1 != part_content_middle_2:
        part_content_middle_list.append(part_content_middle_2)
    # print([part_content_up], part_content_middle_list, [part_content_down])
    divided_part_combos = list(product([part_content_up], part_content_middle_list, [part_content_down]))
    for divided_part_combo in divided_part_combos:
        concat = []
        concat.extend(divided_part_combo[0])
        concat.extend([divided_part_combo[1]])
        concat.extend(divided_part_combo[2])
        concat_list.append(concat)
    return concat_list

def generate_part_mixed_variant(height, width):
    print("=" * 60)
    print(f"{height}x{width}框架布局变体")
    print("=" * 60)
    filename = f"layouts/layouts_mixed_variant_{height}_{width}.json"
    part_list = load_all_layouts(filename=f"layouts/layouts_mixed_{height}_{width}.json")

    part_combos = list(product(part_list, part_list))

    height_half = height // 2

    concat_list = []
    for part_combo in part_combos:
        part1 = part_combo[0]
        part2 = part_combo[1]
        concat_list.extend(combin_part_column(part1=part1, part2=part2))
        concat_list.extend(combin_part_row(part1=part1, part2=part2))
    # for part_combo in part_combos:
    #     part1 = part_combo[0]
    #     part2 = part_combo[1]


    print(concat_list)
    # # 保存到JSON
    # with open(filename, 'w', encoding='utf-8') as f:
    #     json.dump(concat_list, f, indent=2)


def generate_part_mix_all():
    height = 4
    while height < 8:
        width = 4
        while width < 8:
            if width > height:
                width += 1
                continue
            generate_part_mix(height=height, width=width)
            width += 1
        height += 1


def do_part_mix(part1, part2):
    part_mix = []
    i = 0
    while i < len(part1):
        part_mix_row = []
        j = 0
        while j < len(part1[i]):
            if part1[i][j] == 1 and part2[i][j] == 1:
                return None
            if part1[i][j] == 1:
                part_mix_row.append(1)
                j += 1
                continue
            if part2[i][j] == 1:
                part_mix_row.append(2)
                j += 1
                continue
            part_mix_row.append(0)
            j += 1
        part_mix.append(part_mix_row)
        i += 1
    return part_mix

def generate_part_mix(height, width):
    print("=" * 60)
    print(f"{height}x{width}框架布局混合")
    print("=" * 60)
    filename = f"layouts/layouts_mixed_{height}_{width}.json"
    part_list = get_part_all(height=height, width=width)

    part_mix_list = []
    part_combos = list(product(part_list, part_list))
    for part_combo in part_combos:
        part_mix = do_part_mix(part_combo[0], part_combo[1])
        if part_mix is None:
            continue
        part_mix_list.append(part_mix)
        print(part_mix)

    # 保存到JSON
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(part_mix_list, f, indent=2)



def main():
    # generate_part_all()
    # generate_part_mix_all()
    # generate_part_mixed_variant_all()
    # height = 7
    # width = 7
    # filename = f"layouts/layouts_mixed_{height}_{width}.json"
    # layouts = load_all_layouts(filename=filename)
    # index_random = random.randint(0, len(layouts) - 1)
    # print(index_random)
    # BasePart(part_content=layouts[index_random]).show()

    generate_part_mixed_variant(height=4, width=4)


if __name__ == "__main__":
    main()