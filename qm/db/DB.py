import psycopg2
from psycopg2.extras import DictCursor


class DBINFO():

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

        try:
            self.db = psycopg2.connect(
                host=self.host, dbname=self.dbname, password=self.password, port=self.port, user=self.user)
            self.cursor = self.db.cursor(cursor_factory=DictCursor)
        except Exception as e:
            print("DB connection error: ", e)

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

    def insertDB(self, table, value, column=''):
        if type(value) is tuple:
            query = f"INSERT INTO {table}{column} VALUES {value}"
        else:
            query = f"INSERT INTO {table}{column} VALUES ({value})"

        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print("Insert DB Error", e)

    def readDB(self, table, column):
        '''
        column: str
        '''
        query = f"SELECT {column} from {table}"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
        except Exception as e:
            result = ("Read DB Error", e)
        return result

    def deleteDB(self, table, condition=None):
        if condition == None:
            query = f"DELETE from {table}"
        else:
            query = f"DELETE from {table} where {condition}"
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print("Delete DB Error", e)

    def updateDB(self, table, column, value, condition):
        '''
        single-condition: "column='data'"
        multi-condition: "column1='data1' and column2='data2'"
        '''
        query = f"UPDATE {table} SET {column}='{value}' WHERE {condition}"
        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print("Update DB Error", e)

    def upsertDB(self, table, value, target, action='NOTHING', column=''):
        '''
        - action
            - NOTHING
            - UPDATE SET ({col1}, {col2}) = ({val1}, {val2})
        '''
        if type(value) is tuple:
            query = f"INSERT INTO {table}{column} VALUES {value} ON CONFLICT ({target}) DO {action}"
        else:
            query = f"INSERT INTO {table}{column} VALUES ({value}) ON CONFLICT ({target}) DO {action}"

        try:
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print("Upsert DB Error", e)
