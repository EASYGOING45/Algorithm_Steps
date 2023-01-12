import copy

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl



#初始化种群
def ga_initpopulation(chromosome_length,pop_size):
    popx1=[]
    popx2=[]
    for k in range(2):
        for i in range(pop_size):
            arry_interim = []
            for j in range(chromosome_length):
                arry_interim.append(np.random.randint(0,2))
            if(k==1):
                popx1.append(arry_interim)
            else:
                popx2.append(arry_interim)
    pop = []
    for i in range(pop_size):
        temp=[]
        temp.append(popx1[i])
        temp.append(popx2[i])
        pop.append(temp)
    #print(pop)
    return pop


# 解码
def deCode(pop,lower_limit,upper_limit,pop_size,a,b,c):
    real_value=[]
    popx_list=[]
    for i in range(pop_size):
        temp1=0
        temp2=0
        tempx=[]
        for j,valuex1 in enumerate(pop[i][0]):
            temp1 += valuex1 * (2 ** j)
        for k,valuex2 in enumerate(pop[i][1]):
            temp2 += valuex2 * (2 ** k)
        x1 = lower_limit + temp1 * (upper_limit-lower_limit) / (2**26-1)
        x2 = lower_limit + temp2 * (upper_limit - lower_limit) / (2 ** 26 - 1)
        tempx.append(x1)
        tempx.append(x2)
        popx_list.append(tempx)
        sumtemp1 = np.exp(np.sqrt((x1**2+x2**2)/2)*-b)*a
        sumtemp2 = np.exp(((np.cos(c*x1))+(np.cos(c*x2)))/2)
        function = -sumtemp1-sumtemp2+a+np.exp(1)
        real_value.append(function)
    return popx_list,real_value


#计算出当代个体适应度并且找出适应度最高的个体
def calac_fit_value(pop,popx_list,real_value):
    fit_value = []
    fit_list = []
    fitmax_value = 0

    k=0
    for i in range(len(real_value)):
        fit_function = 30 - real_value[i]
        fit_list.append(fit_function)
        if(fit_function>fitmax_value):
            fitmax_value=fit_function
            k=i
    fit_value.append(pop[k])            #0当代最佳个体的二进制编码
    fit_value.append(popx_list[k])      #1当代最佳个体的十进制大小
    fit_value.append(real_value[k])     #2当代最佳个体带入目标函数的结果
    fit_value.append(fitmax_value)      #3当代最佳个体的适应度值
    return fit_list,fit_value

#计算累计概率
def cum_sum(fit_list):
    sum=0                            #当代累计适应度之和
    sumtemp=0
    pop_cum_sum=[]                   #当代累计概率数组  累计之和为1
    for i in range(len(fit_list)):  #求适应度之和
        sum+=fit_list[i]
    for i in range(len(fit_list)):  #使累计概率为1
        sumtemp+=fit_list[i]
        pop_cum_sum.append(sumtemp/sum)
    return pop_cum_sum

#轮盘赌选择法
def roulette_wheel_selection(pop,pop_cum_sum):
    pop_len = len(pop_cum_sum)
    #print(pop_len)
    pop_new = []                       #选择出新一代的个体，淘汰掉部分个体
    pop_random=[]
    for i in range(pop_len):           #随机选出该种群数量0-1的小数
        pop_random.append(np.random.random())
    for i in range(len(pop_random)):   #开始选择
        for j in range(pop_len):
            if(pop_cum_sum[j]>=pop_random[i]):
                pop_new.append(pop[j])
                break
    return pop_new

