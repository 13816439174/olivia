# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/22 上午11:35
# @File: apiKey.py

import requests
import json
import jsonpath
import configparser
import time


# 这是接口的关键字驱动类，用于实现基本的接口测试业务关键字封装
class ApiKey:
    # get请求
    def do_get(self, url, params=None, **kwargs):
        return requests.get(url=url, params=params, **kwargs)

    # post请求
    def do_post(self, url, data=None, **kwargs):
        return requests.post(url=url, data=data, **kwargs)

    # put请求
    def do_put(self, url, data=None, **kwargs):
        return requests.put(url=url, data=data, **kwargs)

    # delete请求
    def do_delete(self, url, params=None, **kwargs):
        return requests.delete(url=url, params=params, **kwargs)

    def get_text(self, res, key):
        if res is not None:
            try:
                text=json.loads(res)
                value=jsonpath.jsonpath(text, '$..{0}'.format(key))
                # 因为jsonpath默认返回的是一个list,如果没有获取到内容，就默认为False
                if value:
                    if len(value) == 1:
                        return value[0]
                return value
            except Exception as e:
                return e
        else:
            return None

    def get_string_by_startStr_endStr(self, str, startStr, endStr):
        if str is not None:
            try:
                startIndex=str.find(startStr, 0, len(str))
                endIndex=str.find(endStr, 0, len(str))
                subStr=str[startIndex:endIndex]
                return subStr
            except Exception as e:
                return e
        else:
            return None

    def get_string_by_startStr_endStr_multi(self, str, startStr, endStr):
        if str is not None:
            try:
                startIndex=str.find(startStr, 0, len(str))
                endIndex=str.find(endStr, startIndex, len(str))
                subStr=str[startIndex:endIndex]
                return subStr
            except Exception as e:
                return e
        else:
            return None

    def get_current_timestamp(self):
        # current_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        # print(current_time)
        current_timestamp = int(time.time())
        # print(int(current_timestamp))
        return current_timestamp