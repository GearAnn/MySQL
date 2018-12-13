#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: 字符串拼接SQL.py
@time: 2018/10/30 0030 上午 11:47
"""

"""
需求：让用户输入班级，完成插入SQL数据的操作。
"""

import pymysql


conn = pymysql.connect(
    host='127.0.0.1', port=3306, user='root',
    passwd=325249, db='sqltest', charset='utf8')

cursor = conn.cursor()

inp = input('请输入班级：')

# 参数传递：把inp通过占位符 %s 输入到cursor.execute, 让pymysql内部完成字符串的拼接
r = cursor.execute('insert into class(caption) values (%s)', inp)  # 插入1个数据

conn.commit()
cursor.close()
conn.close()


"""
同时插入多个数据

方法一:用多个占位符，最后加上一个元组
r = cursor.execute('insert into student(gender,name) values (%s,%s)', ('女', 'Alex'))

方法二：可以多个数据打包成一个list,调用 cursor.executemany 整体插入 

list_1 = [('女', 'Alex'),('女', 'Bob'),('女', 'Sasa')]
r = cursor.executemany('inset into student(gendr,name) values(%s,%s)')


总结：1.SQL语句中的 insert,delect,update 都可以在cursor.execute（）中去执行！！ 
     
     2.只有select查询有所不同（具体看pymySQL_数据查询）
     
"""

# 设置游标的数据类型，其默认为元组类型，可以设置为字典类型














