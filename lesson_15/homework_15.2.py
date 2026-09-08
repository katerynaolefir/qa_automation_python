import definitions
import json
import os
from logger import function_logger

json_folder = definitions.TEMP_FOLDER / 'work_with_json'

for file in os.listdir(json_folder):
    file_path = os.path.join(json_folder, file)

    with open(file_path, "r", encoding="utf-8") as f:
        try:
            json.load(f)
            print(f"{file} - файл валідний")
        except json.JSONDecodeError as error:
            print(f"{file} - файл НЕ ВАЛІДНИЙ")
            function_logger.error(f"Error was found in {file}   -  {error}")
