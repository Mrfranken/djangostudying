from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(254, 255), random.randint(254, 255), random.randint(254, 255))

# 随机颜色2:
def rndColor2():
    # return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
    return (0, 0, 0)

def create_image(i):
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    # 创建Font对象:
    font = ImageFont.truetype(r'C:\Windows\Fonts\SIMYOU.TTF', 40)
    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), (255, 106, 106))
    # 输出文字:
    for t in range(4):
        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
    # 模糊:
    image = image.filter(ImageFilter.SMOOTH)
    # ImageFilter.
    image.save(r'D:\code{}.jpg'.format(i), 'jpeg')

for i in range(2):
    create_image(i) #创造四张图片并保存


