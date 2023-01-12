# http://car.chd.edu.cn/

## 长安大学出入管理平台

## 域名：[**car.chd.edu.cn**](http://ip.webmasterhome.cn/?ip=car.chd.edu.cn)

## IP：202.117.64.91

## 指纹识别

### Web服务器-IIS7.5

### Web服务框架-ASP.NET

## 漏洞扫描

​	![image-20220316100056162](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316100056162.png)

![image-20220316100128238](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316100128238.png)

![image-20220316100154732](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316100154732.png)

![image-20220316100230028](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316100230028.png)

## 目录扫描

![image-20220316094717709](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316094717709.png)

​	打开敏感地址 http://202.117.64.91/m

![image-20220316095728986](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316095728986.png)

![image-20220316095744401](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316095744401.png)

​	这一网页不需要任何权限便可上交，可能会存在注入漏洞。

​	同时，IIS7.5系统存在解析漏洞，

> IIS7/7.5在Fast-CGI运行模式下,在一个文件路径(/xx.jpg)后面加上/xx.php会将/xx.jpg/xx.php 解析为 php 文件。

​	再对http://202.117.64.91/m进行扫描

​	![image-20220316100023726](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316100023726.png)

![image-20220316100540610](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316100540610.png)

​	我们发现了敏感文件 3.rar

​	![image-20220316100648315](https://happygoing.oss-cn-beijing.aliyuncs.com/img/image-20220316100648315.png)

​	里面全是教职工的个人信息 可能会有信息泄露风险

