from nonebot import on_command
from nonebot.adapters.cqhttp import Event, Bot
from nonebot.adapters.cqhttp import MessageSegment,Message
import json,os

PATH = os.path.abspath('.')

help = on_command('help', aliases={'帮助'})


@help.handle()
async def _(bot: Bot, event: Event):
    setuJson = {
        "app": "com.tencent.miniapp",
        "desc": "",
        "view": "notification",
        "ver": "0.0.0.1",
        "prompt": "",
        "appID": "",
        "sourceName": "",
        "actionData": "",
        "actionData_A": "",
        "sourceUrl": "",
        "meta": {
            "notification": {
                "appInfo": {
                    "appName": f"帮助1",
                    "appType": "",
                    "appid": "",
                    "iconUrl": "https://dss0.bdstatic.com/6Ox1bjeh1BF3odCf/it/u=1348432222,2058638649&fm=74&app=80&f=PNG&size=f121,121?sec=1880279984&t=8bef360aab47a34204c38aa496ccdb57"
                },
                "data": [
                    {
                        "title": "功能1",
                        "value": f"抽十连/抽小保底/抽大保底(加好友私聊)"
                    },
                    {
                        "title": "功能2",
                        "value": f"武器/天赋/周本/黄历"
                    },
                    {
                        "title": "功能3",
                        "value": f"武器查询 武器名"
                    },
                    {
                        "title": "功能4",
                        "value": f"角色资料 名字"
                    },
                    {
                        "title": "功能5",
                        "value": f"命座 名字ep.命座 琴四命"
                    },
                    {
                        "title": "功能6",
                        "value": f"涩图/setu/无内鬼，可带关键字"
                    },
                    {
                        "title": "功能7",
                        "value": f"搜图"
                    },
                    {
                        "title": "功能8",
                        "value": f"彩虹屁/笑话/学说话"
                    },
                    {
                        "title": "功能9",
                        "value": f"问答调教"
                    }
                ],
                "title": "",
                "emphasis_keyword": ""
            }
        },
        "text": "",
        "sourceAd": ""
    }
    await bot.send(event=event, message=MessageSegment.json(data=json.dumps(setuJson)))
    setuJson = {
        "app": "com.tencent.miniapp",
        "desc": "",
        "view": "notification",
        "ver": "0.0.0.1",
        "prompt": "",
        "appID": "",
        "sourceName": "",
        "actionData": "",
        "actionData_A": "",
        "sourceUrl": "",
        "meta": {
            "notification": {
                "appInfo": {
                    "appName": f"帮助2",
                    "appType": "",
                    "appid": "",
                    "iconUrl": "https://dss0.bdstatic.com/6Ox1bjeh1BF3odCf/it/u=1348432222,2058638649&fm=74&app=80&f=PNG&size=f121,121?sec=1880279984&t=8bef360aab47a34204c38aa496ccdb57"
                },
                "data": [
                    {
                        "title": "功能10",
                        "value": f"营销号 主体/事件/另一种说法 ep.营销号群主/爱看setu/是个lsp"
                    },
                    {
                        "title": "功能11",
                        "value": f"狗屁不通 主题ep.狗屁不通看色图"
                    },
                    {
                        "title": "功能12",
                        "value": f"记仇 天气/主题 ep.记仇晴/群主一个人吃独食"
                    },
                    {
                        "title": "功能13",
                        "value": f"无中生友 内容/qq号 ep.无中生友来张色图/群主的qq号"
                    },
                    {
                        "title": "功能14",
                        "value": f"舔狗日记ep.舔狗日记抹茶"
                    },
                    {
                        "title": "功能15",
                        "value": f"给作者留言"
                    }
                ],
                "title": "",
                "emphasis_keyword": ""
            }
        },
        "text": "",
        "sourceAd": ""
    }
    await bot.send(event=event, message=MessageSegment.json(data=json.dumps(setuJson)))
    
tiaojiao = on_command('tiaojiao', aliases={'问答调教'})
@tiaojiao.handle()
async def _(bot: Bot, event: Event):
    await tiaojiao.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/tiaojiao.png]'))