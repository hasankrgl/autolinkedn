from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path=r"Chrome Path in your Computer"
driver=webdriver.Chrome(chrome_path)

driver.get("URL OF THE JOBS YOU ARE APPLYING AT LINKEDLN")

sign_in_button = driver.find_element_by_link_text("Oturum aç")
sign_in_button.click()
time.sleep(3)

e_mail=driver.find_element_by_id("username")
e_mail.send_keys("your e mail")
password=driver.find_element_by_id("password")
password.send_keys("your password")
password.send_keys(Keys.ENTER)

first_result = driver.find_element_by_css_selector('.jobs-search-results ul li')
first_result.click()

time.sleep(5)
jobs_apply_button = driver.find_element_by_css_selector('.jobs-apply-button--top-card button')
jobs_apply_button.click()
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()
