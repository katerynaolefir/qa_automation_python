import logging

function_logger = logging.getLogger(__name__)

function_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('json__olefyr.log',  mode="a")
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

function_logger.handlers.clear()

function_logger.addHandler(file_handler)
function_logger.addHandler(console_handler)
