import sys


class FileDocumentMap(object):
    """
    Class to map the FileDocument
    """
    def __init__(self):
        self._document_body = {'header': {
                            'top_line': 1,
                            'bottom_line': None
                            },
                          'table': {
                            'top_line': None,
                            'bottom_line': None
                            },
                          'footer': {
                            'top_line': None,
                            'bottom_line': None
                            },
                          }

    def get_header_bottom_line(self):
        return self._document_body['header']['bottom_line']

    def set_header_bottom_line(self, line_number):
        self._document_body['header']['bottom_line'] = line_number
        self._document_body['table']['top_line'] = line_number + 1

    def get_table_bottom_line(self):
        return self._document_body['table']['bottom_line']

    def set_table_bottom_line(self, line_number):
        self._document_body['table']['bottom_line'] = line_number
        self._document_body['footer']['top_line'] = line_number + 1

    def persist(self, file_name):
        # TODO: save the document body to a file
        pass


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
def main(file_path=r't:\tmp\cl01.txt'):

    ROWS_LIMIT = 30000
    file_Document_map = FileDocumentMap()

    pages_list = list()

    rows_type = {
                    "date": "‎:תאריך"
                }

    print("Opening ", file_path)
    with open(file_path, encoding="Windows-1255") as input_file:
        # lines = input_file.read().strip('\u200e').split('\n')
        lines = input_file.read().split('\n')
        print(len(lines))

        line_counter = 0

        page_start = 0
        page_end = 0
        for line in lines[:ROWS_LIMIT]:
            line_counter += 1
            # line_items = line.split('\u200e')
            # print(len(line_items), line_items)
            print(line_counter, len(line), "]{}[".format(line))

            # find header lines
            if line.strip().startswith("* *"):
                print('*** Header row ***')

            # find page breaks
            if line.endswith(rows_type["date"]):
                if file_Document_map.get_header_bottom_line() is None:
                    print("setting header boundaries")
                    file_Document_map.set_header_bottom_line(line_counter)

                print('*** Page Break ***')
                file_Document_map.set_table_bottom_line(line_counter)
                page_start = line_counter

            if line.endswith("-" * 10):
                print('*** Line Separator ***')

            if line.endswith("\f"):
                print("End of table ", line_counter)

                # add page borders to the pages list
                page_end = line_counter
                pages_list.append((page_start, page_end))
                file_Document_map.set_table_bottom_line(line_counter)

        print("end of header ", file_Document_map.get_header_bottom_line())
        print("end of table ", file_Document_map.get_table_bottom_line())

        print(pages_list)
        table_lines = list()
        _ = pages_list.pop(0)       # remove first page - it's the header
        for page in pages_list:
            start_line, end_line = page
            print(start_line, end_line, end_line - start_line)
            line_counter = start_line + 8   # skip 8 lines of table header
            while line_counter < end_line:
                line_to_add = u200_strip(lines[line_counter]) + " " + u200_strip(lines[line_counter + 2])   # merge two data lines
                table_lines.append(line_to_add)
                line_counter += 4
                print(line_to_add)

        # print("table lines:", table_lines)
        #parse only table
        # for row in lines[file_Document_map.get_header_bottom_line():file_Document_map.get_table_bottom_line()]:
        #     if not (row.endswith("-" * 10) or row.endswith("\f") or len(u200_strip(row).split('|')) == 1):
        #          list_lines = u200_strip(row).split('|')
        #          print(list_lines[1:len(list_lines)-1])


    # print(sep_counter)
    print('\n\n\n')
    # print(u200_strip(lines[20]))
    # print(u200_strip(lines[21]))
    # print(20, string_dump(u200_strip(lines[20])))
    # print(21, string_dump(u200_strip(lines[21])))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: \npython cl01.py [input_file]")
    main(sys.argv[1])
