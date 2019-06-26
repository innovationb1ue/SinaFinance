import requests
from bs4 import BeautifulSoup as bs
import time
import json
import asyncio

URL_BASE = 'http://roll.finance.sina.com.cn/finance/gjcj/gjjj/index_PAGENUM.shtml'
Headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}


def main():
    s = requests.Session()
    f = open('./url.json','w')
    finallist = []
    for i in range(1,271):
        i = str(i)
        url = URL_BASE.replace('PAGENUM',i)
        content = s.get(url,headers=Headers).content.decode('gbk')
        UrlList = process(content)
        finallist.append(UrlList)
    json.dump(finallist,f)
    f.close()

def process(content):
    soup = bs(content,'lxml')
    list = soup.find_all('a',attrs={'target':'_blank'})[3:]
    result = [a['href'] for a in list]
    print(result)
    return result

if __name__ == '__main__':
    main()
