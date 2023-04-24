import yagmail
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("YAGMAIL_PASS")
from datetime import datetime as dt
import pandas

sender = 'lauri.kyttala@gmail.com'
subject = "Open Jobs on Indeed"

yag = yagmail.SMTP(user=sender, password=token)
df = pandas.read_csv('contacts.csv')

for index, row in df.iterrows():
    contents = [f"""
        Here {row['name']} is the content of the email! 
        Hi!""",row['filepath'],
    ]
    print(row['email'])
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email Sent!")