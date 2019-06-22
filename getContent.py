import requests
from bs4 import BeautifulSoup as bs
import json
import asyncio

def main():
    urlList = []
    json.load(open('./url.json'),urlList)
    print(urlList)










if __name__ == '__main__':
    main()