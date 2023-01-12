# Python&Git

## Python

- 一种弱类型语言 不需要单独指定类型
- 使用 # 作为注释符号
- 三种序列 列表（list）、元组（tuple）、数列（range）

### 列表list

列表：可变序列 使用方括号表示[] 可存放不同类型的数据

- 添加元素：append  
- 清空 clear
- 浅复制 copy
- 统计某一元素出现的次数 count
- 插入 insert
- 排序 sort
- 翻转：reverse
- 切片 list[start:stop:step] start的默认值是0 step的默认值是1

![image-20220610161401266](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220610161401266.png)

### 元组 tuple

- 元组使用圆括号()表示
- 元组和列表可以相互转换  list(tupleName)  tuple(listName)
- ![image-20220610161918596](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220610161918596.png)

### 数列 range

- 常用于for循环中的控制迭代
- range(start,stop,step)  step默认值为1 前闭后开区间
- ![image-20220610162522143](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220610162522143.png)

### 字符串 str

- python中字符串可以用单引号、双引号、三引号构成
- join方法 str.join(str)
- ![image-20220610163038340](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220610163038340.png)

### 集合 set

- 常用 用于算法题中进行元素去重
- 集合中的元素具有唯一性 不可重复出现
- ![image-20220610163553677](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220610163553677.png)
- frozenset 不可更改的set

### 函数

- def 注意使用冒号
- ![image-20220610163930874](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220610163930874.png)

### 控制语句

![image-20220610170325371](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220610170325371.png)



- if while for需要掌握 这些句子的后面都需要冒号:

- try except语句用于异常捕获与处理

- ```
  try:
  	1/0
  except Exception as e:
  	print(e)
  finally:
  	print("run over")
  ```

  

- with语句块常用于打开文件

- with open(file)

### 类

- class表示类 注意冒号
- 初始化写在 _ _ init _ _函数中
- 时刻留意self的使用
- 类中所有的函数的第一个形参永远且必须是self
- 类的成员使用 self.data
- ![image-20220610191057211](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220610191057211.png)

## Git

- 配置全局信息：git config --global user.name "name"
- git config --global user.email "email"
- 初始化仓库 git init
- 添加所有文件 git add .
- 添加单个文件 git add filename
- 提交到缓冲区 git commit -m "message"
- 提交到仓库 git push origin branchName
- 克隆仓库 git clone URL
- 分支操作
  - 新建分支 git branch branchName
  - 切换分支 git checkout branchName
  - 查看当前仓库的所有分支 git branch
- 查看git 日志 git log
- 查看当前状态  git status