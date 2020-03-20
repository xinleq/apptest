# -*- coding=utf-8 -*-

"""
    需求: 进入主界面动作实现
    步骤：
        1 加载数据
        2 滑屏跳过引导页
        3 点击进入按钮
"""
import time
from selenium.webdriver.common.by import By
from base.baseAction import BaseAction


class HomePageAction(BaseAction):

    # 获取当前到动作层需要用到的所有元素
    enter_btn_feature = By.ID, "com.tpshop.malls:id/start_Button"
    myself_btn_feature = By.XPATH, ("resource-id,com.tpshop.malls:id/tab_txtv,1", "text,我的,1")

    # 1 定义一个进入主界面的动作
    def enter_home(self):

        time.sleep(3)

        try:
            self.syy_get_element(self.myself_btn_feature)
            print("欢迎进入主界面")
        except:

            for i in range(3):
                self.syy_swipe_left(0.8, 0.5, 0.1, 0.5)
                time.sleep(0.5)

            self.syy_click(self.enter_btn_feature)

    # 2 定义一个点击 我的 的动作
    def click_myself(self):
        self.syy_click(self.myself_btn_feature)



