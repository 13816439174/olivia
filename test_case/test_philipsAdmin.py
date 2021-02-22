# _*_ coding:utf-8 _*_
# 作者：Olivia
# @Time: 2021/2/22 上午11:39
# @File: test_philipsAdmin.py.py

import unittest
import requests
from ddt import ddt, file_data
from api_keywords.apiKey import ApiKey
from api_keywords.log import test_log
from api_keywords.readIni import ReadIni
import time
import HTMLTestRunner

@ddt
class TestCase(unittest.TestCase):

    def assignment(self,kwargs):
        for key,value in kwargs.items():
            # 基于数据内容的格式来进行判断该用何种处理方式
            if type(value) is dict:
                self.assignment(value)
            else:
                if value:
                    pass
                else:
                    kwargs[key]=getattr(self,key)
        return kwargs

    '''
        实现从用户登录，到获取用户信息，项目信息的自动化测试
    '''
    # 通过赋值全局变量的方式，来实现接口关联数据的交互
    @classmethod
    def setUpClass(cls) -> None:
        cls.ak=ApiKey()
        cls.log=test_log()
        cls.cookie = None
        cls.url = ReadIni('TEST_SERVER','url') #从config.ini文件中读取url
        # cls.userId = '2'
        # cls.projectid = '12'

    # 登录
    @file_data('../test_data/loginUserData.yaml')
    def test_01(self,**kwargs):
        self.log.info('--------------------')
        self.log.info('test_01: test login')
        url_login = self.url+kwargs['path']
        self.log.info('访问URL{}'.format(url_login))
        self.log.info('user信息 {}'.format(kwargs['user']))
        # response = requests.post(url=url_login, json=data) # requests.post() 可以用自定义的do_post方法替代
        response = self.ak.do_post(url=url_login,json=kwargs['user']) #json=data, 可以自动转成json格式
        # print('test_01 status: '+response.json()['status'])
        # phone = self.ak.get_text(response.text,'phone')
        status = self.ak.get_text(response.text,'status')
        self.log.info('返回status {}'.format(status))
        self.assertEqual(status,kwargs['status'],msg='test pass')
        set_cookie = response.headers['Set-Cookie']
        self.log.info('set_cookie的内容 {}'.format(set_cookie))
        sub1 = self.ak.get_string_by_startStr_endStr(set_cookie,'JSESSIONID=','Path=/api')
        sub2 = self.ak.get_string_by_startStr_endStr_multi(set_cookie,'token=','Max-Age=')
        sub3 = self.ak.get_string_by_startStr_endStr_multi(set_cookie,'fingerprint=','Max-Age=')
        sub4 = self.ak.get_string_by_startStr_endStr_multi(set_cookie,'clientcode=','Max-Age=')
        if sub2:
            cookie=sub1 + sub2 + sub3 + sub4
            self.log.info('cookie的内容{}'.format(cookie))
            TestCase.cookie=cookie
        self.log.info('response {}'.format(response.text))

    # 获取所有用户信息
    @file_data('../test_data/userData.yaml')
    def test_02(self,path,headers):
        self.log.info('--------------------')
        self.log.info('test_02: get user list')
        url_getAllUser = self.url+path
        self.log.info('访问URL{}'.format(url_getAllUser))
        headers['cookie']=self.cookie
        response = self.ak.do_get(url=url_getAllUser,headers=headers)
        # print('test_02 status: '+response.json()['status'])
        status = self.ak.get_text(response.text,'status')
        # print(status+'testPass')
        self.log.info('返回status {}'.format(status))
        self.assertEqual(status,'success',msg='test pass')
        self.log.info('response {}'.format(response.text))

    # 获取单个用户信息
    @file_data('../test_data/singleUserInfo.yaml')
    def test_03(self,path,headers,data):
        self.log.info('--------------------')
        self.log.info('test_03: test get single user info')
        url_singleUser = self.url+path+data['userId']
        self.log.info('访问URL{}'.format(url_singleUser))
        headers['cookie']=self.cookie
        response = self.ak.do_get(url=url_singleUser, headers=headers)
        status = self.ak.get_text(response.text,'status')
        self.log.info('返回status {}'.format(status))
        self.assertEqual(status, 'success', msg='test pass')
        self.log.info('response {}'.format(response.text))

    # 获取项目列表
    @file_data('../test_data/projectListInfo.yaml')
    def test_04(self,path,headers):
        self.log.info('--------------------')
        self.log.info('test_04: test get project list')
        url_getProjectList = self.url+path
        self.log.info('访问URL{}'.format(url_getProjectList))
        headers['cookie'] = self.cookie
        response = self.ak.do_get(url=url_getProjectList,headers=headers)
        status=self.ak.get_text(response.text, 'status')
        self.log.info('返回status {}'.format(status))
        self.assertEqual(status, 'success', msg='test pass')
        self.log.info('response {}'.format(response.text))

    # 获取单个项目信息
    @file_data('../test_data/singleProjectInfo.yaml')
    def test_05(self,path,headers,data):
        self.log.info('--------------------')
        self.log.info('test_05: test get single project info')
        url_getSingleProjectInfo=self.url + path+data['projectId']
        self.log.info('访问URL{}'.format(url_getSingleProjectInfo))
        headers['cookie']=self.cookie
        response=self.ak.do_get(url=url_getSingleProjectInfo, headers=headers)
        status=self.ak.get_text(response.text, 'status')
        self.log.info('返回status {}'.format(status))
        self.assertEqual(status, 'success', msg='test pass')
        self.log.info('response {}'.format(response.text))

    # 同样获取单个项目，使用assignment方法做
    @file_data('../test_data/singleProjectInfo.yaml')
    def test_06(self, path, **kwargs):
        self.log.info('--------------------')
        self.log.info('test_06: test get single project info with assignment function')
        value=self.assignment(kwargs)
        self.log.info('value {}'.format(value))
        url_getSingleProjectInfo=self.url + path + value['data']['projectId']
        self.log.info('访问URL{}'.format(url_getSingleProjectInfo))
        response=self.ak.do_get(url=url_getSingleProjectInfo, headers=value['headers'])
        status=self.ak.get_text(response.text, 'status')
        self.log.info('返回status {}'.format(status))
        self.assertEqual(status, 'success', msg='test pass')
        self.log.info('response {}'.format(response.text))

if __name__ == '__main__':
    # unittest.main()

    current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    print(current_time)
    testunit = unittest.makeSuite(TestCase)
    # testunit.addTest('test_01')
    report_path = '../test_report/'
    report_name = report_path+'result_'+current_time+'.html'
    print('%s' %report_name)
    fp = open(report_name,'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='unittest report for'+report_name,description='description')
    runner.run(testunit)
    fp.close()

