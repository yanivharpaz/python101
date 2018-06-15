import  os.path
import sys
import settings
import util
from pprint import pprint as pp

from FileDocumentMap import SHFileDocumentMap

# ------------------------------------
# updated: 15/06/2018
# ------------------------------------

# ----------------
# main
# ----------------
def main(file_path= r't:\tmp\cl01.txt'):

    util.logger.info('-' * 40)
    util.logger.info('File processing | starting ')
    util.logger.info('-' * 40)
    tests_time = util.RunningTimer()  # start timer

    util.logger.info("Opening file: {}".format(file_path))


    # init the file_document_map object
    file_document_map = SHFileDocumentMap(file_path)
    file_document_map.process_lines()

    file_name = os.path.splitext((os.path.basename(file_path)))[0] + '.csv'
    #  TODO: add dest_path to argv
    dest_path = "T:\\tmp\\"

    # write data to csv file
    file_document_map.persist(dest_path, file_name)
    # pp(file_document_map.table_lines)
    util.logger.info("Output file {} written to disk.".format(dest_path + file_name))



    tests_time.stop()
    util.logger.info('File processing completed. ' + tests_time.display() + " Running time.")
    util.logger.info('-' * 60)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: \npython cl01.py [input_file]")
    main(sys.argv[1])
