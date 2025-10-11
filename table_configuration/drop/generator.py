import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from table_configuration.drop.desk_cfg import *
# 解决中文字体显示问题
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def draw_pachinko(cfg):
    fig, ax = plt.subplots(figsize=(10, 12))

    for item in cfg:
        comp = item["component"]
        pos = item["position"]
        if comp in (0, 1):  # 下落口 / 得分口 (线段)
            verts = np.array(item["vertex"])
            verts = verts + np.array(pos)
            ax.plot(verts[:, 0], verts[:, 1],
                    color="blue" if comp == 0 else "green",
                    linewidth=3)

        elif comp == 2:  # 钉子
            circle = patches.Circle(pos, item["radius"],
                                    color="red", zorder=3)
            ax.add_patch(circle)

        elif comp == 3:  # 缓冲器
            bumper = patches.Circle(pos, item["radius"],
                                    edgecolor="orange", facecolor="none",
                                    linewidth=2, zorder=2)
            ax.add_patch(bumper)

        elif comp == 4:  # 多边形障碍
            verts = np.array(item["vertex"]) + np.array(pos)
            poly = patches.Polygon(verts, closed=True,
                                   facecolor="purple", alpha=0.3,
                                   edgecolor="black")
            ax.add_patch(poly)
    # ==== 修正后的【四周描边】 ====
    # 定义边界范围
    left, right = -2, 1002
    top, bottom = -2, 1002   # y 向下翻转了，所以 top 是小值，bottom 是大值
    # 上边
    ax.plot([left, right], [top, top], color="black", linewidth=2)
    # 下边
    ax.plot([left, right], [bottom, bottom], color="black", linewidth=2)
    # 左边
    ax.plot([left, left], [top, bottom], color="black", linewidth=2)
    # 右边
    ax.plot([right, right], [top, bottom], color="black", linewidth=2)

    ax.set_aspect("equal")
    ax.invert_yaxis()  # 让Y向下符合“下落”直觉
    ax.set_title("柏青哥盘面配置可视化", fontsize=16)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    plt.show()


# ---- 直接使用你的配置 ----
def main():
    draw_pachinko(cfg_6)


if __name__ == '__main__':
    main()