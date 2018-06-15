import logging

# ----------------------
# files processing
# ----------------------
ROWS_LIMIT = -1
ROW_TYPES = {
    "date": "‎:תאריך"
}

# ----------------------
# Logger
# ----------------------
logger_name = "clalit_file_processing"              # unique name for the logger
logger_file_name = logger_name + ".log"             # file name for the log file handler
log_file_debug_level = logging.DEBUG                # log level for the log file
console_debug_level = logging.INFO                  # log level for the window console
