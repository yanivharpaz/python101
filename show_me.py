import pymssql as sql
import DAL


def access_elastic(count_number=4067):
    my_result = {
       "count": count_number,
       "_shards": {
              "total": 335,
              "successful": 335,
              "skipped": 0,
              "failed": 0
           }
    }
    return my_result



def do_the_work():
    result = access_elastic()
    print("First result:", result['count'])
    conn = sql.connect(host='HARPAZ_DESKTOP', database='EAISSIS')
    cursor = conn.cursor()
    cursor.executemany("insert into dbo.count_medical_approval(count_doc) values(%d)", [(result['count'])])
    conn.commit()


    if __name__ == "__main__":
        do_the_work()
