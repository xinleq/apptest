# 在这个py文件我们希望放置一些可以专门服务于 action 层的通用代码。

# 形参在定义的时候是没有值的，它在我们调用的时候是会有具体值
# 我们当前写 BaseAction 类是为了服务于 action


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    # 1 自定义一个获取元素的方法
    def syy_get_element(self, feature):
        """
        调用该函数的时候 用户可以传入一个具体的元素特征，然后我们就可以依据这个特征返回最终定位到的元素
        :feature: 是一个元组类型，它里面包含了想要被获取元素的特征信息
        例如：skip_feature = (By.ID, "com.netease.newsreader.activity:id/qq")
        :return:
        """
        by = feature[0]
        val = feature[1]
        # 因为我们自已花力气定义了一个叫 install_xpath 的工具方法，而这个方法对于 id class 查找
        # 元素是没用的，所以我们需要在 get_element 方法内部去判断一下当前用户是否在按着 xpath找元
        # 素
        # print(by, type(by))
        if by == "xpath":
            # 当我们发现用户是在用 xpath 规则选取元素的时候，我们就直接将对应的 xpath 值传给 isntall_xpath
            val = self.install_xpath(val)
        return self.driver.find_element(by, val)

    # 2 自定义一个 点击 函数，可以专门用于帮助我们找到某个元素，然后对它进行点击
    def syy_click(self, ele_feature1):
        """
        希望使用者调用该函数的时候可以帮助我们找到某一个元素，然后点击它。
        :return:
        """
        # 找到别人，然后点击别人
        self.syy_get_element(ele_feature1).click()

    # 3 自定义一个专门用于输入值的函数
    def syy_input_value(self, ele_feature2, value):
        """
        当使用者调用访函数的时候传入 具体元素的特征，和想要写入的 value 值 ，这个函数就可以找到这个元素，然后往这个元素的身上写入value值
        :param ele_feature: 元组类型，包含二个值，一个是By.*** ,一个是具体的属性值
        :param value: python 里的简单数据类型，是我们最终想要写入元素的具体值
        :return:None
        """
        # 1 下面这句话就是帮我们找到 账号框 ，然后输入了一个邮箱值
        self.syy_get_element(ele_feature2).send_keys(value)

    # 4 自定义一个专门用于组装 xpath 路径的工具函数
    def install_xpath(self, path):
        """
        希望使用者在调用这个函数的时候，可以接收使用者传入一个 值，然后这个函数内部就会对这个值进行处理，最终返回我们想要的 xpath 路径
        :return:
        """

        # 在当前函数的作用域内定义需要使用的变量
        res_path = ""

        if isinstance(path, str):
            # ***** 为了兼容原始正常写法，我们拿到一个用户传入的字符串之后并不会直接对其进行 split 拆分
            # 我们可以判断一下当前的字符是否以  //*[ 开头，如果是我们就认为用户给到的是一个传统写法
            if path.startswith("//*["):
                return path

            # 如果我们发现用户传进来的是一个字符串，那么我们就可以使用 "," 进行拆分，拆完之后得到的必然是一个列表
            # 此时我们就可以依据这个列表的长度来判断用户当前希望采用的是何种查找方式
            tmp_list1 = path.split(",")

            if len(tmp_list1) == 2:
                res_path = "contains(@%s, '%s')" % (tmp_list1[0], tmp_list1[1])

            elif len(tmp_list1) == 3:
                res_path = "@%s='%s'" % (tmp_list1[0], tmp_list1[1])

        elif isinstance(path, tuple):
            for item in path:
                # 1 如果我们发现 item 又是字符串类型，那么我们就可以直接对它进行 split
                tmp_list2 = item.split(",")

                # 2 当我们将字符串进一步拆成列表之后，我们还需要依据长度对其进行判断如果是3....
                if len(tmp_list2) == 2:
                    res_path += "contains(@%s, '%s') and " % (tmp_list2[0], tmp_list2[1])
                elif len(tmp_list2) == 3:
                    res_path += "@%s='%s' and " % (tmp_list2[0], tmp_list2[1])

            last_and = res_path.rfind(" and ")
            res_path = res_path[0: last_and]


        else:
            print("请按规则使用")

        return "//*[" + res_path + "]"

    # 5 自定义一个专门用于执行从右向左滑动的工具函数
    def syy_swipe_left(self, start_per_x, start_per_y, end_per_x, end_per_y):

        start_x = self.driver.get_window_size()["width"]*start_per_x
        start_y = self.driver.get_window_size()["height"]*start_per_y
        end_x = self.driver.get_window_size()["width"]*end_per_x
        end_y = self.driver.get_window_size()["height"]*end_per_y

        self.driver.swipe(start_x, start_y, end_x, end_y)


