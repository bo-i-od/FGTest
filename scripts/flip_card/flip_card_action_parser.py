import json
from pathlib import Path

def save_line(log_path, line):
    if not line:
        return
    # target_file = Path(__file__).parent.parent.parent / "statistics" / log_path
    f = open(log_path, "a")
    f.write(json.dumps(line) + "\n")
    f.close()

def clear_roll_log(log_path):
    """清空.txt文件"""
    print(f"清空{log_path}")
    f = open(f"{log_path}", "w")
    f.close()


def parser_startFlipCardAction(action, res: dict):
    action_result_list = action["actionResultLis"]
    for action_result in action_result_list:
        if "subtractItemActionResult" in action_result_list[action_result]:
            res["subtractItemActionResult"] = action_result_list[action_result]["subtractItemActionResult"]
            continue

def parser_createFlipCardAction(action, res: dict):
    action_result_list = action["actionResultLis"]
    for action_result in action_result_list:
        if "createFlipCardResult" in action_result_list[action_result]:
            res["createFlipCardResult"] = action_result_list[action_result]["createFlipCardResult"]
            continue

def parser_chooseFlipCardAction(action, res: dict):
    action_result_list = action["actionResultLis"]
    for action_result in action_result_list:
        if "chooseFlipCardResult" in action_result_list[action_result]:
            res["chooseFlipCardResult"] = action_result_list[action_result]["chooseFlipCardResult"]
            continue
        if "useFuncCardResult" in action_result_list[action_result]:
            res["useFuncCardResult"] = action_result_list[action_result]["useFuncCardResult"]
            continue
        if "progressPointAddResult" in action_result_list[action_result]:
            res["progressPointAddResult"] = action_result_list[action_result]["progressPointAddResult"]
            continue


def parser_main(log_path, json_data):
    actions = json_data["actions"]
    # pprint(actions)

    for action_index in actions:
        action = actions[action_index]
        action_name = "startFlipCardAction"
        if action_name in action:
            line = {}
            parser_startFlipCardAction(action[action_name], line)
            save_line(log_path, line=line)
            continue
        action_name = "createFlipCardAction"
        if action_name in action:
            line = {}
            parser_createFlipCardAction(action[action_name], line)
            save_line(log_path, line=line)
            continue
        action_name = "chooseFlipCardAction"
        if action_name in action:
            line = {}
            parser_chooseFlipCardAction(action[action_name], line)
            save_line(log_path, line=line)
            continue


def main():
    log_path = "flip_card_actions_log.txt"
    clear_roll_log(log_path)
    # 获取当前文件的父目录的父目录，然后进入 statistics 目录
    target_file = Path(__file__).parent.parent.parent / "statistics" / "cs_validate_actions_msg_log.txt"
    f = open(target_file, "r")
    data_list = f.readlines()
    f.close()
    for data in data_list:
        d = json.loads(data)
        line = parser_main(log_path,d)


if __name__ == '__main__':
    main()