# SMTP Information
# Gmail = smtp.gmail.com
# Hotmail = smtp.live.com
# Yahoo = smtp.mail.yahoo.com

# import smtplib

# GMAIL_SMTP = "smtp.gmail.com"
# my_email = "pythontest916@gmail.com"
# app password
# password = "jsoa bzxw bjiu fjds"

# connection = smtplib.SMTP("smtp.gmail.com")
# # make connection secure
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="pythontest916@yahoo.com",
#     msg="Subject:Hello\n\nThis is the email body")
# connection.close()

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     # make connection secure
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="pythontest916@yahoo.com",
#         msg="Subject:Hello\n\nThis is the email body")


# def send_email(sender_email, sender_password, smtp_string, recipet_email, subject, body):
#     with smtplib.SMTP(smtp_string) as connection:
#         connection.starttls()
#         connection.login(user=sender_email, password=sender_password)
#         connection.sendmail(
#             from_addr=sender_email,
#             to_addrs=recipet_email,
#             msg=f"Subject:{subject}\n\n{body}")
#
# send_email(my_email, password, GMAIL_SMTP, "pythontest916@yahoo.com", "Bake sale!", "Would you like to buy a moist cupcake?")

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1980, month=7, day=19)
# print(date_of_birth)

from random import choice
import datetime
import smtplib

QUOTES_FILE = "quotes.txt"
EMAIL = "pythontest916@gmail.com"
PASSWORD = "jsoa bzxw bjiu fjds"
GMAIL_SMTP = "smtp.gmail.com"


def get_random_quote():
    with open(QUOTES_FILE) as file:
        quotes = file.readlines()
        return choice(quotes)


def is_day(day):
    now = datetime.datetime.now()
    return now.weekday() == day


def send_email(sender_email, sender_password, smtp_string, recipet_email, subject, body):
    with smtplib.SMTP(smtp_string) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipet_email,
            msg=f"Subject:{subject}\n\n{body}")

MONDAY = 0
if is_day(MONDAY):
    quote = get_random_quote()
    send_email(EMAIL, PASSWORD, GMAIL_SMTP, "pythontest916@yahoo.com", "Monday's quote", quote)