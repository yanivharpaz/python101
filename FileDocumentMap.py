import csv


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
                                             'bottom_line': None,
                                             'data_pages': None
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

    def set_table_data_pages(self, table_lines):
        self._document_body['table']['data_pages'] = table_lines

    def get_table_data_pages(self):
        return self._document_body['table']['data_pages']

    def persist(self, dest_path, file_name):
        with open(dest_path + file_name, 'w') as csvfile:
            for row in self.get_table_data_pages():
                writer = csv.writer(csvfile, lineterminator='\n', quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow(row)


class SHFileDocumentMap(FileDocumentMap):
    pass

class MRFileDocumentMap(FileDocumentMap):
    pass

