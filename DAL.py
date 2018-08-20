import pymssql

class DAL(object):
    def __init__(self):
        try:
            self.connection = pymssql.connect(server=settings.db_connection['Server'],
                                              database=settings.db_connection['Database'])

        except _mssql.MssqlDatabaseException as e:
            util.logger.error('database exception ' + str(e))
        except _mssql.MSSQLDriverException as e:
            util.logger.error('database exception ' + str(e))