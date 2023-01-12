# Ch4、贪心算法

## 贪心-一种短视的决策策略

> 任何一个问题，先明确算法问题的输入输出，再查看条件限制

- 贪心算法基本思想
- 求解最优化问题的算法包含一系列步骤
- 每一步都有一组选择
- 做出在当前看来最好的选择
- 局部最优推出全局最优
- 贪心算法不一定总能产生最优解
- 贪心算法经常伴随着排序等预处理操作
- 贪心算法的优势：算法简单、时空复杂度较低
- 解题时需要先明确要使用的贪心策略

## 活动选择问题-依赖排序

![image-20220602094822286](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602094822286.png)

![image-20220602095413404](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602095413404.png)

## 最优装载问题-轻者优先

![image-20220602100442508](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602100442508.png)

![image-20220602100501223](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602100501223.png)

![image-20220602100509123](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602100509123.png)

## 最小延迟调度问题-减少空闲时间

![image-20220602101549438](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602101549438.png)

![image-20220602101641680](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602101641680.png)

![image-20220602101655525](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602101655525.png)

## 得不到最优解如何处理？

进行输入参数分析以及误差分析

输入参数分析：考虑输入参数在什么取值范围内使用贪心法可以得到最优解

误差分析：估计贪心法--近似算法所得到的解与最优解的误差（对所有的输入实例在最坏情况下误差的上界）

## 找零钱问题

![image-20220602102233220](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602102233220.png)

![image-20220602102244776](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602102244776.png)

![image-20220602102257477](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602102257477.png)

![image-20220602102306017](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220602102306017.png)