import requests
import re
from bs4 import BeautifulSoup as bs
import codecs
import csv
import chardet

TXT_PATH = ''
Headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15'}
SAVE_PATH_GBK = './手机端/info1_GBK.csv'
SAVE_PATH_UTF8 = './手机端/info1_UTF8.csv'
def main():
    s = requests.Session()
    with open(JSON_PATH) as f:
        URL_LIST = f.read().split('\n')
    for url in URL_LIST:
        content = s.get(url,headers=Headers).content
        # infer encode
        encode_type = chardet.detect(content)['encoding']

        # init soup
        soup = bs(content)
        # get article information
        title = get_title(soup)
        time = get_time(soup)
        result = get_result(soup)
        source = get_source(soup)
        author = get_author(soup)
        finallist = [title,author,source,time,result]
        if encode_type == 'utf-8' or encode_type == 'UTF-8':
            with codecs.open(SAVE_PATH_UTF8,'a+','utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(finallist)
        elif encode_type == 'gbk' or encode_type == 'GB2312'or encode_type == 'GBK':
            with codecs.open(SAVE_PATH_GBK,'a+','gbk') as f:
                writer = csv.writer(f)
                writer.writerow(finallist)

def get_author(soup):
    return ''

def get_title(soup):
    try:
        title = soup.find('h1',attrs={'class':'art_tit_h1'})
        if title != None:
            title = title.text
        else:
            time = ''
    except:
        title = ''
    return title

def get_time(soup):
    try:
        time = soup.find('time',attrs={'class':'art_time'})
        if time != None:
            time = time.text
        else:
            time = soup.find('time',attrs={'class':'weibo_time'})
            if time != None:
                time = time.text
            else:
                time = ''
    except:
        time = ''
    return time
def get_result(soup):
    try:
        result = soup.find('section',attrs={'class':'art_pic_card art_content'})
        if result != None:
            result = time.text
        else:
            result = ''
    except:
        result = ''
    return result
def get_source(soup):
    try:
        source = soup.find('cite',attrs={'class':'art_cite'})
        if source != None:
            source = time.text
        else:
            source = soup.find('h2',attrs={'class':'weibo_user'})
            if source != None:
                source = time.text
            else:
                source = ''
    except:
        source = ''
    return source
