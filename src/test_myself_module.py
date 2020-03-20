# -*- coding=utf-8 -*-
"""
    需求：进入登录注册界面

        1 进入到主界面
        2 在主界上点击 我的 按钮
        3 点击 登录/注册按钮
"""
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.initDriver import init_driver
from action.action import Action
from base.get_data import analysis_yml

class TestMyself:

    def setup(self):
        self.driver = init_driver()
        self.action = Action(self.driver)

    @pytest.mark.parametrize("user_info", analysis_yml("myself", "login_reg"))
    def test_login_reg(self, user_info):
        # user_info = {"num":123456, "pwd":"abcdef"}
        # 进入主界面
        self.action.init_home_action.enter_home()

        # 防止首页加载过慢
        time.sleep(2)

        # 点击我的
        self.action.init_home_action.click_myself()

        # 点击登录/注册
        self.action.init_myself_action.click_login_reg()

        time.sleep(2)

        # 输入账号
        self.action.init_myself_action.input_num(user_info["num"])

        # 输入密码
        self.action.init_myself_action.input_pwd(user_info["pwd"])

        # 点击登录
        self.action.init_myself_action.click_enter()

        # # 添加断言
        wait = WebDriverWait(self.driver, 5, 0.1)
        ele = wait.until(lambda x: x.find_element(By.XPATH, "//*[contains(@text,'账号不')]"))

        if ele.text == "账号不存在!":
            assert True
        else:
            assert False

