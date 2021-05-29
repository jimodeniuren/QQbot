# -*- coding: utf-8 -*-
from typing import List, Tuple
from urllib.parse import urljoin
import requests
from lxml.html import fromstring
import aiohttp
from nonebot.adapters.cqhttp import MessageSegment


def parse_html(html: str):
    selector = fromstring(html)
    for tag in selector.xpath('//div[@class="container"]/div[@class="row"]/div/div[@class="row item-box"]')[1:5]:
        if pic_url := tag.xpath('./div/img[@loading="lazy"]/@src'):  # 缩略图url
            pic_url = urljoin("https://ascii2d.net/", pic_url[0])
        if description := tag.xpath('./div/div/h6/a[1]/text()'):  # 名字
            description = description[0]
        if author := tag.xpath('./div/div/h6/a[2]/text()'):  # 作者
            author = author[0]
        if origin_url := tag.xpath('./div/div/h6/a[1]/@href'):  # 原图地址
            origin_url = origin_url[0]
        if author_url := tag.xpath('./div/div/h6/a[2]/@href'):  # 作者地址
            author_url = author_url[0]
        yield pic_url, description, author, origin_url, author_url

    pass


async def get_pic_from_url(url: str):
    # real_url = "https://ascii2d.net/search/url/" + url
    url = 'https://ascii2d.net/search/url/{}'.format(url)
    headers = {
        'authority': 'ascii2d.net',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    }
    response = requests.get(url, headers=headers)
    real_url = (response.url, response.url.replace("color","bovw"))
    real_url = real_url[1]
    print(real_url)
    async with aiohttp.ClientSession() as session:
        async with session.get(real_url) as resp:
            html: str = await resp.text()
        return [i for i in parse_html(html)]


async def get_des(url: str):
    image_data: List[Tuple] = await get_pic_from_url(url)
    if not image_data:
        msg: str = "找不到高相似度的"
        yield msg
        return
    for pic in image_data:
        msg = MessageSegment.image(file=pic[0]) + "\n"
        for i in pic[1:]:
            msg = msg + f"{i}\n"
        yield msg
