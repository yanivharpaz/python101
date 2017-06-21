import datetime
import os
import sys


def check_file_prefix(file_name, file_name_prefix):
    file_name_prefix = 'MF120.' if file_name.find('120', 0, 3) != -1 else None
    if file_name_prefix is None:
        file_name_prefix = 'MF624.' if file_name.find('624', 0, 3) != -1 else None
    return file_name_prefix


def main():
    directory = r"T:\Users\yaniv\Dropbox\Dropbox\dev\python\PycharmProjects\python101\test_MF_files"
    output_path = r"t:\Users\yaniv\Dropbox\Dropbox\dev\python\PycharmProjects\python101\out\{}.txt"

    file_names_with_error = list()
    files_to_read = os.listdir(directory)
    # files_to_read.sort()

    file_name_prefix = None

    for file_name in files_to_read:

        file_name_prefix = check_file_prefix(file_name, file_name_prefix)
        if file_name_prefix is None:
            file_names_with_error.append(file_name)
            continue

        start_timer = datetime.datetime.now()
        # line_limit = 460000
        line_counter = 0
        previous_line_prefix = "__"

        with open(directory + '/' + file_name, 'r') as input_file:

            # skip the first line of the file
            temp_first_line = next(input_file)

            first_run = True
            for line in input_file:
                # count the lines
                line_counter += 1
                if line_counter % 2000 == 0:
                    print '.',

                # break on limit
                # if line_counter >= line_limit:
                #     print("Line limit has been reached ", line_limit)
                #     break

                line_prefix = line[:3]
                # create first line
                if first_run:
                    first_run = False
                    output_file_name = output_path.format(file_name_prefix + line_prefix)
                    output_file = open(output_file_name, 'w')
                    # output_file.write(line)
                elif line_prefix != previous_line_prefix and line_prefix != '@@@':
                    # close current file and open a new file
                    print("\n\nPrefix changed {} ".format(line_prefix))
                    output_file.close()
                    previous_line_prefix = line_prefix

                    output_file_name = output_path.format(file_name_prefix + line_prefix)
                    output_file = open(output_file_name, 'w')

                previous_line_prefix = line_prefix

                # write the current line to the file
                if line_prefix != '@@@':
                    output_file.write(line)

            output_file.close()

    print('\n\n')
    print("Lines processed: ", line_counter)

    end_timer = datetime.datetime.now()
    print("Run duration: {} ".format(str(end_timer - start_timer)))

    if len(file_names_with_error) > 0:
        sys.exit("File names do not fit the expected pattern {}".format(str(file_names_with_error)))
    else:
        print("Files process complete.")


if __name__ == "__main__":
    main()
