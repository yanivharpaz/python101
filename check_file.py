import os
import time
import traceback


def get_file_size_date(full_path):
    result = None
    file_size = 0
    file_date_string = ""
    try:
        file_size = os.stat(full_path).st_size
        file_date_string = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(full_path).st_mtime))
        result = (file_size, file_date_string)
    except WindowsError:
        print("Error! File {} not found.".format(full_path))
        # print(traceback.print_exc())

    return result


my_path = r'd:\tmp\02\y.pdf'
print(get_file_size_date(my_path))

# for root, dirs, files in os.walk(some_directory):
#     for fn in files:
#         path = os.path.join(root, fn)
#         size = os.stat(path).st_size # in bytes
#         print(fn, dir(os.stat(path)))
#         print(os.stat(path).st_size)
#         print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(path).st_atime)))
#         print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(path).st_ctime)))
#         print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(path).st_mtime)))


#time.strftime('%Y-%m-%d %H:%M:%S'