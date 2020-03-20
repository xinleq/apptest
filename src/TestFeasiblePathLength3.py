 #
 #
 # 此文件由龙测科技(1.0)自动产生。
 #
 #

from src.core.BaseTest import BaseTest
import unittest
from src.core.DT import DT as dt
import pytest
from src.field.Elements import Elements
import allure
from src.core.getImage import getImage
from src.utils.loggers import JFMlogging
import time
from parameterized import parameterized

class TestFeasiblePathLength3(unittest.TestCase, dt):
    elements = Elements()
    def setUp(self):
        self.driver=BaseTest.setUp(self)
        driver = self.driver; 
    def tearDown(self):
        self.driver.quit()
    @allure.story("流程2")
    @allure.feature("")
    @allure.description("")
    @getImage
    def testCase2(self): 
       # 1. 首页面 --- click ---> hangqing----->行情 
        #click -->hangqing
        self.click(self.elements.a_by, self.elements.a)
       # 2. 行情 --- click ---> shichang----->市场 
        #click -->shichang
        self.click(self.elements.b_by, self.elements.b)
       # 3. 市场 --- click ---> more----->更多 
        #click -->more
        self.click(self.elements.c_by, self.elements.c)
