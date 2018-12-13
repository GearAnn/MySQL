#!/usr/bin/python
# coding: utf-8 

"""
@version: Python3
@author: Ann 
@contact: 494792590@qq.com 
@software: Pycharm
@file: pymysql_数据查询.py
@time: 2018/10/30 0030 下午 12:35
"""

"""
pymysql查询语句：
cursor.fetchall()  cursor.fetchone()  cursor.scroll()的调用

cursor游标的数据类型，其默认为元组类型，可以设置为字典类型
语句： 
cursor = conn.cursor(cursor=mysql.cursors.DictCursor)
在取值的时候：cursor.execute('select 字典关键字 fromm student')
"""

import  pymysql

conn = pymysql.connect(
    host='127.0.0.1', port=3306, user='root',
    passwd=325249, db='sqltest', charset='utf8')

cursor = conn.cursor()

r = cursor.execute('select * from student')
print(r)
# 这里的打印结果是student的数据量,也叫做受影响的数量，这是这些受影响的数据已经进入内存等待调用

# 取全部数据 fetchall调用
result = cursor.fetchall()
print(result)

# 取单个数据 fetchone调用
result = cursor.fetchaone()
print(result)

# 取任意数据 fetchmany(x)
result = cursor.fetchaone(4)  # 取4条数据
print(result)


"""
注意：fetchall,fetchone 是指针函数，按照顺序依次调用数据，数据调用完后，继续调用则返回 None。

在fetch按照顺序调用数据时，可以使用 cursor.scroll(num,mode)来指定数据序号，并取出数据。

1.相对当前位置移动：
    语句：cursor.scroll(3,mode='relative')  
    表示：在当前位置，往下走3条数据
    
    语句：cursor.scroll(-5,mode='relative') 
    表示：在当前位置，往回走5条数据

2.相对绝对位置移动：
    语句：cursor.scroll(2,mode='absolute')
    表示：从头开始往下走2条数据
    
3.获取自增ID
    nid = cursor.lastrowid
"""

























