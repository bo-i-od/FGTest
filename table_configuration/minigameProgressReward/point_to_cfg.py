import random


def progress_part(point_list, point_begin):
    progress_range_max = point_list[-2] - point_list[-4]
    progress_range = int(random.randint(int(progress_range_max * 0.8), int(progress_range_max * 0.95)) // 10 * 10)

    progress_range_end_min = point_list[-1] - point_list[-2]
    progress_range_end = int(random.randint(int(progress_range_end_min * 1.3), int(progress_range_end_min * 1.5)) // 10 * 10)
    progress_node_list = []
    # 第一条涵盖前三个
    cur = 0
    while cur < len(point_list):
        progress_node = {"point": point_list[cur] + point_begin}
        if cur < len(point_list) - 2:

            if cur == 0:
                progress_node["pointStart"] = point_begin
            else:
                progress_node["pointStart"] = point_list[cur - 1] + point_begin
            progress_node["pointEnd"] = progress_node["pointStart"] + progress_range
            progress_node["forceMoveOut"] = 1
            progress_node_list.append(progress_node)
            cur += 1
            continue
        # 倒数第二个节点的条 要保证数第二个节点完成后左移
        if cur < len(point_list) - 1:

            a = progress_range*random.randint(105, 125) * 0.01
            print(a, progress_range_end)
            progress_range = int(min(a, progress_range_end) // 10 * 10)
            # position_normal = point_list[-2] / (point_list[cur] + point_begin - progress_node["pointEnd"] + progress_range_end) + random.randint(25, 45) * 0.01
            progress_node["pointStart"] = point_list[-3] + point_begin
            progress_node["pointEnd"] = progress_node["pointStart"] + progress_range
            progress_node_list.append(progress_node)
            cur += 1
            continue
        # 最后个节点的条 要涵盖住倒数第二个节点
        point_end = point_list[cur] + point_begin
        progress_node["pointStart"] = point_end - progress_range_end
        progress_node["pointEnd"] = point_end
        progress_node["grandPrize"] = 1
        progress_node_list.append(progress_node)
        cur += 1
    return progress_node_list

def main():
    # progress_list = [[440, 1265, 2480, 3920, 6400],[1600, 4400, 7200, 12400,16800, 24320]]
    progress_list = [[380, 1090, 2150, 3390, 4620, 6400], [1000, 3050, 4960, 7860,11200, 16210, 24320]]
    # progress_list = [[450, 1210, 2330, 4250, 7660], [960, 2660, 4830, 7660, 11900, 16000, 23060]]
    # progress_list = [[450, 1000, 2480, 5500, 9000], [1300, 2690, 4370, 6500, 9330, 13260, 18900]]
    # progress_list = [[380, 930, 1680, 2810, 4650], [560, 1380, 2430, 3860, 5980, 9300,],[ 1000, 2260, 3860, 6030, 9170, 13950]]
    # progress_list = [[300, 930, 1700, 2860, 4700], [530, 1300, 2330, 3800, 5900, 9000],[960,2200,3800,5960,9160, 14200]]
    # progress_list = [[1420, 3210, 7890, 17490, 28640, 32820, 37230, 42560, 49350, 58420, 70320, 84000]]
    cfg = []
    point_begin = 0
    for point_list in progress_list:
        progress_node_list = progress_part(point_list=point_list, point_begin=point_begin)
        point_begin = progress_node_list[-1]["point"]
        cfg.extend(progress_node_list)
    print(cfg)



if __name__ == '__main__':
    main()