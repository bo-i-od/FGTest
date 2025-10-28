import glob
import os
import shutil
import struct
from typing import Optional

import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import cdist
import json


class TrajectoryDiversitySampler:
    def __init__(self, n_samples=100):
        self.n_samples = n_samples

    def extract_features(self, trajectory_data):
        """提取轨迹特征向量"""
        positions = trajectory_data['track_positions']

        # 提取坐标序列
        xs = [p['x'] for p in positions]
        ys = [p['y'] for p in positions]
        rots = [p['rotation_z'] for p in positions]

        features = []

        # 1. 统计特征
        features.extend([
            trajectory_data.get('life_time', 0),
            trajectory_data.get('velocity', 0),
            trajectory_data.get('global_trigger_count', 0),
            trajectory_data.get('ground_trigger_count', 0),
            len(trajectory_data.get('events', []))
        ])

        # 2. 轨迹形状特征
        features.extend([
            np.mean(xs), np.std(xs), np.min(xs), np.max(xs),
            np.mean(ys), np.std(ys), np.min(ys), np.max(ys),
            np.mean(rots), np.std(rots)
        ])

        # 3. 运动特征
        if len(xs) > 1:
            dx = np.diff(xs)
            dy = np.diff(ys)
            speeds = np.sqrt(dx ** 2 + dy ** 2)
            features.extend([
                np.mean(speeds), np.std(speeds), np.max(speeds)
            ])

            # 方向变化
            angles = np.arctan2(dy, dx)
            angle_changes = np.abs(np.diff(angles))
            features.extend([
                np.mean(angle_changes), np.max(angle_changes)
            ])
        else:
            features.extend([0, 0, 0, 0, 0])

        # 4. 轨迹采样点（等间隔采样20个点）
        sample_indices = np.linspace(0, len(xs) - 1, 20, dtype=int)
        for idx in sample_indices:
            features.extend([xs[idx], ys[idx]])

        return np.array(features)

    def select_diverse_samples(self, trajectories):
        """选择多样化的样本"""
        print(f"提取特征，共 {len(trajectories)} 条轨迹...")

        # 提取所有轨迹特征
        features_list = []
        valid_indices = []

        for i, traj in enumerate(trajectories):
            try:
                feat = self.extract_features(traj)
                features_list.append(feat)
                valid_indices.append(i)
            except Exception as e:
                print(f"轨迹 {i} 特征提取失败: {e}")

        features = np.array(features_list)

        # 标准化特征
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)

        # K-Means聚类
        print(f"执行K-Means聚类...")
        kmeans = KMeans(n_clusters=self.n_samples, random_state=42, n_init=10)
        labels = kmeans.fit_predict(features_scaled)

        # 从每个簇中选择最接近中心的样本
        selected_indices = []
        for cluster_id in range(self.n_samples):
            cluster_mask = labels == cluster_id
            if not cluster_mask.any():
                continue

            cluster_features = features_scaled[cluster_mask]
            cluster_center = kmeans.cluster_centers_[cluster_id]

            # 找到最接近中心的样本
            distances = cdist([cluster_center], cluster_features)[0]
            closest_idx = np.argmin(distances)

            # 转换回原始索引
            original_idx = valid_indices[np.where(cluster_mask)[0][closest_idx]]
            selected_indices.append(original_idx)

        return selected_indices


