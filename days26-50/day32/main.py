# import smtplib
#
# my_email = "x@gmail.com"
# my_password = "pass"
#
# to_email = "x@yahoo.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=to_email,
#         msg="Subject: {}\n\n{}".format("Happy Birthday", "Hope if finds you well")
#     )
#
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1949, month=8, day=6)
# print(date_of_birth)

# import random
# import smtplib as smtp
# import datetime as dt
#
# from_email = "x@gmail.com"
# from_pass = ""
# email_host = "smtp.gmail.com"
# to_email = "x@yahoo.com"
# now = dt.datetime.now()
#

# def send_mail(message):
#     with smtp.SMTP(email_host) as connection:
#         connection.starttls()
#         connection.login(user=from_email, password=from_pass)
#         connection.sendmail(
#             from_addr=from_email,
#             to_addrs=to_email,
#             msg=f"Subject: Inspirational Message\n\n{message}"
#         )
#
#
# def get_quote():
#     with open("quotes.txt") as message_file:
#         data = message_file.readlines()
#         return random.choice(data)
#
#
# if now.weekday() == 1:
#     quote = get_quote()
#     send_mail(quote)


import pandas as pd
import datetime as dt
import smtplib as smtp
import random

from_email = "x@gmail.com"
from_pass = ""
email_host = "smtp.gmail.com"
now = dt.datetime.now()


def check_birthdays(month, day):
    data = pd.read_csv("birthdays.csv")
    rows = [row for (iter, row) in data.iterrows() if row["month"] == month and row["day"] == day]
    for row in rows:
        send_message(row["name"], row.email)


def send_message(name, email):
    number = random.randint(1,3)
    with open(f"letter{number}.txt") as message_file:
        letter = message_file.read()
        letter = letter.replace("[Name]", name)
    with smtp.SMTP(email_host) as connection:
        connection.starttls()
        connection.login(user=from_email, password=from_pass)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=email,
            msg=f"Subject: Happy Birthday\n\n{letter}"
        )


check_birthdays(now.month, now.day)
