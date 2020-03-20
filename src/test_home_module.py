# -*- coding=utf-8 -*-
"""
    需求： 实现 home_module 当中的动作的调用 和需要使用动作的设计

    步骤：
        1 连接手机
        2 设计当前被测功能点需要用到的动作

"""
from base.initDriver import init_driver
from action.action_home import HomePageAction


class TestHome:

    # 连接手机
    def setup(self):
        self.driver = init_driver()
        self.home_action = HomePageAction(self.driver)

    # 设计被测功能点需要用到的动作
    def test_enter_home(self):
        # 调用 进入主界面 动作
        self.home_action.enter_home()

        # 点击 我的
        self.home_action.click_myself()


