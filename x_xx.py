from elasticsearch import Elasticsearch
import requests, elasticsearch, sys
import datetime


def main(params):
    es = Elasticsearch()

    doc = {
        'author': 'kimchy',
        'text': 'Elasticsearch: cool. bonsai cool.',
        'timestamp': datetime.datetime.now(),
    }

    res = es.index(index="test-index", doc_type='tweet', id=2, body=doc)
    res = es.index(index="test-index", doc_type='tweet', id=3, body=doc)
    res = es.index(index="test-index", doc_type='tweet', id=4, body=doc)
    print(res['result'])

    res = es.get(index="test-index", doc_type='tweet', id=1)
    print(res['_source'])

    es.indices.refresh(index="test-index")

    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
        print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])


if __name__ == "__main__":
    print("hello...")
    main(sys.argv)





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
