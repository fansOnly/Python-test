# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# virtualenv
# virtualenv就是用来为一个应用创建一套“隔离”的Python运行环境。

# 第一步，创建目录：

# Mac:~ michael$ mkdir myproject
# Mac:~ michael$ cd myproject/
# Mac:myproject michael$

# 第二步，创建一个独立的Python运行环境，命名为venv：

# Mac:myproject michael$ virtualenv --no-site-packages venv
# Using base prefix '/usr/local/.../Python.framework/Versions/3.4'
# New python executable in venv/bin/python3.4
# Also creating executable in venv/bin/python
# Installing setuptools, pip, wheel...done.


# 新建的Python环境被放到当前目录下的venv目录。有了venv这个Python环境，可以用source进入该环境：

# Mac:myproject michael$ source venv/bin/activate
# (venv)Mac:myproject michael$



# 退出当前的venv环境，使用deactivate命令：

# (venv)Mac:myproject michael$ deactivate 
# Mac:myproject michael$