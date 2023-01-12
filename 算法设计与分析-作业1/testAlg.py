"""
算法设计与分析
作业-1
小组：刘易行 李欢欢
testAlg.py
最终测试文件
"""

import generator
import alg
import time
import matplotlib.pyplot as plt

testList = [5, 10, 15, 100, 500, 1000, 2000, 3000, 4000, 5000]  # 测试样本数量


def Alg(func):
    timeList = []
    for num in testList:
        array_origin, array_toSort, array_ans = generator.Generate_Data(num)
        print("本次排序数据集大小:{}".format(num))
        start = time.time()
        array_res = func(array_toSort)
        end = time.time()
        if array_res == array_ans:
            print("排序结果正确")
            print("耗时：{}".format(end - start))
        else:
            print("排序结果有误")
        if num < 50:
            print("原始数据:{}".format(array_origin))
            print("排序后的数据:{}".format(array_res))
        print("----------------------------------------------------------")
        timeList.append(end - start)
    plt.figure()
    plt.plot(testList, timeList, 'r')
    plt.title("Sort Algorithm Time Map")
    plt.xlabel("DataSize")
    plt.ylabel("SortTime")
    plt.show()

print("各种排序算法的Python实现及测试")

print("选择排序")
Alg(alg.Selection_Sort)

print("冒泡排序")
Alg(alg.Bubble_Sort)

print("插入排序")
Alg(alg.Insertion_Sort)

print("快速排序")
Alg(alg.Quick_Sort)

print("堆排序")
Alg(alg.Heap_Sort)

print("归并排序")
Alg(alg.Merge_Sort)