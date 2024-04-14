from PIL import Image
import tqdm

# 设置最大图像像素数量
Image.MAX_IMAGE_PIXELS = 301194001

# 原始TIF图片路径
original_image_path = 'E:\\2025\\1\\cat.tif'

# 打开TIF图片获取宽度和高度
img = Image.open(original_image_path)
width, height = img.size

# 获取原始图片的信息，以便在保存裁剪后的图片时保持相同品质
original_info = img.info.copy()

# 计算每一份图片的宽度
split_count = 25
piece_width = width // split_count

# 创建进度条
with tqdm.tqdm(total=split_count) as pbar:
    # 遍历所有部分进行裁剪
    for i in range(split_count):
        # 计算裁剪区域的左边界
        left = i * piece_width
        # 右边界是下一个部分的左边界，防止重叠
        right = (i + 1) * piece_width if i < split_count - 1 else width

        # 创建裁剪框
        box = (left, 0, right, height)

        # 裁剪图片
        cropped_img = img.crop(box)

        # 保存裁剪后的图片为TIF格式，同时传递原始图片的信息以保持相同的品质
        output_path = f'cropped_image_{i + 1}.tif'
        cropped_img.save(output_path, format='TIFF', **original_info)

        # 更新进度条
        pbar.update(1)
