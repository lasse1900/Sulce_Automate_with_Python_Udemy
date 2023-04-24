import schedule
import time
import subprocess
# https://schedule.readthedocs.io/en/stable/

def job():
    print("I'm working...")
    # Run the bash script using subprocess
    # subprocess.run("./myscript.sh")




schedule.every(10).seconds.do(job)
# schedule.every(2).minutes.do(job)
# schedule.every(15).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)