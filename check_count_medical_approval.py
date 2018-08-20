import pymssql as sql
import json
import sys
from pprint import pprint as pp

def main():

    my_result = {
       "count": 4067,
       "_shards": {
              "total": 335,
              "successful": 335,
              "skipped": 0,
              "failed": 0
           }
    }

    print(my_result["count"], my_result)
    sys.exit()

    conn = sql.connect(host='HARPAZ_DESKTOP', database='EAISSIS')
    cursor = conn.cursor()
    query = "select * from TableMappingInterfaces_tbl "
    cursor.execute(query)

    rows = cursor.fetchall()
    j = json.dumps(rows)

    print(j)

    #
    # for row in cursor:
    #     print(row)
    
    conn.close()


if __name__ == '__main__':
    main()