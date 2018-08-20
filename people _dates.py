import datetime
import sys




def create_days(current_day, days_ahead=30):
    days_list = [current_day + datetime.timedelta(days=new_day) for new_day in range(days_ahead)]
    return days_list


def main(argv):
    people = ['Yigal', 'Tal', 'Naama', 'Keren', 'Yuli', 'Limor']

    current_day = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    print(current_day)
    print(current_day + datetime.timedelta(days=1))
    days = create_days(current_day, 30)

    print(days)

    workers_placement = dict()
    # workers_day = {key: value for (key, value) in }
    employee_iterator = 0
    for day in days:
        employee_iterator += 1
        if employee_iterator > len(people):
            employee_iterator = 1
        workers_placement[day] = people[employee_iterator - 1]

    for day_key, worker_value in workers_placement.items():
        print(day_key, worker_value)



if __name__ == "__main__":
    main(sys.argv)
