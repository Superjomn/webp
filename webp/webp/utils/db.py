# -*- coding: utf-8 -*-
from __future__ import division
'''
Created on 11 21, 2013

@author: Chunwei Yan @ pkusz
@mail:  yanchunwei@outlook.com
'''
from django.db import connection, transaction

class DB(object):
    def __init__(self):
        self.cursor = connection.cursor()

    def exe_commit(self, sql):
        self.execute(sql)
        self.commit()

    def execute(self, cmd):
        self.cursor.execute(cmd)

    def commit(self):
        transaction.commit_unless_managed()

    def fetchone(self):
        res = self.cursor.fetchone()
        return res

    def fetchall(self):
        res = self.cursor.fetchall()
        return res

    def get_value(self, sql):
        self.execute(sql)
        res = self.fetchone()
        if res:
            return res[0]

    def __del__(self):
        self.cursor.close()


if __name__ == "__main__":
    pass

