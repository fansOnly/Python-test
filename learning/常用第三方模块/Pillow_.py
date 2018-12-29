# !/usr/bin/env python3
# -*- codeing: utf-8 -*-


# Pillow
# pip install pillow

# 操作图像
from PIL import Image

im = Image.open('F:/python/Python-test/learning/常用第三方模块/images/0.jpg')
w, h = im.size
print('宽度: %s, 高度: %s' % (w,h))
im.thumbnail((w//2, h//2))
im.save('F:/python/Python-test/learning/常用第三方模块/images/1.jpg', 'jpeg')
print('*'*100)


# 模糊效果
from PIL import Image, ImageFilter

im = Image.open('F:/python/Python-test/learning/常用第三方模块/images/0.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('F:/python/Python-test/learning/常用第三方模块/images/2.jpg', 'jpeg')


# 生成字母验证码图片
from PIL import Image, ImageFont, ImageFilter, ImageDraw
import random

def ranChar():
    return chr(random.randint(65, 90))

def ranColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def ranColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 240
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=ranColor())
# 输出文字:
for i in range(4):
    draw.text((60*i+10, 10), ranChar(), font=font, fill=ranColor2())
# 模糊图片
image = image.filter(ImageFilter.BLUR)
image.save('F:/python/Python-test/learning/常用第三方模块/images/code.jpg', 'jpeg')
# image.show()