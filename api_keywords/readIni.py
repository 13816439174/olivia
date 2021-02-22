# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/22 上午11:36
# @File: readIni.py
import configparser



def ReadIni(selection,option):
    conf=configparser.ConfigParser()
    conf.read('/Users/jinshengnan/PycharmProjects/olivia/config/config.ini')
    value=conf.get(selection,option)
    return value