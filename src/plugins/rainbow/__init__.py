from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

from .data_source import get_caihong_data

joke = on_command('彩虹屁')

@joke.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    msg = await get_caihong_data()
    await joke.finish(msg)
