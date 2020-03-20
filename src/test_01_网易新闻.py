# -*- coding=utf-8 -*-
import time

import pytest
from appium import webdriver


class TestDemo:

    # 1 连接手机
    def setup(self):
        desired_caps = dict()

        desired_caps["platformName"] = "android"  # 指定当前的测试平台
        desired_caps["platformVersion"] = "5"  # 指定当前平台的版本
        desired_caps["deviceName"] = "*****"  # 指定当前的被测试机的机器码( 如果测试安卓可以不 )
        desired_caps["appPackage"] = "com.netease.newsreader.activity"  # 指定当前脚本想要没试的APP 包名
        desired_caps["appActivity"] = "com.netease.nr.biz.ad.AdActivity"
        desired_caps["unicodeKeyboard"] = True  # 允许手机接收 unicode 码
        desired_caps["resetKeyboard"] = True  # 重置手机的键盘输入
        desired_caps["noReset"] = True  # 不希望每次进入APP时都是第一次

        # 将上述的准备好的配置信息 通过 http 协议的方式发送给 appium
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    @pytest.mark.skip()
    def test_delete(self):
        # 强制等待跳过加载界面
        time.sleep(2)

        # 使用脚本点击跳过，进入到主界面
        self.driver.find_element_by_id("com.netease.newsreader.activity:id/qq").click()

        # 选择一个 删除 按钮进行点击
        self.driver.find_element_by_id("com.netease.newsreader.activity:id/i9").click()

        # 选择  不想看 进行点击
        self.driver.find_element_by_xpath("//*[@text='不想看']").click()

    def test_login(self):

        # 强制等待跳过加载界面
        time.sleep(2)

        # 使用脚本点击跳过，进入到主界面
        self.driver.find_element_by_id("com.netease.newsreader.activity:id/qq").click()

        # 点击 “我” 按钮
        self.driver.find_element_by_xpath("//*[@text='我' and @resource-id='com.netease.newsreader.activity:id/zp' ]").click()

        # 进入到 “我” 这个界面之后，接下来就点击登录按钮。 [此时我们就进入了登录表单信息收集页]
        self.driver.find_element_by_id("com.netease.newsreader.activity:id/a7a").click()

        # 接下来我们就可以依次的输入 邮箱 + 密码 + 点击登录
        self.driver.find_element_by_id("com.netease.newsreader.activity:id/ph").send_keys("123@126.com")
        self.driver.find_element_by_id("com.netease.newsreader.activity:id/ph").click()
        # time.sleep(2)
        self.driver.find_element_by_id("com.netease.newsreader.activity:id/pn").send_keys("1234")
        self.driver.find_element_by_id("com.netease.newsreader.activity:id/pp").click()


