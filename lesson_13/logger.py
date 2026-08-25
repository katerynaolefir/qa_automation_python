import logging

function_logger = logging.getLogger(__name__)

function_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('login_system.log',  mode="a")

file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

file_handler.setFormatter(formatter)

function_logger.handlers.clear()

function_logger.addHandler(file_handler)
