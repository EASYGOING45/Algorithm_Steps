from turtle import left, right
from numpy import partition

from sympy import Ellipse


def InsertSort(data):          #插入排序
    for i in range(len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and temp < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = temp

def bubbleSort(arr):            #冒泡排序
    n = len(arr)
    # 遍历所有数组元素
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quick_sort(list, low = None, high = None):  #快速排序
    low=0 if not isinstance(low,int) else low
    high=len (list)-1 if not isinstance(high,int) else high 
    if low <high :
        PartitionIndex = partition (list ,low ,high )
        quick_sort(list ,low ,PartitionIndex - 1)
        quick_sort(list ,PartitionIndex + 1,high)
        return list 
