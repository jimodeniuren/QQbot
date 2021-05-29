from nonebot import on_command
from nonebot.adapters.cqhttp import MessageEvent
from nonebot.adapters import Bot, Event
from datetime import datetime
from nonebot.typing import T_State
contact = on_command("给作者留言", aliases={"feedback"}, priority=1, block=True)


@contact.handle()
async def _city(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["words"] = args


@contact.got("words", prompt="想要留什么言呢？")
async def handle_city(bot: Bot, event: Event, state: T_State):
    content = state["words"]

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    is_from_private = True
    session_id = event.get_session_id().split("_")
    if len(session_id) == 3:
        is_from_private = False
        group_id = session_id[1]

    if is_from_private:
        msg = f"[Contact Message]\nSender: {event.get_user_id()}\nFrom: Private\nTime: {now}\nContent: {content}"
    else:
        msg = f"[Contact Message]\nSender: {event.get_user_id()}\nFrom: Group({group_id})\nTime: {now}\nContent: {content}"
    await bot.send_private_msg(user_id=超级用户的QQ号填这里, message=msg)

    await contact.finish("已经成功传达给主人啦~")
