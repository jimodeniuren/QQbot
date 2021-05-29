import base64
import re
import random
import json
import os
import datetime
import requests
from io import BytesIO
from random import choice
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from nonebot.adapters.cqhttp import Event, Bot
from nonebot.adapters.cqhttp import MessageSegment, Message
from nonebot import on_command


def pic2b64(im):
    # im是Image对象，把Image图片转成base64
    bio = BytesIO()
    im.save(bio, format='PNG')
    base64_str = base64.b64encode(bio.getvalue()).decode()
    return 'base64://' + base64_str


def ba64_to_cq(base64_str):
    return f"[CQ:image,file={base64_str}]"


def load_config(path):
    try:
        with open(path, 'r', encoding='utf8') as f:
            config = json.load(f)
            return config
    except:
        return {}


def measure(msg, font_size, img_width):
    i = 0
    l = len(msg)
    length = 0
    positions = []
    while i < l:
        if re.search(r'[0-9a-zA-Z]', msg[i]):
            length += font_size // 2
        else:
            length += font_size
        if length >= img_width:
            positions.append(i)
            length = 0
            i -= 1
        i += 1
    return positions


def get_pic(qq):
    apiPath = f'http://q1.qlogo.cn/g?b=qq&nk={qq}&s=100'
    return requests.get(apiPath, timeout=20).content


def get_name(qq):
    url = 'http://r.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg'
    params = {'uins': qq}
    res = requests.get(url, params=params)
    res.encoding = 'GBK'
    data_match = re.search(r'\((?P<data>[^\(\)]*)\)', res.text)
    if data_match:
        j_str = data_match.group('data')
        return json.loads(j_str)[qq][-2]
    else:
        return '富婆'

yingxiaohao = on_command('yingxiaohao', aliases={'营销号'})


@yingxiaohao.handle()
async def _(bot: Bot, event: Event):
    kw = str(event.get_message()).strip()
    arr = kw.split('/')
    msg = f'    {arr[0]}{arr[1]}是怎么回事呢？{arr[0]}相信大家都很熟悉，但是{arr[0]}{arr[1]}是怎么回事呢，下面就让小编带大家一起了解吧。\n    {arr[0]}{arr[1]}，其实就是{arr[2]}，大家可能会很惊讶{arr[0]}怎么会{arr[1]}呢？但事实就是这样，小编也感到非常惊讶。\n    这就是关于{arr[0]}{arr[1]}的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'
    await bot.send(event, msg)


goupibutong = on_command('goupibutong', aliases={'狗屁不通'})


@goupibutong.handle()
async def _(bot: Bot, event: Event):
    data = load_config(os.path.join(os.path.dirname(__file__), 'data.json'))
    title = str(event.get_message()).strip()
    length = 500
    body = ""
    while len(body) < length:
        num = random.randint(0, 100)
        if num < 10:
            body += "\r\n"
        elif num < 20:
            body += random.choice(data["famous"]) \
                .replace('a', random.choice(data["before"])) \
                .replace('b', random.choice(data['after']))
        else:
            body += random.choice(data["bosh"])
        body = body.replace("x", title)
    await bot.send(event, body)


jichou = on_command('jichou', aliases={'记仇'})


@jichou.handle()
async def _(bot: Bot, event: Event):
    kw = str(event.get_message()).strip()
    arr = kw.split('/')
    image = Image.open(os.path.join(os.path.dirname(__file__), 'jichou.jpg'))
    # 创建Font对象:
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'simhei.ttf'), 80)

    time = datetime.datetime.now().strftime('%Y年%m月%d日')
    msg = f'{time}，{arr[0]}，{arr[1]}，这个仇我先记下了'
    place = 12
    line = len(msg.encode('utf-8')) // place + 1

    positions = measure(msg, 80, 974)
    str_list = list(msg)
    for pos in positions:
        str_list.insert(pos, '\n')
    msg = "".join(str_list)
    # 创建Draw对象:
    image_text = Image.new('RGB', (974, 32 * line), (255, 255, 255))
    draw = ImageDraw.Draw(image_text)
    draw.text((0, 0), msg, fill=(0, 0, 0), font=font)
    # 模糊:
    image_text = image_text.filter(ImageFilter.BLUR)
    image_back = Image.new('RGB', (974, 32 * line + 764), (255, 255, 255))
    image_back.paste(image, (0, 0))
    image_back.paste(image_text, (0, 764))

    await bot.send(event, Message(ba64_to_cq(pic2b64(image_back))))


