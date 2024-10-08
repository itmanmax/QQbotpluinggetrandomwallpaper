from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost
from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类

import requests

from mirai import Image
import logging
import traceback


# 注册插件
@register(name="randomwallpaper", description="Hello randomwallpaper", version="0.1", author="max")
class randomwallpaperPlugin(BasePlugin):

    # API URL
    image_api_url = "https://api.btstu.cn/sjbz/api.php?lx=dongman&format=images"

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    @handler(PersonNormalMessageReceived)
    @handler(GroupNormalMessageReceived)
    async def _(self, event: EventContext):
        try:
            text = event.event.text_message
            if text == "randomwallpaper" or text == "随机壁纸":
                event.prevent_default()
                event.prevent_postorder()
                # 发送图片
                response = requests.get(self.image_api_url)
                if response.ok:  # 使用 response.ok 来检查请求是否成功
                    event.add_return("reply", [Image(url=response.url)])
                else:
                    event.add_return("reply", ["图片获取失败，请稍后再试。"])
                logging.info("randomwallpaper!")
        except Exception as e:
            logging.error(traceback.format_exc())

    # 插件卸载时触发
    def __del__(self):
        pass
