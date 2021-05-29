# -*- coding: utf-8 -*-
import traceback
from typing import Dict

from aiohttp.client_exceptions import ClientError
from nonebot.plugin import on_command, on_message
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, MessageEvent, GroupMessageEvent, Message
from nonebot.typing import T_State

from .ex import get_des as get_des_ex
from .iqdb import get_des as get_des_iqdb
from .saucenao import get_des as get_des_sau
from .ascii2d import get_des as get_des_asc
from .trace import get_des as get_des_trace
from .yandex import get_des as get_des_yandex

global superMode,isFirst

async def get_des(url: str, mode: str):
    """
    :param url: 图片链接
    :param mode: 图源
    :return:
    """
    if mode == "iqdb":
        async for msg in get_des_iqdb(url):
            yield msg
    elif mode == "ex":
        async for msg in get_des_ex(url):
            yield msg
    elif mode == "trace":
        async for msg in get_des_trace(url):
            yield msg
    elif mode == "yandex":
        async for msg in get_des_yandex(url):
            yield msg
    elif mode.startswith("asc"):
        async for msg in get_des_asc(url):
            yield msg
    else:
        async for msg in get_des_sau(url):
            yield msg


setu = on_command("搜图", aliases={"search"})


@setu.handle()
async def handle_first_receive(bot: Bot, event: MessageEvent, state: T_State):
    msg = event.message
    global superMode,isFirst
    isFirst = True
    superMode = str(msg).strip("搜图")
    if msg:
        state["setu"] = msg
    pass


# @setu.got("mod", prompt="从哪里查找呢? ex/nao/trace/iqdb/ascii2d")
# async def get_func(bot: Bot, event: MessageEvent, state: dict):
#     pass


@setu.got("setu", prompt="图呢？")
async def get_setu(bot: Bot, event: MessageEvent, state: T_State):
    """
    发现没有的时候要发问
    :return:
    """
    msg: Message = Message(state["setu"])
    global superMode,isFirst
    mod: str = superMode  # 模式
    try:
        if msg[0].type == "image":
            await bot.send(event=event, message="正在处理图片，要是卡在这就是结果被风控了发不出来，可以试试私聊")
            url = msg[0].data["url"]  # 图片链接
            async for msg in get_des(url, mod):
                await bot.send(event=event, message=msg)
            await setu.finish("hso")
            # image_data: List[Tuple] = await get_pic_from_url(url)
        elif isFirst:
            isFirst = False
            await setu.reject("图呢？")
        else:
            await setu.finish("这不是图，本次搜索结束")
    except (IndexError, ClientError):
        await bot.send(event, traceback.format_exc())
        await setu.finish("参数错误")


# pic_map: Dict[str, str] = {}  # 保存这个群的其阿金一张色图 {"123456":http://xxx"}


# async def check_pic(bot: Bot, event: MessageEvent, state: T_State) -> bool:
#     if isinstance(event, MessageEvent):
#         for msg in event.message:
#             if msg.type == "image":
#                 url: str = msg.data["url"]
#                 state["url"] = url
#                 return True
#         return False


# notice_pic = on_message(check_pic)


# @notice_pic.handle()
# async def handle_pic(bot: Bot, event: GroupMessageEvent, state: T_State):
#     try:
#         group_id: str = str(event.group_id)
#         pic_map.update({group_id: state["url"]})
#     except AttributeError:
#         pass


# previous = on_command("上一张图是什么", aliases={"上一张", "这是什么"})


# @previous.handle()
# async def handle_previous(bot: Bot, event: GroupMessageEvent, state: T_State):
#     await bot.send(event=event, message="processing...")
#     try:
#         url: str = pic_map[str(event.group_id)]
#         async for msg in get_des(url, "nao"):
#             await bot.send(event=event, message=msg)
#     except (IndexError, ClientError):
#         await bot.send(event, traceback.format_exc())
#         await previous.finish("参数错误")
#     except KeyError:
#         await previous.finish("没有图啊QAQ")
