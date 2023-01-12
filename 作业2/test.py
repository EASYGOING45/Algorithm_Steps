"""
测试各个算法
"""

import generator
import alg


def MaxSubArrayTest(func):
    testList = [1, 5, 10, 50]
    for i in range(len(testList)):
        array = generator.MakeData_53(testList[i])
        Sum = func(array)
        print("测试数组:{}".format(array))
        print("最大子数组和：", Sum)
        print("-----------------")


MaxSubArrayTest(alg.maxSubArray_DC)
