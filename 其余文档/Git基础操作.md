# Git基础操作

## 本地->Gitee仓库

### 1、建立远程Gitee仓库

![image-20220312212714390](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312212714390.png)

![image-20220312212727102](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312212727102.png)

![image-20220312212750773](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312212750773.png)

​	我们可以看到我们的仓库地址

### 2、本地文件初始化 git init

我们有这样的一个本地文件夹，我们要把它上传到Gitee上面

![image-20220312213013661](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312213013661.png)

​	右键->更多选项->git bash here

​	输入命令 

> git init

​	会自动生成 .git文件夹，里面是我们的配置信息

### 3、添加要上传的文件 git add .

```
git add 文件名.格式后缀 	//这种是添加单个文件
git add .	//这种是添加全部文件
```

![image-20220312213321935](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312213321935.png)

### 4、上传并添加注释 git commit -m "注释"

```
git commit -m "注释信息"
```

![image-20220312213417758](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312213417758.png)

### 5、绑定远程仓库

```
git remote add origin https://gitee.com/CHD-EASY-GOING/branch-test.git
```

![image-20220312213550973](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312213550973.png)

### 6、提交 push

```
git push -u origin "master"
```

![image-20220312213625596](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312213625596.png)

![image-20220312213718034](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312213718034.png)

上传成功

## 二、分支操作

### 创建分支

```
git branch 新分支名字
```

![image-20220312213931844](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312213931844.png)

​	创建了新分支b，但是当前仍处于master分支

### 切换分支

```
git checkout 要切换到的分支名
```

![image-20220312214022296](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312214022296.png)

### 分支操作

我们在本地文件中新建一个文件  c.txt

![image-20220312215108079](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312215108079.png)

​	我们添加新文件到新分支上面去并进行上传

![image-20220312215037932](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312215037932.png)



![image-20220312215100876](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312215100876.png)

### 合并分支

现在把分支c合并到主分支上！

<font color=red>先要进行切换到主分支master！</font>

​	在主分支上我们使用命令

```
git merge 要合并的副分支名
```

![image-20220312215507975](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312215507975.png)

![image-20220312215328726](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220312215328726.png)

## 同步远程项目

假如你的队友更新了项目代码，你如何在本地进行同步？

```
git pull origin master
```

## 推送本地更新

```
git push origin master
```

## 克隆远程项目

```
git clone 项目仓库地址
```

