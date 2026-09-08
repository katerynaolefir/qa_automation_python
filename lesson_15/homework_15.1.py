import definitions
import csv

file_for_testing_1 = definitions.TEMP_FOLDER / 'random.csv'

with open(file_for_testing_1) as f:
    data_1 = list(csv.reader(f))

file_for_testing_2 = definitions.TEMP_FOLDER / 'random-michaels.csv'

with open(file_for_testing_2) as f:
    data_2 = list(csv.reader(f))

headers = data_1[0]
body_1 = data_1[1:]
body_2 = data_2[1:]

all_rows = body_1 + body_2

clean_rows = []
for row in all_rows:
    clean_row = []
    for value in row:
        clean_value = value.replace('.', '/')
        clean_row.append(clean_value)
    clean_rows.append(clean_row)


result_rows = []

for i in range(len(all_rows)):
    count = 0
    for j in range(len(clean_rows)):
        if clean_rows[i] == clean_rows[j]:
            count =+ 1

    if count == 1:
        result_rows.append(all_rows[i])

result_path = 'result_olefyr.csv'

with open(result_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(result_rows)

print(f"Результат порівняння збережено у {result_path}")