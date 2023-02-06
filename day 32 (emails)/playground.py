import pandas as pd
import datetime as dt

data = pd.read_csv('birthdays.csv')

today = (dt.datetime.now().month, dt.datetime.now().day)

data_dictionary = {(data_row.month, data_row['day ']):data_row for (index, data_row) in data.iterrows()}
birthday_person = data_dictionary[today]
print(birthday_person['email'].strip())