wuzhongshengyou = on_command('wuzhongshengyou', aliases={'无中生友',"无中生有"})


@wuzhongshengyou.handle()
async def _(bot: Bot, event: Event):
    kw = str(event.get_message()).strip()
    arr = kw.split('/')
    msg = arr[0]
    msg = msg.replace('他', '我').replace('她', '我')
    image = Image.open(BytesIO(get_pic(arr[1])))
    img_origin = Image.new('RGBA', (100, 100), (255, 255, 255))
    scale = 3
    # 使用新的半径构建alpha层
    r = 100 * scale
    alpha_layer = Image.new('L', (r, r), 0)
    draw = ImageDraw.Draw(alpha_layer)
    draw.ellipse((0, 0, r, r), fill=255)
    # 使用ANTIALIAS采样器缩小图像
    alpha_layer = alpha_layer.resize((100, 100), Image.ANTIALIAS)
    img_origin.paste(image, (0, 0), alpha_layer)

    # 创建Font对象:
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'simhei.ttf'), 30)
    font2 = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'simhei.ttf'), 25)

    # 创建Draw对象:
    image_text = Image.new('RGB', (450, 150), (255, 255, 255))
    draw = ImageDraw.Draw(image_text)
    draw.text((0, 0), get_name(arr[1]), fill=(0, 0, 0), font=font)
    draw.text((0, 40), msg, fill=(125, 125, 125), font=font2)

    image_back = Image.new('RGB', (700, 150), (255, 255, 255))
    image_back.paste(img_origin, (25, 25))
    image_back.paste(image_text, (150, 40))

    await bot.send(event, Message(ba64_to_cq(pic2b64(image_back))))


pre = 0


tiangouriji = on_command('tiangouriji', aliases={'舔狗日记'})


@tiangouriji.handle()
async def _(bot: Bot, event: Event):
    global pre
    name = '富婆'
    kw = str(event.get_message()).strip()
    if kw != "":
        name = kw
    time = datetime.datetime.now().strftime('%Y年%m月%d日')
    arr = kw.split('/')
    content = ''
    if len(arr) >= 2:
        weather, content = arr
        weather = weather.split(' ')[-1]
    else:
        weather = ''
        if arr[0].split(' ') == 2:
            weather = arr[0].split(' ')[-1]

    if not content:
        with open(os.path.join(os.path.dirname(__file__), 'diary_data.json'), 'r', encoding='utf-8') as file:
            diaries = json.load(file)
            while True:
                index = random.randint(0, len(diaries) - 1)
                if index != pre:
                    pre = index
                    content = diaries[index]
                    for s in '你她':
                        content = content.replace(s, name)
                    break

    image = Image.open(os.path.join(os.path.dirname(__file__), 'diary.png'))
    img_width, img_height = image.size
    # 创建Font对象:
    font_size = img_width // 18
    font = ImageFont.truetype(os.path.join(os.path.dirname(__file__), 'simhei.ttf'), font_size)
    positions = measure(content, font_size, img_width)
    str_list = list(content)
    for pos in positions:
        str_list.insert(pos, '\n')
    # 日期单独一行
    line = len(positions) + 2
    content = f'{time}，{weather}\n' + "".join(str_list)
    line_h = font_size + 4
    # 创建Draw对象:
    image_text = Image.new('RGB', (img_width, line_h * line), (255, 255, 255))
    draw = ImageDraw.Draw(image_text)
    draw.text((0, 0), content, fill=(0, 0, 0), font=font, spacing=2)
    # 模糊:
    # image_text = image_text.filter(ImageFilter.BLUR)
    image_back = Image.new('RGB', (img_width, line_h * line + img_height), (255, 255, 255))
    image_back.paste(image, (0, 0))
    image_back.paste(image_text, (0, img_height))

    await bot.send(event, Message(ba64_to_cq(pic2b64(image_back))))
