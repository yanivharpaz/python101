
import os.path
import sys
import settings
import util
# from pprint import pprint as pp

from FileDocumentMap import SHFileDocumentMap

# ------------------------------------
# updated: 15/06/2018
# ------------------------------------

# ----------------
# main
# ----------------
def main(source_path= r't:\tmp\cl01\*.*', dest_path=r'T:\tmp\''):

    util.logger.info('-' * 40)
    util.logger.info('File processing | starting ')
    util.logger.info('-' * 40)
    tests_time = util.RunningTimer()  # start timer

    util.logger.info("Opening file: {}".format(source_path))


    # init the file_document_map object
    files_to_process = [os.path.join(source_path, file_name) for file_name in os.listdir(source_path)]

    for file_path in files_to_process:
        file_document_map = SHFileDocumentMap(file_path)
        file_document_map.process_lines()

        file_name = os.path.splitext((os.path.basename(file_path)))[0] + '.csv'
        #  TODO: add dest_path to argv
        # dest_path = "T:\\tmp\\"

        # write data to csv file
        file_document_map.persist(dest_path, file_name)

        util.logger.info("Output file {} written to disk.".format(dest_path + file_name))

        tests_time.stop()
        util.logger.info('File processing completed. ' + tests_time.display() + " Running time.")
        util.logger.info('-' * 60)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: \npython cl01.py [input_file]")

    if not os.path.isfile(sys.argv[1]):
        util.logger.error("No such file in directory {}".format(sys.argv[1]))

    if not os.path.exists(sys.argv[1]):
        util.logger.error("Directory not found {}".format(sys.argv[1]))
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])