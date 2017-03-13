# -*- coding: utf-8 -*-

import pymysql
from eastmoney import settings

mysql_host=settings.MYSQL_HOSTS
mysql_port=settings.MYSQL_PORT
mysql_user=settings.MYSQL_USER
mysql_password=settings.MYSQL_PASSWORD
mysql_db=settings.MYSQL_DB
mysql_charset=settings.MYSQL_CHARSET

conn=pymysql.Connection(host=mysql_host,
                     port=mysql_port,
                     user=mysql_user,
                     passwd=mysql_password,
                     db=mysql_db,
                     charset=mysql_charset)
cursor=conn.cursor()

class my_sql:
    
    @classmethod
    def select_urls(cls):
        sql='select stock_url from test.eastmoney_basic_info'
        cursor.execute(sql)
        result=cursor.fetchall()
        return result
