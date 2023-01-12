# 计算智能导论实验二 第二题
# 2020240401-2020905896-刘易行

# 遗传算法求解函数最大值
# f(x) = x + 10sin(5x)+7sin(4x)
# 0 <= x <= 10

import random
import numpy as np
import matplotlib.pyplot as plt

#定义遗传算法的参数
popSize=50  #种群规模
epoches = 100 # 遗传代数
DNAlength = 20  #染色体编码长度
pjc = 0.8  # 交叉概率
pby = 0.1 # 变异概率
targetFunc = lambda x:x+10*np.sin(5*x) + 7*np.sin(4*x)
min_x = 0 # 定义域下限
max_x = 10 # 定义域上限

# matplotlib绘图参数
plt.rcParams['font.sans-serif'] = ['FangSong']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 支持特殊符号

def getChromosome(size,length):
    # 生成 size个长度为length 的染色体 返回一个二维nparray
    temp = []
    for i in range(size):
        # 生成长度为length的随机二进制列表，并存放到temp列表中
        temp.append([random.randint(0,1) for _ in range(length)])
    return temp

def getAccuracy(minV,maxV,length):
    # 计算搜索精度
    return (maxV-minV) / (2**length - 1) # 套用精度计算公式

def ChromosomeDecode(DNAList,minV,accuracy):
    # 染色体解码函数
    decimal = int(''.join([str(i) for i in DNAList]),2) # 二进制列表转为十进制整型
    return minV + accuracy * decimal

def getFitness(x):
    return targetFunc(x)  # 计算适应度 适应度函数即为目标函数 此处计算最大值问题 不用额外操作

def select(chromosome_list, fitness_list):
    """
    选择(轮盘赌算法)
    :param chromosome_list: 二维列表的种群
    :param fitness_list: 适应度列表
    :return: 选择之后的种群列表
    """
    population_fitness = np.array(fitness_list).sum()  # 种群适应度
    fit_ratio = [i / population_fitness for i in fitness_list]  # 每个个体占种群适应度的比例
    fit_ratio_add = [0]  # 个体累计概率
    for i in fit_ratio:
        fit_ratio_add.append(fit_ratio_add[len(fit_ratio_add) - 1] + i)     # 计算每个个体的累计概率，并存放到fit_ratio_add中
    fit_ratio_add = fit_ratio_add[1:]   # 去掉首位的0

    rand_list = [random.uniform(0, 1) for _ in chromosome_list]     # 生成和种群规模相等的随机值列表，用于轮盘赌选择个体
    rand_list.sort()
    fit_index = 0
    new_index = 0
    new_population = chromosome_list.copy()

    # 开始个体选择
    while new_index < len(chromosome_list):
        if rand_list[new_index] < fit_ratio_add[fit_index]:
            new_population[new_index] = chromosome_list[fit_index]
            new_index = new_index + 1
        else:
            fit_index = fit_index + 1
    # 结束个体选择
    return new_population


def exchange(chromosome_list, pc):
    """
    交叉
    :param chromosome_list: 二维列表的种群
    :param pc: 交叉概率
    """
    for i in range(0, len(chromosome_list) - 1, 2):
        if random.uniform(0, 1) < pc:
            c_point = random.randint(0, len(chromosome_list[0]))    # 随机生成交叉点
            '''对第i位和i+1位进行交叉 start'''
            exchanged_list1 = []
            exchanged_list2 = []
            exchanged_list1.extend(chromosome_list[i][0:c_point])
            exchanged_list1.extend(chromosome_list[i + 1][c_point:len(chromosome_list[i])])
            exchanged_list2.extend(chromosome_list[i + 1][0:c_point])
            exchanged_list2.extend(chromosome_list[i][c_point:len(chromosome_list[i])])
            '''对第i位和i+1位进行交叉 end'''

            '''将新交叉后的染色体替换原染色体 start'''
            chromosome_list[i] = exchanged_list1
            chromosome_list[i + 1] = exchanged_list2
            '''将新交叉后的染色体替换原染色体 end'''

def mutation(chromosome_list, pm):
    # 变异
    for i in range(len(chromosome_list)):
        if random.uniform(0, 1) < pm:
            m_point = random.randint(0, len(chromosome_list[0]) - 1)    # 随机生成变异点
            chromosome_list[i][m_point] = chromosome_list[i][m_point] ^ 1


def getBest(fitness_list):
    # 求当前种群中的最优个体
    return fitness_list.index(max(fitness_list))

def eliminate(fitness_list):
    # 淘汰个体（去除负值） 因为是求最大值问题
    fit_value = []
    for i in range(len(fitness_list)):
        fit_value.append(fitness_list[i] if fitness_list[i] >= 0 else 0.0)   # 将小于0的适应度置为0
    return fit_value


if __name__ == '__main__':
    # 主函数运行
    genResults = []  #暂存每一代的最优解
    Fitness = [] #存放每一代中的最高适应度
    pop = getChromosome(popSize,DNAlength) # 种群初始化
    for _ in range(epoches):
        accuracy = getAccuracy(min_x,max_x,DNAlength) # 计算搜索精度
        decodeList = [ChromosomeDecode(individual,min_x,accuracy) for individual in pop] # 解码之后的列表
        fitList = [getFitness(decode_i) for decode_i in decodeList] #  计算每个个体的适应度
        fitList = eliminate(fitList) # 淘汰 去除负值
        genResults.append([decodeList[getBest(fitList)],
                           fitList[getBest(fitList)]]) # 保存每一代最优解，即适应度最高的个体
        Fitness.append(np.array(fitList).sum())  # 保存每一代中的最高适应度和种群适应度
        pop = select(pop.copy(), fitList)
        exchange(pop, pjc) # 交叉
        mutation(pop, pby) # 变异

    genResults.sort(key = lambda x:x[1])
    print('最大值点 x={},y={}'.format(genResults[-1][0], genResults[-1][1]))

    X = [generation_i for generation_i in range(epoches)]
    Y1 = [genResults[generation_i][1] for generation_i in range(epoches)]
    Y2 = [Fitness[generation_i] for generation_i in range(epoches)]

    fig1 = plt.figure('figure', figsize=(13, 5)).add_subplot(121)
    fig1.plot(X, Y1)
    fig2 = plt.figure('figure', figsize=(13, 5)).add_subplot(122)
    fig2.plot(X, Y2)

    fig1.set_title('极值点趋势图')
    fig1.set_xlabel("遗传代数")
    fig1.set_ylabel("极值")
    fig2.set_title('种群整体适应度趋势图')
    fig2.set_xlabel("遗传代数")
    fig2.set_ylabel("种群适应度")

    plt.show()