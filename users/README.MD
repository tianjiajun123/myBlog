## 一、环境配置

1. VSCode 下载，安装python ，chinese，path intellisence，npm ，npm intellisence ,Vetur，Vue3 Snippets ,vscode-icons，live server 这些插件

2. 配置终端

   切换到cmd

3. 安装前端开发工具HbuilderX https://www.dcloud.io/hbuilderx.html

4. 安装小程序开发工具 https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

## 二、安装git：https://git-scm.com/；

1. 创建远程仓库myBlog

2. 初始化本地仓库，也就是在本地的myBLog文件夹下执行：`git init`，执行完后会创建一个.git的隐藏文件

3. 远程仓库和本地仓库进行关联：`git remote add origin "你的远程仓库地址"`

4. 如果出现错误，ssh没有创建

5. 先去创建密钥：`ssh-keygen` ，一路enter，生成密钥

6. 查看生成的密钥 `cat ~/.ssh/id_rsa.pub`，将密钥写入到github上的settings下的SSH and GPG keys下

7. 推送四步骤：

   git status 查看发生变化的文件

   git add . 追踪所有发生变化的文件

   git commit -m "备注" 提交到本地仓库

   git push -u origin master 第一次提交 到远程仓库

   git push 之后的提交

## 三、创建myBlog项目

1. 空文件夹下，执行 `django-admin startproject myBlog`;
2. 给myBlog创建虚拟环境，使用：`python -m venv env`
3. 进入到虚拟环境，windows下：`.\\env\\Scrtipst\\activate`;
4. 退出虚拟环境，windows下：`deactivate`；
5. 使用VSCode打开myBlog，执行：`python manage.py startapp articles`

## 四、创建文章的模型

1.创建model及逆行数据库迁移
2.在admin.py注册每个app
3.对于文章管理员是有文章数据库中的所有相关字段
4.admin.site.register(Articles,ArticlesAdmin) 进行在admin管理员页面网址注册文章以及文章管理员 

## 五、业务逻辑

文章列表页 分页          django
文章详情页  评论         评论库 第三方库
详情列表页/文章搜索/     q对象或的对象标题摘要获得信息
最新文章最新评论排行榜    时间
按照分类标签的聚类操作    分类标签进行搜索
联系我页面，发送邮件      发送邮件的行为和操作

## 六、实现模板复用

如何加载静态页面  网上图片不需要解析  加标签  
在settings.py文件中注册静态页面和templates模板 
创建公共模板进行继承extends 实现模板复用  
将公共内容base.html/aside.html写入common文件夹中实现模板复用减少冗余代码的写入
注册静态内容 {% load static %}  css/js

## 七、注册路由实现页面跳转

在主博客页面的urls.py文件中include引入每个app的urls配置
MVC模式  models.py 数据库字段内容 进行数据展示和增删改查 views.py   