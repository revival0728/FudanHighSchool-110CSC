#!python3.9

from PIL import Image
from Requester import Requester
from Analyzer import Analyzer
import os

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
