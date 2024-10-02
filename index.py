from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.linkedin.com/")

# navigate to the sign up page
# click the join now button or link functionality

join_now = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/p/a')
join_now.click()
time.sleep(2)

# navigate to the first form
# find the email or phone, password and agree elements

email = driver.find_element(By.ID, "email-or-phone")
email.send_keys("test@mailinator.com")
email.click()
time.sleep(3)

password = driver.find_element(By.ID, "password")
password.send_keys("Test123@")
password.click()
time.sleep(3)

agree_button = driver.find_element(By.ID, "join-form-submit")
agree_button.click()
time.sleep(2)

# mavigate to the second form
# find the first name, last name and continue elements

first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("test")
first_name.click()
time.sleep(3)

last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("account")
last_name.click()
time.sleep(3)

continue_button = driver.find_element(By.ID, "join-form-submit")
continue_button.click()
time.sleep(2)

