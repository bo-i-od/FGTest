# preview.py
import csv
import os
import random
import re
from dataclasses import dataclass
from typing import List, Tuple, Optional

import matplotlib
matplotlib.use('Agg')  # 非交互后端，不弹窗
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib import colormaps as mcm  # 替换已弃用的 plt.cm.get_cmap

# 是否允许旋转，例如 1x3 可以作为 3x1 放置
ALLOW_ROTATION = True
# 保存图片 DPI
SAVE_DPI = 180
# 回溯最大尝试次数（增大可提高求解率，但更慢）
MAX_ATTEMPTS = 300

@dataclass
class Piece:
    h: int     # 高
    w: int     # 宽
    label: str # 显示用（例如 "1x3"）

@dataclass
class Placement:
    r: int     # 左上角行（0-based，向下增）
    c: int     # 左上角列（0-based，向右增）
    h: int
    w: int
    label: str # 显示用

def parse_pieces(pieces_str: str) -> List[Piece]:
    """
    解析形如 '1x2=1;1x3=1' -> [Piece(1,2), Piece(1,3)]
    """
    pieces = []
    if not pieces_str:
        return pieces
    parts = [p.strip() for p in pieces_str.split(';') if p.strip()]
    for part in parts:
        if '=' not in part:
            continue
        dims, cnt_str = part.split('=', 1)
        cnt = int(cnt_str.strip())
        dims = dims.lower().replace('×', 'x').strip()
        if 'x' not in dims:
            continue
        a, b = dims.split('x', 1)
        ph = int(a.strip())
        pw = int(b.strip())
        for _ in range(cnt):
            pieces.append(Piece(h=ph, w=pw, label=f"{ph}x{pw}"))
    return pieces

def solve_board(H: int, W: int, pieces: List[Piece], rng: random.Random, max_attempts: int = MAX_ATTEMPTS) -> Optional[List[Placement]]:
    """
    回溯法在 HxW 的网格上放置所有 pieces（允许留空），返回一个解（其中一个）或 None。
    使用 rng 控制随机性，实现可复现。
    """
    if not pieces:
        return []

    grid = [[-1 for _ in range(W)] for _ in range(H)]  # -1 表示空
    idxs = list(range(len(pieces)))

    def can_place(r: int, c: int, ph: int, pw: int) -> bool:
        if r < 0 or c < 0 or r + ph > H or c + pw > W:
            return False
        for rr in range(r, r + ph):
            for cc in range(c, c + pw):
                if grid[rr][cc] != -1:
                    return False
        return True

    def set_cells(r: int, c: int, ph: int, pw: int, val: int):
        for rr in range(r, r + ph):
            for cc in range(c, c + pw):
                grid[rr][cc] = val

    # 面积大 -> 小，长边优先
    base_order = sorted(idxs, key=lambda i: (pieces[i].h * pieces[i].w, max(pieces[i].h, pieces[i].w)), reverse=True)

    for attempt in range(max_attempts):
        placements: List[Placement] = []
        order = base_order[:]
        if attempt > 0:
            rng.shuffle(order)

        # 清空网格
        for r in range(H):
            for c in range(W):
                grid[r][c] = -1

        def backtrack(k: int) -> bool:
            if k == len(order):
                return True
            i = order[k]
            piece = pieces[i]
            orientations: List[Tuple[int, int]] = [(piece.h, piece.w)]
            if ALLOW_ROTATION and piece.h != piece.w:
                orientations.append((piece.w, piece.h))
            rng.shuffle(orientations)

            rows = list(range(H))
            cols = list(range(W))
            rng.shuffle(rows)
            rng.shuffle(cols)

            for ph, pw in orientations:
                for r in rows:
                    for c in cols:
                        if can_place(r, c, ph, pw):
                            set_cells(r, c, ph, pw, k)
                            placements.append(Placement(r=r, c=c, h=ph, w=pw, label=piece.label))
                            if backtrack(k + 1):
                                return True
                            placements.pop()
                            set_cells(r, c, ph, pw, -1)
            return False

        if backtrack(0):
            return placements

    return None

