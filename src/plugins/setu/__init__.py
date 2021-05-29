import json

from nonebot import on_command
from nonebot.adapters.cqhttp import MessageSegment, Message
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from .data_source import get_setu
from httpx import AsyncClient
import base64
from re import findall

setu = on_command('setu', aliases={'色图', "涩图","瑟图", "无内鬼"})


# global data

@setu.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    key = str(event.get_message()).strip()
    # global data
    data = await get_setu(key)
    if (data == 404):
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
                        "appName": f"群友xp真的怪",
                        "appType": "",
                        "appid": "",
                        "iconUrl": "https://dss0.bdstatic.com/6Ox1bjeh1BF3odCf/it/u=1348432222,2058638649&fm=74&app=80&f=PNG&size=f121,121?sec=1880279984&t=8bef360aab47a34204c38aa496ccdb57"
                    },
                    "data": [
                        {
                            "title": "结果:",
                            "value": f"找不到，怎么想都找不到吧"
                        }
                    ],
                    "title": "",
                    "emphasis_keyword": ""
                }
            },
            "text": "",
            "sourceAd": ""
        }
    elif (data == 429):
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
                        "appName": f"API调用次数达到上限",
                        "appType": "",
                        "appid": "",
                        "iconUrl": "https://dss0.bdstatic.com/6Ox1bjeh1BF3odCf/it/u=1348432222,2058638649&fm=74&app=80&f=PNG&size=f121,121?sec=1880279984&t=8bef360aab47a34204c38aa496ccdb57"
                    },
                    "data": [
                        {
                            "title": "结果：",
                            "value": f"每日限量300张，会慢慢回"
                        }
                    ],
                    "title": "",
                    "emphasis_keyword": ""
                }
            },
            "text": "",
            "sourceAd": ""
        }
    else:
        # fakeurl = str(data['url'])
        # fakeurl = fakeurl.replace("i.pixiv.cat", "t.cn/A6cOexT8")
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
            "sourceUrl": f"{data['url']}",
            "meta": {
                "notification": {
                    "appInfo": {
                        "appName": f"标题:{data['title']}",
                        "appType": "4",
                        "appid": "1108249016",
                        "iconUrl": "https://dss0.bdstatic.com/6Ox1bjeh1BF3odCf/it/u=1348432222,2058638649&fm=74&app=80&f=PNG&size=f121,121?sec=1880279984&t=8bef360aab47a34204c38aa496ccdb57"
                    },
                    "data": [
                        {
                            "title": "pid:",
                            "value": f"{str(data['pid'])}"
                        },
                        {
                            "title": "作者:",
                            "value": f"{data['author']}"
                        },
                        {
                            "title": "url:",
                            "value": f"{data['url']}"
                        },
                        {
                            "title": "标签:",
                            "value": f"{str(data['tags'])}"
                        }
                    ],
                    # "button":[{
                    #     "action":"web",
                    #     "url": data['url'],
                    #     "name":"为什么不能点啊"}],
                    "title": "",
                    "emphasis_keyword": ""
                }
            },
            "text": "",
            "sourceAd": ""
        }
    await bot.send(event=event, message="给大佬递图")
    await bot.send(event=event, message=MessageSegment.json(data=json.dumps(setuJson)))
    
    # base64 = await downPic(data['url'])
    # try:
    ImgCq = [
        {
            "type": "image",
            "data": {
                "file": data['url'],
                "type": "flash",
                "c":3
                # "url": data['url'],
                # "url": fakeurl,
                # "title": data['title']
            }
        }
    ]
    # ImgCq = "[CQ:cardimage,file=" + data['url'] + "]"
    # ImgCq ="[CQ:image,type=flash,c=3,file=base64://" + base64 + "]"
    try:
        await bot.send(event=event, message=Message(ImgCq))
    except:
        setu.finish("setu太涩被tx吃掉了")
    #     # raise e
    #     ImgCq = "[CQ:share,url=" + data['url'] +",title=闪照发不出来,content=自己点开看吧,image=https://dss0.bdstatic.com/6Ox1bjeh1BF3odCf/it/u=1348432222,2058638649&fm=74&app=80&f=PNG&size=f121,121?sec=1880279984&t=8bef360aab47a34204c38aa496ccdb57]"
    #     await bot.send(event=event, message=Message(ImgCq))
    # sj = {"app": "com.tencent.mobileqq.reading",
    #       "desc": "",
    #       "view": "singleImg",
    #       "ver": "1.0.0.70",
    #       "prompt": "",
    #       "appID": "",
    #       "sourceName": "",
    #       "actionData": "",
    #       "actionData_A": "",
    #       "sourceUrl": "",
    #       "meta": {
    #           "singleImg": {
    #               "mainImage": f"{data['url']}",
    #               "mainUrl": ""}},
    #       "text": "",
    #       "extraApps": [],
    #       "sourceAd": ""}
    # await bot.send(event=event, message=MessageSegment.json(data=json.dumps(sj)))
# async def downPic(url) -> str:
#     async with AsyncClient() as client:
#         headers = {
#             'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
#                           'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
#         }
#         re = await client.get(url=url, headers=headers)
#         if re:
#             ba = str(base64.b64encode(re.content))
#             pic = findall(r"\'([^\"]*)\'", ba)[0].replace("'", "")
#             return pic