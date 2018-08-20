

DEMO_FILE = r"u:\tmp\11\results.txt"
PING_DETAILS_INDICATOR = "Reply from "


def get_ping_time(line):
    line_items = line.strip().split(" ")
    ping_time = float(line_items[-2].split("=")[1][:-2])
    return ping_time


def analyze_file(file_name=DEMO_FILE):
    times = list()
    with open(file_name) as input_file:
        for line in input_file:
            if PING_DETAILS_INDICATOR in line:
                times.append(get_ping_time(line))
    return times


if __name__ == "__main__":
    ping_times = analyze_file()
    print(ping_times)
