from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os


class InternetSpeedTwitterBot:
    def __init__(self) -> None:

        self.ping = 0.0
        self.down = 0.0
        self.up = 0.0

        # webdriver location
        try:
            self.chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
        except FileNotFoundError:
            print(f"Webdriver not found")

        service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def get_internet_speed(self) -> None:
        """Checks the internet speed and finds the download and upload speed"""

        SPEED_TEST_URL = "https://www.speedtest.net/"
        self.driver.get(SPEED_TEST_URL)

        # clicking on the go button
        go_button = self.driver.find_element(by=By.CLASS_NAME, value="start-text")
        go_button.click()

        # waiting for the process to finish
        time.sleep(60)

        # finding the values for ping, download and upload speed.
        self.ping = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=".result-data-large.number.result-data-value.ping-speed",
        ).text
        self.down = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=".result-data-large.number.result-data-value.download-speed",
        ).text
        self.up = self.driver.find_element(
            by=By.CSS_SELECTOR,
            value=".result-data-large.number.result-data-value.upload-speed",
        ).text

    def tweet_at_provider(self) -> None:
        """Tweets the internet download, upload speed and ping at the internet provider"""

        # twitter details
        tweet_message = f"@BSNLCorporate I'm getting only {self.down} Mbps download speed and {self.up} Mbps upload speed with a ping of {self.ping}, which is really sad. When are you upgrading to 4g?"
        TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
        TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
        TWITTER_URL = "https://twitter.com/login"

        wait = WebDriverWait(self.driver, 30)
        self.driver.get(TWITTER_URL)

        username_input = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
        username_input.send_keys(TWITTER_USERNAME)

        # click on next
        next_button = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div",
        )
        next_button.click()

        # entering the password
        password_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(TWITTER_PASSWORD)

        # click on login
        login_button = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div",
        )
        login_button.click()

        # # waiting for the website to load
        # time.sleep(20)

        # entering the tweet
        enter_tweet = wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div",
                )
            )
        )
        enter_tweet.send_keys(tweet_message)

        time.sleep(1)

        # send tweet
        tweet_button = self.driver.find_element(
            by=By.XPATH,
            value="/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span",
        )
        tweet_button.click()

        time.sleep(10)
        
        self.driver.close()
