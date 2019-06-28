import requests
from bs4 import BeautifulSoup as bs
import re
import json
import os
import time
import csv
import codecs
import chardet
Headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}

JSON_PATH = './国际/国际滚动.json'
SAVE_PATH_GBK = './国际content/国际滚动_GBK.csv'
SAVE_PATH_UTF8 = './国际content/国际滚动_UTF8.csv'
def main():
    # json method
    a = json.load(open(JSON_PATH))
    # txt method
    # with open(JSON_PATH) as f:
    #     a = [f.read().split('\n')]
    s = requests.Session()

    for urllist in a:
        for url in urllist:
            try:
                res = s.get(url, headers=Headers,timeout=5)
            except :
                continue
            finallist = []
            encode_type = chardet.detect(res.content)['encoding']
            print(encode_type)
            content = res.content.decode(encode_type,'ignore').replace("\n",'').strip()
            if '页面没有找到' in content:
                continue
            if 'usstock' in url:
                finallist = handle_usstock(content)
                print(finallist)
            else :
                finallist = handle_world(content,url)
                print(finallist)


            # write into file
            if finallist != [] and finallist != None:
                if encode_type == 'utf-8' or encode_type == 'UTF-8':
                    with codecs.open(SAVE_PATH_UTF8,'a+','utf-8','ignore') as f:
                        writer = csv.writer(f)
                        writer.writerow(finallist)
                elif encode_type == 'gbk' or encode_type == 'GB2312'or encode_type == 'GBK':
                    with codecs.open(SAVE_PATH_GBK,'a+','gbk','ignore') as f:
                        writer = csv.writer(f)
                        writer.writerow(finallist)

# method to handle URL which has 'roll'

def handle_world(content,url=''):
    soup = bs(content,'lxml')
    # get result
    try:
        result = soup.find('div', attrs={'id': 'artibody'}).text.replace('\n','')
    except:
        result = ''
    # get date
    try:
        date = soup.find('span',attrs={'id':'pub_date'})
        if date != None:
            date = date.text
        else:
            date = soup.find('span', attrs={'id': 'time-source'})
            if date != None:
                date = date.text
            else:
                date = soup.find('span',attrs={'class':'date'})
                if date != None:
                    date = date.text
                else:
                    date = ''
    except:
        date = ''
    # get source
    try:
        source = soup.find('span',attrs={'id':'media_name'})
        if source != None:
            source = source.text
        else:
            source = soup.find('span', attrs={'data-sudaclick': 'media_name'})
            if source != None:
                source = source.text
            else:
                source = soup.find('span', attrs={'class': 'source ent-source'})
                if source != None:
                    source = source.text
                else:
                    source = soup.find('a',attrs={'class':'source ent-source'})
                    if source != None:
                        source = source.text
    except:
        source = ''
    # get author
    try:
        author = soup.find('p',attrs={'class':'article-editor'})
        if auth != None:
            author = author.text
        else:
            author  = ''
    except :
        author = ''
    # get title
    try:
        title =soup.find('h1',attrs={'id':'artibodyTitle'})
        if title != None:
            title = title.text
        else:
            title =soup.find('h1',attrs={'class':'main-title'})
            if title != None:
                title = title.text
            else:
                title = ''
    except:
        title = ''
    returnList = [title, author, source, date, result]
    if returnList == ['','','','','']:
        with open('./Error.txt','a+') as f:
            f.write(url)
    return returnList

def handle_usstock(content):
    soup = bs(content,'lxml')
    try:
        result = soup.find('div',attrs={'id':'artibody'})
        if result != None:
            result = result.text
        else:
            result = ''
    except :
        result = ''
    try:
        date = soup.find('span',attrs={'id':'pub_date'})
        if date != None:
            date = date.text
        else:
            date = soup.find('span',attrs={'class':'date'})
            if date != None:
                date = date.text
            else:
                date = ''
    except :
        date = ''
    try:
        title = soup.find('h1',attrs={'id':'artibodyTitle'})
        if title != None:
            title = title.text
        else:
            title = soup.find('h1',attrs={'class':'main-title'})
            if title != None:
                title = title.text
            else:
                title = ''
    except :
        title = ''

    try:
        source = soup.find('span',attrs={'class':'source ent-source'})
        if source != None:
            source = source.text
        else:
            try:
                source = soup.find('span',attrs={'id':'media_name'})
                if source != None:
                    source = source.text
                else:
                    source = ''
            except:
                source = ''
    except:
        source = ''

    author = ''
    try:
        author = soup.find('p',attrs={'class':'article-editor'})
        if author != None:
            author = author.text
        else:
            author = ''
    except:
        author = ''
    returnList = [title,author,source,date,result]
    if returnList == ['','','','','']:
        with open('./Error.txt','a+') as f:
            f.write(url)
    return returnList


def handle_roll(content,url=''):
    soup = bs(content,'lxml')
    # get title
    try:
        title = soup.find('h1',attrs={'id':'artibodyTitle'})
        if title != None:
            title = title.text
        else:
            title = soup.find('h1',attrs={'class':'main-title'})
            if title != None:
                title = title.text
            else:
                title = ''
    except:
        title = ''
    # get author
    author = ''
    # get source
    try:
        source = soup.find('span',attrs={'id':'media_name'})
        if source != None:
            source = title.text
        else:
            source = ''
    except:
        source = ''
    #get date
    try:
        date = soup.find('span',attrs={'id':'pub_date'})
        if date != None:
            date = title.text
        else:
            date = soup.find('span',attrs={'class':'time-source'})
            if date != None:
                date = date.text
            else:
                date = ''
    except:
        date = ''
    # get result
    try:
        result = soup.find('div',attrs={'id':'artibody'})
        if result != None:
            result = title.text
        else:
            result = ''
    except:
        result = ''
    # generate returnList
    returnList = [title,author,source,date,result]
    print(returnList)
    if returnList == ['','','','','']:
        with open('./Error.txt','a+') as f:
            f.write(url)
    return returnList










if __name__ == '__main__':
    main()
