import requests
from bs4 import BeautifulSoup as bs
import asyncio
import time

PID_TXT_PATH = './CIDs/cid2.txt'
PID_SAVE_URL_PATH = './CIDs/cid_url2.txt'
Headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}

async def main():
    # s = requests.Session()
    s = requests.Session()
    # 获取有cid的链接地址
    with open(PID_TXT_PATH) as f:
        urllist = f.read().split('\n')
    for URL_BASE in urllist:
        print(URL_BASE)
        flag = False
        # content2=''
        for page in range(1,10000):
            # 第一次进入时阻塞获取url
            if not flag:
                print('page=',page)
                url = (URL_BASE + '&page=' + str(page))
                try:
                    content = s.get(url,headers=Headers,timeout=5).content.decode('utf-8')
                except:
                    print("Catch Exception")
                    continue
            temp_task = asyncio.create_task(process(content))
            await temp_task
            temp = temp_task.result()
            # if content2:
            #     temp2_task = asyncio.create_task(process(content2))
            #     await temp2_task
            #     temp2 = temp2_task.result()
            #     if temp2 != []:
            #         asyncio.create_task(save(PID_SAVE_URL_PATH,temp2))

            if temp != []:
                print('有货page=',page)
                # print('url2 page=',page+2)
                url = (URL_BASE + '&page=' + str(page+1))
                # url2 = (URL_BASE + '&page=' + str(page+2))
                # 保存的同时异步获取下一个网页的信息
                task1 = asyncio.create_task(save(PID_SAVE_URL_PATH,temp))
                task2 = asyncio.create_task(getcontent(url,s))
                # task3 = asyncio.create_task(fetch(url2))
                await task2
                # await task3
                content = task2.result()
                # content2 = task3.result()
                await task1
                flag = True
            else:
                flag = False
                break

async def getcontent(url,s):
    try:
        return s.get(url,headers=Headers,timeout = 5).content.decode('utf-8')
    except:
        print('Catch Exception in getcontent')
        return ''
#
# async def fetch(url):
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#     async with aiohttp.ClientSession() as session:
#         try:
#             async with session.get(url, headers=headers, verify_ssl=False,timeout=5) as resp:
#                 return await resp.text(errors='ignore')
#         except:
#             return ''

async def print1(info=''):
    if info != '':
        print(info)
    print(time.time())

async def save(path,urllist):
    with open(path,'a+') as f:
        for url in urllist:
            f.write(url)
            f.write('\n')

async def process(content):
    soup = bs(content,'lxml')
    list = soup.find_all('a',attrs={'target':'_blank'})[3:]
    if list == []:
        return []
    else:
        result = [a['href'] for a in list]
    return result

if __name__ == '__main__':
    asyncio.run(main())
