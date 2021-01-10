#coding=utf-8
# @Time :2021/1/10 6:53 下午
# @Author : Jelly
# @File : BaseApi.py
# @Software : PyCharm

import requests
class BaseApi():

    def __init__(self, url):
        self.url = url

    def with_variables(self, variables):
        self.variables = variables
        return self

    def with_headers(self, headers):
        self.headers = headers
        return self

    def get(self):
        self.res = requests.get(url=self.url, headers=self.headers, params=self.variables)
        return self

    def post(self):
        if isinstance(self.variables, str):
            self.res = requests.post(url=self.url, headers=self.headers, data=self.variables)
            print("str", self.res.text)
        elif isinstance(self.variables, dict):
            self.res = requests.post(url=self.url, headers=self.headers, json=self.variables)
            print("dict", self.res.text)
        return self

    def validate(self, key, expected_value):
        acturl_value = getattr(self.res, key)
        print("acturl_value", acturl_value)
        assert acturl_value == expected_value
        return self


class ApiHttpbinGet(BaseApi):
    """
    1.调用方法，默认需要传入url
    2.需要传入params参数 在run方法
    3.进行断言
    """
    pass


class ApiHttpbinPost(BaseApi):
    """
    1.调用方法，默认需要传入url
    2.需要传入json参数 在run方法
    3.进行断言
    """
    pass