# 计算智能导论实验二-遗传算法的实现
# 第二题-求解10维函数最小值问题

import numpy as np
import matplotlib.pyplot as plt
import math
from pylab import mpl

# 中文显示问题，黑体
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
'''
遗传算法基本流程:
初始化种群
适应值评价，保存最优染色体
选择
交配
变异
重新评价适应值，更新最优染色体
满足终止条件则结束，否则继续选择过程
'''

# 计算初始串长度
def Compute_Length(x, prec):
    length = 0.
    value = (x[1] - x[0]) * pow(10, prec) + 1.0
    length = np.log2(value)
    return length


# 根据串长度创建初始种群
def Build_Init_Group(x_range, size, v_num):
    #创建初始种群
    init_popu = np.random.uniform(x_range[0], x_range[1], (size, v_num))
    return init_popu

# 适应度函数
def Fittness_function(x):
    f = 0
    for i in range(len(x)):
        f += x[i] * x[i]
    # 防止除数为0
    return 1. / (f + 0.1)


# 目标函数
def Desti_function(x):
    f = 20
    for i in range(len(x)):
        f += x[i] * x[i]
    return f


# 计算适应度
def Compute_Fitness(init_group):
    ref = np.array([])
    for i in range(init_group.shape[0]):
        ref = np.append(ref, Fittness_function(init_group[i]))
        # ref = np.append(ref, -1*Desti_function(init_group[i]))
    return ref

# 轮盘赌选择
def Roulette_Select(fitness_value, init_pop):
    '''
    计算总体适应度F
    计算选择概率p_select
    计算累积概率q_select
    生成相应数量的[0, 1]之间的随机数
    若q_k-1<r<=q_k, 则选vk
    将选择出来的结果作为新的种群返回
    :param fitness_value: 适应度值
    '''
    # 总体适应度
    F = sum(fitness_value)

    # 计算选择概率
    p_select = fitness_value.copy()
    for i in range(len(fitness_value)):
        p_select[i] = p_select[i] / F

    # 计算累积概率
    q_select = fitness_value.copy()
    for i in range(len(fitness_value)):
        q_select[i] = 0.

    for j in range(len(fitness_value)):
        for k in range(0, j + 1):
            q_select[j] += p_select[k]

    # 生成[0,1]之间的随机数
    np.random.seed()  # 产生不固定的随机数
    rand_num = np.random.uniform(0, 1, len(fitness_value))

    # 比较判别，若q_k-1<r<=q_k, 则选vk
    new_list = []
    for num in range(len(rand_num)):
        for num_ in range(len(q_select)):

            if num_ == 0:
                if (rand_num[num] <= q_select[num_]):
                    new_list.append(init_pop[num_])
            else:
                if (rand_num[num] > q_select[num_ - 1] and rand_num[num] <= q_select[num_]):
                    new_list.append(init_pop[num_])

    # 存放选择结果
    roulette_select_value = np.array(new_list)
    # 还需要将选择出来的二进制表示也选择出来,用于后续交叉和变异
    return roulette_select_value

def Cross_Able(select_pop, cross_prob):
    '''
    判断哪些染色体可以用于交叉操作，存到cross_np中，不可以的存到no_cross_np中
    :return:
    '''
    ran_select = np.random.random(select_pop.shape[0])
    cross_np = select_pop[np.where(ran_select < cross_prob), :]
    no_cross_np = select_pop[np.where(ran_select >= cross_prob), :]

    return cross_np[0, :, :], no_cross_np[0, :, :]


