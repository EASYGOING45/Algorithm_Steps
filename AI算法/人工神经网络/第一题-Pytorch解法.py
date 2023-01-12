import torch.nn as nn
import numpy as np
import torch.nn.functional as Fun
import torch
from torchviz import make_dot
from torch.utils.data import DataLoader
from torch.utils.data import TensorDataset
import matplotlib.pyplot as plt

# 数据准备
data_x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
data_y = np.sin(data_x)   # 套用正弦函数

# print(data_x)

XSet = np.expand_dims(data_x, axis=1)
YSet = data_y.reshape(400, -1)

dataset = TensorDataset(torch.tensor(XSet, dtype=torch.float), torch.tensor(YSet, dtype=torch.float))
dataloader = DataLoader(dataset, batch_size=100, shuffle=True)


def awgn(x, snr, seed=7):
    '''
    加入高斯白噪声 Additive White Gaussian Noise
    :param x: 原始信号
    :param snr: 信噪比
    :return: 加入噪声后的信号
    '''
    np.random.seed(seed)  # 设置随机种子
    snr = 10 ** (snr / 10.0)
    xpower = np.sum(x ** 2) / len(x)
    npower = xpower / snr
    noise = np.random.randn(len(x)) * np.sqrt(npower)
    return x + noise


# 定义BP神经网络结构类
class BPNet(nn.Module):
    def __init__(self, n_features, n_hidden, n_output):
        super(BPNet, self).__init__()
        self.hidden = nn.Linear(n_features, n_hidden)
        self.out = nn.Linear(n_hidden, n_output)

    # BP前向传播过程
    def forward(self, x):
        x = torch.sigmoid(self.hidden(x))
        x = self.out(x)
        return x


# 实例化网络模型
model1 = BPNet(n_features=1, n_hidden=100, n_output=1)
# 配置优化器
optimizer = torch.optim.Adam(model1.parameters(), lr=0.01)
# 配置损失函数
loss_func = nn.MSELoss()

# 训练网络模型
# 下面开始训练：
# 一共训练 1000次
for epoch in range(1000):
    loss = None
    for batch_x, batch_y in dataloader:
        y_predict = model1(batch_x)
        loss = loss_func(y_predict, batch_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    # 每100次 的时候打印一次日志
    if (epoch + 1) % 100 == 0:
        print("step: {0} , loss: {1}".format(epoch + 1, loss.item()))

# 明确optimizer优化器的作用, 形象地来说，优化器就是需要根据网络反向传播的梯度信息来更新网络的参数，以起到降低loss函数计算值的作用

# 使用训练好的模型进行预测
predict = model1(torch.tensor(XSet, dtype=torch.float))

# 绘图展示预测的和真实数据之间的差异

data_x_noise = awgn(data_x, 35)
data_y_noise = np.sin(data_x_noise)

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.plot(data_x, data_y, label="实际值")
plt.plot(data_x, predict.detach().numpy(), label="预测值")
#plt.plot(data_x,data_y_noise,label='白噪声信号')
plt.title("BP神经网络拟合正弦函数")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
# plt.savefig(fname="result.png",figsize=[10,10])
plt.show()

# x = torch.randn(1, 1, 50, 1).requires_grad_(True)
# y = model1(x)
# MyConvnetis = make_dot(y, params=dict(list(model1.named_parameters()) + [('x', x)]))
# MyConvnetis.format = "png"
# MyConvnetis.directory = r"C:\2.png"
# MyConvnetis.view()
