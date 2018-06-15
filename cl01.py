import  os.path
import sys
import settings
import util
from FileDocumentMap import SHFileDocumentMap

# ------------------------------------
# updated: 15/06/2018
# ------------------------------------


# ----------------
# main
# ----------------


def get_line_headers(lines):
    """
    get the headers from the report table
    :param lines: report text
    :return: list of headers
    """
    list_title_names = list()
    line1 = util.u200_strip(lines[17]).split('|')
    line2 = util.u200_strip(lines[18]).split('|')
    line3 = util.u200_strip(lines[19]).split('|')
    title = zip(line1, line2, line3)
    for row in title:
        list_title_names.append(''.join(row))
    return list_title_names


def main(file_path= r't:\tmp\cl01.txt'):

    util.logger.info('-' * 40)
    util.logger.info('File processing | starting ')
    util.logger.info('-' * 40)
    tests_time = util.RunningTimer()  # start timer

    file_document_map = SHFileDocumentMap()

    pages_list = list()

    util.logger.info("Opening file: {}".format(file_path))

    with open(file_path, encoding="Windows-1255") as input_file:
        lines = input_file.read().split('\n')

        # title
        list_title_names = get_line_headers(lines)

        line_counter = 0
        page_start = 0
        page_end = 0

        for line in lines[:settings.ROWS_LIMIT]:
            line_counter += 1
            util.logger.debug("{} {} {}".format(line_counter, len(line), "]{}[".format(line)))

            # find page breaks
            if line.endswith(settings.ROW_TYPES["date"]):
                if file_document_map.get_header_bottom_line() is None:
                    file_document_map.set_header_bottom_line(line_counter)

                util.logger.debug(('*** Page Break ***'))
                file_document_map.set_table_bottom_line(line_counter)
                page_start = line_counter

            # if line.endswith("-" *  10):
                util.logger.debug('*** Line Separator ***')

            if line.endswith("\f"):
                util.logger.debug("End of table {}".format(line_counter))
                page_end = line_counter
                pages_list.append((page_start, page_end))
                file_document_map.set_table_bottom_line(line_counter)

        util.logger.debug("end of header {} ".format(file_document_map.get_header_bottom_line()))
        util.logger.debug("end of table {} ".format(file_document_map.get_table_bottom_line()))

        table_lines = list()
        table_lines.append(list_title_names[1:])  # add title to list
        _ = pages_list.pop(0)  # remove first page - it's the header

        for page in pages_list:
            start_line, end_line = page
            util.logger.debug("row_number_table_start: {} row_number_table_end: {} num_rows: {}".format(start_line,
                                                                                     end_line, end_line - start_line))
            line_counter = start_line + 8   # skip 8 lines of table header
            while line_counter < end_line:
                line_to_add = str(util.u200_strip(lines[line_counter]) + " " +
                                  util.u200_strip(lines[line_counter + 2])).split('|')   # merge two data lines
                line_to_add = [line.strip() for line in line_to_add]
                table_lines.append(line_to_add[1:len(line_to_add) - 1])
                line_counter += 4

    file_document_map.set_table_data_pages(table_lines)

    file_name = os.path.splitext((os.path.basename(file_path)))[0] + '.csv'
    #  TODO: add dest_path to argv
    dest_path = "T:\\tmp\\"

    # write data to csv file
    file_document_map.persist(dest_path, file_name)
    util.logger.info("Output file {} written to disk.".format(dest_path + file_name))

    tests_time.stop()
    util.logger.info('File processing completed. ' + tests_time.display() + " Running time.")
    util.logger.info('-' * 60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: \npython cl01.py [input_file]")
    main(sys.argv[1])
