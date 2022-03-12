########## 批量加水印文字 #########
import os
import sys
from PIL import Image, ImageFont, ImageDraw

def add_watermark(image_file):
    image = Image.open(image_file)
    draw_txt = ImageDraw.Draw(image)

    im_size = image.size
    print('原始图片尺寸：', im_size)
    if im_size[0] > im_size[1]:  # 如果是横版
        txt_size = int(im_size[0] * 0.05)
    else:
        txt_size = int(im_size[1] * 0.05)
    print('水印文字尺寸：', txt_size)

    # 设置字体和文字大小
    chi_font = ImageFont.truetype('./font/fzstk.ttf', size=txt_size)

    # 直接在照片上写文字
    draw_txt.text(xy=(im_size[0] // 2 - txt_size // 2, im_size[1] - int(txt_size * 1.2)),
                  text='@AdsRyen',
                  font=chi_font)

    name = os.path.basename(image_file)
    new_name = os.path.join('.\output', name)
    image.save(new_name, quality=99)

if __name__ == '__main__':

    ### 循环读入照片
    files = os.listdir('.\input')
    for file in files:
        image_file = os.path.join('.\input', file)
        print(image_file)
        add_watermark(image_file)
