import smtplib

my_email = "dominvitaliyyy@gmail.com"
password = "tmpuknfyicthyzno"

class NotificationManager:

    def send_message(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="deminvitaliy@yahoo.com",
                                msg=message)