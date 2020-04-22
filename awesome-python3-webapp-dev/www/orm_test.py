import asyncio
import orm
import random
from models import User,Blog,Comment

async def test(loop):
    await orm.create_pool(loop, user='root', password='root', db='clc')
    u = User(name='test', email='test%s@example.com' % random.randint(0,100), passwd='abc123456', image='about:blank')
    await u.save()

async def test_save(loop):
    await orm.create_pool(loop=loop, user='root', password='root', db='clc')
    u = User(name='Test4', email='tes4@example.com', passwd='888888', image='about:blank')
    await u.save()

async def test_get(loop):
    await orm.create_pool(loop, user='root', password='root', db='clc')
    U = await User().findAll()
    print(U)

#要运行协程，需要使用事件循环
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(test(loop))
#     print('Test finished.')
#     loop.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [test(loop), test_get(loop)]
    loop.run_until_complete(asyncio.wait(tasks))
    # loop.close() 用了wait，不需要close了
    print('Test finished')