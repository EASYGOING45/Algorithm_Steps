"""
算法设计与分析
作业-1
小组：刘易行 李欢欢
generator.py
用于生成测试数据集
统一生成格式为list
"""

import numpy as np


def Generate_Data(x):
    """生成长度为x的随机测试数据，统一类型为list"""
    # 生成x个数据
    array_origin = np.random.randint(0, 10000, x).tolist()
    array_test = array_origin.copy()
    array_ans = sorted(array_origin)
    return array_origin, array_test, array_ans
