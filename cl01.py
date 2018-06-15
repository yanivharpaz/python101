import  os.path
import sys
from FileDocumentMap import FileDocumentMap

# ------------------------------------
# updated: 15/06/2018
# ------------------------------------

# ----------------
# general functions
# ----------------


def string_dump(input_string):
    result_list = [ord(current_char) for current_char in input_string]
    return result_list


def u200_strip(input_string):
    return input_string.replace('\u200e', ' ').strip()

# ----------------
# main
# ----------------


def main(file_path= r't:\tmp\cl01.txt'):
    ROWS_LIMIT = 30000
    file_Document_map = FileDocumentMap()

    pages_list = list()

    rows_type = {
                    "date": "‎:תאריך"
                 }

    print("Opening ",  file_path)
    with open(file_path, encoding="Windows-1255") as input_file:
        lines = input_file.read().split('\n')

        # title
        list_title_names = list()
        line1 = u200_strip(lines[17]).split('|')
        line2 = u200_strip(lines[18]).split('|')
        line3 = u200_strip(lines[19]).split('|')
        title = zip(line1, line2, line3)
        for row in title:
            list_title_names.append(''.join(row))

        line_counter = 0
        page_start = 0
        page_end = 0

        for line in lines[:ROWS_LIMIT]:
            line_counter += 1
            # print(len(line_items), line_items)
            # print(line_counter, len(line), "]{}[".format(line))

            # find header lines
            # if line.strip().startswith("* *"):
            #     print('*** Header row ***')

            list_pages = list()

            # find page breaks
            if line.endswith(rows_type["date"]):
                if file_Document_map.get_header_bottom_line() is None:
                    file_Document_map.set_header_bottom_line(line_counter)

                # print('*** Page Break ***')
                file_Document_map.set_table_bottom_line(line_counter)
                page_start = line_counter

            # if line.endswith("-" *  10):
                # print('*** Line Separator ***')

            if line.endswith("\f"):
                # print("End of table ", line_counter)
                page_end = line_counter
                pages_list.append((page_start, page_end))
                file_Document_map.set_table_bottom_line(line_counter)

        # print("end of header ", file_Document_map.get_header_bottom_line())
        # print("end of table ", file_Document_map.get_table_bottom_line())

        # print(pages_list)
        table_lines = list()
        table_lines.append(list_title_names[1:])  # add title to list
        _ = pages_list.pop(0)  # remove first page - it's the header

        for page in pages_list:
            start_line, end_line = page
            print("row_number_table_start: {} row_number_table_end: {} num_rows: {}".format(start_line, end_line, end_line - start_line))
            line_counter = start_line + 8   # skip 8 lines of table header
            while line_counter < end_line:
                line_to_add = str(u200_strip(lines[line_counter]) + " " + u200_strip(lines[line_counter + 2])).split('|')   # merge two data lines
                line_to_add = [line.strip() for line in line_to_add]
                table_lines.append(line_to_add[1:len(line_to_add) - 1])
                line_counter += 4
                print(line_to_add[1:len(line_to_add) - 1])

    file_Document_map.set_table_data_pages(table_lines)

    file_name = os.path.splitext((os.path.basename(file_path)))[0] + '.csv'
    #  TODO: add dest_path to argv
    dest_path = "T:\\tmp\\"  #"c:\\"

    # write data to csv file
    file_Document_map.persist(dest_path, file_name)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: \npython cl01.py [input_file]")
    main(sys.argv[1])