import definitions
import csv

file_for_testing_1 = definitions.TEMP_FOLDER / 'random.csv'

with open(file_for_testing_1, newline='') as f:
    data_1 = list(csv.reader(f))

file_for_testing_2 = definitions.TEMP_FOLDER / 'random-michaels.csv'

with open(file_for_testing_2, newline='') as f:
    data_2 = list(csv.reader(f))

headers = data_1[0]
body_1 = data_1[1:]
body_2 = data_2[1:]

all_rows = body_1 + body_2

unique_rows = set()
for row in all_rows:
    unique_rows.add(tuple(row))


result_path = 'result_olefyr.csv'

with open(result_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(unique_rows)

print(f"Результат порівняння збережено у {result_path}")