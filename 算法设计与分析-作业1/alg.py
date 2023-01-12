"""
算法设计与分析
作业-1
小组：刘易行 李欢欢
alg.py
撰写了六类排序代码
"""

import numpy as np
import math


# 冒泡排序
def Bubble_Sort(inArr):
    """冒泡排序"""
    # 比较相邻的元素。如果第一个比第二个大，就交换他们两个
    for i in range(1, len(inArr)):
        for j in range(0, len(inArr) - i):
            if inArr[j] > inArr[j + 1]:
                temp = inArr[j]
                inArr[j] = inArr[j + 1]
                inArr[j + 1] = temp
    return inArr


# 选择排序
def Selection_Sort(inArr):
    """选择排序-核心思想-每一趟找出最小数，并记录其索引"""
    for i in range(len(inArr) - 1):
        # 找到并记录最小的数值的索引
        Index_Min = i
        for j in range(i + 1, len(inArr)):
            if inArr[j] < inArr[Index_Min]:
                # 如果当前数值比之前记录的值更小的话，更新Index_Min
                Index_Min = j
        # 将i位置元素置为当前剩余序列中的最小元素
        if i != Index_Min:
            temp = inArr[i]
            inArr[i] = inArr[Index_Min]
            inArr[Index_Min] = temp
    return inArr


# 插入排序
def Insertion_Sort(inArr):
    """插入排序"""
    # 将第一待排序序列第一个元素看做一个有序序列，把第二个元素到最后一个元素当成是未排序序列
    for i in range(len(inArr)):
        preIndex = i - 1
        current = inArr[i]
        while preIndex >= 0 and inArr[preIndex] > current:
            inArr[preIndex + 1] = inArr[preIndex]
            preIndex -= 1
        inArr[preIndex + 1] = current
    return inArr


# 快速排序
def swap(array, i, j):
    """交换"""
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def Partition(array, left, right):
    """实现划分操作"""
    pivot = left  # 基准值
    index = pivot + 1
    i = index
    while i <= right:
        if array[i] < array[pivot]:
            swap(array, i, index)
            index += 1
        i += 1
    swap(array, pivot, index - 1)
    return index - 1


def Quick_Sort(array, left=None, right=None):
    """快速排序算法的最终实现，递归实现"""
    # 初始化left、right isinstance方法主要是针对None情况
    left = 0 if not isinstance(left, int) else left
    right = len(array) - 1 if not isinstance(right, int) else right
    if left < right:
        PartitionIndex = Partition(array, left, right)  # 划分
        Quick_Sort(array, left, PartitionIndex - 1)
        Quick_Sort(array, PartitionIndex + 1, right)
    return array


# 堆排序
def heapify(array, i):
    "堆调整算法"
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < arrayLen and array[left] > array[largest]:
        largest = left
    if right < arrayLen and array[right] > array[largest]:
        largest = right
    if largest != i:
        swap(array, i, largest)
        heapify(array, largest)


def buildMaxHeap(array):
    """构造大根堆"""
    # math.floor相当于向下取整
    for i in range(math.floor(len(array) / 2), -1, -1):
        heapify(array, i)


def Heap_Sort(array):
    global arrayLen
    arrayLen = len(array)
    buildMaxHeap(array)
    for i in range(len(array) - 1, 0, -1):
        swap(array, 0, i)
        arrayLen -= 1
        heapify(array, 0)
    return array


# 归并排序
def merge(left, right):
    """归并操作"""
    result = []
    while left and right:  # 当两个子集都有元素时，比较它们顶部的两个元素
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def Merge_Sort(array):
    """归并排序"""
    if len(array) < 2:
        return array
    middle = math.floor(len(array) / 2)
    # 分解区间
    leftArray = array[0:middle]
    rightArray = array[middle:]
    return merge(Merge_Sort(leftArray), Merge_Sort(rightArray))  # 递归