#交叉 单点交叉 其中pc为交叉概率
def crossover(pop_new, pc,chromosome_length):
    crossover_new_pop = []  #交叉后的新群体
    crossover_pop_size = 0
    while(len(crossover_new_pop)!=len(pop_new)):                                    #保证种群数量稳定
        parents = np.random.choice(np.arange(len(pop_new)), size=2, replace=False)  # 随机选出两个父代
        if(np.random.random()<pc):                                                  #随机数小于pc概率交叉
            parent1 = pop_new[parents[0]]
            parent2 = pop_new[parents[1]]
            temp_x1 = []                #x1基因
            temp_x2 = []                #x2基因
            temp_parent1 = []
            temp_parent2 = []
            crossover_x1 = np.random.randint(0,chromosome_length)                   #x1基因单点交叉点
            crossover_x2 = np.random.randint(0, chromosome_length)                  #x2基因单点交叉点
            temp_x1.extend(parent1[0][0:crossover_x1])
            temp_x1.extend(parent2[0][crossover_x1:chromosome_length])
            temp_x2.extend(parent1[0][0:crossover_x2])
            temp_x2.extend(parent2[0][crossover_x2:chromosome_length])
            temp_parent1.append(temp_x1)         #新的x1,x2基因组合成新的个体1
            temp_parent1.append(temp_x2)

            temp_x1 = []               # x1基因置空 为第二个个体准备
            temp_x2 = []               # x2基因置空 为第二个个体准备
            temp_x1.extend(parent2[0][0:crossover_x1])
            temp_x1.extend(parent1[0][crossover_x1:chromosome_length])
            temp_x2.extend(parent2[0][0:crossover_x2])
            temp_x2.extend(parent1[0][crossover_x2:chromosome_length])
            temp_parent2.append(temp_x1)        # 新的x1,x2基因组合成新的个体2
            temp_parent2.append(temp_x2)

            crossover_new_pop.append(temp_parent1)
            crossover_new_pop.append(temp_parent2)
    return crossover_new_pop

#变异 位翻转突变 其中pm为变异概率
def mutation(crossover_new_pop,pm,chromosome_length):
    mutation_new_pop = copy.deepcopy(crossover_new_pop)
    for i in range(len(mutation_new_pop)):
        if(np.random.random()<pm):           #x1基因突变
            k = np.random.randint(0,chromosome_length)
            if(mutation_new_pop[i][0][k]==0):
                mutation_new_pop[i][0][k]=1
            else:
                mutation_new_pop[i][0][k]=0
        if (np.random.random() < pm):       #x2基因突变
            k = np.random.randint(0, chromosome_length)
            if (mutation_new_pop[i][1][k] == 0):
                mutation_new_pop[i][1][k] = 1
            else:
                mutation_new_pop[i][1][k] = 0
    return mutation_new_pop


if __name__ == '__main__':
    lower_limit=-32.768
    upper_limit=32.768
    pop_size=100
    chromosome_length=26 #染色体长度
    a=20
    b=0.2
    c=2*np.pi
    pc = 0.6           #交叉概率
    pm = 0.01           #变异概率
    pop =  ga_initpopulation(chromosome_length,pop_size)
    value_list_y = []   #每代最优解数组
    iterations = 0      #迭代次数
    for i in range(1000):                #迭代1000次
        popx_list,real_value = deCode(pop,lower_limit,upper_limit,pop_size,a,b,c)
        fit_list,fit_value = calac_fit_value(pop,popx_list,real_value)
        print("x1=",fit_value[1][0],"x2=",fit_value[1][1],"y=",fit_value[2])
        best_value = fit_value[2]
        value_list_y.append(fit_value[2]) #每代最优解
        if(fit_value[2]<0.01):            #如果函数值小于0.001，则结束迭代
            iterations=i+1                #迭代次数
            break
        pop_cum_sum = cum_sum(fit_list)
        pop_new = roulette_wheel_selection(pop,pop_cum_sum)
        crossover_new_pop = crossover(pop_new,pc,chromosome_length)
        mutation_new_pop = mutation(crossover_new_pop,pm,chromosome_length)
        pop = mutation_new_pop


    mpl.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']  # 汉字字体,优先使用楷体，如果找不到楷体，则使用黑体
    mpl.rcParams['font.size'] = 12  # 字体大小
    plt.title('Ackley函数-迭代次数与优化值收敛图表')
    plt.plot(value_list_y,'b', linewidth = 1)
    plt.xlim(0,len(value_list_y))
    plt.xlabel("迭代次数")
    plt.ylabel("函数值")
    plt.axis()
    plt.show()