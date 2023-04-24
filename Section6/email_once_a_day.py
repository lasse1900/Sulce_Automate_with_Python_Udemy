import yagmail
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("YAGMAIL_PASS")
import time
from datetime import datetime as dt
# https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
# https://www.pythonanywhere.com/

sender = 'lauri.kyttala@gmail.com'
receiver = 'lauri.kyttala@etteplan.com'

subject = "This is the subject!"


contents = """
Here is the content of the email! 
Hi!
"""

while True:
  now = dt.now()
  if now.hour == 14 and now.minute == 46:
  # if now.hour == 7:
    yag = yagmail.SMTP(user=sender, password=token)
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")
    time.sleep(60)
    # time.sleep(3600)