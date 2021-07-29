import driver as driver
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "C:/Users/Meng Chien/Desktop/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
email = "Your mail"
password = "Your password"

driver.get("https://tinder.com/")
time.sleep(3)
log_in = driver.find_element_by_xpath(
    '//*[@id="o-738591094"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in.send_keys(Keys.ENTER)
time.sleep(3)
facebook_log_in = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_log_in.click()
time.sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
# ----------------login--------------
account = driver.find_element_by_xpath('//*[@id="email"]')
password_input = driver.find_element_by_xpath('//*[@id="pass"]')
account.send_keys(email)
password_input.send_keys(password)
submit = driver.find_element_by_xpath('//*[@id="loginbutton"]')
submit.click()
# ----------------
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(5)
allow = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div/div/div[3]/button[1]')
allow.click()
dismiss = driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div/div/div[3]/button[2]')
dismiss.click()
accept_botton = driver.find_element_by_xpath('//*[@id="o-738591094"]/div/div[2]/div/div/div[1]/button')
accept_botton.click()
time.sleep(5)

for x in range(90):
    time.sleep(3)
    try:
        like_botton = driver.find_element_by_xpath('//*[@id="o-738591094"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[4]/div/div[4]/button')
        like_botton.click()
        time.sleep(1)

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
