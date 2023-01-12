# 计算智能导论实验二 第二题
# 2020240401-2020905896-刘易行

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sko.GA import GA

# matplotlib绘图参数
plt.rcParams['font.sans-serif'] = ['FangSong']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 支持特殊符号

def f(x):
    # 目标函数  求最小值问题
    return 20 + np.sum(np.power(x, 2))

# 调用Scikit-OPT中的GA算法 实例化
ga = GA(func=f, n_dim=10, size_pop=50, max_iter=100, lb=[-20]*10, ub=[20]*10,precision=1e-9,prob_mut = 0.01)
best_x, best_y = ga.run()
print('最优解对应的x:{}'.format(best_x))
print("最小值为:{}".format(best_y))

# 绘制图线 查看结果
Y_history = pd.DataFrame(ga.all_history_Y)
fig, ax = plt.subplots(2, 1)
ax[0].plot(Y_history.index, Y_history.values, '.', color='red')
Y_history.min(axis=1).cummin().plot(kind='line')
plt.title('遗传算法')
plt.show()