from tools.commonTools import lua_dict_to_python_dict
import json
from pathlib import Path

# 获取脚本文件所在目录
script_dir = Path(__file__).parent
# 构建statistics目录的绝对路径
statistics_dir = script_dir.parent / "statistics"

def deal_with_msg(msg):
    # if '<==== [Lua] Receive Net Msg "SC' in msg:
    #     print(msg)

    # print(msg)
    if '<==== [Lua] Send net Msg "CSValidateActionsMsg" ====>' in msg:
        deal_with_CSValidateActionsMsg(msg)
        return

    if '<==== [Lua] Receive Net Msg "SCValidateActionsMsg" ====>' in msg:
        deal_with_SCValidateActionsMsg(msg)
        return



    # if '<==== [Lua] Receive Net Msg "SCEnterGameMsg" ====>' in msg:
    #     print(msg)
    #     return


def deal_with_CSValidateActionsMsg(msg):
    # print(msg)
    msg_data=lua_dict_to_python_dict(msg)
    statistics_dir.mkdir(exist_ok=True)

    log_file = statistics_dir / "cs_validate_actions_msg_log.txt"
    with open(log_file, "a") as f:
        f.write(json.dumps(msg_data) + "\n")

def deal_with_SCValidateActionsMsg(msg):
    # print(msg)
    msg_data=lua_dict_to_python_dict(msg)
    log_file = statistics_dir / "sc_validate_actions_msg_log.txt"
    with open(log_file, "a") as f:
        f.write(json.dumps(msg_data) + "\n")
    if msg_data["notify"]["msg"] == "success":
        return
    print(msg_data["notify"]["msg"])
