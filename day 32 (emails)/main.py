import smtplib
import random
import datetime as dt
import pandas as pd

my_email = "dominvitaliyyy@gmail.com"
password = "tmpuknfyicthyzno"

data = pd.read_csv('birthdays.csv')

today = (dt.datetime.now().month, dt.datetime.now().day)

data_dictionary = {(data_row.month, data_row['day ']):data_row for (index, data_row) in data.iterrows()}
birthday_person = data_dictionary[today]

file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
with open(file_path) as file:
    letter = file.read()
    letter = letter.replace("[NAME]", birthday_person['name'])
    letter = letter.replace("Angela", "Vitaliy")


if today in data_dictionary:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'].strip(),
                            msg=f"Subject:Happy Birthday!\n\n{letter}")
