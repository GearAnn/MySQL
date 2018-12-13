#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: pymysql操作流程.py
@time: 2018/10/30 0030 上午 10:22
"""


"""
通过python来操作MySQL,需要导入 pymysql 模块。 

通过5步完成python对SQL的操作：
创建连接，创建游标，确认操作，关闭游标，关闭连接

"""

import pymysql

# 1.创建连接
conn = pymysql.connect(
    host='127.0.0.1', port=3306, user='root',
    passwd=325249, db='sqltest', charset='utf8')

# 2.创建游标，所有数据库的语句都是通过游标来执行的
cursor = conn.cursor()

# FIXME 创建连接和游标是 Python 管理数据库之前的必要条件！！
cursor.execute('insert into class(caption) values (”全站二班“)')

# 3.确认SQL操作
#   注意：通过python操作SQL需要确认操作，别忘记。
conn.commit()

# 4.关闭游标
cursor.close()

# 5.关闭连接
conn.close()


