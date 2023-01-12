"""
生成各个题目所需要的测试数据
"""
import numpy
## 生成数据
def MakeData_53(x):
    array_test = numpy.random.randint(-100,100,x).tolist()
    return array_test