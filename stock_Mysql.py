#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
from warnings import filterwarnings
filterwarnings('ignore', category = MySQLdb.Warning)

SVNAME = "localhost"
SVUSER = "root"
SVPAWD = "1234321xy"
DBNAME = "TESTDB"
class stock_Mysql():
    '''专用于stock的数据库方法类'''
    login = ()
    def __init__(self):
        pass

    def addInfo(self,info):
        '''给stock_info数据库添加一行数据'''
        db = MySQLdb.connect(SVNAME, SVUSER, SVPAWD, DBNAME, charset="utf8")
        cursor = db.cursor()
        try:
            sql = "INSERT IGNORE INTO stock_info\
                   VALUES (%s,%s,%s,%s,%s,%s,,%s,%s,%s,%s,%s,%s,%s,%s,,%s,%s,\
                           %s,%s,%s,%s,%s,%s,,%s,%s,%s,%s,%s,%s,%s,%s,,%s,%s)"
            # 执行sql语句
            n = cursor.execute(sql,info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7],info[8],info[9] \
                               , info[10], info[11], info[12], info[13], info[14], info[15], info[16], info[17], info[18],info[19] \
                               , info[20], info[21], info[22], info[23], info[24], info[25], info[26], info[27], info[28],info[29] \
                               ,info[30], info[31])
            # 提交到数据库执行
            db.commit()
        except :
            # Rollback in case there is any error
            print("有错误，rollback")
            db.rollback()
        # 关闭数据库连接
        db.close()

    def showTable(self,table):
        '''显示数据库中所有信息'''
        db = MySQLdb.connect(SVNAME, SVUSER, SVPAWD, DBNAME, charset="utf8")
        cursor = db.cursor()
        # SQL 查询语句
        sql = "SELECT * FROM " + table
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                # 打印结果
                print(row)
        except:
            print("Error: unable to fecth data")
        db.close()

    def clearDB(self):
        '''清除股票的数据'''
        db = MySQLdb.connect(SVNAME, SVUSER, SVPAWD, DBNAME, charset="utf8")
        cursor = db.cursor()
        sql ="DELETE FROM stock_info "
        n = cursor.execute(sql)
        print(n)
        db.commit()
        db.close()

    def initSP(self,):
        '''初始化READSP数据库，将SP设为1'''
        db = MySQLdb.connect(SVNAME, SVUSER, SVPAWD, DBNAME, charset="utf8")
        cursor = db.cursor()
        sql = "DELETE FROM READSP"
        n = cursor.execute(sql)
        sql = "INSERT INTO READSP(SP,CHANGEDATE) VALUES(0,CURRENT_DATE)"
        n = cursor.execute(sql)
        db.commit()
        db.close()

    def getSP(self):
        '''得到sp的数值'''
        db = MySQLdb.connect(SVNAME, SVUSER, SVPAWD, DBNAME, charset="utf8")
        cursor = db.cursor()
        sql = "SELECT SP FROM READSP"
        n = cursor.execute(sql)
        sp = cursor.fetchone()
        if sp!=None:
            sp = sp[0]
        else:
            n = cursor.execute("INSERT INTO XUEQIU(SP,CHANGEDATE) VALUES(0,CURRENT_DATE)")
            sp = 0
        db.close()
        return sp

    def getTotalOfRoles(self):
        '''得到sp的数值'''
        db = MySQLdb.connect(SVNAME, SVUSER, SVPAWD, DBNAME, charset="utf8")
        cursor = db.cursor()
        sql = "SELECT COUNT(*) FROM XUEQIU"
        try:
            n = cursor.execute(sql)
            tatol = cursor.fetchone()
            ta = tatol[0]
            db.close()
            return ta
        except:
            db.rollback()
            db.close()

    def gConnectDB(self):
        '''建立一个外部可以操作的数据连接'''
        self.db = MySQLdb.connect(SVNAME, SVUSER, SVPAWD, DBNAME, charset="utf8")
        self.cursor = self.db.cursor()

    def gConnectDB2(self):
        '''建立一个外部可以操作的数据连接'''
        self.db2 = MySQLdb.connect(SVNAME, SVUSER, SVPAWD, DBNAME, charset="utf8")
        self.cursor2 = self.db2.cursor()


    def gExcuteCmd(self, sql, repeatParam=None, commit = 0):
        '''执行命令'''
        try:
            if not repeatParam:
                n = self.cursor.execute(sql)
            else:
                n = self.cursor.executemany(sql, repeatParam)
            if commit:
                self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("数据库执行有错误")
            print(e)

    def gExcuteCmd2(self, sql, repeatParam=None, commit = 0):
        '''执行命令'''
        try:
            if not repeatParam:
                n = self.cursor2.execute(sql)
            else:
                n = self.cursor2.executemany(sql, repeatParam)
            if commit:
                self.db2.commit()
        except Exception as e:
            self.db2.rollback()
            print("数据库执行有错误")
            print(e)


    def gScroll(self,num):
        '''移动指针'''
        self.cursor.scroll(num,mode='absolute')

    def gScroll2(self,num):
        '''移动指针'''
        self.cursor2.scroll(num,mode='absolute')

    def gFetch(self,num=0):
        if num==0:
            results = self.cursor.fetchall()
        elif num==1:
            results = self.cursor.fetchone()
        elif num>1:
            results = self.cursor.fetchmany(num)
        else :
            print("参数设置错误")
            results = None
        return results

    def gFetch2(self,num=0):
        if num==0:
            results = self.cursor2.fetchall()
        elif num==1:
            results = self.cursor2.fetchone()
        elif num>1:
            results = self.cursor2.fetchmany(num)
        else :
            print("参数设置错误")
            results = None
        return results

    def gCloseDB(self):
        self.db.close()

    def gCloseDB(self):
        self.db2.close()



c = XueQiuSql()