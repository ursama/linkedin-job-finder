from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


def main():
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3352929054&f_E=1%2C2&f_JT=F%2CI&geoId=106518625&"
               "keywords=python%20developer&location=Łódź%2C%20Łódzkie%2C%20Poland&refresh=true")

    time.sleep(2)
    button = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
    button.click()
    time.sleep(2)

    email = driver.find_element(By.ID, "username")
    email.send_keys("Your Username")

    password = driver.find_element(By.ID, "password")
    password.send_keys("Your Password")

    sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    sign_in.click()

    time.sleep(2)
    job_scroll = driver.find_element(By.CLASS_NAME, 'scaffold-layout__list')
    job_scroll.click()
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.END)
    time.sleep(2)
    html.send_keys(Keys.HOME)

    jobs = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")
    for job in jobs:
        job.click()
        time.sleep(2)
        save = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]'
                                             '/div[1]/div[3]/div/button/span[1]')
        if save.text == "Save":
            save.click()

    time.sleep(2)

    driver.close()


if __name__ == "__main__":
    main()
