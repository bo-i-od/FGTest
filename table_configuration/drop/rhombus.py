import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def rhombus_vertices_after_rotation(d1, d2, angle_degrees, center=(0, 0)):
    """
    计算菱形旋转后的顶点坐标

    参数:
    d1: 第一条对角线长度 (初始时沿x轴)
    d2: 第二条对角线长度 (初始时沿y轴)
    angle_degrees: 旋转角度 (度)
    center: 旋转中心 (默认为原点)

    返回:
    vertices: 旋转后的四个顶点坐标 [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]
    """

    # 将角度转换为弧度
    angle_rad = np.radians(angle_degrees)

    # 初始菱形的四个顶点（对角线与xy轴重合）
    # 顶点顺序：右、上、左、下
    initial_vertices = np.array([
        [d1 / 2, 0],  # 右顶点
        [0, d2 / 2],  # 上顶点
        [-d1 / 2, 0],  # 左顶点
        [0, -d2 / 2]  # 下顶点
    ])

    # 旋转矩阵
    rotation_matrix = np.array([
        [np.cos(angle_rad), -np.sin(angle_rad)],
        [np.sin(angle_rad), np.cos(angle_rad)]
    ])

    # 应用旋转
    rotated_vertices = []
    for vertex in initial_vertices:
        # 先移动到原点（如果旋转中心不是原点）
        vertex_centered = vertex - np.array(center)
        # 旋转
        rotated_vertex = rotation_matrix @ vertex_centered
        # 移回旋转中心
        final_vertex = rotated_vertex + np.array(center)
        rotated_vertices.append(final_vertex)

    return np.array(rotated_vertices)


def plot_rhombus(vertices, title="菱形"):
    """
    绘制菱形
    """
    plt.figure(figsize=(8, 8))

    # 闭合菱形（连接最后一个点到第一个点）
    vertices_closed = np.vstack([vertices, vertices[0]])

    plt.plot(vertices_closed[:, 0], vertices_closed[:, 1], 'b-o', linewidth=2, markersize=8)

    # 标注顶点
    for i, (x, y) in enumerate(vertices):
        plt.annotate(f'P{i + 1}({x:.2f}, {y:.2f})',
                     (x, y), xytext=(5, 5), textcoords='offset points')

    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')

    # 绘制坐标轴
    plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
    plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)

    plt.show()


# 示例使用
if __name__ == "__main__":
    # 菱形参数
    diagonal1 = 100  # 对角线1长度
    diagonal2 = 50  # 对角线2长度
    rotation_angle = -27  # 旋转角度（度）

    print(f"菱形参数：")
    print(f"对角线1长度：{diagonal1}")
    print(f"对角线2长度：{diagonal2}")
    print(f"旋转角度：{rotation_angle}°")
    print("-" * 40)

    # 计算初始顶点
    initial_vertices = rhombus_vertices_after_rotation(diagonal1, diagonal2, 0)
    print("初始顶点坐标：")
    for i, (x, y) in enumerate(initial_vertices):
        print(f"'vertex': [{x:.2f}, {-y:.2f}]}}")

    # 计算旋转后顶点
    rotated_vertices = rhombus_vertices_after_rotation(diagonal1, diagonal2, rotation_angle)
    print(f"\n旋转{rotation_angle}°后的顶点坐标：")
    res = "'vertex':[ "
    for i, (x, y) in enumerate(rotated_vertices):
        res += f"[{x:.2f}, {-y:.2f}],"
    res += "]}"
    print(res)

    # 绘制图形
    plt.subplot(1, 2, 1)
    vertices_closed = np.vstack([initial_vertices, initial_vertices[0]])
    plt.plot(vertices_closed[:, 0], vertices_closed[:, 1], 'b-o', linewidth=2, markersize=8)
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.title('初始菱形')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.subplot(1, 2, 2)
    vertices_closed = np.vstack([rotated_vertices, rotated_vertices[0]])
    plt.plot(vertices_closed[:, 0], vertices_closed[:, 1], 'r-o', linewidth=2, markersize=8)
    plt.grid(True, alpha=0.3)
    plt.axis('equal')
    plt.title(f'旋转{rotation_angle}°后')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.tight_layout()
    plt.show()