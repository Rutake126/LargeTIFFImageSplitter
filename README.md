


# TIF图像分割器

## 项目简介
这是一个Python脚本，用于将大尺寸的TIF图像分割成多份小图像，同时保留原始图片的质量设置。特别适用于处理因尺寸过大而不便于存储或处理的情况。

## 依赖项
- [Pillow](https://pypi.org/project/Pillow/)：用于读取、操作和保存图像数据。

安装Pillow：
```shell
pip install Pillow
```

## 使用方法

1. 将待分割的原始TIF图像放置在指定的路径（在脚本中已定义为 `original_image_path`）。
2. 调整脚本中的 `split_count` 参数以适应所需的图像分割份数。
3. 脚本会自动创建并保存裁剪后的图像至指定的输出目录（在示例中为 `output_directory`）。

## 示例脚本配置与执行

```python
# 脚本片段（假设您已经将相关变量按照需求进行了配置）

from PIL import Image
import tqdm

# 设置最大图像像素数量限制
Image.MAX_IMAGE_PIXELS = 301194001

# 原始TIF图片路径
original_image_path = 'E:\\2025\\1\\cat.tif'

# 输出目录（请确保该目录存在或根据需要创建）
output_directory = "E:\\2025\\1\\cropped_images"

# ... 其余脚本内容 ...
```

## 运行脚本
1. 在命令行或者终端中进入包含此脚本的目录。
2. 运行脚本，例如（假设脚本名为 `image_splitter.py`）：
```shell
python image_splitter.py
```
执行后，脚本将会按照预设参数将原始TIF图像分割，并将裁剪后的图片保存在指定的输出目录中。

## 注意事项
- 确保输出目录存在且有写入权限。
- 根据实际需求调整裁剪参数。

