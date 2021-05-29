from nonebot import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

tts = on_command(cmd="tts", aliases={"学说话"})


@tts.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()  
    if args:
        state["words"] = args  


@tts.got("words", prompt="说什么？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    words = state["words"]
    msg = [
        {
            "type": "tts",
            "data": {
                "text": words
            }

        }
    ]
    await bot.send(event=event, message=msg)
