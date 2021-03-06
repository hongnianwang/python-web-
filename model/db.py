# -*- coding: utf-8 -*-

import pymysql

PY_MYSQL_CONN_DICT = {
    'host': 'localhost',  # This database is in the same server as the web.
    'user': 'user_name',
    'password': 'password',
    'database': 'db_name',
    'port': port,
    'charset': 'utf8'
}

class DbConnection:

    def __init__(self):
        self.__conn_dict = PY_MYSQL_CONN_DICT
        self.conn = None
        self.cursor = None

    def connect(self, cursor=pymysql.cursors.DictCursor):
        self.conn = pymysql.connect(**self.__conn_dict)
        self.cursor = self.conn.cursor(cursor=cursor)
        return self.cursor

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

