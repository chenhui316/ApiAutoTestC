import configparser
import os
from pprint import pprint

import yaml


def get_project_path():
    """
    获取项目相对路径
    :return:F:\ApiAutoTest\zonghe
    """
    # 当前文件路径 F:\ApiAutoTest\zonghe\caw\DataRead.py
    file_path = os.path.realpath(__file__)
    # print(file_path)
    # 上一级目录 F:\ApiAutoTest\zonghe\caw
    dir_path = os.path.dirname(file_path)
    # print(dir_path)
    #再上一级目录  F:\ApiAutoTest\zonghe
    dir_path = os.path.dirname(dir_path)
    # print(dir_path)
    return dir_path + "\\"


def read_ini(file_path,key):
    """
    读取配置文件
    :param file_path: 配置文件路径
    :param key: 配置文件中的key，比如url
    :return: 返回key对应的value
    """
    config = configparser.ConfigParser()
    file_path = get_project_path()+file_path
    config.read(file_path)

    value = config.get("env",key)
    # print("..........", value)
    return value


def read_yaml(file_path):
    '''

    :param file_path:
    :return:
    '''
    file_path = get_project_path() + file_path
    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read()
        content = yaml.load(file_content, Loader=yaml.FullLoader)
        return content


if __name__ == '__main__':
    v = read_ini(r"\test_env\env.ini", "url")
    print(v)
    v = read_ini(r"\test_env\env.ini", "db_info")
    print(v)
    content = read_yaml(r"\test_data\register_fail.yaml")
    pprint(content)