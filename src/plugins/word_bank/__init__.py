import random

from nonebot import on_command, on_message, on_regex, export
from nonebot.permission import SUPERUSER
from nonebot.typing import T_State
from nonebot.adapters.cqhttp.bot import Bot
from nonebot.adapters.cqhttp.message import Message
from nonebot.adapters.cqhttp.event import MessageEvent, GroupMessageEvent
from nonebot.adapters.cqhttp.utils import unescape
from nonebot.adapters.cqhttp.permission import GROUP_OWNER, GROUP_ADMIN, PRIVATE_FRIEND,GROUP_MEMBER

from .data_source import OPTIONS, word_bank as wb
from .util import parse, parse_cmd

reply_type = "random"

export().word_bank = wb

wb_matcher = on_message()


@wb_matcher.handle()
async def _(bot: Bot, event: MessageEvent):
    if isinstance(event, GroupMessageEvent):
        index = event.group_id
    else:
        index = event.user_id

    msgs = wb.match(index, unescape(event.raw_message))
    if msgs:
        if reply_type == 'random':
            msg = Message(unescape(parse(msg=random.choice(msgs),
                                         nickname=event.sender.card or event.sender.nickname,
                                         sender_id=event.sender.user_id)))
            await bot.send(event, message=msg)

        else:
            for msg in msgs:
                await bot.send(event,
                               message=Message(
                                   unescape(
                                       parse(msg=msg,
                                             nickname=event.sender.card or event.sender.nickname,
                                             sender_id=event.sender.user_id)
                                   )
                               )
                               )


wb_set_cmd = on_regex(r"^(?:全局|模糊|正则)*问", permission=GROUP_ADMIN | GROUP_OWNER | PRIVATE_FRIEND | SUPERUSER|GROUP_MEMBER, )


@wb_set_cmd.handle()
async def wb_set(bot: Bot, event: MessageEvent):
    if isinstance(event, GroupMessageEvent):
        index = event.group_id
    else:
        index = event.user_id

    msg = event.raw_message
    kv = parse_cmd(r"([模糊全局正则]*)问(.+?)答(.+)", msg)

    if kv:
        flag, key, value = kv[0]
        type_ = 3 if '正则' in flag else 2 if '模糊' in flag else 1

        res = wb.set(0 if '全局' in flag else index,
                     unescape(key),
                     value,
                     type_)
        if res:
            await bot.send(event, message='我记住了~')


wb_del_cmd = on_command('删除词条', permission=SUPERUSER | GROUP_OWNER | GROUP_ADMIN | PRIVATE_FRIEND|GROUP_MEMBER, )


@wb_del_cmd.handle()
async def wb_del_(bot: Bot, event: MessageEvent):
    if isinstance(event, GroupMessageEvent):
        index = event.group_id
    else:
        index = event.user_id

    msg = str(event.message)
    res = wb.delete(index, unescape(msg))
    if res:
        await bot.send(event, message='删除成功~')


wb_del_admin = on_command('删除全局词条', permission=SUPERUSER, )


@wb_del_admin.handle()
async def wb_del_admin_(bot: Bot, event: MessageEvent):
    msg = str(event.message).strip()
    if msg:
        res = wb.delete(0, unescape(msg))
        if res:
            await bot.send(event, message='删除成功~')


async def wb_del_all(bot: Bot, event: MessageEvent, state: T_State):
    msg = str(event.message).strip()
    if msg:
        state['is_sure'] = msg


wb_del_all_cmd = on_command('删除词库', permission=SUPERUSER | GROUP_OWNER | PRIVATE_FRIEND, handlers=[wb_del_all])
wb_del_all_admin = on_command('删除全局词库', permission=SUPERUSER, handlers=[wb_del_all])
wb_del_all_bank = on_command('删除全部词库', permission=SUPERUSER, handlers=[wb_del_all])


@wb_del_all_cmd.got('is_sure', prompt='此命令将会清空您的群聊/私人词库，确定请发送 yes')
async def wb_del_all_(bot: Bot, event: MessageEvent, state: T_State):
    if state['is_sure'] == 'yes':

        if isinstance(event, GroupMessageEvent):
            res = wb.clean(event.group_id)
            if res:
                await wb_del_all_cmd.finish(message='删除群聊词库成功~')

        else:
            res = wb.clean(event.user_id)
            if res:
                await wb_del_all_cmd.finish(message='删除个人词库成功~')

    else:
        await wb_del_all_cmd.finish('命令取消')


@wb_del_all_admin.got('is_sure', prompt='此命令将会清空您的全局词库，确定请发送 yes')
async def wb_del_all_admin_(bot: Bot, event: MessageEvent, state: T_State):
    if state['is_sure'] == 'yes':
        res = wb.clean(0)

        if res:
            await bot.send(event, message='删除全局词库成功~')

    else:
        await wb_del_all_admin.finish('命令取消')


@wb_del_all_bank.got('is_sure', prompt='此命令将会清空您的全部词库，确定请发送 yes')
async def wb_del_all_bank_(bot: Bot, event: MessageEvent, state: T_State):
    if state['is_sure'] == 'yes':
        res = wb._clean_all()

        if res:
            await bot.send(event, message='删除全部词库成功~')

    else:
        await wb_del_all_bank.finish('命令取消')
