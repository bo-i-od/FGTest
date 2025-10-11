import json
import os

def get_max_same_color_ball_count_and_max_count(puzzle):
    puzzle_split_list = puzzle.split(';')
    max_repeat_color_ball_count = 0
    max_count = 0
    for puzzle_split in puzzle_split_list:
        res = puzzle_split.split(':')
        res_0 = int(res[0])
        res_1 = int(res[1])
        if res_0 > max_repeat_color_ball_count:
            max_repeat_color_ball_count = res_0
        if res_1 > max_count:
            max_count = res_1
    return max_repeat_color_ball_count, max_count


def load_cost_cfg() -> dict:
    path = "cost_cfg.json"
    return json.load(open(path, "r")) if os.path.exists(path) else {}

def get_detail(cost_cfg):
    reward_ratio = 8
    detail = []
    for item in cost_cfg:
        temp_res = {}
        temp_res["puzzle"] = item
        temp_res["expect_cost"] = cost_cfg[item]
        max_same_color_ball_count, max_count = get_max_same_color_ball_count_and_max_count(item)
        temp_res["reward_quantity"] = int(cost_cfg[item] * reward_ratio * 0.2 + 1.5 * (max_same_color_ball_count - 1) + 0.5) * 5
        # temp_res["reward_quantity"] *= max_same_color_ball_count * 10
        temp_res["weight"] = int(max_count * 100 * (1 + 0.1 * max_same_color_ball_count))
        detail.append(temp_res)
    return detail



def main():
    cost_cfg = load_cost_cfg()
    detail = get_detail(cost_cfg)
    detail.sort(key=lambda x: x['expect_cost'])
    print(detail)



if __name__ == "__main__":
    main()