##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
from random import choice
import smtplib

BIRTHDAY_DATA_FILE = "birthdays.csv"
NAME_DATA_COLUMN = "name"
EMAIL_DATA_COLUMN = "email"
MONTH_DATA_COLUMN = "month"
DAY_DATA_COLUMN = "day"
EMAIL = "pythontest916@gmail.com"
PASSWORD = "jsoa bzxw bjiu fjds"
GMAIL_SMTP = "smtp.gmail.com"

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]


def send_email(sender_email, sender_password, smtp_string, recipet_email, subject, body):
    with smtplib.SMTP(smtp_string) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=recipet_email,
            msg=f"Subject:{subject}\n\n{body}")


data = pandas.read_csv(BIRTHDAY_DATA_FILE)
now = dt.datetime.now()

birthdays = [row for index, row in data.iterrows() if now.month == row[MONTH_DATA_COLUMN]
             and now.day == row[DAY_DATA_COLUMN]]

for entry in birthdays:
    name = entry[NAME_DATA_COLUMN]
    email = entry[EMAIL_DATA_COLUMN]

    with open(choice(letters)) as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", name)
        send_email(EMAIL, PASSWORD, GMAIL_SMTP, email, "Happy birthday", letter_content)