def draw_and_save_board(H: int, W: int, placements: Optional[List[Placement]], title: str, save_path: str):
    """
    画出棋盘与已放置的矩形块，并保存为 PNG。
    """
    # 画布大小：每格 0.8 英寸，外加边距
    fig_w = max(3, W * 0.8 + 1.5)
    fig_h = max(3, H * 0.8 + 1.2)

    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_title(title, fontsize=11)

    # 画网格
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)  # 让 y 轴向下
    ax.set_aspect('equal')
    ax.set_xticks(range(0, W + 1))
    ax.set_yticks(range(0, H + 1))
    ax.grid(True, which='both', color='#CCCCCC', linewidth=1)

    # 使用新 API 获取颜色表
    cmap = mcm.get_cmap('tab20')
    palette_colors = list(getattr(cmap, 'colors', []))
    if not palette_colors:
        palette_colors = [cmap(i / max(1, (cmap.N - 1))) for i in range(cmap.N)]
    color_map = {}

    def get_color(label: str):
        if label not in color_map:
            color_map[label] = palette_colors[len(color_map) % len(palette_colors)]
        return color_map[label]

    if placements:
        for p in placements:
            rect = Rectangle((p.c, p.r), p.w, p.h,
                             facecolor=get_color(p.label), alpha=0.78,
                             edgecolor='black', linewidth=1.5)
            ax.add_patch(rect)
            ax.text(p.c + p.w / 2, p.r + p.h / 2, p.label,
                    color='black', ha='center', va='center',
                    fontsize=10, weight='bold')
    else:
        ax.text(W / 2, H / 2, "无解（无法放置）",
                color='red', ha='center', va='center',
                fontsize=14, weight='bold')

    plt.tight_layout()
    fig.savefig(save_path, dpi=SAVE_DPI, bbox_inches='tight', pad_inches=0.15)
    plt.close(fig)

def build_row_signature(row: dict) -> str:
    """
    严格使用 CSV 行的六个字段拼接：
    board_h,board_w,total_area,board_area,fill_rate,pieces
    例如：3,4,7,12,0.583333,1x3=1;2x2=1
    保留逗号和分号，便于匹配。
    """
    h = (row.get('board_h') or '').strip()
    w = (row.get('board_w') or '').strip()
    total_area = (row.get('total_area') or '').strip()
    board_area = (row.get('board_area') or '').strip()
    fill_rate = (row.get('fill_rate') or '').strip()
    pieces_str = (row.get('pieces') or '').strip()
    return f"{h},{w},{total_area},{board_area},{fill_rate},{pieces_str}"

def safe_filename(base: str) -> str:
    """
    将标题字符串转换为安全的文件名：
    - Windows: 替换非法字符 \ / : * ? " < > | 为下划线
    - 允许逗号、分号和点
    - 去除首尾空格、换行、制表符
    - 避免以点或空格结尾
    """
    s = base.strip().replace('\r', ' ').replace('\n', ' ').replace('\t', ' ')
    if os.name == 'nt':
        s = re.sub(r'[\\/:*?"<>|]', '_', s)
    else:
        s = s.replace('/', '_').replace('\\', '_').replace(':', '_')
    s = re.sub(r'\s+', '', s)  # 去掉空白
    s = s.rstrip('. ')         # Windows 不允许以点或空格结尾
    if not s:
        s = "untitled"
    # 防止路径过长
    return s[:240]

def read_rows_from_csv(csv_path: str):
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def main():
    csv_path = "results.csv"
    out_dir = "preview_output"
    os.makedirs(out_dir, exist_ok=True)

    rows = list(read_rows_from_csv(csv_path))
    if not rows:
        print("CSV 没有数据")
        return

    total = len(rows)
    print(f"共 {total} 行，开始生成 PNG 到：{out_dir}")

    for idx, row in enumerate(rows, start=1):
        try:
            H = int((row.get('board_h') or '0').strip())
            W = int((row.get('board_w') or '0').strip())
            pieces_str = (row.get('pieces') or '').strip()
        except Exception as e:
            print(f"[第{idx}/{total}行] 解析失败: {e}")
            continue

        pieces = parse_pieces(pieces_str)

        # 稳定种子，保证同一行每次生成一致布局
        seed = hash((H, W, pieces_str)) & 0xFFFFFFFF
        rng = random.Random(seed)

        placements = solve_board(H, W, pieces, rng=rng, max_attempts=MAX_ATTEMPTS)

        # 标题与文件名都使用整行签名（标题原样，文件名做安全化）
        row_sig = build_row_signature(row)
        title = row_sig
        filename = safe_filename(row_sig) + ".png"
        save_path = os.path.join(out_dir, filename)

        draw_and_save_board(H, W, placements, title, save_path)

        status = "OK" if placements else "无解"
        print(f"[{idx}/{total}] {status} -> {save_path}")

    print("全部 PNG 已生成。")

if __name__ == '__main__':
    main()