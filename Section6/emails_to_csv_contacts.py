import yagmail
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("YAGMAIL_PASS")
import time
from datetime import datetime as dt
import pandas
# https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
# https://www.pythonanywhere.com/

sender = 'lauri.kyttala@gmail.com'

subject = "This is the subject!"


yag = yagmail.SMTP(user=sender, password=token)


df = pandas.read_csv('contacts.csv')
# print(df)

for index, row in df.iterrows():
  contents = f"""
Here {row['name']} is the content of the email! 
Hi!
"""
  print(row['email'])
  yag.send(to=row['email'], subject=subject, contents=contents)
  print("Email Sent!")
