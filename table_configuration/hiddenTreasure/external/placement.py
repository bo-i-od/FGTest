from table_configuration.hiddenTreasure.external.base_part import BasePart
import math


class PartAssembler:
    """用于将多个BasePart拼接成大的Part"""

    def __init__(self, target_width, target_height):
        self.target_width = target_width
        self.target_height = target_height
        self.grid = [[0 for _ in range(target_width)] for _ in range(target_height)]
        self.layout_type = "未知布局"

    def assemble(self, part_specs):
        total_area = sum(spec['part'].area * spec['count'] for spec in part_specs)
        if total_area != self.target_width * self.target_height:
            raise Exception(f"总面积不匹配: 需要{self.target_width * self.target_height}, 实际{total_area}")

        # 面积从大到小排序
        sorted_specs = sorted(part_specs, key=lambda x: x['part'].area, reverse=True)

        # 检查1：2x2网格布局（4个相同块）
        if len(sorted_specs) == 1 and sorted_specs[0]['count'] == 4:
            if self._assemble_2x2_grid(sorted_specs[0]):
                self.layout_type = "2x2网格布局"
                return BasePart(part_content=self.grid)

        # 检查2：完整的四边框架布局 (4角, 4边, 1中心)
        if len(sorted_specs) == 3:
            counts = sorted([spec['count'] for spec in sorted_specs])
            if counts == [1, 4, 4]:
                if self._assemble_frame_layout_v2(sorted_specs):
                    self.layout_type = "完整四边框架布局"
                    return BasePart(part_content=self.grid)

        # 检查3：垂直堆叠布局（2个相同块）
        if len(sorted_specs) == 1 and sorted_specs[0]['count'] == 2:
            if self._assemble_vertical_stack(sorted_specs[0]):
                self.layout_type = "垂直堆叠布局"
                return BasePart(part_content=self.grid)

        # 检查4：中间缝隙布局
        if len(sorted_specs) == 2:
            counts = sorted([spec['count'] for spec in sorted_specs])
            # 支持 [2, 4] 或 [1, 2] 组合
            if counts == [2, 4] or counts == [1, 2]:
                if self._assemble_middle_gap_layout_v2(sorted_specs):
                    self.layout_type = "中间缝隙布局"
                    return BasePart(part_content=self.grid)

        # 检查5：矩形框架布局
        if len(sorted_specs) == 4:
            counts = sorted([spec['count'] for spec in sorted_specs])
            if counts == [1, 2, 2, 4]:
                if self._assemble_rect_frame_layout(sorted_specs):
                    self.layout_type = "矩形框架布局"
                    return BasePart(part_content=self.grid)

        # 通用贪心填充
        all_individual_parts = []
        for spec in sorted_specs:
            all_individual_parts.extend(spec.get('parts', [spec['part']] * spec['count']))

        for part in all_individual_parts:
            placed = self._place_part_greedy(part)
            if not placed:
                raise Exception(f"无法放置 {part.width}x{part.height} 的部件")

        self.layout_type = "通用贪心填充"
        return BasePart(part_content=self.grid)

    def _assemble_2x2_grid(self, spec):
        """2x2网格布局：4个相同的块排列成2行2列"""
        parts = spec.get('parts', [spec['part']] * 4)
        if len(parts) != 4:
            return False

        base_part = parts[0]

        # 尝试原始方向
        if self._try_2x2_grid(parts, base_part.width, base_part.height):
            return True

        # 尝试转置方向
        if base_part.width != base_part.height:
            if self._try_2x2_grid_transposed(parts, base_part.height, base_part.width):
                return True

        return False

    def _try_2x2_grid(self, parts, w, h):
        if self.target_width != 2 * w or self.target_height != 2 * h:
            return False
        try:
            self._place(parts[0], 0, 0)
            self._place(parts[1], 0, w)
            self._place(parts[2], h, w)
            self._place(parts[3], h, 0)
            return True
        except:
            self.grid = [[0 for _ in range(self.target_width)] for _ in range(self.target_height)]
            return False

    def _try_2x2_grid_transposed(self, parts, w, h):
        if self.target_width != 2 * w or self.target_height != 2 * h:
            return False
        try:
            self._place(parts[0].get_transpose(), 0, 0)
            self._place(parts[1].get_transpose(), 0, w)
            self._place(parts[2].get_transpose(), h, w)
            self._place(parts[3].get_transpose(), h, 0)
            return True
        except:
            self.grid = [[0 for _ in range(self.target_width)] for _ in range(self.target_height)]
            return False

    def _assemble_middle_gap_layout_v2(self, sorted_specs):
        """
        改进的中间缝隙布局
        """
        if len(sorted_specs) != 2:
            return False

        # 识别哪个是主块，哪个是边块
        if sorted_specs[0]['count'] > sorted_specs[1]['count']:
            main_spec, edge_spec = sorted_specs[0], sorted_specs[1]
        else:
            edge_spec, main_spec = sorted_specs[0], sorted_specs[1]

        main_parts = main_spec.get('parts', [main_spec['part']] * main_spec['count'])
        edge_parts = edge_spec.get('parts', [edge_spec['part']] * edge_spec['count'])

        # 尝试不同的布局模式
        if main_spec['count'] == 4 and edge_spec['count'] == 2:
            return self._try_4plus2_layout(main_parts, edge_parts)
        elif main_spec['count'] == 2 and edge_spec['count'] == 1:
            return self._try_2plus1_layout(main_parts, edge_parts)

        return False

    def _assemble_vertical_stack(self, spec):
        """垂直堆叠：2个相同块上下排列"""
        parts = spec.get('parts', [spec['part']] * 2)
        if len(parts) != 2:
            return False

        p1, p2 = parts[0], parts[1]

        # 尝试原始方向
        if self.target_width == p1.width and self.target_height == 2 * p1.height:
            try:
                self._place(p1, 0, 0)
                self._place(p2, p1.height, 0)
                return True
            except:
                self.grid = [[0 for _ in range(self.target_width)] for _ in range(self.target_height)]

        # 尝试转置方向
        if p1.width != p1.height:
            p1_t = p1.get_transpose()
            p2_t = p2.get_transpose()
            if self.target_width == p1_t.width and self.target_height == 2 * p1_t.height:
                try:
                    self._place(p1_t, 0, 0)
                    self._place(p2_t, p1_t.height, 0)
                    return True
                except:
                    self.grid = [[0 for _ in range(self.target_width)] for _ in range(self.target_height)]

        return False

    def _try_4plus2_layout(self, main_parts, edge_parts):
        """4个主块 + 2个边块的布局"""
        m = main_parts[0]
        e = edge_parts[0]

        # 获取主块和边块的两种方向尺寸
        m_sizes = [(m.width, m.height), (m.height, m.width)]
        e_sizes = [(e.width, e.height), (e.height, e.width)]

        # 尝试所有组合
        for idx_m, (mw, mh) in enumerate(m_sizes):
            transpose_main = (idx_m == 1)

            for idx_e, (ew, eh) in enumerate(e_sizes):
                # 尝试水平缝隙：2x2主块上下，中间边块
                if self.target_width == 2 * mw and self.target_height == 2 * mh + eh:
                    if ew == mw:
                        if self._place_horizontal_gap(main_parts, edge_parts, mw, mh, ew, eh, transpose_main,
                                                      idx_e == 1):
                            return True

                # 尝试垂直缝隙：2x2主块左右，中间边块
                if self.target_width == 2 * mw + ew and self.target_height == 2 * mh:
                    if eh == mh:
                        if self._place_vertical_gap(main_parts, edge_parts, mw, mh, ew, eh, transpose_main, idx_e == 1):
                            return True

        return False

    def _place_horizontal_gap(self, main_parts, edge_parts, mw, mh, ew, eh, transpose_main, transpose_edge):
        """放置水平缝隙布局"""
        try:
            # 放置主块
            # 假设输入的 main_parts 顺序为 [TL, TR, BR, BL] (基于 5x7 的逻辑推断)
            parts_to_place = [p.get_transpose() if transpose_main else p for p in main_parts]

            # 如果 parts 数量不足4个，补齐以防越界
            while len(parts_to_place) < 4:
                parts_to_place.append(parts_to_place[0])

            self._place(parts_to_place[0], 0, 0)  # TL
            self._place(parts_to_place[1], 0, mw)  # TR
            self._place(parts_to_place[3], mh + eh, 0)  # BL (注意索引修正：3)
            self._place(parts_to_place[2], mh + eh, mw)  # BR (注意索引修正：2)

            # 放置边块
            if len(edge_parts) >= 2:
                e0 = edge_parts[0].get_transpose() if transpose_edge else edge_parts[0]
                e1 = edge_parts[1].get_transpose() if transpose_edge else edge_parts[1]
                self._place(e0, mh, 0)
                self._place(e1, mh, mw)
            else:
                edge_for_placement = edge_parts[0].get_transpose() if transpose_edge else edge_parts[0]
                self._place(edge_for_placement, mh, 0)
                self._place(edge_for_placement.get_flip(flip_x=True), mh, mw)

            return True
        except:
            self.grid = [[0 for _ in range(self.target_width)] for _ in range(self.target_height)]
            return False

    def _place_vertical_gap(self, main_parts, edge_parts, mw, mh, ew, eh, transpose_main, transpose_edge):
        """放置垂直缝隙布局"""
        try:
            # 放置主块
            # 假设输入的 main_parts 顺序为 [TL, TR, BR, BL]
            parts_to_place = [p.get_transpose() if transpose_main else p for p in main_parts]

            while len(parts_to_place) < 4:
                parts_to_place.append(parts_to_place[0])

            self._place(parts_to_place[0], 0, 0)  # TL
            self._place(parts_to_place[3], mh, 0)  # BL (注意索引修正：3)
            self._place(parts_to_place[1], 0, mw + ew)  # TR (注意索引修正：1)
            self._place(parts_to_place[2], mh, mw + ew)  # BR (注意索引修正：2)

            # 放置边块
            if len(edge_parts) >= 2:
                e0 = edge_parts[0].get_transpose() if transpose_edge else edge_parts[0]
                e1 = edge_parts[1].get_transpose() if transpose_edge else edge_parts[1]
                self._place(e0, 0, mw)
                self._place(e1, mh, mw)
            else:
                edge_for_placement = edge_parts[0].get_transpose() if transpose_edge else edge_parts[0]
                self._place(edge_for_placement, 0, mw)
                self._place(edge_for_placement.get_flip(flip_y=True), mh, mw)

            return True
        except:
            self.grid = [[0 for _ in range(self.target_width)] for _ in range(self.target_height)]
            return False

    def _try_2plus1_layout(self, main_parts, edge_parts):
        """2个主块 + 1个边块的纵向堆叠"""
        m = main_parts[0]
        e = edge_parts[0]

        # 纵向堆叠：main + edge + main
        if self.target_width == m.width and self.target_height == 2 * m.height + e.height:
            if e.width == m.width:
                try:
                    self._place(main_parts[0], 0, 0)
                    edge_for_middle = edge_parts[0] if edge_parts[0].width >= edge_parts[0].height else edge_parts[
                        0].get_transpose()
                    self._place(edge_for_middle, m.height, 0)
                    # 尝试使用列表中的第二个主块，如果不存在则复用第一个并翻转
                    if len(main_parts) > 1:
                        self._place(main_parts[1], m.height + e.height, 0)
                    else:
                        self._place(main_parts[0].get_flip(flip_y=True), m.height + e.height, 0)
                    return True
                except:
                    self.grid = [[0 for _ in range(self.target_width)] for _ in range(self.target_height)]

        return False

    def _assemble_rect_frame_layout(self, sorted_specs):
        """矩形框架布局"""
        try:
            corner_spec = next(spec for spec in sorted_specs if spec['count'] == 4)
            center_spec = next(spec for spec in sorted_specs if spec['count'] == 1)
            edge_specs = [spec for spec in sorted_specs if spec['count'] == 2]
        except StopIteration:
            return False
        if len(edge_specs) != 2:
            return False

        corner_base = corner_spec['part']
        c_w, c_h = corner_base.width, corner_base.height
        c_long = max(c_w, c_h)
        c_short = min(c_w, c_h)

        options = [
            (2 * c_short + 1, 2 * c_long + 1),
            (2 * c_long + 1, 2 * c_short + 1),
        ]
        if (self.target_width, self.target_height) == options[0]:
            corner_width_expected = c_short
            corner_height_expected = c_long
        elif (self.target_width, self.target_height) == options[1]:
            corner_width_expected = c_long
            corner_height_expected = c_short
        else:
            return False

        def norm_edge(spec):
            w, h = spec['part'].width, spec['part'].height
            L = max(w, h)
            T = min(w, h)
            return L, T, spec

        e1L, e1T, es1 = norm_edge(edge_specs[0])
        e2L, e2T, es2 = norm_edge(edge_specs[1])
        if e1T != 1 or e2T != 1:
            return False

        vertical_spec = None
        horizontal_spec = None
        for L, T, spec in [(e1L, e1T, es1), (e2L, e2T, es2)]:
            if L == corner_height_expected:
                vertical_spec = spec
            elif L == corner_width_expected:
                horizontal_spec = spec
        if vertical_spec is None or horizontal_spec is None:
            return False

        def orient_corner(p: BasePart):
            w, h = p.width, p.height
            if (w, h) == (corner_width_expected, corner_height_expected):
                return p
            if (w, h) == (corner_height_expected, corner_width_expected):
                return p.get_transpose()
            return None

        def to_vertical(p: BasePart, length: int):
            q = p if p.height >= p.width else p.get_transpose()
            if q.width != 1 or q.height != length:
                return None
            return q

        def to_horizontal(p: BasePart, length: int):
            q = p if p.width >= p.height else p.get_transpose()
            if q.height != 1 or q.width != length:
                return None
            return q

        corners = corner_spec.get('parts', [])
        if len(corners) != 4:
            return False

        corner_TL = orient_corner(corners[0])
        corner_TR = orient_corner(corners[1])
        corner_BR = orient_corner(corners[2])
        corner_BL = orient_corner(corners[3])
        if None in (corner_TL, corner_TR, corner_BR, corner_BL):
            return False

        v_parts = vertical_spec.get('parts', [vertical_spec['part']] * vertical_spec['count'])
        h_parts = horizontal_spec.get('parts', [horizontal_spec['part']] * horizontal_spec['count'])

        v_top = to_vertical(v_parts[0], corner_height_expected)
        if v_top is None:
            return False
        if len(v_parts) >= 2:
            v_bottom = to_vertical(v_parts[1], corner_height_expected)
            if v_bottom is None:
                return False
        else:
            v_bottom = v_top.get_flip(flip_y=True)

        h_left = to_horizontal(h_parts[0], corner_width_expected)
        if h_left is None:
            return False
        if len(h_parts) >= 2:
            h_right = to_horizontal(h_parts[1], corner_width_expected)
            if h_right is None:
                return False
        else:
            h_right = h_left.get_flip(flip_x=True)

        center_part = center_spec['parts'][0]
        if center_part.width != 1 or center_part.height != 1:
            return False

        off_w = corner_width_expected
        off_h = corner_height_expected

        try:
            self._place(corner_TL, 0, 0)
            self._place(corner_TR, 0, off_w + 1)
            self._place(corner_BR, off_h + 1, off_w + 1)
            self._place(corner_BL, off_h + 1, 0)
            self._place(v_top, 0, off_w)
            self._place(v_bottom, off_h + 1, off_w)
            self._place(h_left, off_h, 0)
            self._place(h_right, off_h, off_w + 1)
            self._place(center_part, off_h, off_w)
            return True
        except Exception:
            self.grid = [[0 for _ in range(self.target_width)] for _ in range(self.target_height)]
            return False

    def _assemble_frame_layout_v2(self, sorted_specs):
        """
        框架布局V2：边缘部件填充顺序修改为顺时针（左->上->右->下）
        """
        specs_by_count = sorted(sorted_specs, key=lambda x: x['count'])
        center_spec, edge_spec, corner_spec = specs_by_count[0], specs_by_count[1], specs_by_count[2]

        # 如果排序后发现面积大小关系不符合预期（例如边框比角大），交换变量
        if edge_spec['part'].area > corner_spec['part'].area:
            edge_spec, corner_spec = corner_spec, edge_spec

        corner_parts = corner_spec['parts']
        center_part = center_spec['parts'][0]
        edge_parts = edge_spec['parts']  # 获取实际的边缘部件列表

        if len(corner_parts) != 4 or len(edge_parts) != 4:
            return False

        size = self.target_width
        corner_size = corner_parts[0].width

        # 计算中间缝隙的大小（即边缘部件的“短边”或者是中心块的边长）
        gap_size = size - 2 * corner_size

        # 尺寸校验
        if gap_size <= 0:
            return False
        if center_part.width != gap_size or center_part.height != gap_size:
            return False

        # 辅助函数：根据目标宽高调整部件方向
        def get_oriented(part, target_w, target_h):
            # 如果尺寸完全匹配，直接返回
            if part.width == target_w and part.height == target_h:
                return part
            # 如果尺寸颠倒，进行转置
            if part.width == target_h and part.height == target_w:
                return part.get_transpose()
            # 尺寸不匹配，返回原样（后续贪心放置可能会失败，或者由调用者处理）
            return part

        try:
            # 1. 放置四个角 (TL, TR, BR, BL) - 保持不变
            self._place(corner_parts[0], 0, 0)  # Top-Left
            self._place(corner_parts[1], 0, size - corner_size)  # Top-Right
            self._place(corner_parts[2], size - corner_size, size - corner_size)  # Bottom-Right
            self._place(corner_parts[3], size - corner_size, 0)  # Bottom-Left

            # 2. 放置四个边，顺序修改为：左 -> 上 -> 右 -> 下

            # Left Edge (index 0): 位于最左列中间，垂直填充
            # 目标尺寸: Width=corner_size, Height=gap_size
            # 坐标: row=corner_size, col=0
            p_left = get_oriented(edge_parts[0], corner_size, gap_size)
            self._place(p_left, corner_size, 0)

            # Top Edge (index 1): 位于第一行中间，水平填充
            # 目标尺寸: Width=gap_size, Height=corner_size
            # 坐标: row=0, col=corner_size
            p_top = get_oriented(edge_parts[1], gap_size, corner_size)
            self._place(p_top, 0, corner_size)

            # Right Edge (index 2): 位于最右列中间，垂直填充
            # 目标尺寸: Width=corner_size, Height=gap_size
            # 坐标: row=corner_size, col=corner_size + gap_size
            p_right = get_oriented(edge_parts[2], corner_size, gap_size)
            self._place(p_right, corner_size, corner_size + gap_size)

            # Bottom Edge (index 3): 位于最后一行中间，水平填充
            # 目标尺寸: Width=gap_size, Height=corner_size
            # 坐标: row=corner_size + gap_size, col=corner_size
            p_bottom = get_oriented(edge_parts[3], gap_size, corner_size)
            self._place(p_bottom, corner_size + gap_size, corner_size)

            # 3. 放置中心 - 保持不变
            self._place(center_part, corner_size, corner_size)
            return True
        except Exception:
            # 如果放置过程中发生重叠或越界，回滚
            self.grid = [[0 for _ in range(self.target_width)] for _ in range(self.target_height)]
            return False

    def _place_part_greedy(self, part):
        for r in range(self.target_height):
            for c in range(self.target_width):
                if self._can_place(part, r, c):
                    self._place(part, r, c)
                    return True
        return False

    def _can_place(self, part, start_row, start_col):
        if start_row < 0 or start_col < 0 or start_row + part.height > self.target_height or start_col + part.width > self.target_width:
            return False
        for i in range(part.height):
            for j in range(part.width):
                if self.grid[start_row + i][start_col + j] != 0 and part.part_content[i][j] != 0:
                    return False
        return True

    def _place(self, part, start_row, start_col):
        for i in range(part.height):
            for j in range(part.width):
                if part.part_content[i][j] != 0:
                    self.grid[start_row + i][start_col + j] = part.part_content[i][j]


