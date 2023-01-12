from numpy import random

class Generator:
    def __init__(self, length):  # length = 需要生成的数据规模
        self.length = length  # 数据的规模
        self.base = list(range(1, length + 1))  # 生成数据的范围1~length
        self.groundtruth = self.base.copy()  # 数据的正确排序
        random.seed()
        random.shuffle(self.base)


def make_data(length):
    length = length  # 数据的规模
    base = list(range(1, length + 1))  # 生成数据的范围1~length
    groundtruth = base.copy()  # 数据的正确排序
    random.seed()
    random.shuffle(base)
    return base, groundtruth
