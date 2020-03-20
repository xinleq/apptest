# -*- coding=utf-8 -*-
from selenium.webdriver.common.by import By
from base.baseAction import BaseAction


class MyselfPageAction(BaseAction):

    # 将 myself 动作层需要用到的元素提前获取
    num_feature = By.ID, "com.tpshop.malls:id/edit_phone_num"
    pwd_feature = By.ID, "com.tpshop.malls:id/edit_password"
    enter_feature = By.ID, "com.tpshop.malls:id/btn_login"

    # 准备好当前界面动作层需要用到的元素信息
    login_reg_feature = By.ID, "com.tpshop.malls:id/nickname_txtv"

    # 定义一个点击 登录/注册 按钮的动作
    def click_login_reg(self):
        self.syy_click(self.login_reg_feature)

    # 输入账号 动作
    def input_num(self, num_val):
        self.syy_input_value(self.num_feature, num_val)

    # 输入密码 动作
    def input_pwd(self, pwd_val):
        self.syy_input_value(self.pwd_feature, pwd_val)

    # 点击登录 动作
    def click_enter(self):
        self.syy_click(self.enter_feature)