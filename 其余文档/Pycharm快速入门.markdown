# Pycharm快速入门

> Pycharm--The Python IDE for Professional Developers!
>
> ALL THE PYTHON TOOLS IN ONE PLACE!

阅读了此前的一系列教程，我们学习了Markdown、Conda、Git、VSCode等一系列编程工具，也对Python语言有了初步的认知。

上一节我们学习了VSCode这一轻量级跨平台IDE的基本使用方法，而除了VSCode之外，Pycharm也是一款面向Python语言的开发利器。

Pycharm是一款面向专业Python开发者的IDE，其内部集成了诸多Python的使用插件和工具，相比VSCode而言，它更纯粹的面向Python语言，如果您感兴趣的话，也可以安装Pycharm进行学习了解。

这是来自刘易行同学的Pycham快速入门教程❤️ ，水平有限，难免有失偏颇，烦请您见谅，希望能够帮助到大家。🎉️

![图片.png](https://images.gitee.com/uploads/images/2021/1231/113708_4b87257b_8583917.png)

## 安装Pycharm

### 版本选择

Pycharm分为专业版Professional Edition和免费的社区版Community Edition。

其中专业版适用于科学和Web Python开发，其支持HTML、JS、SQL等语言。

而社区版仅适用于纯Python开发。

专业版需要JetBrains会员（需要付费购买），社区版则是免费开源。

在这里，社区版即可满足我们的使用需求，因此我们选择下载社区版。

### 下载Installer

我们进入Pycharm的官网下载页--[官网下载页](https://www.jetbrains.com/zh-cn/pycharm/download/#section=windows)

![图片.png](https://images.gitee.com/uploads/images/2021/1231/114627_4b8afc92_8583917.png)

### 安装流程

打开安装包，选择安装路径，不要选择C盘
![图片.png](https://images.gitee.com/uploads/images/2021/1231/114754_db642194_8583917.png)

![图片.png](https://images.gitee.com/uploads/images/2021/1231/114817_d90ff57e_8583917.png)
![图片.png](https://images.gitee.com/uploads/images/2021/1231/114841_8a5711bb_8583917.png)

安装完成后，我们打开IDE，开始装一些常用的插件

![图片.png](https://images.gitee.com/uploads/images/2021/1231/115652_5d572af7_8583917.png)

## 安装插件

Pycharm开源社区提供了许多非常便捷实用的插件，涵盖语言支持及VCS版本控制工具等。

我们点击左侧菜单栏中的Plugins打开插件市场来下载一些

![图片.png](https://images.gitee.com/uploads/images/2021/1231/115734_662ee7c9_8583917.png)

### 中文插件（如果需要的话）

建议大家适用英文版，还能锻炼一波英语水平不是嘛，中文版需要下载中文插件：

输入Chinese，找到中文语言包并进行下载。安装完成后会提示让我们重启IDE，重启即可

![图片.png](https://images.gitee.com/uploads/images/2021/1231/115910_5cb1665f_8583917.png)
![图片.png](https://images.gitee.com/uploads/images/2021/1231/120000_95ca37b3_8583917.png)

![图片.png](https://images.gitee.com/uploads/images/2021/1231/120022_02be2b00_8583917.png)

再次打开后，我们看到页面如下所示，成功的成为了中文页面：

![图片.png](https://images.gitee.com/uploads/images/2021/1231/120106_234cb565_8583917.png)

### Markdown支持

![图片.png](https://images.gitee.com/uploads/images/2021/1231/120253_e75dba18_8583917.png)

### Gitee插件

![图片.png](https://images.gitee.com/uploads/images/2021/1231/120343_e0a7e042_8583917.png)

### 自定义主题

![图片.png](https://images.gitee.com/uploads/images/2021/1231/120446_7584f10c_8583917.png)

## 新建项目

现在，我们从0开始新建一个Python项目，并选择之前已经创建好的Conda虚拟环境作为Python解释器。

当然，也可以远端拉取项目（fork）。详见后文VCS教程

**点击新建项目**

![图片.png](https://images.gitee.com/uploads/images/2021/1231/120651_4d26fd17_8583917.png)

### 配置Python解释器

在配置解释器时，我们可以选择适用Conda新建一个，也可以选择之前创建好的虚拟环境：

![图片.png](https://images.gitee.com/uploads/images/2021/1231/120946_2fe2ab4e_8583917.png)

![图片.png](https://images.gitee.com/uploads/images/2021/1231/121142_4bb7ac8d_8583917.png)
![图片.png](https://images.gitee.com/uploads/images/2021/1231/121145_348fca14_8583917.png)

![图片.png](https://images.gitee.com/uploads/images/2021/1231/121326_b2354d1f_8583917.png)

### 新建Python文件

右键点击项目名称，鼠标悬浮至新建字样，选择Python文件
![图片.png](https://images.gitee.com/uploads/images/2021/1231/121620_62295338_8583917.png)

![图片.png](https://images.gitee.com/uploads/images/2021/1231/124026_207a1f45_8583917.png)

看到新建成功
![图片.png](https://images.gitee.com/uploads/images/2021/1231/124029_21e8a7e8_8583917.png)

### 运行Python代码

![图片.png](https://images.gitee.com/uploads/images/2021/1231/124158_5a824a45_8583917.png)

运行成功

![图片.png](https://images.gitee.com/uploads/images/2021/1231/124215_cff79c9a_8583917.png)

## 关闭项目


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/130557_f98a5951_8583917.png)

## VCS版本控制教程

如果需要上传项目的话需要预先安装Gitee插件，详见前文安装插件模块👀️

### 新建远端Gitee仓库并上传

![图片.png](https://images.gitee.com/uploads/images/2021/1231/124633_fa404f39_8583917.png)

点击 Share Project on Gitee 字样 进入以下页面

![图片.png](https://images.gitee.com/uploads/images/2021/1231/125110_7f76c8c3_8583917.png)

一开始的Share by一栏为空 因为我们还没有进行登录 点击Add Account  选择 log in via gitee （通过账户密码进行登录，当然你也可以选择第二种方式：令牌登录）

![图片.png](https://images.gitee.com/uploads/images/2021/1231/125217_b3394895_8583917.png)

账号一般填写邮箱地址，就是您之前注册过的那个账户地址，登录成功后页面如下

![图片.png](https://images.gitee.com/uploads/images/2021/1231/125242_6843ee36_8583917.png)

我们点击Share，选择要提交的文件，并填写提交信息：

![图片.png](https://images.gitee.com/uploads/images/2021/1231/125307_2f37173f_8583917.png)

点击添加，软件开始帮助我们进行提交（Push），成功后看到以下字样：

![图片.png](https://images.gitee.com/uploads/images/2021/1231/125332_5fd346c4_8583917.png)

然后，我们打开我们的Gitee主页，看看我们的仓库：

![图片.png](https://images.gitee.com/uploads/images/2021/1231/125408_f1e19767_8583917.png)

可以看到，我们创建了新的仓库并提交了一些文件，打开仓库，看到以下页面，即代表成功

![图片.png](https://images.gitee.com/uploads/images/2021/1231/125447_7bac2935_8583917.png)

### 提交新文件

我们现在创建一个新的Python文件，然后将其更新到我们之前的仓库中去：


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/125727_fdfd1393_8583917.png)

选择添加，有变动且未上传的文件会呈现绿色


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/125742_5db26f96_8583917.png)

右键点击项目，Git->提交目录


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/130001_e1aa71df_8583917.png)

填写提交信息
![图片.png](https://images.gitee.com/uploads/images/2021/1231/130104_f2f7781b_8583917.png)

点击推送
![图片.png](https://images.gitee.com/uploads/images/2021/1231/130126_552ff976_8583917.png)

成功;


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/130152_8dde6e95_8583917.png)


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/130208_2282c5b8_8583917.png)

### 远端拉取项目到本地

假如，我们在Gitee社区上看到了一个非常好的项目，我们想在本地查看它，我们可以选择从远端进行拉取(fork).

在这里，我们以拉取我本人的一个仓库为例：


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/130941_e692b9a0_8583917.png)


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/130937_a6f335c6_8583917.png)


首先关闭原项目，来到如下页面，选择从VCS获取：


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/130707_d5898b91_8583917.png)

然后我们需要输入要拉取的项目的URL
![图片.png](https://images.gitee.com/uploads/images/2021/1231/130815_08285371_8583917.png)


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/130958_30e71ed8_8583917.png)

点击左下角的克隆

![图片.png](https://images.gitee.com/uploads/images/2021/1231/131020_7923ec34_8583917.png)
 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/131047_907226ee_8583917.png)

克隆成功


 ![图片.png](https://images.gitee.com/uploads/images/2021/1231/131118_b5e4d618_8583917.png)



## 小结

> Pycharm是一款更纯粹，更门户化的面向Python语言的IDE,您可以在VSCode和Pycharm之间选择一款作为常用IDE
