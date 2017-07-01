import logging
import sys

def get_logger(logLevel=None, name=None):

    logger = logging.getLogger(name or "logger.demo")
    if logLevel is not None:
        logger.setLevel(logLevel)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s %(message)s')

        stdoutHandler = logging.StreamHandler(sys.stdout)
        stdoutHandler.setFormatter(formatter)

        log_file_handler = logging.FileHandler("logger_demo.log")
        log_file_handler.setFormatter(formatter)

        logger.addHandler(stdoutHandler)
        logger.addHandler(log_file_handler)

    return logger


def main():
    logger = get_logger(logLevel=logging.INFO, name="Demo")
    logger.info("my first info")

if __name__ == "__main__":
    main()