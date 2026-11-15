from pathlib import Path



BASE_FOLDER = Path(__file__).parent
TEMP_FOLDER = BASE_FOLDER / 'temp'
# RESOURCES_FOLDER = BASE_FOLDER / 'tests' / 'resources'
RESOURCES_FOLDER = Path(BASE_FOLDER, 'tests', 'resources')
LIST_IDS_FILE_PATH = Path(RESOURCES_FOLDER, 'list_of_required_user_ids.txt')

SQLITE_DB_FOLDER = BASE_FOLDER / 'test.db'

SCREENSHOTS_DIR = BASE_FOLDER / 'tests' / 'ui' / 'sause_demo' / 'screenshots'