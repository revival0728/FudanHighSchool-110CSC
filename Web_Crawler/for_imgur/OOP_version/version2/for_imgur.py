#!python3.9

from PIL import Image
import os
import requests as rqs
from bs4 import BeautifulSoup as bsp

class Analyzer:
    def __init__(self, html_text):
        self.__html = bsp(html_text, 'html.parser')
        self.__result = None
    @property
    def result(self):
        return self.__result
    def find_all(self, name: str ='', attrs: dict ={}, recursive: bool =True, limit: int=None):
        self.__result = self.__html.find_all(name=name, attrs=attrs, recursive=recursive, limit=limit)
    def pickup(self, index: int):
        self.__html = self.__result[index]

class Requester:
    def __init__(self, url: str, html_type: str = 'https') -> None:
        self.__url = html_type + '://' + url
        self.__response = None
    @property
    def response(self):
        return self.__response
    def __make_req_url(self, additional_url: list):
        req_url = self.__url
        for i in additional_url:
            req_url += '/'
            req_url += i
        return req_url
    def get(self, additional_url: list, stream: bool = False, timeout: int =1):
        req_url = self.__make_req_url(additional_url)
        self.__response = rqs.get(req_url, timeout=timeout, stream=stream)
    def post(self, additional_url: list, payload: dict, timeout: int =1):
        req_url = self.__make_req_url(additional_url)
        self.__response = rqs.post(req_url, data=payload, timeout=timeout)

def get_input():
    ipt = input('Please input the keyword: ')
    ret = ''
    for i in ipt.strip().split():
        ret += i + '+'
    return ret[:-1]

def main():
    rq = Requester('imgur.com')
    rq.get([f'search?q={get_input()}'])
    anl = Analyzer(rq.response.text)
    anl.find_all(name='div', attrs={'class': 'cards'})
    anl.pickup(0)
    anl.find_all(name='img')
    picture_urls = []
    for i in anl.result:
        picture_urls.append(i.get('src')[14:])
    rq_pic = Requester('i.imgur.com')
    for i in picture_urls:
        rq_pic.get([i], stream=True, timeout=5)
        image = Image.open(rq_pic.response.raw)
        image.show()
        os.system('pause')

if __name__ == '__main__':
    main()

