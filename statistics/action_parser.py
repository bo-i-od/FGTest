# roll_action_parser.py
import json

def parser_roll(action, res: dict):
    # pprint(action)
    action_result_list = action["actionResultLis"]
    dice_action_result = action_result_list["1"]["diceActionResult"]
    move_action_result = action_result_list["2"]["moveActionResult"]
    res["diceActionResult"] = dice_action_result
    res["moveActionResult"] = move_action_result



def parser_atk_building(action, res: dict):
    action_result_list = action["actionResultLis"]
    action_result = action_result_list["1"]
    atk_building_result = action_result["atkBuildingResult"]
    res["atkBuildingResult"] = atk_building_result


def parser_heist(action, res: dict):
    action_result_list = action["actionResultLis"]
    action_result = action_result_list["1"]
    bank_heist_action_result = action_result["bankHeistActionResult"]
    res["bankHeistActionResult"] = bank_heist_action_result


def parser_main_roll(log_path, json_data, line):
    actions = json_data["actions"]
    # pprint(actions)

    for action_index in actions:
        action = actions[action_index]
        action_name = "rollAction"
        if action_name in action:
            save_line(log_path, line=line)
            line = {}
            # pprint(action)
            parser_roll(action[action_name], line)
            continue
        action_name = "atkBuildingAction"
        if action_name in action:
            parser_atk_building(action[action_name], line)
            continue
        action_name = "bankHeistAction"
        if action_name in action:
            parser_heist(action[action_name], line)
            continue
    return line


def parser_fish_cast(action, res: dict):
    fish_cast_result = action["fishCastResult"]
    res["fishCastResult"] = fish_cast_result

def parser_fish_hook(action, res: dict):
    fish_hook_result = action["fishHookResult"]
    res["fishHookResult"] = fish_hook_result


def parser_main_fish(log_path, json_data, line):
    actions = json_data["actions"]
    # pprint(actions)

    for action_index in actions:
        action = actions[action_index]
        action_name = "fishCastAction"
        if action_name in action:
            save_line(log_path, line=line)
            line = {}
            parser_fish_cast(action[action_name], line)
            continue
        action_name = "fishHookAction"
        if action_name in action:
            parser_fish_hook(action[action_name], line)
            continue
    return line


def save_line(log_path, line):
    if not line:
        return
    f = open(f"../statistics/{log_path}", "a")
    f.write(json.dumps(line) + "\n")
    f.close()


def clear_roll_log(log_path):
    """清空.txt文件"""
    print(f"清空{log_path}")
    f = open(f"../statistics/{log_path}", "w")
    f.close()


def parser_fish_actions():
    log_path = "fish_actions_log.txt"
    clear_roll_log(log_path)
    f = open("../statistics/cs_validate_actions_msg_log.txt", "r")
    data_list = f.readlines()
    f.close()
    line = {}
    for data in data_list:
        d = json.loads(data)
        line = parser_main_fish(log_path,d, line)
    save_line(log_path, line=line)


def parser_roll_actions():
    log_path = "roll_actions_log.txt"
    clear_roll_log(log_path)
    f = open("../statistics/cs_validate_actions_msg_log.txt", "r")
    data_list = f.readlines()
    f.close()
    line = {}
    for data in data_list:
        d = json.loads(data)
        line = parser_main_roll(log_path,d, line)
    save_line(log_path, line=line)


if __name__ == '__main__':
    parser_roll_actions()
