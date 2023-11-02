import logging
from datetime import datetime

class LogGen:
    @staticmethod
    def logger():
        logging.basicConfig(filename='.\\logs\\log_file.log',
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%H:%M:%S',

                            level=logging.INFO)

        logger = logging.getLogger()
        return logger
         
    

