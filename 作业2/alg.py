"""
算法的具体实现
"""
from typing import List

# 53-最大子数组和
# 53-最大子数组和 Divide and Conquer
def maxSubArray_DC(nums: List[int]) -> int:
    # 分治算法
    n = len(nums)  # 数组长度
    if n == 1:
        return nums[0]
    else:
        # 递归计算左半边的最大子数组和
        MaxSubLeft = maxSubArray_DC(nums[0:len(nums) // 2])
        # 递归计算右半边的最大子数组和
        MaxSubRight = maxSubArray_DC(nums[len(nums) // 2: len(nums)])

    # 计算中间的最大子数组和 从右至左计算左边的最大子数组和 从左至右计算右边的最大子数组和
    Max_Left = nums[len(nums) // 2 - 1]
    temp = 0
    for i in range(len(nums) // 2 - 1, -1, -1):
        temp += nums[i]
        Max_Left = max(temp, Max_Left)

    Max_Right = nums[len(nums) // 2]
    temp = 0
    for i in range(len(nums) // 2, len(nums)):
        temp += nums[i]
        Max_Right = max(temp, Max_Right)

    # 返回最终结果
    return max(MaxSubLeft, MaxSubRight, Max_Left + Max_Right)
