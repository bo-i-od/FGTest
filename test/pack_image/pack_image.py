import os
import csv
from PIL import Image

from configs.pathConfig import DEV_EXCEL_PATH


def pack_images_from_csv(csv_path, root_dir, output_path, icon_size=64, columns=8):
    """
    根据 CSV 文件里列出的图片路径拼接成大图 (SpriteSheet)

    :param csv_path: CSV 文件路径
    :param root_dir: PNG 所在的资源根目录（CSV 里的路径是相对它）
    :param output_path: 输出大图路径 (PNG)
    :param icon_size: 每个小图缩放到的宽高 (像素)
    :param columns: 一行最多的图标数
    """
    image_files = []

    # 读取 CSV 文件
    with open(csv_path, newline='', encoding="utf-8") as f:
        reader = csv.reader(f, delimiter='\t')  # 注意你举例的是“序号<TAB>路径”，所以 delimiter 用 \t
        header = next(reader)  # 第一行表头
        for row in reader:
            if len(row) < 2:
                continue
            rel_path = row[1].strip()
            if not rel_path.lower().endswith(".png"):
                rel_path += ".png"   # 如果路径里没写扩展名，就补上
            full_path = os.path.join(root_dir, rel_path)
            image_files.append(full_path)

    if not image_files:
        print("⚠️ CSV 中没有有效路径")
        return

    print(f"从 CSV 中读取到 {len(image_files)} 张图，准备拼接...")

    rows = (len(image_files) + columns - 1) // columns
    atlas_width = columns * icon_size
    atlas_height = rows * icon_size

    atlas = Image.new("RGBA", (atlas_width, atlas_height), (0, 0, 0, 0))

    for idx, file in enumerate(image_files):
        if not os.path.exists(file):
            print(f"❌ 路径不存在: {file}")
            continue

        img = Image.open(file).convert("RGBA")
        img = img.resize((icon_size, icon_size), Image.LANCZOS)

        x = (idx % columns) * icon_size
        y = (idx // columns) * icon_size
        atlas.paste(img, (x, y), img)

    atlas.save(output_path, "PNG")
    print(f"✅ 已生成大图: {output_path} ({atlas_width}x{atlas_height})")


if __name__ == "__main__":
    # 示例配置
    csv_path = r"icons.csv"     # 记录路径的 CSV 文件
    root_dir = r"C:/ProjectMG/trunk/client/MainProject/Assets/InBundle"            # PNG 根目录（CSV 的路径是相对它的）
    output_path = r"./icons_in_text.png" # 输出大图
    icon_size = 128               # 每个图标缩放后的尺寸
    columns = 8                   # 每行最多放多少张
    pack_images_from_csv(csv_path, root_dir, output_path, icon_size, columns)

