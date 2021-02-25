# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/25 下午6:03
# @File: unit_skip_demo.py

import unittest
class Demo(unittest.TestCase):
    def test_1(self):
        print('test_1')

    def test_2(self):
        print('test_2')

if __name__ == '__main__':
    unittest.main()