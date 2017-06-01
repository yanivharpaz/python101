import pymssql


class SsisMoveToProd(object):
    def __init__(self, packagename, jobname, dbserver='mksqlp089/instance01', databace = 'EAISSISDB'):
        self.packagename = packagename
        self.jobname = jobname
        self.dbserver = dbserver
        self.databace = databace

    def insertprocessparameterstbl(self):
        with pymssql.connect(self.dbserver,self.databace) as conn:
            with conn.cursor() as cursor:
                cursor.callproc('spInsertProcessParametersTbl_prod', self.jobname)

    def insertssisconfigurationstbl(self):
        with pymssql.connect(self.dbserver,self.databace) as conn:
            with conn.cursor() as cursor:
                cursor.callproc('spInsertSisconfigurationsTbl_prod', self.packagename)

    def insertprocesses(self):
        with pymssql.connect(self.dbserver,self.databace) as conn:
            with conn.cursor() as cursor:
                cursor.callproc('spInsertProcesses_prod', self.jobname)

    def insertexitecode(self):
        with pymssql.connect(self.dbserver,self.databace) as conn:
            with conn.cursor() as cursor:
                cursor.callproc('spInsertExiteCode_prod', self.jobname)

    def insertexitecodedescription(self):
        with pymssql.connect(self.dbserver,self.databace) as conn:
            with conn.cursor() as cursor:
                cursor.callproc('spInsertExiteCodeDescription_prod', self.jobname)




