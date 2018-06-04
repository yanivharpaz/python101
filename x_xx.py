

xx = {1: 'one',
      2: 'two',
      3: 'three'
      }

if 1 in xx:
    print '1 is in'

print(xx)





# from pprint import pprint as pp
# from collections import defaultdict
#
# hours = defaultdict()
# for hour_counter in xrange(24):
#     current = hour_counter
#     if current < 10:
#         my_str = '0' + str(current)
#     else:
#         my_str = str(current)
#     print(hour_counter, my_str)
#     hours[my_str] = 0
#
# my_raw_rdd = sc.textFile("hdfs://ip-172-31-36-67/user/admin/trips_1m/tripdata_1m.csv")
# my_records_rdd = my_raw_rdd.flatMap(lambda line: line.split('\n'))
#
# for line in my_records_rdd.collect():
#     items = line.split(',')
#     try:
#         hours[items[1].split(' ')[1][:2]] += 1
#         hours[items[2].split(' ')[1][:2]] += 1
#     except:
#         pass
#
# hours_sorted = list()
# hours_sorted = sorted(hours.items(), key=lambda x: (-x[1], x[0]))
# pp(hours_sorted)
#
#
