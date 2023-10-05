from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3732237241&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
# Login
driver.find_element(By.LINK_TEXT, value="Sign in").click()
driver.find_element(By.ID, value="username").send_keys("")
driver.find_element(By.ID, value="password").send_keys("")
# Submit this
#
driver.find_element(By.LINK_TEXT, value="Apply").click()
