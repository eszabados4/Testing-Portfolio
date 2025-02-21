import logging
import inspect

def create_logger(log_level=logging.DEBUG):
    #Create logger
    logger_name = inspect.stack()[1][3]
    logger =  logging.getLogger(logger_name)
    logger.setLevel(log_level)

    #Create file handler
    file_handler = logging.FileHandler("automation.log", mode="a")
    file_handler.setLevel(log_level)

    #Setting formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)

    #Add handler to the logger, avoid adding multiple handler
    if not logger.handlers:
        logger.addHandler(file_handler)

    return logger
