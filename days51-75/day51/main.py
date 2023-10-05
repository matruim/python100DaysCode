import time

from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 450
PROMISED_UP = 450
CHROME_DRIVER_PATH = "/Users/angela/Development/chromedriver"
TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        self.driver.find_element(By.LINK_TEXT, value="GO").click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.CSS_SELECTOR, ".result-data .download-speed").text)
        self.up = float(self.driver.find_element(By.CSS_SELECTOR, ".result-data .upload-speed").text)
        print(f"Download: {self.down} Upload: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")
        time.sleep(30)
        username_box = self.driver.find_element(By.NAME, value="text")
        username_box.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH,
                                               value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(5)
        password_box = self.driver.find_element(By.NAME, value="password")
        password_box.send_keys(TWITTER_PASSWORD)
        log_in_button = self.driver.find_element(By.XPATH,
                                                 value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        log_in_button.click()
        time.sleep(10)
        tweet_text_input = self.driver.find_element(By.XPATH,"//div[contains(@aria-label, 'Tweet text')]")
        post_button = self.driver.find_element(By.XPATH,'//div[@data-testid="tweetButtonInline"]')

        if self.down < PROMISED_DOWN:
            tweet_text_input.send_keys(
                f"@metronetfiber whats up with these speeds? Download: {self.down} Upload: {self.up}")
            post_button.click()
        else:
            tweet_text_input.send_keys(
                f"@metronetfiber Thanks for these great speeds! Download: {self.down} Upload: {self.up}")
            post_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
