from __future__ import print_function
import sys
import _mssql
import pymssql

class Files(object):
    def __init__(self):
        self.files = dict()

    def load(self):
        pass


class Clinic(object):
    def __init__(self):
        self.clinic_info = dict()

    def load(self):
        pass

class IsraelClinics(object):
    def __init__(self):
        self.clinic_list = list()

    def load(self):
        pass

class DAL(object):
    def __init__(self):
        # self.connection = _mssql.connect(server='localhost', user='yaniv', password='yh', database='home01')
        # self.connection = _mssql.connect(
        #     server='HARPAZ-PC',
        #     # trusted=True,
        #     # user=r'HARPAZ-PC\yanivharpaz',
        #     # password='xxxx',
        #     database='home01')
        self.connection = pymssql.connect(
            server='HARPAZ-PC',
            database='home01')

    def query_db(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM dbo.test')

        for row in cursor:
            print('row = %r' % (row,))

    def close(self):
        self.connection.close()

def main(argv):
    files = Files()
    clinic = Clinic()
    print("Hello, trying to connect to DB")
    local_db = DAL()
    print("Connected")
    local_db.query_db()
    local_db.close()
    print("Connection Closed")



if __name__ == "__main__":
    main(sys.argv)
