#coding=utf-8
# @Time :2021/1/10 4:30 下午
# @Author : Jelly
# @File : test.py
# @Software : PyCharm

import requests
#
# res =requests.get(url="http://httpbin.org/")
# status_code = getattr(res, "status_code")
# print(status_code)

json = {"abc": 1234, "ddd": 456}
data = "abc=1234&ddd=456"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
res =requests.post(url="http://httpbin.org/post", headers=headers, data=data)

status_code = getattr(res, "status_code")
print(res.text)


# class NewClass(object):
#     def __init__(self, name):
#         self.name = name
#         print("我的名字是%s" % self.name)
#
# cc = NewClass("jelly")
