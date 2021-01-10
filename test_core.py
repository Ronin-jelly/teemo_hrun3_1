# coding=utf-8
# @Time :2021/1/10 9:39 上午
# @Author : Jelly
# @File : test_core.py
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

    # url = "http://httpbin.org/get"
    # params = {"adc": 123}
    # def __init__(self, url):
    #     self.url = url
    #
    # def run(self, params):
    #     self.res = requests.get(url=self.url, params=params)
    #     return self
    #
    # def validate(self, key, expected_value):
    #     acturl_value = getattr(self.res, key)
    #     print("acturl_value", acturl_value)
    #     assert acturl_value == expected_value
    #     return self


class ApiHttpbinPost(BaseApi):
    """
    1.调用方法，默认需要传入url
    2.需要传入json参数 在run方法
    3.进行断言
    """
    pass

    # url = "http://httpbin.org/post"
    # json = {"abc": 123}
    # def __init__(self, url):
    #     self.url = url
    #
    # def run(self, json):
    #     self.res = requests.post(url=self.url, json=json)
    #     return self
    #
    # def validate(self, key, expected_value):
    #     acturl_value = getattr(self.res, key)
    #     print("acturl_value", acturl_value)
    #     assert acturl_value == expected_value
    #     return self


def test_httpbin_get():
    url = "http://httpbin.org/get"
    # res = requests.get(url)
    # print(res.status_code)
    ApiHttpbinGet(url).with_variables({"adc": 123}).\
        get(). \
        validate("status_code", 200). \
        validate("url", "http://httpbin.org/get?adc=123")
    # assert res.status_code == 200


# test_httpbin_get()

def test_httpbin_get_with_param():
    url = "http://httpbin.org/get"
    params = {"abc": 123}
    res = requests.get(url=url, params=params)
    assert res.status_code == 200


def test_httpbin_post_with_json():
    # url = "http://httpbin.org/post"
    # json = {"abc": 123}
    # res = requests.get(url=url, json=json)
    # assert res.status_code == 200
    ApiHttpbinPost("http://httpbin.org/post"). \
        with_headers({"Content-Type": "application/x-www-form-urlencoded"}). \
        with_variables("abc=1234&ddd=456"). \
        post(). \
        validate("status_code", 200)
        # validate("url", "http://httpbin.org/post")


test_httpbin_post_with_json()
