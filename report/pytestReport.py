# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/22 上午11:38
# @File: pytestReport.py

import pytest
import time
import os

current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())


# pytest.main(['-v','../test_case/test_philipsAdmin.py','--html=../test_report/pytestReport'+current_time+'.html'])

pytest.main(['-v','../test_case/test_philipsAdmin.py','--alluredir','../temp'])
os.system('allure generate ../temp -o ../test_report --clean')