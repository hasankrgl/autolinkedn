from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path=r"C:\Users\Hasan22\Desktop\Yeni klasör\chromedriver.exe"
driver=webdriver.Chrome(chrome_path)

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=91000000&keywords=python%20developer&location=Avrupa%20Birli%C4%9Fi&sortBy=R")

sign_in_button = driver.find_element_by_link_text("Oturum aç")
sign_in_button.click()
time.sleep(3)

e_mail=driver.find_element_by_id("username")
e_mail.send_keys("hasankaragol98@gmail.com")
password=driver.find_element_by_id("password")
password.send_keys("Departed22.")
password.send_keys(Keys.ENTER)

first_result = driver.find_element_by_css_selector('.jobs-search-results ul li')
first_result.click()

time.sleep(5)
jobs_apply_button = driver.find_element_by_css_selector('.jobs-apply-button--top-card button')
jobs_apply_button.click()
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()
