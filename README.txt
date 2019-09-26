使用说明：
1.安装python3.7，MySQL8.0以及requirement.txt中的依赖库（xadmin可能需要手动安装）。
2.新建数据库，使用spiderdb3.24.sql导入表结构和数据（或使用之前已经建立好的数据库）
3.配置biasi/bisai/settings.py中的相关配置
4.使用python ide（最好是pycharm2018.3)打开项目，运行python manage.py makemigrations以及python manage.py migrate
5.运行python manage.py runserver 在本地服务器启动。
6.浏览器输入127.0.0.1查看。