##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
import pandas
import random

date_today = dt.datetime.today()
today_tuple = (date_today.month, date_today.day)

data = pandas.read_csv('birthdays.csv')

smtp_server = 'smtp.ethereal.email'
my_email = 'cameron.glover@ethereal.email'
my_password = '5JBCd2DC5J4vhGffWA'

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1, 3)}.txt'
    with open(file_path, "r") as letter:
        read_letter = letter.read()
        final_letter = read_letter.replace('[NAME]', birthday_person['name'])
    with smtplib.SMTP(smtp_server, 587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        print(final_letter)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person['email'],
                            msg=f'Subject: Happy Birthday!\n\n {final_letter}')

