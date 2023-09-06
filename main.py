import os
import random

from PIL import Image, ImageDraw, ImageFont


def generate_captcha():
    # 创建目录
    if not os.path.exists('captcha'):
        os.mkdir('captcha')
    # 获取目录下文件数量
    count = len(os.listdir('captcha'))
    # 生成100个验证码
    for i in range(10):
        # 生成随机字符串
        captcha = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 4))
        # 创建画布
        img = Image.new('RGB', (120, 30), (255, 255, 255))
        # 创建画笔
        draw = ImageDraw.Draw(img)
        # 设置字体
        font = ImageFont.truetype('arial.ttf', 25)
        # 绘制字符
        for i in range(4):
            draw.text((30 * i + 10, 0), captcha[i], font=font, fill=(0, 0, 0))
        # 添加干扰线
        for i in range(5):
            x1 = random.randint(0, 120)
            y1 = random.randint(0, 30)
            x2 = random.randint(0, 120)
            y2 = random.randint(0, 30)
            draw.line((x1, y1, x2, y2), fill=(0, 0, 0))
        # 添加干扰点
        for i in range(50):
            x = random.randint(0, 120)
            y = random.randint(0, 30)
            draw.point((x, y), fill=(0, 0, 0))
        # 将验证码保存到文件中
        with open(f'captcha/{count + i + 1}.txt', 'w') as f:
            f.write(captcha)
        img.save(f'captcha/{count + i + 1}.png')

if __name__ == '__main__':
    generate_captcha()
