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