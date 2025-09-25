from tools.commonTools import lua_dict_to_python_dict
import json

def deal_with_msg(msg):
    # if '<==== [Lua] Receive Net Msg "SC' in msg:
    #     print(msg)

    # print(msg)
    if '<==== [Lua] Receive Net Msg "SCFishingCastMsg" ====>' in msg:
        deal_with_SCFishingCastMsg(msg)
        return



    # if '<==== [Lua] Receive Net Msg "SCEnterGameMsg" ====>' in msg:
    #     print(msg)
    #     return


def deal_with_SCFishingCastMsg(msg):
    # print(msg)
    msg_data=lua_dict_to_python_dict(msg)
    f = open("../statistics/new_cast_log.txt", "a")
    f.write(json.dumps(msg_data)+"\n")
    f.close()



    