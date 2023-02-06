import smtplib
import datetime as dt
import random

my_email = "dominvitaliyyy@gmail.com"
password = "tmpuknfyicthyzno"


with open("quotes.txt", 'r') as file:
    data = file.readlines()

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 3:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="weaary2002@gmail.com",
                            msg=f"Subject:-VD. Reminder\n\n{random.choice(data)}\nHave a beautiful day, my Love!\nVitaliy")





