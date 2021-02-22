# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/22 上午11:38
# @File: unittestReport.py

import unittest
import HTMLTestRunner
import time
# 找到测试用例 defaultTestLoader加载用例 找discover（目录.用例文件)
discover = unittest.defaultTestLoader.discover('./test_case','test_philipsAdmin.py')

current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
report_path = './test_report/'
report_name = report_path+'unit test result_'+current_time+'.html'
with open(report_name,'wb') as f:
    # './test_report/report.html'
    # 执行用例
    HTMLTestRunner.HTMLTestRunner(stream=f, verbosity=2).run(discover)