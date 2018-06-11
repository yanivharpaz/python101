import sys

def main(file_path = r"t:\tmp\TransportFiles.txt"):

    print("Processing:", file_path)

    rows_type = {
            "clinic": "Clinic_",    # line type #1
            "moved": "moved.",      # line type #2
    }

    rows_count = 0
    ROWS_LIMIT = 10000
    ROWS_FEEDBACK = 100

    clinics_count = 0
    previous_date = 0
    previous_hour = 0
    previous_time = 0

    clinic_date = 0
    clinic_hour = 0
    clinic_time = 0

    files_moved = 0
    clinic_files_moved = 0

    with open(file_path, "r") as input_file:
        lines = input_file.read().split("\n")

        # process lines
        for line in lines:
            rows_count += 1
            # break if rows limit reached
            if rows_count > ROWS_LIMIT:
                print("\n\nRows limit {} reached. breaking...".format(ROWS_LIMIT))
                break

            # print feedback - just to see it's running
            if rows_count % ROWS_FEEDBACK == 0:
                print(".", end="")

            # process line type #1
            if line.startswith(rows_type["clinic"]):
                clinics_count += 1
                clinic_code = line.split(" ")[0].split("_")[1]
                clinic_date = int(str(line.split(" ")[2].split("/")[2]) +
                                str(line.split(" ")[2].split("/")[0]) +
                                str(line.split(" ")[2].split("/")[1]))

                time_to_process = line.split()[3]
                clinic_hour = int(str(time_to_process.split(":")[0]))
                clinic_time = int(str(time_to_process.split(":")[0]) + str(time_to_process.split(":")[1]))
                # process line type #2
            elif line.endswith(rows_type["moved"]):
                files_moved += int(line.split(" ")[-3])
                clinic_files_moved += 1

            # on the first run
            if previous_date == 0:
                previous_date = clinic_date
                previous_hour = clinic_hour
                previous_time = clinic_time

            # encountered new run info - print summary of current run
            if clinic_date != previous_date or clinic_hour != previous_hour:
                print("\nClinic date / hour changed ", previous_date, previous_hour, " to ", clinic_date, clinic_hour)
                print("Completed at ", previous_time)
                print("Clinics scanned: ", clinics_count)
                print("Files moved: ", files_moved)
                print("Clinics with files moved: ", clinic_files_moved)
                clinics_count = 0
                files_moved = 0
                clinic_files_moved = 0

            previous_date = clinic_date
            previous_hour = clinic_hour
            previous_time = clinic_time

    print("{} Rows processed.".format(rows_count))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: \npython analyze_transport.py [input_file]")
    main(sys.argv[1])
