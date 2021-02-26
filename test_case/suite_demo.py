# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/25 下午5:53
# @File: suite_demo.py

# 冒烟测试

import unittest
# from test_case.unit_skip_demo import Demo
from test_case.test_philipsAdmin import Demo

# 添加用例到套件执行
# 创建套件
suite = unittest.TestSuite()

name = unittest.TestLoader().getTestCaseNames(Demo)
print(name)

# 添加用例到套件中: 添加单个测试用例
suite.addTest(Demo(name[0]))
# suite.addTest(Demo('test_2'))

# 运行套件，一定要通过运行器来进行操作，默认到是TextTestRunner()
runner = unittest.TextTestRunner()
runner.run(suite)


