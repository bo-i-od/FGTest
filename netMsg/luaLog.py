from tools.commonTools import lua_dict_to_python_dict
import json

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
    f = open("../statistics/cs_validate_actions_msg_log.txt", "a")
    f.write(json.dumps(msg_data)+"\n")
    f.close()

def deal_with_SCValidateActionsMsg(msg):
    # print(msg)
    msg_data=lua_dict_to_python_dict(msg)
    f = open("../statistics/sc_validate_actions_msg_log.txt", "a")
    f.write(json.dumps(msg_data)+"\n")
    f.close()
    if msg_data["notify"]["msg"] == "success":
        return
    print(msg_data["notify"]["msg"])
