import logging
from imaplib import Debug
from logging import warning, error

from coverage.debug import info_header


class log_generator_class:

    @staticmethod
    def loggen_method():
        logger = logging.getLogger()
        log_file = logging.FileHandler(r"D:\A Credence Testing\Practice\Credkart_Project\Logs\Credkart_Automation.log")
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s')
        log_file.setFormatter(log_format)
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger

 # Debug
 # info
 # warning
 # error
 # critical

