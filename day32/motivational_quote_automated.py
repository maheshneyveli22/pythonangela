import datetime as dt
import random
import smtplib

#get todays date and time
MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "wxfn aepv bpwj vsfu"
now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
#Weeekday 1 means monday
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        print(all_quotes)
        print(type(all_quotes))
        randomquote= random.choice(all_quotes)
        print(randomquote)


        with smtplib.SMTP("smtp.gmail.com") as connection
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg= f"Subject:Monday motivation\n\n{randomquote}")
