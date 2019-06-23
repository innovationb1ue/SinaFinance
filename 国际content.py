import requests
from bs4 import BeautifulSoup as bs
import re
import json
import os
import time
import csv
import codecs

Headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}

def main():
    a = json.load(open('./国际/亚洲经济.json'))
    s = requests.Session()
    # print(a[0][3])
    # try:
    #     content = s.get(a[0][3],headers=Headers).content.decode('utf-8','ignore')
    #     result = handle_yzjj_doc(content)
    #     if '页面没有找到' in content:
    #         print('页面没了')
    #         return
    # except IndexError:
    #     print('解析出错')

    #
    for urllist in a:
        for url in urllist:
            res = s.get(url, headers=Headers,timeout=5)
            infolist = []
            if 'yzjj' in url and 'doc' in url:
                content = res.content.decode('utf-8','ignore')
                infolist = handle_yzjj_doc(content)
                print(infolist)
            if 'yzjj' in url and 'world' in url and 'doc' not in url:
                content = res.content.decode('gbk', 'ignore')
                infolist = handle_yzjj_world(content,url)
                print(infolist)
            if infolist != [] and infolist != None:
                with codecs.open('./国际content/亚洲经济.csv','a+','utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(infolist)


def handle_yzjj_doc(content):
    soup = bs(content, 'lxml')
    result = soup.find('div', attrs={'id': 'artibody'}).text
    try:
        date = soup.find('span', attrs={'class': 'date'}).text
    except AttributeError:
        date = soup.find('span',attrs={'class':'time-source'}).text
    try:
        title = soup.find('h1',attrs={'class':'main-title'}).text
    except AttributeError:
        title = soup.find('h1',attrs={'id':'artibodyTitle'}).text
    try:
        author = soup.find('p',attrs={'class':'article-editor'}).text
    except AttributeError:
        author = ''
    try:
        source = soup.find('a',attrs={'class':'source ent-source'})
        if source == None:raise AttributeError
        if source:
            source = source[1].text
            print('source=',source)
    except AttributeError:
        print('source error')
        source = soup.find('span',attrs={'class':'time-source'}).text
    returnList = [title,author,source,date,result]
    print(returnList)
    return returnList

def handle_yzjj_world(content,url=''):
    soup = bs(content,'lxml')
    try:
        result = soup.find('div', attrs={'id': 'artibody'}).text.replace('\n','')
        date = soup.find('span',attrs={'id':'pub_date'})
        if date == None:
            date = soup.find('span', attrs={'id': 'time-source'})
            if date == None:
                date = ''
            else:
                date = date.text
        else:
            date = date.text
        source = soup.find('span',attrs={'id':'media_name'})
        if source == None:
            source = soup.find('span', attrs={'data-sudaclick': 'media_name'})
            if source == None:
                source = ''
            else:
                source = source.text
        else:
            source = source.text

        author = ''
        title =soup.find('h1',attrs={'id':'artibodyTitle'}).text
        returnList = [title, author, source, date, result]
        return returnList
    except:
        print('ERROR in handle_yzjj_world')
        time.sleep(1)
        with open('./error.txt','w+') as f:
            f.write(url)
            f.write('\n')
        return []


def handle_usstock(content):
    soup = bs(content)
    result = soup.find('div',attrs={'id':'artibody'}).text
    date = soup.find('span',attrs={'id':'pub_date'})
    title = soup.find('h1',attrs={'id':'artibodyTitle'})
    source = '美股'










if __name__ == '__main__':
    main()