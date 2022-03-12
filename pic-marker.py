########## 批量加水印照片 #########
import os
import sys
from PIL import Image, ImageFont, ImageDraw

# 读入水印图
mark_image = Image.open('./prlrr.png')
def del_file(path_data):
    for i in os.listdir(path_data) :# os.listdir(path_data)#返回一个列表，里面是当前目录下面的所有东西的相对路径
        file_data = path_data + "\\" + i#当前文件夹的下面的所有东西的绝对路径
        if os.path.isfile(file_data) == True:#os.path.isfile判断是否为文件,如果是文件,就删除.如果是文件夹.递归给del_file.
            os.remove(file_data)
        else:
            del_file(file_data)
def add_watermark(image_file):
    image = Image.open(image_file)
    im_size = image.size
    print('文件原始图片尺寸：', im_size)

    if im_size[0] > im_size[1]:  # 如果是横版
        mark_size = int(im_size[0] * 0.5)
    else:
        mark_size = int(im_size[1] * 0.5)

    mark_image.thumbnail((mark_size, mark_size))
    # print('水印图片尺寸：', mark_image.size)

    position = im_size[0] - int(mark_size * 1.2), im_size[1] - int(mark_size * 0.5)
    image.paste(mark_image, position, mark_image)

    name = os.path.basename(image_file)
    new_name = os.path.join('.\\blogpic', name)
    image.save(new_name, quality=99)

if __name__ == '__main__':

    # 循环读入照片
    try:
        del_file('.\\blogpic')
    except:
        print("blogpic 为空，继续执行。")
    files = os.listdir('.\\blogpic-first')
    for file in files:
        print("="*30)
        print('当前文件：',file,)
        file_format = file.split(".")[1]
        # print(file_format) #文件后缀
        if file_format != "gif":
            image_file = os.path.join('.\\blogpic-first', file)
            print('当前路径：',image_file,'\n',)
            add_watermark(image_file)
            print("添加成功！")
        else:
            print(file,"格式不符跳过添加")
            os.system("copy .\\blogpic-first\\" + file + " " + ".\\blogpic\\" + file)