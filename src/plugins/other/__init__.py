from nonebot import on_notice, on_message
from nonebot.adapters.cqhttp import GroupRecallNoticeEvent, Bot, Message, FriendRecallNoticeEvent, PokeNotifyEvent, \
    MessageEvent
from nonebot.rule import to_me
from random import choice

poke = on_notice(rule=to_me())
# recall = on_notice()
# flashimg = on_message()


# 群聊
# @recall.handle()
# async def _(bot: Bot, event: GroupRecallNoticeEvent):
#     mid = event.message_id
#     meg = await bot.get_msg(message_id=mid)
#     if event.user_id != event.self_id and 'type=flash,' not in meg['message']:
#         # re = '刚刚说了:' + meg['message'] + '\n不要以为派蒙没看见！'
#         re = '防撤回功能已被管理员关闭'
#         # re = '啊这'
#         await recall.finish(message=Message(re), at_sender=True)


# 私聊
# @recall.handle()
# async def _(bot: Bot, event: FriendRecallNoticeEvent):

#      mid = event.message_id
#      meg = await bot.get_msg(message_id=mid)
#      if event.user_id != event.self_id and 'type=flash,' not in meg['message']:
#         # re = '刚刚说了:' + meg['message'] + '\n不要以为派蒙没看见！'
#         re = '防撤回功能已被管理员关闭'
#         # re = '啊这'
#         await recall.finish(message=Message(re))


@poke.handle()
async def _poke(bot: Bot, event: PokeNotifyEvent, state: dict) -> None:
    rely = [{
        "type": "poke",
        "data": {
            "qq": event.get_user_id()
        }
    }]
    await bot.send(event=event, message=rely)
    msg = choice([
        "你再戳！", "？再戳试试？", "别戳了别戳了再戳就坏了555", "我爪巴爪巴，球球别再戳了", "你戳你🐎呢？！",
        "那...那里...那里不能戳...绝对...", "(。´・ω・)ん?", "有事恁叫我，别天天一个劲戳戳戳！", "欸很烦欸！你戳🔨呢",
        "?", "差不多得了😅", "欺负咱这好吗？这不好", "我希望你耗子尾汁",'嘤嘤嘤,好疼','你再戳，我就把你的作案工具没收了，哼哼~','别戳了别戳了，戳怀孕了',
   '嘤嘤嘤，人家痛痛','我错了我错了，别戳了','桥豆麻袋,别戳老子','手感怎么样','戳够了吗？该学习了','戳什么戳，没戳过吗',
   '你用左手戳的还是右手戳的？','不要啦，别戳啦'
    ])
    await poke.finish(msg, at_sender=True)


# @flashimg.handle()
# async def _(bot: Bot, event: MessageEvent):
#     msg = str(event.get_message())
#     if 'type=flash,' in msg:
#         # msg = msg.replace('type=flash,', '')
#         # await flashimg.finish(message=Message("不要发闪照，好东西就要分享。" + msg), at_sender=True)
#         await flashimg.finish(message = "有人不喜欢，关了")
