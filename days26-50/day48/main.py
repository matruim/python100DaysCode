from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep window open after finish
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.amazon.com/Teyleten-Robot-ESP-WROOM-32-Development-Microcontroller/dp/B08246MCL5/ref=sr_1_1_sspa?crid=15JP267RFG79X&keywords=esp32&qid=1696280661&sprefix=esp3%2Caps%2C168&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# price = f"${price_dollar.text}.{price_cents.text}"
#
# print(price)


# Challenge 1 web scrape upcoming event dates and names from python.org

# driver.get("https://www.python.org/")
#
# event_widget = driver.find_element(By.CLASS_NAME, value="event-widget")
# dates = event_widget.find_elements(By.CSS_SELECTOR, value=".menu li time")
# names = event_widget.find_elements(By.CSS_SELECTOR, value=".menu li a")
# events = {}
#
# for index, date in enumerate(dates):
#     print(f"{index}: {date.text} - {names[index].text}")
#     events[index] = {date.text, names[index].text}
#
# print(events)


# Challenge 2 web scrape from wikipedia the number of articles in english
#
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article.text)


# Interacting with webpages
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# article.click()
#
# search_bar = driver.find_element(By.NAME, value="search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

# Challenge 3 fill out a form
# driver.get("http://secure-retreat-92358.herokuapp.com/")
# form = driver.find_element(By.TAG_NAME, value="form")
# first_name = form.find_element(By.NAME, value="fName")
# last_name = form.find_element(By.NAME, value="lName")
# email = form.find_element(By.NAME, value="email")
# submit = form.find_element(By.TAG_NAME, value="button")
#
# first_name.send_keys("Jared")
# last_name.send_keys("Good")
# email.send_keys("joe@work.com")
# submit.click()


# Challenge 4 Cookie Clicker Game
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver.get("http://orteil.dashnet.org/cookieclicker/")
try:
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN"))
    )

    driver.find_element(By.ID, value="langSelect-EN").click()

except:
    driver.quit()

try:
    elem = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "bigCookie"))
    )

    cookie = driver.find_element(By.ID, value="bigCookie")
    print(cookie.id)
    store = driver.find_element(By.ID, value="store")
    t_end = time.time() + 60 * 5
    while True:
        cookie.click()
        products = store.find_elements(By.CLASS_NAME, value="enabled")
        if len(products) > 0:
            products.reverse()
            products[0].click()
finally:
    print("done")
# driver.quit()
