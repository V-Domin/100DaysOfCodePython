# with open('1.txt') as file_1:
#     numbers_file_1 = file_1.readlines()
#
# with open('2.txt') as file_2:
#     numbers_file_2 = file_2.readlines()
#
#
# result = [int(num) for num in numbers_file_1 if num in numbers_file_2]
# print(result)

import pandas as pd

weather_c = {
    'Monday': 12,
    'Tuesday': 14,
    'Wednesday': 15,
    'Thursday': 14,
    'Friday': 21,
    'Saturday': 22,
    'Sunday': 24,
}

# weather_f = {day:(temp_c*9/5) + 32 for (day, temp_c) in weather_c.items()}
# print(weather_f)

# for (key, value) in weather_c.items():
#     print(value)

df = pd.DataFrame(weather_c, index=[0])
# for (key, value) in df.items():
#     print(value)

for (index,row) in df.iterrows():
    if row.Monday == 12:
        print(row.Friday)