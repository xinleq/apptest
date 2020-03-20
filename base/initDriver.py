# -*- coding=utf-8 -*-
from appium import webdriver


def init_driver():

    """
    当前函数的作用就是在被调用的时候可以直接返回一个 driver 驱动对象
    :return: driver
    """
    desired_caps = dict()
    desired_caps["platformName"] = "android"  # 指定当前的测试平台
    desired_caps["platformVersion"] = "8"  # 指定当前平台的版本
    desired_caps["deviceName"] = "*****"  # 指定当前的被测试机的机器码( 如果测试安卓可以不 )
    desired_caps["appPackage"] = "com.android.haitong"  # 指定当前脚本想要没试的APP 包名
    desired_caps["appActivity"] = "cn.htsec.SecurityHome t922"
    desired_caps["unicodeKeyboard"] = True  # 允许手机接收 unicode 码
    desired_caps["resetKeyboard"] = True  # 重置手机的键盘输入
    desired_caps["noReset"] = True  # 不希望每次进入APP时都是第一次
    desired_caps['automationName'] = 'Uiautomator2'  # 指定当前使用的测试框架为  uiautomator2
    # 将上述的准备好的配置信息 通过 http 协议的方式发送给 appium
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    return driver
