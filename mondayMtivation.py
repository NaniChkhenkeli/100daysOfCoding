import random
import datetime as dt
import smtplib
#
# my_email = "chkhnani@gmail.com"
# password = "abc123"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="chKeta@gmail.com",msg="Subject:hello")
# connection.close()

MY_EMAIL = "chkhnn@gmail.com"
MY_PASSWORD = "abcdef123"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"subject:monday motivation\n\n{quote}")