# 交叉运算
def Cross_Select(cross_np):
    '''
    首先判断是否满足交叉条件，即根据给定交叉概率，为每个染色体产生随机概率，与给定交叉概率比较
    符合条件的则进行交叉操作
    :param select_pop: 选择出来的结果
    :return:返回交叉后的结果
    '''

    for i in range(cross_np.shape[0] // 2):
        # 为交叉产生随机位置
        index = np.random.randint(0, cross_np.shape[1] - 1)
        # 交叉操作
        trans_array = np.array(cross_np[[i * 2, i * 2 + 1], index:])
        cross_np[[i * 2, i * 2 + 1], index:] = cross_np[[i * 2 + 1, i * 2], index:]
        cross_np[[i * 2 + 1, i * 2], index:] = trans_array[:]

    return cross_np


# 变异运算
def Mutations_Select(lamda, crossed_pop, x_range):
    '''
    传入变异概率参数lamda
    对每个染色体的每个基因随机生成[0, 1]的随机数
    若该随机数<lamda，则改变基因的值
    否则不改变基因的值
    '''

    # 为每个染色体的每个基因产生变异概率muta_pro
    ref_list = []
    muta_pop = crossed_pop.copy()

    for i in range(crossed_pop.shape[0]):
        ref_list.append(np.random.uniform(0, 1, crossed_pop.shape[1]))

    muta_pro = np.array(ref_list)

    # 判断是否满足变异条件，若是，则进行变异
    for i in range(len(crossed_pop)):
        for j in range(len(crossed_pop[i])):
            if muta_pro[i][j] < lamda:
                muta_pop[i][j] = np.random.uniform(x_range[0], x_range[1], 1)
    return muta_pop


'''
初始化种群:
首先根据x0和x1的区间范围，设置精度，确定串长度L
然后生成一系列长度为L的随机数，存到np中
'''

if __name__ == '__main__':
    # 变量区间
    x_range = [-20, 20]  # f1 f2 f3

    # 种群个数
    popusize = 50
    # 变量个数
    variable_num = 10
    # 迭代次数
    itera_times = 100
    # 交叉概率
    cross_prob = 0.8
    # 变异概率
    mut_prob = 0.1
    # 记录目前为止的最小值
    record_min = float("inf")

    # 用于记录当代的最大适应度，对应目标函数最优(最小)
    max_fitness = []
    # 用于记录代数、当前代的最优解、当前代的最优解值
    record = []
    # 用于记录当前代的最优解的值
    cur_genera_best_solu = []
    # 用于记录历史最优解的值
    min_dest_value = []

    # 开始GA过程

    # 创建初始种群
    np.random.seed(0)  # 随机数种子，产生固定随机数
    init_group = Build_Init_Group(x_range, popusize, variable_num)
    # 开始迭代
    for i in range(itera_times):

        # 计算适应度值
        fitness_value = Compute_Fitness(init_group)

        # 最大适应度值，即对应的最小目标函数值
        f_max = np.max(fitness_value)
        max_fitness.append(f_max)

        # 获取最优个体
        best_xy = init_group[np.argmax(fitness_value)]

        # 计算相应的目标值
        best_dest_value = Desti_function(best_xy)

        cur_genera_best_solu.append(best_dest_value)

        # 记录每一代的代数、最优解、最优解的值
        if i == 0:
            record_min = best_dest_value
            record = [i + 1, best_xy, record_min]
        if best_dest_value < record_min:
            record_min = best_dest_value
            record = [i + 1, best_xy, record_min]

        min_dest_value.append(record_min)

        # 轮盘赌选择
        select_pop = Roulette_Select(fitness_value, init_group)

        # 交叉  首先获取能进行交叉的染色体
        cross_np, no_cross_np = Cross_Able(select_pop, cross_prob)

        cross_pop = Cross_Select(cross_np)

        cross_result_pop = np.vstack((cross_pop, no_cross_np))

        # 变异
        init_group = Mutations_Select(mut_prob, cross_result_pop, x_range)

        '''
        需要记录：
        当前代数，当代的最优个体(x, y)，当代的目标函数值dest_value

        '''
    print("计算智能导论实验二-第二题")
    print('[迭代次数， 最优解， 最优解的值] = ', record)

    # 绘制收敛曲线
    plt.title('求解十维函数最小值')
    plt.plot(range(itera_times), cur_genera_best_solu, label='当前代最优解的值')
    plt.plot(range(itera_times), min_dest_value, label='目前为止的最优解的值')
    plt.legend()
    plt.scatter([record[0]], [record[2]], color='red')
    plt.text(record[0], record[2], (record[0], record[2]))
    plt.show()
