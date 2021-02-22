# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/22 上午11:36
# @File: log.py

import logging


def test_log():

    # 创建日志器
    logger = logging.getLogger()

    # 设置日志级别
    logger.setLevel(logging.INFO)

    # 日志信息输出到控制台，创建一个控制台
    sh = logging.StreamHandler()

    # 把日志信息输出到控制台
    logger.addHandler(sh)


    # 创建格式器
    fmt = '%(asctime)s %(filename)s %(levelname)s %(funcName)s %(message)s'
    formator = logging.Formatter(fmt=fmt)

    # 給控制台设置格式
    sh.setFormatter(formator)



    # 把日志信息输出到文件, 创建一个文件，文件在哪？

    fh = logging.FileHandler('log.log',encoding='utf-8')
    logger.addHandler(fh)
    fh.setFormatter(formator)

    # logger.info('---------------------')

    return logger