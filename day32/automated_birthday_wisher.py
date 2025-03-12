import smtplib
from datetime import datetime
import pandas
import random



#Check if today matches a birthday in birthdays.csv
#1 Create a tuple from today's month and day using datetime
today = (datetime.now().month, datetime.now().day)
today_tuple = (today.month, today.day)
MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "wxfn aepv bpwj vsfu"

#2 Use pandas to read birthdays.csv
data = pandas. read_csv("birthdays.csv")

#3 Use dictionary comprehension to create a dictionary from birthdays.csv that is formatted
#format of dictionary
# birthdays_dict = {
#     (birtday_month, birthday_day):data_row
# }

birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index,data_row) in data.iterrows()}

#4 check if today matches a birthday in birthdays.csv
#If there is a match then pick a random letter(from letter text files) from letter templates
if today_tuple  in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]",birthday_person["name"])

#5 send the letter generated in step3 to the person's email address
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg = f"Subject:Happy Birthday!\n\n{contents}")

#5 Use the replace() method to replace [name] with actual name of the person who has bday
