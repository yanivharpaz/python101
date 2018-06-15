import sys
import logging

# ----------------------
# files processing
# ----------------------

# ROWS_LIMIT = sys.maxsize
ROWS_LIMIT = 99999999999

ROW_TYPES = {
    "date": "‎:תאריך"
}

FILE_DOCUMENT_MAP_BASELINE = {'header': {
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

# ----------------------
# Logger
# ----------------------
logger_name = "clalit_file_processing"              # unique name for the logger
logger_file_name = logger_name + ".log"             # file name for the log file handler
log_file_debug_level = logging.DEBUG                # log level for the log file
console_debug_level = logging.INFO                  # log level for the window console
