# -*- coding=utf-8 -*-
import yaml


def analysis_yml(file_name, fn_name):
    """
    该函数的主要作用就是负责找到指定的 yml 文件，然后将它里面的数据解析成 python 可以使用的数据
    :return: module 层中可用的数据
    """

    # 因为在 module 层当中使用到的数据类型必须是 列表的格式，所以我们在 analysis_yml 函数中提前将这些数据放置于列表中
    data_list = list()

    with open("../data/data_"+file_name +".yml", "r", encoding="utf8") as f:

        # data = {'test_fn1_1': {'gender': '男', 'hobby': '花钱'}, 'test_fn1_2': {'gender': '女', 'hobby': '学习'}}
        data = yaml.load(f)["test_"+fn_name]

        for key in data:
            data_list.append(data[key])

    return data_list


if __name__ == '__main__':
    print(analysis_yml("home","fn1"))




