import logging

function_logger = logging.getLogger(__name__)
function_logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("hb_test.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.WARNING)
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)


function_logger.handlers.clear()
function_logger.addHandler(file_handler)

