import pymssql
import time
import datetime
import shutil


conn = pymssql.connect(server= '127.0.0.1', user='limor', password='shina', database= 'clinic')
cursor = conn.cursor()
cursor.execute('select * from mirpaot')

for row in cursor:
    # get data into variables
    catalog_type = row[1]
    StoreCode = row[2]

    # set the date and time in the required format
    now = datetime.datetime.today()
    current_date = now.strftime("%Y%m%d")
    current_time = now.strftime("%H%M%S")

    # build the file name by the required format
    NewFileName = "StoreCatalog_{}_{}_{}.xml".format(str(StoreCode), current_date, current_time)
    print(NewFileName)

    if catalog_type == 1:
        print("1")
    elif catalog_type == 2 or catalog_type == 4:
        print("2 4")
    elif catalog_type == 3:
        print(3)

