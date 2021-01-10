#coding=utf-8
# @Time :2021/1/10 6:56 下午
# @Author : Jelly
# @File : test_case.py
# @Software : PyCharm
import requests

from base.BaseApi import ApiHttpbinGet, ApiHttpbinPost


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
        with_headers({"Content-Type": "application/json"}). \
        with_variables({"aaa":1, "bbb":222}). \
        post(). \
        validate("status_code", 200)

test_httpbin_post_with_json()