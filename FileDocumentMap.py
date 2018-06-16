import csv
import settings
import util
# from pprint import pprint as pp

class FileDocumentMap(object):
    """
    Class to map the FileDocument
    """

    def __init__(self, file_path):
        self.list_title_names = None
        self.pages_list = list()
        self.table_lines = list()
        self.data_matrix = list()
        self._document_body = settings.FILE_DOCUMENT_MAP_BASELINE
        try:
            with open(file_path, encoding="Windows-1255") as input_file:
                # TODO: try - except file exists / open to read
                self.lines = input_file.read().split('\n')
                util.logger.info("File content: {} lines".format(len(self.lines)))
        except IOError as ex:
            util.logger.error("Can not open file: {}. IO ERROR: {}".format(file_path, ex))


    def process_lines(self):
        # process titles
        self.data_matrix.append(self.get_line_headers()[1:])

        self.locate_pages_part()

        _ = self.pages_list.pop(0)  # remove first page - it's the header

        for page in self.pages_list:
            start_line, end_line = page
            util.logger.debug("row_number_table_start: {} row_number_table_end: {} num_rows: {}".format(start_line,
                                                                                                        end_line,
                                                                                                end_line - start_line))
            line_counter = start_line + 8  # skip 8 lines of table header
            while line_counter < end_line:
                line_to_add = str(util.u200_strip(self.lines[line_counter]) + " " +
                                  util.u200_strip(self.lines[line_counter + 2])).strip()  # merge two data lines
                # line_to_add = [line.strip() for line in line_to_add]
                self.table_lines.append(line_to_add)
                line_counter += 4


        print("len(self.table_lines)", len(self.table_lines))
        for line in self.table_lines:
            line_to_add = line.split('|')
            self.data_matrix.append(line_to_add[1:len(line_to_add) - 1])    # skip the first and last empty items

        print(len(self.table_lines))
        self.set_table_data_pages(self.data_matrix)

    def locate_pages_part(self):
        """
        scan the lines of the file and find the pages, headers and data inside
        :return:
        """
        line_counter = 0
        page_start = 0
        page_end = 0
        scan_rows_limit = settings.ROWS_LIMIT if len(self.lines) > settings.ROWS_LIMIT else len(self.lines)
        # scan through all the file lines
        for line in self.lines[:scan_rows_limit]:
            line_counter += 1
            util.logger.debug("{} {} {}".format(line_counter, len(line), "]{}[".format(line)))

            # find page breaks
            if line.endswith(settings.ROW_TYPES["date"]):
                if self.get_header_bottom_line() is None:
                    self.set_header_bottom_line(line_counter)

                util.logger.debug('*** Page Break ***')
                self.set_table_bottom_line(line_counter)
                page_start = line_counter

                # if line.endswith("-" *  10):
                util.logger.debug('*** Line Separator ***')

            if line.endswith("\f"):
                util.logger.debug("End of table {}".format(line_counter))
                page_end = line_counter
                self.pages_list.append((page_start, page_end))
                self.set_table_bottom_line(line_counter)

            util.logger.debug("end of header {} ".format(self.get_header_bottom_line()))
            util.logger.debug("end of table {} ".format(self.get_table_bottom_line()))


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

    def set_table_data_pages(self, table_lines):
        self._document_body['table']['data_pages'] = table_lines

    def get_table_data_pages(self):
        return self._document_body['table']['data_pages']
        # return self.table_lines

    def persist(self, dest_path, file_name):
        try:
            with open(dest_path + file_name, 'w') as csvfile:
                for row in self.get_table_data_pages():
                    writer = csv.writer(csvfile, lineterminator='\n', quotechar='\'', quoting=csv.QUOTE_ALL)
                    writer.writerow(row)
        except IOError as ex:
            util.logger.error("Can not write to file {}. IO ERROR: {}".format(dest_path + file_name, ex))

    def get_line_headers(self):
        """
        get the headers from the report table
        :param lines: report text
        :return: list of headers
        """
        lines = self.lines
        list_title_names = list()
        line1 = util.u200_strip(lines[17]).split('|')
        line2 = util.u200_strip(lines[18]).split('|')
        line3 = util.u200_strip(lines[19]).split('|')
        title = zip(line1, line2, line3)
        for row in title:
            list_title_names.append(''.join(row))
        return list_title_names


class SHFileDocumentMap(FileDocumentMap):
    pass

class MRFileDocumentMap(FileDocumentMap):
    pass

