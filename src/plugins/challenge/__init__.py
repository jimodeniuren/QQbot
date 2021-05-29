from nonebot import on_command
from nonebot.adapters.cqhttp import Bot, Event, Message
from datetime import datetime
import os

tf = on_command('天赋')
we = on_command('武器')
zb = on_command('周本')

PATH = os.path.abspath('.')
print(PATH)

@zb.handle()
async def _(bot: Bot, event: Event):
    key = str(event.get_message()).strip()
    if(key!=""):
        return
    # await zb.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/zb.png]'))
    await zb.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/zb.png]'))


@tf.handle()
async def _(bot: Bot, event: Event):
    key = str(event.get_message()).strip()
    if(key!=""):
        return
    mes = str(event.get_message())
    if '一' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf1.png]'))
    elif '二' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf2.png]'))
    elif '三' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf3.png]'))
    elif '四' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf4.png]'))
    elif '五' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf5.png]'))
    elif '六' in mes:
        await tf.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf6.png]'))
    else:
        day = str(datetime.now().isoweekday())
        if '明' in mes:
            if day == '7':
                day = '1'
                await tf.finish(
                    message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf{day}.png]'))
            elif day == '6':
                await tf.finish(message='明天星期天所有副本都可以刷哦！')
            else:
                day = str(int(day) + 1)
                await tf.finish(
                    message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf{day}.png]'))
        elif day != '7':
            await tf.finish(
                message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/tf{day}.png]'))
        else:
            await tf.finish(message='今天星期天所有副本都可以刷哦！')


@we.handle()
async def _(bot: Bot, event: Event):
    key = str(event.get_message()).strip()
    if(key!=""):
        return
    mes = str(event.get_message())
    if '一' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we1.png]'))
    elif '二' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we2.png]'))
    elif '三' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we3.png]'))
    elif '四' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we4.png]'))
    elif '五' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we5.png]'))
    elif '六' in mes:
        await we.finish(message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we6.png]'))
    else:
        day = str(datetime.now().isoweekday())
        if '明' in mes:
            if day == '7':
                day = '1'
                await we.finish(
                    message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we{day}.png]'))
            elif day == '6':
                await tf.finish(message='明天星期天所有副本都可以刷哦！')
            else:
                day = str(int(day) + 1)
                await we.finish(
                    message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we{day}.png]'))
        elif day != '7':
            await we.finish(
                message=Message(f'[CQ:image,file=file:///{PATH}/src/data/challenge/we{day}.png]'))
        else:
            await we.finish(message='今天星期天所有副本都可以刷哦！')
