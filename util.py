import os
import sys
import logging
import settings
import socket
import platform
import datetime


# --------------------------------
# files and location
# --------------------------------
def get_script_directory():
    """
    Get the python script path
    :return: path
    """
    return os.path.dirname(os.path.realpath(__file__))


def get_hostname():
    """
    Get the hostname of the current host
    :return: hostname
    """
    return socket.gethostname()


def get_ip():
    """
    Get the ip of the current host
    :return: ip
    """
    return socket.gethostbyname(socket.gethostname())

# ---------------------------------------
# string processing
# ---------------------------------------
def string_dump(input_string):
    """
    Return a list of ASCII codes for a string
    :param input_string: input string
    :return: list of ASCII codes
    """
    result_list = [ord(current_char) for current_char in input_string]
    return result_list


def u200_strip(input_string):
    """
    Remove special characters
    :param input_string: input string
    :return: string striped of the special character
    """
    return input_string.replace('\u200e', ' ').strip()


# --------------------------------
# Logger
# --------------------------------
def get_logger(log_level=None, name=None):
    """
    Initiate the logger
    :param log_level: logging level (debug / info / warning / error / critical / fatal etc.
    :param name: logger name
    :return: nothing
    """
    logger = logging.getLogger(name or settings.logger_name)
    if log_level is not None:
        logger.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setFormatter(formatter)
        stdout_handler.setLevel(settings.console_debug_level)

        log_file_handler = logging.FileHandler(get_script_directory() + '/' + settings.logger_file_name)
        log_file_handler.setFormatter(formatter)
        log_file_handler.setLevel(settings.log_file_debug_level)

        logger.addHandler(stdout_handler)
        logger.addHandler(log_file_handler)

    return logger


# initiate the logger
logger = get_logger(log_level=settings.log_file_debug_level)
logger.info("Platform : " + str(platform.uname()))
logger.info("Version :  " + str(sys.version_info))
logger.info("Hostname :  " + str(get_hostname()))
logger.info("IP Address :  " + str(get_ip()))


# ----------------------
# Timer
# ----------------------
class RunningTimer(object):
    # Class for basic timer management
    def __init__(self, remove_micro_seconds=False):
        self.end_timer = None
        if remove_micro_seconds:
            self.timer = datetime.datetime.now().replace(microsecond=0)
            self.remove_micro_seconds = remove_micro_seconds
        else:
            self.timer = datetime.datetime.now()
            self.remove_micro_seconds = remove_micro_seconds

    def restart(self, remove_micro_seconds=False):
        if remove_micro_seconds:
            self.timer = datetime.datetime.now().replace(microsecond=0)
        else:
            self.timer = datetime.datetime.now()

    def stop(self):
        if self.remove_micro_seconds:
            self.end_timer = datetime.datetime.now().replace(microsecond=0)
        else:
            self.end_timer = datetime.datetime.now()

    def display(self):
        if self.end_timer is None:
            return "The timer did not stop"
        result = str(self.end_timer - self.timer)
        return result

