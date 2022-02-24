import psycopg2
# from psycopg2 import sql
from psycopg2.extras import DictCursor


class POSTGRES():

    def __init__(self, param):
        for key, value in param.items():
            if key == 'host':
                self.host = value
            if key == 'dbname':
                self.dbname = value
            if key == 'user':
                self.user = value
            if key == 'password':
                self.password = value
            if key == 'port':
                self.port = value
        self.db = psycopg2.connect(
            host=self.host, dbname=self.dbname, password=self.password, port=self.port)
        self.cursor = self.db.cursor(cursor_factory=DictCursor)

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def _execute(self, query, args={}):
        self.cursor.execute(query, args)
        rows = self.cursor.fetchall()
        return rows

    def commit(self):
        self.cursor.commit()


class POSTGRESCRUD(POSTGRES):

    def insertDB(self, schema, table, column, data):
        if type(data) is tuple:
            query = f"INSERT INTO {schema}.{table}{column} VALUES {data}"
        else:
            query = f"INSERT INTO {schema}.{table}{column} VALUES ({data})"

        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print("Insert DB Error", e)

    def readDB(self, schema, table, column):
        '''
        column: str
        '''
        query = f"SELECT {column} from {schema}.{table}"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
        except Exception as e:
            result = ("Read DB Error", e)
        return result

    def deleteDB(self, schema, table, condition=None):
        if condition==None:
            query = f"DELETE from {schema}.{table}"
        else:
            query = f"DELETE from {schema}.{table} where {condition}"
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print("Delete DB Error", e)

    def updateDB(self, schema, table, column, value, condition):
        '''
        single-condition: "column='data'"
        multi-condition: "column1='data1' and column2='data2'"
        '''
        query = f"UPDATE {schema}.{table} SET {column}='{value}' WHERE {condition}"
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print("Update DB Error", e)