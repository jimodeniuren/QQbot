#!/usr/bin/env python3

import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
# nonebot.load_builtin_plugins() # 加载 nonebot 内置插件
nonebot.load_plugins("src/plugins")
# nonebot.load_plugins("nonebot-plugin-wordbank")
# nonebot.load_plugin('nonebot_plugin_picsearcher')
if __name__ == "__main__":
    nonebot.run()
