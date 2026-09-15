import xml.etree.ElementTree as ET
import definitions
from logger import function_logger

tree = ET.parse(str(definitions.TEMP_FOLDER / 'groups.xml'))
root = tree.getroot()


def find_all_incoming_in_group():
    for group in root.findall('group'): #
        number = group.find('number')
        if number is not None:
            incoming = group.find('timingExbytes/incoming')
            if incoming is not None:
                print(f"Результат пошуку 'incoming' - {incoming.text}")
                function_logger.info(f"group {number.text} - incoming: {incoming.text}")

            else:
                print(f"Результат пошуку відсутній, 'incoming' - не знайдено")
                function_logger.info(f"group {number.text} - incoming: NOT FOUND")


find_all_incoming_in_group()