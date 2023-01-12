import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler  # 用于数据归一化

def sigmoid(z):
    return  1/(1+np.exp(-z))

def sigmoid_delta(z): #sigmoid的偏导数
    return 1/((1+np.exp(-z))**2)*np.exp(-z)

#读取数据
data = pd.read_csv('TrafficData.csv', encoding='utf-8')
x = data[['人数', '机动车数', '公路面积']]
y = data[['公路客运量', '公路货运量']]

# 数据归一化处理
x_scaler = MinMaxScaler(feature_range=(-1, 1))
y_scaler = MinMaxScaler(feature_range=(-1, 1))

x = x_scaler.fit_transform(x)
y = y_scaler.fit_transform(y)

# 转置
sample_in=x.T
sample_out=y.T

#BP神经网络网络参数
max_epochs=50000 #最大循环迭代次数
learn_rate=0.02  #学习率
mse_final=7.5e-4  #设置一个均方误差（MSE）的阈值，小于它则停止迭代
sample_number=x.shape[0]  #样本规模
input_number=x.shape[1]  #输入规模
output_number=y.shape[1]  #输出规模
hidden_units=8 #隐含层（Hidden Layer）神经元个数

print(sample_number,input_number,output_number)

#一层隐含层
#W1矩阵:M行N列，M等于该层神经元个数，N等于输入特征个数
W1=0.5*np.random.rand(hidden_units,input_number)-0.1
b1=0.5*np.random.rand(hidden_units,1)-0.1

W2=0.5*np.random.rand(output_number,hidden_units)-0.1
b2=0.5*np.random.rand(output_number,1)-0.1

mse_history=[]  #空列表，存储迭代的误差

for i in range(max_epochs):
    #训练
    hidden_out=sigmoid(np.dot(W1,sample_in)+b1)  #np.dot矩矩阵相乘,hidden_out1结果为8行20列
    network_out=np.dot(W2,hidden_out)+b2  #np.dot矩阵相乘,W2是2行8列，则output结果是2行20列
    #误差
    err=sample_out-network_out
    mse_err=np.average(np.square(err)) #均方误差
    mse_history.append(mse_err)
    if(i+1)% 100 == 0:
        print("Iter:{}次,mse_err(loss=){}".format(i+1,mse_err))
    if mse_err<mse_final:
        print("Iter:{}次,mse_err(loss=){}".format(i+1,mse_err))
        print("训练结束")
        break
    #BP
    #误差向量
    delta2=-err #最后一层的误差
    delta1=np.dot(W2.transpose(),delta2)*sigmoid_delta(hidden_out)  #前一层的误差向量,这一层对hidden_out用了sigmoid激活函数,要对hidden_out求偏导数；注意最后一步是两个矩阵的点乘，是两个完全相同维度矩阵
    #梯度：损失函数的偏导数
    delta_W2=np.dot(delta2,hidden_out.transpose())
    delta_W1=np.dot(delta1,sample_in.transpose())
    delta_b2=np.dot(delta2,np.ones((sample_number,1)))
    delta_b1=np.dot(delta1,np.ones((sample_number,1)))
    W2-=learn_rate*delta_W2
    b2-=learn_rate*delta_b2
    W1-=learn_rate*delta_W1
    b1-=learn_rate*delta_b1

print("w1={},b1={},w2={},b2={}".format(W1,b1,W2,b2))

#损失值画图
print(mse_history)
loss=np.log10(mse_history)
min_mse=min(loss)
plt.plot(loss,label='loss')
plt.plot([0,len(loss)],[min_mse,min_mse],label='min_mse')
plt.xlabel('迭代次数')
plt.ylabel('均方误差')
plt.title('历史误差信息',fontdict={'fontsize':18,'color':'red'})
plt.legend()
plt.show()

#模型预测输出和实际输出对比图
hidden_out=sigmoid(np.dot(W1,sample_in)+b1)
network_out=np.dot(W2,hidden_out)+b2

#反转获取实际值：
network_out=y_scaler.inverse_transform(network_out.T)
sample_out=y_scaler.inverse_transform(y)

#解决图片中文无法显示
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(8, 6))
plt.plot(network_out[:,0],label='预测值')
plt.plot(sample_out[:,0],'r.',label='实际值')
x_labels = range(1990,2010)
x_ticks=range(0,20)
plt.xticks(ticks=x_ticks, labels=x_labels)
plt.title('公路客运量 ')
plt.legend()
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(network_out[:,1],label='预测值')
plt.plot(sample_out[:,1],'r.',label='实际值')
plt.title('公路货运量 ')

x_labels = range(1990,2010)
x_ticks=range(0,20)
plt.xticks(ticks=x_ticks, labels=x_labels)

plt.legend()
plt.show()
# 现在开始预测环节
PredictDataFrame = pd.read_csv('DataUnknown.csv',encoding='utf-8')

Pre_x=PredictDataFrame[['人数', '机动车数', '公路面积']]
Pre_y=PredictDataFrame[['公路客运量', '公路货运量']]

pre_x_scaler = MinMaxScaler(feature_range=(-1,1))
pre_y_scaler=MinMaxScaler(feature_range=(-1,1))

pre_x=pre_x_scaler.fit_transform(Pre_x)
pre_y=pre_y_scaler.fit_transform(Pre_y)
#对样本进行转置，矩阵运算
pre_in=pre_x.T
pre_out=pre_y.T

#模型预测输出值
hidden_out_pre = sigmoid(np.dot(W1,pre_in)+b1)
network_out_pre=np.dot(W2,hidden_out_pre)+b2
#翻转获取实际值
network_out_pre=pre_y_scaler.inverse_transform(network_out_pre.T)

