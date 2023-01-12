# Git-操作指北

## 我们来学习一下Git的分支操作

## 我们先建立一个远程仓库

![image-20220316215714912](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316215714912.png)

## 然后我们在本地建立一个仓库（文件夹）

## Step1-初始化本地仓库

```
git init
```

![image-20220316215810357](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316215810357.png)

​	我们给本地仓库里面添加一个文件master.txt

## Step2-绑定到远程仓库

```
git remote add origin 远程地址
```

![image-20220316215934990](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316215934990.png)

## Step3-添加本地文件并上传到缓冲区

```
git add 文件名.格式名
git commit -m "注释信息"
```

![image-20220316220054901](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316220054901.png)

## Step4-推送本地分支到远端

```
git push origin 分支名
```

![image-20220316220108309](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316220108309.png)

## 分支操作

## 建立分支

```
git branch 新分支名
```

![image-20220316220142577](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316220142577.png)

## 查看所有分支

```
git branch -a
```

![image-20220316220205460](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316220205460.png)

白色的为本地分支 绿色的为当前所处分支

红色的为远端分支

## 切换分支

```
git checkout 分支名
```

![image-20220316220305601](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316220305601.png)

我们现在在分支b上面新建文件b.txt

## 推送分支

```
git push origin 分支名
```

![image-20220316220445520](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316220445520.png)

![image-20220316220456537](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316220456537.png)

我们现在在本地切换回master分支看看会发生什么

会发现文件消失

和远端之前的保持一致

## 查看上传日志

```
git log
```

只会查看当前分支的日志

## 从远端拉取分支

```
git pull 分支名
```

## Pull Requests

请求合并！

![image-20220316220752929](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316220752929.png)

合并成功!

