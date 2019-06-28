import json
import requests
from bs4 import BeautifulSoup as bs
import asyncio

# lid = 宏观经济1687 134页 金融新闻1690 162 地方经济1688  442 部委动态1689 46
# http://finance.sina.com.cn/chanjing/
# lid = 产经滚动1693 3212页
URL_PATTERN = 'http://feed.mix.sina.com.cn/api/roll/get?pageid=164&lid=1693&num=50&page=PAGENUM'
Headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}

FINAL = []
FP = open('./产经/产经滚动.txt','w+')

@asyncio.coroutine
def main(pagenum = 1):
    global FINAL
    s = requests.Session()
    content = s.get(URL_PATTERN.replace('PAGENUM',str(pagenum)),headers=Headers).content.decode('utf-8')
    info = json.loads(content)
    resultlist = [a['url'] for a in info['result']['data']]
    for i in resultlist:
        FP.write(i)
        FP.write('\n')
    print(resultlist[1:5])

if __name__ == '__main__':
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(asyncio.wait([main(i) for i in range(1,3213)]))
    loop.close()
    FP.close()
