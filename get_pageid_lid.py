import requests
from bs4 import BeautifulSoup as bs
import json
import asyncio
s = requests.Session()
Headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}
URL_BASE = 'http://feed.mix.sina.com.cn/api/roll/get?pageid=PAGEIDH&lid=LIDH&num=50&page=1'
def main():
    for pageid in range(1,1000):
        for lid in range(0,4000):
            pageid = str(pageid)
            lid = str(lid)
            URL = URL_BASE.replace('PAGEIDH',pageid).replace('LIDH',lid)
            try:
                content = s.get(URL,headers=Headers,timeout=5).content.decode('utf-8')
            except:
                content = ''
            if 'wapurl' in content:
                print(URL)
            with open('./Total.txt','a+') as f:
                f.write(URL)
                f.write('\n')

if __name__ == '__main__':
    main()
