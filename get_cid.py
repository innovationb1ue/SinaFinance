import requests
from bs4 import BeautifulSoup as bs
import asyncio
URL_BASE = 'http://finance.sina.com.cn/roll/index.d.html?cid=CIDH'

Headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}

SAVE_PATH = './cid.txt'
s = requests.Session()
@asyncio.coroutine
def main(i):
    # for i in range(10000,99999):
    print(i)
    i = str(i)
    URL = URL_BASE.replace('CIDH',i)
    try:
        content = s.get(URL,headers=Headers,timeout=5).content.decode("utf-8")
    except :
        content = ''
    soup = bs(content,'lxml')
    flag = soup.find("ul",attrs={'class':'list_009'})
    if flag != None:
        print('有货')
        with open(SAVE_PATH,'a+') as f:
            f.write(URL)
            f.write('\n')









if __name__ == '__main__':
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(asyncio.wait([main(i) for i in range(70000,99999)]))
    loop.close()
    FP.close()
