简易个人博客
===

### **这个项目是跟着[BILIBILI上杨仕航老师的django教程](http://space.bilibili.com/252028233/#/channel/detail?cid=28138)一步一步打下来的，完全不原创**

### **非常感谢杨老师的视频教程！教程通俗易懂，由浅入深，非常有实用性，推荐想入坑django的小伙伴去B站看一看。**

### **关于这个教程的更详细代码可以在[杨老师的github](https://github.com/HaddyYang/django2.0-course)上找到**

### **更多相关内容可以参考[杨老师的博客](http://yshblog.com/)**

-------

#### 简介

语言：python3、HTML、CSS、JavaScript  
web框架：django2.0  
前端框架：bootstrap、jQuery  
数据库：MySQL  
在学习django的过程中，跟着教程写下来的博客。  
如果您觉得好或者也想学习django，可以去B站看一下[这个教程](http://space.bilibili.com/252028233/#/channel/detail?cid=28138)。

#### 使用介绍

将项目克隆到本地
```bash
git clone git@github.com:NAkeshu/SimplePersonalBlog.git
```
然后进入项目目录
```shell
cd SimplePersonalBlog
```
修改`/testsite/settings`文件中的`DATABASE`参数
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # 可以修改成其它数据库
        'NAME': 'testsite', # 数据库名称
        'USER': 'root', # 用户名
        'PASSWORD': '123', # 密码
        'HOST': 'localhost', # host地址，本地数据库不用改，远程数据库的话改成数据库的IP地址
        'PORT': 3306, # 端口，一般不用改
    }
}
```
初始化数据库
```bash
python manage.py migrate
```
再新建个管理员用户
```bash
python manage.py createsuperuser
```
然后依次输入用户名（可跳过，默认admin）、邮箱地址（可跳过）、密码即可。
最后启动本地服务器
```bash
python manage.py runserver
```
在浏览器输入地址`localhost:8000`即可，输入地址`localhost:8000/admin`即可进入后台。

#### 截图

![index](https://i.loli.net/2018/06/14/5b22405624111.png)
首页

![blog_list](https://i.loli.net/2018/06/14/5b223fbd87818.png)
博客列表

![blog_type_django](https://i.loli.net/2018/06/14/5b224002c2e52.png)
![blog_type_type_ganwu](https://i.loli.net/2018/06/14/5b22402417c61.png)
博客分类列表

![日期归档](https://i.loli.net/2018/06/14/5b223f83462a1.png)
日期归档

![blog_detail](https://i.loli.net/2018/06/14/5b223f6f5c42f.png)
博客详情

![后台](https://i.loli.net/2018/06/14/5b22406913c35.png)
![后台文章类型](https://i.loli.net/2018/06/14/5b2240787fcd0.png)
![后台文章列表](https://i.loli.net/2018/06/14/5b22408b7a080.png)
后台

**随着学习的深入，还会更新修改这个项目，TO BE CONTINUE**