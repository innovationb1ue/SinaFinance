import requests
from bs4 import BeautifulSoup as bs
import re
import json
import os
import time
import csv
import codecs

Headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}

JSON_PATH = './国内/地方经济.txt'
SAVE_PATH = './国内content/国内滚动.csv'
def main():
    # json method
    # a = json.load(open(JSON_PATH))
    # txt method
    with open(JSON_PATH) as f:
        a = [f.read().split('\n')]
    s = requests.Session()

    for urllist in a:
        for url in urllist:
            try:
                res = s.get(url, headers=Headers,timeout=5)
            except :
                continue
            infolist = []
            content = res.content.decode('utf-8','ignore')
            if '页面没有找到' in content:
                continue
            if 'roll' in url:
                infolist = handle_world(content,url)
                print(infolist)
            elif 'china' in url :
                infolist = handle_world(content,url)
                print(infolist)
            elif 'special' in url:
                infolist = handle_world(content,url)
                print(infolist)
            elif 'usstock' in url:
                content = res.content.decode('utf-8', 'ignore')
                infolist = handle_usstock(content)
                print(infolist)
            # write into file
            if infolist != [] and infolist != None:
                with codecs.open(SAVE_PATH,'a+','utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(infolist)


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
