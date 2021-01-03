"""
    mysql数据库操作对象封装
"""
import pymysql
from config.configdata import GlobalVar
class OperationDatabase(object):

    def __init__(self):
        self.conn = self.get_connection()
        self.cursor = self.get_cursor()

    def get_connection(self):
        """
        host=None, user=None, password="",
        database=None, port=0, charset='',
        """
        return pymysql.connect(
            GlobalVar.MYSQL_HOST,GlobalVar.MYSQL_USER,GlobalVar.MYSQL_PASSWPRD,
            GlobalVar.MYSQL_DATABASE,GlobalVar.MYSQL_PORT,GlobalVar.MYSQL_CHARSET
        )

    def get_cursor(self):
        return self.conn.cursor()

    def fetch_one_data(self,sql,data):
        try:
            self.cursor.execute(sql,data)
            data = self.cursor.fetchone()
        except Exception as e:
            print("get_data_error",e)
        finally:
            self.source_close()
            return data

    def fetch_all_data(self,sql,data):
        try:
            self.cursor.execute(sql,data)
            data = self.cursor.fetchall()
        except Exception as e:
            print("get_data_error",e)
        finally:
            self.source_close()
            return data

    def insert_data(self,sql,data):
        try:
            self.cursor.execute(sql,data)
            self.conn.commit()
        except Exception as e:
            print("insert_data_error", e)
            self.conn.rollback()
        finally:
            self.source_close()

    def delete_data(self,sql,data):
        try:
            self.cursor.execute(sql,data)
            self.conn.commit()
        except Exception as e:
            print("delete_data_error", e)
            self.conn.rollback()
        finally:
            self.source_close()

    def update_data(self,sql,data):
        try:
            self.cursor.execute(sql,data)
            self.conn.commit()
        except Exception as e:
            print("update_data_error", e)
            self.conn.rollback()
        finally:
            self.source_close()


    def source_close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
        if self.cursor:
            self.cursor.close()
            self.cursor = None



