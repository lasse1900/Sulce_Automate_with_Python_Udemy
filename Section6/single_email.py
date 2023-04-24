import yagmail
import os
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("YAGMAIL_PASS")
print("token", token)
# https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
# https://www.pythonanywhere.com/

sender = 'lauri.kyttala@gmail.com'
receiver = 'lauri.kyttala@etteplan.com'

subject = "This is the subject!"


contents = """
Here is the content of the email! 
Hi!
"""

yag = yagmail.SMTP(user=sender, password=token)
yag.send(to=receiver, subject=subject, contents=contents)
print("Email Sent!")