import logging;logging.basicConfig(level=logging.INFO)

import asyncio

from aiohttp import web


def index(request):  # 参考aiohttp的文档
    # 与老师的源码相比，最重要的是要加content_type这个参数，否则会变成下载文件
    return web.Response(body='<h1>Awesome</h1>'.encode('utf-8'), content_type='text/html')


async def init():
    app = web.Application()
    app.add_routes([web.get('/',index)])

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 9000)
    await site.start()
    print('服务器启动成功！')

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