def get_bumper_sequence(folder_path, file_name):
    with open(fr"{folder_path}\{file_name}.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if "缓冲器碰撞序列" not in line:
                continue
            return line.split('=')[1].strip()
    return ""

def read_bytes_file(file_path):
    """读取C#保存的.bytes文件"""
    if not os.path.exists(file_path):
        print(f"文件不存在: {file_path}")
        return None

    data = {}

    with open(file_path, 'rb') as f:
        # 读取基础数据
        data['scene_id'] = struct.unpack('<i', f.read(4))[0]
        data['born_index'] = struct.unpack('<i', f.read(4))[0]
        data['dead_index'] = struct.unpack('<i', f.read(4))[0]

        # 读取筛选数据
        data['life_time'] = struct.unpack('<f', f.read(4))[0]
        data['velocity'] = struct.unpack('<f', f.read(4))[0]
        data['global_trigger_count'] = struct.unpack('<i', f.read(4))[0]
        data['ground_trigger_count'] = struct.unpack('<i', f.read(4))[0]

        # 读取统计数据
        statistic_count = struct.unpack('<i', f.read(4))[0]
        data['statistics'] = []
        for i in range(statistic_count):
            ball_type = struct.unpack('<i', f.read(4))[0]
            ball_index = struct.unpack('<i', f.read(4))[0]
            trigger_count = struct.unpack('<i', f.read(4))[0]
            data['statistics'].append({
                'ball_type': ball_type,
                'ball_index': ball_index,
                'trigger_count': trigger_count
            })

        # 读取碰撞事件
        events_count = struct.unpack('<i', f.read(4))[0]
        data['events'] = []
        for i in range(events_count):
            ball_type = struct.unpack('<i', f.read(4))[0]
            ball_index = struct.unpack('<i', f.read(4))[0]
            frame = struct.unpack('<i', f.read(4))[0]
            data['events'].append({
                'ball_type': ball_type,
                'ball_index': ball_index,
                'frame': frame
            })

        # 读取运动轨迹
        track_count = struct.unpack('<i', f.read(4))[0]
        data['track_positions'] = []
        for i in range(track_count):
            pos_x = struct.unpack('<h', f.read(2))[0] / 10.0  # 还原压缩的坐标
            pos_y = struct.unpack('<h', f.read(2))[0] / 10.0  # 还原压缩的坐标
            rotate_z = struct.unpack('<h', f.read(2))[0]
            data['track_positions'].append({
                'x': pos_x,
                'y': pos_y,
                'rotation_z': rotate_z
            })

    return data

def classification():
    folder_path = "arranged_data"  # 替换为你的文件路径
    output_base_folder = 'c2'
  # 创建输出基础文件夹
    if not os.path.exists(output_base_folder):
        os.makedirs(output_base_folder)

    pattern = os.path.join(folder_path, "*.bytes")
    files = glob.glob(pattern)

    for file_path in files:
        # print(f"\n处理文件: {os.path.basename(file_path)}")
        # print(file_path)
        data = read_bytes_file(file_path)
        file_name = os.path.basename(file_path).split(".")[0]
        bumper_sequence = get_bumper_sequence(folder_path=folder_path, file_name=file_name)
        bumper_attack_count = bumper_sequence.count("0")
        born_index = data["born_index"]
        dead_index = data["dead_index"]
        folder_name = f"born{born_index}_dead{dead_index}_attack{bumper_attack_count}"
        output_folder = os.path.join(output_base_folder, folder_name)


        # 复制原始 .bytes 文件到分类文件夹
        file_name = os.path.basename(file_path)

        dest_text_path = os.path.join(output_folder, file_name.split(".bytes")[0] + ".txt")
        file_path_txt = file_path.split(".bytes")[0] + ".txt"
        copy_file_to_target(source_file_path=file_path, target_directory=output_folder)
        copy_file_to_target(source_file_path=file_path_txt, target_directory=output_folder)
        # shutil.copy2(file_path, dest_bytes_path)
        # shutil.copy2(file_path_txt, dest_text_path)

    print("文件分类完成！")
    # 统计各个文件夹的文件数量
    print("\n各分类文件夹统计:")
    for folder_name in os.listdir(output_base_folder):
        folder_path = os.path.join(output_base_folder, folder_name)
        if os.path.isdir(folder_path):
            file_count = len([f for f in os.listdir(folder_path) if f.endswith('.bytes')])
            print(f"  {folder_name}: {file_count} 个文件")

def screening_all():
    cfg_list = [
        {0: 18, 1: 10, 2: 5, 3: 3, 4: 1, 5: 2, 7: 1},
        {0: 20, 1: 9, 2: 5, 3: 4, 4: 1, 5: 1},
        {0: 20, 1: 10, 2: 5, 3: 3, 4: 1, 5: 1},
        {0: 21, 1: 10, 2: 5, 3: 3, 4: 1},
        {0: 20, 1: 10, 2: 5, 3: 3, 4: 1, 5: 1},
        {0: 20, 1: 10, 2: 5, 3: 3, 5: 1, 6: 1},
        {0: 19, 1: 10, 2: 5, 3: 2, 4: 1, 5: 1, 7: 1, 8: 1},
        {0: 19, 1: 10, 2: 5, 3: 2, 4: 1, 5: 2, 6: 1},
        {0: 20, 1: 9, 2: 5, 3: 4, 4: 1, 5: 1},
        {0: 21, 1: 10, 2: 5, 3: 2, 4: 2},
        {0: 21, 1: 10, 2: 5, 3: 3, 4: 1},
        {0: 21, 1: 10, 2: 5, 3: 2, 4: 2},
        {0: 20, 1: 10, 2: 5, 3: 3, 5: 1, 6: 1},
        {0: 19, 1: 10, 2: 5, 3: 3, 4: 1, 6: 1, 7: 1},
        {0: 18, 1: 10, 2: 5, 3: 3, 4: 2, 5: 1, 6: 1},
        {0: 20, 1: 10, 2: 5, 3: 3, 4: 1, 7: 1},
        {0: 21, 1: 10, 2: 4, 3: 3, 4: 1, 5: 1},
        {0: 21, 1: 10, 2: 6, 3: 2, 4: 1},
        {0: 20, 1: 11, 2: 5, 3: 2, 4: 1, 5: 1},
        {0: 20, 1: 10, 2: 5, 3: 3, 5: 1, 6: 1},
        {0: 20, 1: 9, 2: 5, 3: 2, 4: 1, 5: 1, 6: 1, 8: 1},
        {0: 18, 1: 10, 2: 5, 3: 3, 4: 1, 5: 2, 7: 1},
        {0: 20, 1: 10, 2: 5, 3: 2, 4: 2, 6: 1},
        {0: 20, 1: 10, 2: 5, 3: 3, 4: 1, 5: 1},
        {0: 21, 1: 11, 2: 5, 3: 2, 4: 1},
        {0: 20, 1: 10, 2: 5, 3: 3, 4: 1, 5: 1},
        {0: 20, 1: 10, 2: 5, 3: 2, 4: 2, 6: 1},
        {0: 18, 1: 10, 2: 6, 3: 2, 4: 1, 5: 1, 6: 1, 7: 1},
        {0: 19, 1: 10, 2: 5, 3: 2, 4: 1, 5: 2, 6: 1},
        {0: 20, 1: 10, 2: 5, 3: 2, 4: 2, 6: 1},
        {0: 21, 1: 10, 2: 5, 3: 2, 4: 2},
        {0: 21, 1: 11, 2: 5, 3: 2, 4: 1},
        {0: 21, 1: 10, 2: 5, 3: 2, 4: 2},
        {0: 20, 1: 10, 2: 5, 3: 2, 4: 2, 6: 1},
        {0: 19, 1: 10, 2: 5, 3: 3, 4: 1, 6: 1, 7: 1},
    ]

    born_index = 0
    while born_index < 5:
        dead_index = 0
        while dead_index < 7:
            # 找到对应的
            index = born_index * 7 + dead_index
            cfg = cfg_list[index]
            for bumper_attack_count in cfg:
                screening(born_index=born_index, dead_index=dead_index, bumper_attack_count=bumper_attack_count, script_count=cfg[bumper_attack_count])
            dead_index += 1
        born_index += 1



def screening(born_index, dead_index, bumper_attack_count, script_count):
    source_base_folder = 'classified_data'
    source_folder_name = f"born{born_index}_dead{dead_index}_attack{bumper_attack_count}"
    source_folder = os.path.join(source_base_folder, source_folder_name)
    # 检查源文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"源文件夹不存在: {source_folder}")
        return []

    # 读取文件夹中的所有.bytes文件
    pattern = os.path.join(source_folder, "*.bytes")
    files = glob.glob(pattern)
    file_path_list = []
    trajectories = []
    for file in files:
        data = read_bytes_file(file_path=file)
        if data["life_time"] < 4.5:
            continue
        if data["global_trigger_count"] < 6:
            continue
        if data["track_positions"][-1]["y"] > -550:
            continue
        if not freeze_check(track_positions=data["track_positions"]):
            continue
        file_path_list.append(file)
        trajectories.append(data)

    # 初始化采样器
    sampler = TrajectoryDiversitySampler(n_samples=script_count)

    # 选择多样化轨迹
    selected_indices = sampler.select_diverse_samples(trajectories)

    print(f"选择了 {len(selected_indices)} 条轨迹")
    output_folder = "arranged_data"
    for i in selected_indices:
        copy_file_to_target(source_file_path=file_path_list[i], target_directory=output_folder)
        copy_file_to_target(source_file_path=file_path_list[i].split(".bytes")[0] + ".txt", target_directory=output_folder)





def copy_file_to_target(source_file_path: str, target_directory: str, new_name: Optional[str] = None) -> Optional[str]:
    """
    复制文件到目标目录

    Args:
        source_file_path: 源文件路径
        target_directory: 目标目录
        new_name: 新文件名（可选，如果不提供则保持原名）

    Returns:
        目标文件路径
    """
    try:
        # 转换为字符串类型确保类型正确
        source_path = str(source_file_path)
        target_dir = str(target_directory)

        # 确保目标目录存在
        os.makedirs(target_dir, exist_ok=True)

        # 获取源文件名
        if new_name:
            target_file_name = str(new_name)
        else:
            target_file_name = os.path.basename(source_path)

        # 构建目标文件路径
        target_file_path = os.path.join(target_dir, target_file_name)

        # 复制文件 - 确保参数都是字符串类型
        shutil.copy2(source_path, target_file_path)
        print(f"已复制: {os.path.basename(source_path)} -> {target_file_path}")

        return target_file_path

    except Exception as e:
        print(f"复制文件失败: {source_file_path} -> {target_directory}, 错误: {e}")
        return None

def freeze_check(track_positions):
    if len(track_positions) < 75:
        return True
    total = 0
    cur = 50
    y_pre = track_positions[-cur]['y']
    x_pre = track_positions[-cur]['x']
    while cur <= 70:
        cur += 1
        y_delta = abs(y_pre - track_positions[-cur]['y'])
        x_delta = abs(x_pre - track_positions[-cur]['x'])
        y_pre = track_positions[-cur]['y']
        x_pre = track_positions[-cur]['x']
        total += y_delta + x_delta
    if total < 5:
        return False
    return True

def main():
    # # 把原数据根据口和碰撞缓冲器的次数分类到classified_data文件夹下
    # classification()

    # 筛选出最离散的若干数据
    screening_all()




# 使用示例
if __name__ == "__main__":
    main()