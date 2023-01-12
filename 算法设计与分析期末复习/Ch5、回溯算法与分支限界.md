# Ch5、回溯算法与分支限界

## 基本思想

- 适用：求解搜索问题以及优化问题
- 本质仍是递归和暴力遍历 可以通过剪枝等策略进行时空优化
- 搜索空间：树结构，节点对应部分解向量，可行解在树叶上
- 搜索过程：遍历搜索树 分为纵向和恒好像
- 搜索策略：深度优先、宽度优先、函数优先、宽深结合
- 节点分支判定条件：递归终止条件

### 适用条件

​	满足多米诺性质

​	![image-20220602104320918](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602104320918.png)

## 货郎问题 了解即可

![image-20220602103239366](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602103239366.png)

## 经典问题-N皇后问题 重点！

## 装载问题

![image-20220602104524892](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602104524892.png)

![image-20220602104531709](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602104531709.png)

![image-20220602104601044](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602104601044.png)

![image-20220602104711097](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602104711097.png)

![image-20220602104719608](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602104719608.png)

## 着色问题

![image-20220602104933956](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602104933956.png)

![image-20220602104941587](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602104941587.png)

着色问题类似于会场分配问题

## 搜索树结点数估计

![image-20220602105423784](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602105423784.png)

- Monte Carlo方法
- 目的：估计搜索树真正访问得到结点数目
- 步骤：随机抽样，选择一条路径
- 用这条路径代替其他路径
- 逐层累加树的结点数
- 多次选择，取结点数的平均值