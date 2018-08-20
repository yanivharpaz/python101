import itertools


def str_lpad(num):
    return "{:02d}".format(num)


minutes = [str_lpad(minute) for minute in range(0, 60, 5)]
hours = [str_lpad(hour) for hour in range(0, 24)]
days = [str_lpad(day + 1) for day in range(7)]
docs = [str_lpad(doc + 1) for doc in range(3)]

daily_slots = [current_time for current_time in itertools.product(docs, days, hours, minutes)]
slots = [doc_id + day + hour + minute for doc_id, day, hour, minute in daily_slots]
print(slots)
