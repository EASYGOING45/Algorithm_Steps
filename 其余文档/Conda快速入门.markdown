# Conda快速入门

> *Package, dependency and environment management for any language—Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN, and more.*

通过阅读前一篇杨麒瞳同学撰写的Python简要教程👍 ，你应该对Python语言有了一个模糊的认知，Python之所以风靡全球的一大原因便在于其拥有优秀的开源社区和成千上万的第三方包和库，那么，既然拥有这么多的工具包，我们也需要对这些包进行版本管理和环境整理，由此引出了本小节的主人翁--Conda🎉️。

设想以下情景，现在我们手上有两个项目，项目A使用的Python版本是3.10，项目B使用的Python版本是2.7，然而我们只有一台电脑，那我们应该怎么办呢？

Conda可以帮助解决这个问题，只需要创建两个对应版本的虚拟环境就好了！😄

![图片.png](https://images.gitee.com/uploads/images/2021/1230/132006_8bd257be_8583917.png)

## Conda简要介绍

Conda是一个开源的软件包管理系统和环境管理系统，用于安装多个版本的软件包及其依赖关系，并在它们之间轻松切换👀️ 。

Conda是为Python语言创建的，适用于Linux、Mac OS以及Windows等多款操作系统，当然，正如它官方文档所说，它也可以用于打包和管理其他编程语言的环境。

## 安装Conda

Conda分为**Anaconda**和**Miniconda**。

**Anaconda**是一个用于科学计算的Python发行版，支持Linux，Mac，Windows，其中包含了众多流行的科学计算、数据分析的Python包（如Numpy、Matplotlib等等）。

**Miniconda**是一个Anaconda的轻量级替代，默认只包含了Python和Conda，但是可以通过pip和conda等来安装所需要的包。

作为人工智能专业的学生，Python语言可以说是必备知识，数据分析和科学计算在后续的学习中也经常会使用到，因此本教程选择安装的是**Anaconda**，后续的操作也都基于**Anaconda🚀️ 。**

### 获得Installer

我们从Anaconda官网下载安装包，[点这里进入下载页面](https://www.anaconda.com/products/individual)，然后点击Download下载即可，网速慢的话建议使用迅雷🚀️ 。

官网打不开的话也可以直接复制以下链接到迅雷进行下载。

下载链接：[https://repo.anaconda.com/archive/Anaconda3-2021.11-Windows-x86_64.exe]()

![图片.png](https://images.gitee.com/uploads/images/2021/1230/134535_581a0874_8583917.png)

### 安装流程

下载完成后，打开我们的安装包（右键点击安装包文件，点击以管理员身份运行，这样能避免后续的一些繁琐步骤）：

依次点击Next、I Agree进入后续页面

![图片.png](https://images.gitee.com/uploads/images/2021/1230/135213_079521e2_8583917.png)
![图片.png](https://images.gitee.com/uploads/images/2021/1230/135234_255ebf7b_8583917.png)强烈不建议安装在C盘！！！安装在C盘会让你的电脑非常卡（猜猜我怎么知道的😕 ）！

![图片.png](https://images.gitee.com/uploads/images/2021/1230/135302_674c1564_8583917.png)
几个需要勾选的地方如图勾选即可。

安装成功后在开始菜单能看到以下信息即成功：

![图片.png](https://images.gitee.com/uploads/images/2021/1230/135746_5f3b91b9_8583917.png)

## Anaconda Prompt入门

Anaconda Prompt是Anaconda中的命令行程序，相当于Windows系统下的cmd，用于执行一些命令，我们平时也通过它来新建指定内容的虚拟环境和安装指定版本的第三方软件包。

我们通过点击开始菜单中的Anaconda Prompt字样来进入以下页面，（注意，不是Anaconda Powershell Prompt）

![图片.png](https://images.gitee.com/uploads/images/2021/1230/145440_7e7751f8_8583917.png)

下面我们来介绍一些常用的conda命令。

### 查看Conda基本信息

* `conda list`    查看安装了哪些包
* `conda env list` 或 `conda info -e`  查看当前存在哪些虚拟环境
* `conda --version`  查询当前的Conda版本
* `conda update conda`  检查更新当前Conda
* `conda -h`  查询Conda命令的使用

![图片.png](https://images.gitee.com/uploads/images/2021/1230/152448_0f699fe8_8583917.png)

### 更换国内下载源

Anaconda默认的下载源在国外，导致下载速度异常缓慢，我们可以通过命令行来更改为国内的下载源，这里我们选择更改为清华源，命令代码如下，在Anaconda Prompt中依次输入：

1. `conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/`
2. `conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge`
3. `conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/`
4. `conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/`
5. `conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/`
6. `conda config --set show_channel_urls yes`

输入完毕后，我们使用命令：`conda config --show`   来查看当前的下载源

如图所示：

![图片.png](https://images.gitee.com/uploads/images/2021/1230/150503_ee492310_8583917.png)

### 虚拟环境管理

Conda的核心功能之一就是多个不同的虚拟环境的创建以及对应的管理👍

#### 新建指定Python版本的虚拟环境

假设，现在我们需要一个Python版本号为3.8的虚拟环境，我们可以在Anaconda Prompt中使用以下命令来完成：

* `conda create --name LYXts python=3.8`  这行命令意为：创建一个名为LYXts，python版本为3.8的虚拟环境
* 如果你没有按照前面的流程更改为国内下载源的话速度会非常慢！

![图片.png](https://images.gitee.com/uploads/images/2021/1230/153525_47c070bf_8583917.png)

成功后，我们可以看到以下页面，使用 `conda env list`来查看当前系统下的虚拟环境列表，其中*号所处的虚拟环境为我们当前所在的虚拟环境。

![图片.png](https://images.gitee.com/uploads/images/2021/1230/153540_f9eff23d_8583917.png)

#### 进入指定的虚拟环境

在Anaconda Prompt中敲入以下代码 进入指定名称的虚拟环境中

* `conda activate name`  激活名称为name的虚拟环境

![图片.png](https://images.gitee.com/uploads/images/2021/1230/153840_fcf4342c_8583917.png)

#### 删除指定的虚拟环境

在Anaconda Prompt中，通过键入以下命令来删除指定名称的虚拟环境：

* `conda remove -n name --all` 删除名称为name的虚拟环境

![图片.png](https://images.gitee.com/uploads/images/2021/1230/154658_482e035a_8583917.png)

![图片.png](https://images.gitee.com/uploads/images/2021/1230/154709_6972109f_8583917.png)

### 软件包管理

Python最大的特点便是其优秀的开源生态环境和成千上万优秀的开发者所提供的第三方拓展包，涵盖了方方面面，从数据分析到科学计算再到web应用搭建👍

#### 软件包信息

* `conda search PackageName`  在所有已添加的仓库中搜索指定名称的包
* `conda list`  查看当前环境中安装的所有包的信息
* `conda list -n envname` 查看指定虚拟环境中安装的所有包的信息
* `conda install pip` pip是python自带的包安装方式

#### 在指定环境中安装指定包

比如，我们要在指定的虚拟环境下安装指定的软件包，我们可以按以下流程操作：

1. 打开Anaconda Prompt
2. 进入指定的虚拟环境  `conda avtivate envname`
3. 安装指定包 `conda install PackageName`

下图，展示了在LYXts环境中安装numpy包的流程：
![图片.png](https://images.gitee.com/uploads/images/2021/1230/160600_b7287284_8583917.png)

待下载完成后，我们进行查看：


 ![图片.png](https://images.gitee.com/uploads/images/2021/1230/161229_adf3aff2_8583917.png)

#### 安装指定版本的某包

`conda install PackageName==1.0.0`  安装指定版本号的某个包 

#### 删除指定环境中的某个包

我们以删除某环境下的requests包为例：

1. `conda activate envname` 进入指定的虚拟环境
2. `conda remove packageName` 删除当前环境中的指定包

 ![图片.png](https://images.gitee.com/uploads/images/2021/1230/161951_b3d51d09_8583917.png)


 ![图片.png](https://images.gitee.com/uploads/images/2021/1230/162023_355e6a99_8583917.png)

#### 更新包

* `conda update packageName` 更新指定包
* `conda update --all` 更新全部

## Anaconda Navigator简介

Anaconda Navigator是Anaconda的可视化图形程序，如果不喜欢使用命令行的话可以使用它来进行包管理和环境管理。

直接在开始菜单Anaconda3目录下点击Anaconda Navigator字样即可进入。

主页面介绍大致如下图：![图片.png](https://images.gitee.com/uploads/images/2021/1230/141640_441dacd7_8583917.png)

Environments页面![图片.png](https://images.gitee.com/uploads/images/2021/1230/143732_591386c4_8583917.png)
