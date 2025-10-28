from configs.pathConfig import DEV_EXCEL_PATH
from tools.run_excel_vba_function import runVBAExcel
from time import sleep

if __name__ == "__main__":
    # excel_list = ['FORTUNE_FLIP_DEAL.xlsm', 'ITEM_MAIN.xlsm', 'ITEM_PACKAGE.xlsm', 'JUGGLE_JAM_EVENT.xlsm', 'MINIGAME_PROGRESS_REWARD.xlsm', 'POINT_PROGRESS_REWARD.xlsm', 'RESOURCE.xlsm', 'ITEM_CONVERT_RULE.xlsm']
    excel_list = [ 'ITEM_PACKAGE.xlsm', 'ITEM_CONVERT_RULE.xlsm', 'MINIGAME_PROGRESS_REWARD.xlsm', 'POINT_PROGRESS_REWARD.xlsm',]

    # 'BATTLE_SKILL.xlsm', 'SKILL.xlsm', 'SKILL_POWER.xlsm','BATTLE_BUFF.xlsm', 'SKILL_POWER_INIT.xlsm'
    # ['BATTLE_SKILL.xlsm', 'SKILL.xlsm', 'SKILL_LANGUAGE.xlsm', 'BATTLE_BUFF.xlsm', 'BATTLE_ATTR.xlsm',
     # 'BATTLE_NOTICE.xlsm']

    for excel in excel_list:
        path = DEV_EXCEL_PATH + excel
        print(path)
        runVBAExcel(path)
        sleep(1)