def create_part_from_base_parts(*base_parts):
    if not base_parts:
        raise Exception("至少需要一个BasePart")

    total_area = sum(part.area for part in base_parts)
    side_length = int(math.sqrt(total_area))

    if side_length * side_length == total_area:
        target_width = target_height = side_length
    else:
        target_width, target_height = _find_best_dimensions(total_area)

    # 将相同"尺寸+块数"的部件归为一组，并保持输入顺序
    part_groups = {}
    for part in base_parts:
        key = _part_to_key(part)
        if key not in part_groups:
            part_groups[key] = []
        part_groups[key].append(part)

    part_specs = []
    for key, parts_list in part_groups.items():
        part_specs.append({
            'part': parts_list[0],
            'count': len(parts_list),
            'parts': parts_list
        })

    assembler = PartAssembler(target_width, target_height)
    result = assembler.assemble(part_specs)

    # 将布局类型信息附加到结果中
    result.layout_type = assembler.layout_type
    return result


def _part_to_key(part):
    # 尺寸归一化 + 方块数，保证同类部件分到一组，同时保留各自具体 pattern
    dims = tuple(sorted((part.width, part.height)))
    return (dims[0], dims[1], part.block_count)


def _find_best_dimensions(area):
    best_ratio = float('inf')
    best_dims = (area, 1)
    for width in range(1, int(math.sqrt(area)) + 1):
        if area % width == 0:
            height = area // width
            ratio = max(width, height) / min(width, height)
            if ratio < best_ratio:
                best_ratio = ratio
                best_dims = (min(width, height), max(width, height))
    return best_dims



