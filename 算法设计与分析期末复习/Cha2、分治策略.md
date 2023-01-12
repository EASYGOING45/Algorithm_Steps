# Cha2、分治策略

## 最常见的两类分治算法：二分检索、二分（路）归并排序

![image-20220601194202460](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220601194202460.png)

```python
# 二分检索算法 应用到了分治的思想
# 返回 x 在 arr 中的索引，如果不存在返回 -1
def binarySearch (arr, l, r, x): 
    # 基本判断
    if r >= l: 
        mid = int(l + (r - l)/2)
        # 元素刚好在中间位置
        if arr[mid] == x: 
            return mid 
        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        # 元素大于中间位置的元素，只需要再比较右边的元素
        else: 
            return binarySearch(arr, mid+1, r, x) 
    else: 
        # 不存在
        return -1
```

![image-20220601201456099](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220601201456099.png)

```python
#二路归并排序 运用到了分治思想
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
```

## 分治算法核心思想：划分 求解子问题 合并	

​	分治策略：

- 将原始问题划分或者归结为规模较小的子问题
- 迭代或递归求解每个子问题
- 将子问题的解综合能够得到原始问题的解
- 通过递归或者迭代进行实现

​	注意点：

- 子问题与原始问题的性质必须完全一样
- 子问题之间可以彼此独立地求解
- 递归停止时子问题可直接求解

## 分治算法的描述

![image-20220601201538028](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220601201538028.png)

![image-20220601201806684](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220601201806684.png)

## 芯片测试

![image-20220601195558924](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220601195558924.png)

![image-20220601195608404](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220601195608404.png)

![image-20220601201843558](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220601201843558.png)

![image-20220601201900286](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220601201900286.png)

## 如何改进分治算法？

​	从分治算法的特征下手

- 可以通过减少子问题数
- 增加预处理