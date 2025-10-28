from common.basePage import BasePage
from panelObjs.LoginPanel import LoginPanel


def init(bp: BasePage):
    if LoginPanel.is_panel_active(bp):
        return
    logout(bp)



def connect(bp: BasePage, accountName):
    bp.clear_popup()
    lua_code = f"""
_G.NetworkMgr:SDKLogin("{accountName}")
    """
    bp.lua_console(lua_code)


def disconnect(bp: BasePage):
    lua_code ="""local logout = function()
    local strResult = '{"code":0}'
    local json = require "cjson"
    local jsonResult = json.decode(strResult)
    if jsonResult.code ~= 0 then
        return
    end
    SavingSystem:SaveData("Login_Token", "")
    SavingSystem:Save()
    coroutine.start(function ()
        _G.CURRENT_SDK_MANUAL_LOGIN = true
        local co = PanelMgr:CloseAllOpend()
        Global_ClearCacheData()
        NetworkMgr.channelPurl = nil
        NetworkMgr:StopTimeOutTimer()
        NetworkMgr:Disconnect()
        UIFacade.Reset()
        coroutine.waitCo(co)
        EventMgr:SendEvent(GameMsg.CHANGE_GAME_STATE, GAME_STATE_ENUM.Login, true)
    end)
end
logout()
"""
#     lua_code = """_G.CURRENT_SDK_MANUAL_LOGIN = true
# PanelMgr:CloseAllOpend()
# Global_ClearCacheData()
# Global_SendLogout()
# _G.NetworkMgr:StopTimeOutTimer()
# _G.NetworkMgr:Disconnect()
# UIFacade.Reset()
# --Util.GoToLogin()
# EventMgr:SendEvent(GameMsg.CHANGE_GAME_STATE, GAME_STATE_ENUM.Login, true)
# """
    bp.lua_console(lua_code)


def login(bp: BasePage, name):
    LoginPanel.wait_for_panel_appear(bp)
    connect(bp, name)
    bp.sleep(1)


def logout(bp: BasePage):
    bp.sleep(1)
    disconnect(bp)



if __name__ == '__main__':
    bp = BasePage(is_mobile_device=False, serial_number="127.0.0.1:21503")

