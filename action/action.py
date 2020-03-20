# -*- coding=utf-8 -*-
from action.action_home import HomePageAction
from action.action_myself import MyselfPageAction


class Action:

    def __init__(self, driver):
        self.driver = driver

    @property
    def init_home_action(self):
        return HomePageAction(self.driver)

    @property
    def init_myself_action(self):
        return MyselfPageAction(self.driver)

