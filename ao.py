import asyncio
from aiohttp import ClientSession

queue = asyncio.Queue()

tasks = []


url = "http://www.baidu.com/{}"
async def hello(url,semaphore):
    async with semaphore:
        async with ClientSession() as session:
            async with session.get(url,allow_redirects=False,timeout=10) as response:
                code = response.status
                # if code == 200:
                #     print("200 : " +  url)

def run():
    semaphore = asyncio.Semaphore(500)
    with open('dic.txt') as f:
        for dic in f:
            dic = dic.strip()
            task = asyncio.ensure_future(hello(url.format(dic),semaphore))
            tasks.append(task)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    run()
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
