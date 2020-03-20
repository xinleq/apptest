# -*- coding=utf-8 -*-
# 导入python需要的 webdriver 库
import time

from appium import webdriver

# 定义一个空字典来存放具体的配置参数
desired_caps = dict()

# 书写具体的参数
desired_caps["platformName"] = "android"  # 当前的系统平台名称
desired_caps["platformVersion"] = "8.0.0"  # 当前连接设备的 android 版本
desired_caps["deviceName"] = "WTKDU16928010269" # 当前已连接设备的名称
desired_caps["appPackage"] = "com.android.haitong"  # 被测试 APP 的包名
desired_caps["appActivity"] = "cn.htsec.SecurityHome t922" # 被测试 APP 的启动名


# 获取对应的连接
driver  = webdriver.Remote( "http://localhost:4723/wd/hub",desired_caps )
driver.find_element_by_id("com.android.haitong:id/dlg_tv_agree").click()
time.sleep(1)

driver.find_element_by_xpath("//*[contains(@text,'始终允许')]").click()
driver.find_element_by_xpath("//*[contains(@text,'始终允许')]").click()