import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

FOLLOWER_URL = "https://www.instagram.com/chefsteps/followers/"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = ""
PASSWORD = ""


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com")
        time.sleep(3)
        self.driver.find_element(By.NAME, value="username").send_keys(USERNAME)
        self.driver.find_element(By.NAME, value="password").send_keys(PASSWORD)
        self.driver.find_element(By.CSS_SELECTOR, value="form button[type='submit']").click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/followers/")
        time.sleep(2)
        followers_popup = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="_aano"]'))
        )
        scroll_script = "arguments[0].scrollTop = arguments[0].scrollHeight;"
        for i in range(3):
            self.driver.execute_script(scroll_script, followers_popup)
            time.sleep(2)  # Add a delay to allow time for the followers to load

    def follow(self):
        followers = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        for follower in followers:
            try:
                follower.click()
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel.click()


insta = InstaFollower()
insta.login()
insta.find_followers()
insta.follow()
