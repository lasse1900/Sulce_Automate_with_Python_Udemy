from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service('c:\\bin\\chromedriver.exe')
# service = Service('c:/bin/chromedriver.exe') on Mac

def get_driver():
    # Set options
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infoboards")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def main():
    driver = get_driver()
    driver.find_element(by="id",value="id_username").send_keys("automated")
    time.sleep(1)
    driver.find_element(by="id",value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(1)
    # Click Home
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)

print(main())