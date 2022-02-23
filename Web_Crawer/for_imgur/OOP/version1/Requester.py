import requests as rqs

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