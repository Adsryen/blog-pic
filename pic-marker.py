########## 批量加水印照片 #########
import os
import sys
from PIL import Image, ImageFont, ImageDraw

# 读入水印图
mark_image = Image.open('./web-icon2.png')


def add_watermark(image_file):
    image = Image.open(image_file)
    im_size = image.size
    print('原始图片尺寸：', im_size)

    if im_size[0] > im_size[1]:  # 如果是横版
        mark_size = int(im_size[0] * 0.5)
    else:
        mark_size = int(im_size[1] * 0.5)

    mark_image.thumbnail((mark_size, mark_size))
    print('水印图片尺寸：', mark_image.size)

    position = im_size[0] - int(mark_size * 1.2), im_size[1] - int(mark_size * 0.5)
    image.paste(mark_image, position, mark_image)

    name = os.path.basename(image_file)
    new_name = os.path.join('.\\blogpic', name)
    image.save(new_name, quality=99)


# 循环读入照片
files = os.listdir('.\\blogpic-first')
for file in files:
    image_file = os.path.join('.\\blogpic', file)
    print(image_file)
    add_watermark(image_file)
