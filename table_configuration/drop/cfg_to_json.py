import json

from table_configuration.drop.desk_cfg import *


def convert_cfg_to_json():

    # 继续添加其他配置... (为了节省篇幅，这里只展示cfg_1和cfg_2)
    # 你需要将所有的cfg_3到cfg_7也复制进来

    # 组织数据
    game_configs = {
        "component_types": {
            "0": "下落口",
            "1": "得分口",
            "2": "钉",
            "3": "缓冲器",
            "4": "多边形障碍",
            "5": "墙",
        },
        "level": cfg_6,
    }

    return game_configs


def save_to_json(data, filename="game_configs.json"):
    """保存数据到JSON文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"数据已保存到 {filename}")


def save_to_pretty_json(data, filename="game_configs_pretty.json"):
    """保存为格式化的JSON文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False, separators=(',', ': '))
    print(f"格式化数据已保存到 {filename}")


def print_json_string(data):
    """打印JSON字符串"""
    json_string = json.dumps(data, indent=2, ensure_ascii=False)
    print("JSON格式数据:")
    print(json_string)


if __name__ == "__main__":
    # 转换数据
    converted_data = convert_cfg_to_json()

    # # 选择输出方式
    # print("请选择输出方式:")
    # print("1. 保存到文件")
    # print("2. 打印到控制台")
    # print("3. 两者都要")
    #
    # choice = input("请输入选择 (1/2/3): ").strip()

    # if choice in ['1', '3']:
    save_to_json(converted_data)
    # save_to_pretty_json(converted_data)

    # if choice in ['2', '3']:
    print_json_string(converted_data)