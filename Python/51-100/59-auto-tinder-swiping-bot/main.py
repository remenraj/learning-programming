# Automated Tinder Swiping Bot

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException
import time, os


if __name__ == "__main__":
    # webdriver location
    try:
        chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
    except FileNotFoundError:
        print(f"Webdriver not found")

    URL = "https://tinder.com/"

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()  # maximizing window
    driver.get("https://tinder.com/")

    # waiting for the webpage to load
    time.sleep(5)

    # accept the privacy settings
    privacy_accept = driver.find_element(
        by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/span"
    )
    privacy_accept.click()

    # click on the login button
    login = driver.find_element(
        by=By.XPATH,
        value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span",
    )
    login.click()

    time.sleep(10)


    # <----signing into tinder account using facebook login---------------------------------------------------------------------------->

    try:
        facebook_login = driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button",
        )
        facebook_login.click()

    except NoSuchElementException:
        time.sleep(2)
        more_options = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div[3]/span/button")
        # more_options = WebDriverWait(driver, 10).until( # 10 is the delay
        #     EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div[3]/span/button"))
        # )
        more_options.click()
        time.sleep(2)
        facebook_login = driver.find_element(
            by=By.XPATH,
            value="/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]",
        )
        facebook_login.click()


    time.sleep(4)

    # switching to the facebook login window
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    # using print to verify that it's the facebook login window that is currently target:
    print(f"Window Title: {driver.title}")

    # entering email and password into facebook
    FACEBOOK_EMAIL = os.getenv("FACEBOOK_EMAIL")
    FACEBOOK_PASSWORD = os.getenv("FACEBOOK_PASSWORD")

    time.sleep(2)
    email = driver.find_element(by=By.ID, value="email")
    email.send_keys(FACEBOOK_EMAIL)
    password = driver.find_element(by=By.ID, value="pass")
    password.send_keys(FACEBOOK_PASSWORD)

    # clicking on the login button
    fb_login = driver.find_element(by=By.NAME, value="login")
    fb_login.click()


    # <----swiping/liking profiles----------------------------------------------------------------------------------------------------------------------->

    # switching back to the base window
    driver.switch_to.window(base_window)
    print(driver.title)

    time.sleep(5)

    # clicking on allow location and notifications
    allow_location = WebDriverWait(driver, 10).until( # 10 is the delay
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div/div/div[3]/button[1]/span"))
        )
    allow_location.click()

    time.sleep(1)
    dismiss_notifications = driver.find_element(
        by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[2]/span"
    )
    dismiss_notifications.click()

    time.sleep(20)
    # liking the profiles
    like_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button")

    for _ in range(100):
        
        time.sleep(2)    
        
        try:
            like_button.click()
            time.sleep(1)
        except ElementClickInterceptedException:  # If got a match
            time.sleep(2)
            try:
                say_something_nice = driver.find_element(By.ID, 'q1673317088')
                say_something_nice.send_keys(
                    "Knock Knock!")
                send_something_nice = driver.find_element(By.XPATH,
                                                            '/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/div[3]/form/button')
                send_something_nice.click()
                time.sleep(1)
            except NoSuchElementException:  # If Tinder "add to home screen" popup
                try:
                    not_interested_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/button[2]')
                    not_interested_btn.click()
                    time.sleep(1)
                except NoSuchElementException:  # If Tinder "upgrade to premium" popup
                    no_thanks_btn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button[2]')
                    no_thanks_btn.click()
                    time.sleep(1)
                    
            try:
                like_button.click()

            #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
            except ElementClickInterceptedException:
                print("You're out of likes! Try again tomorrow!")
                break


        # # can also swipe right/like a profile by pressing the right arrow
        # from pynput.keyboard import Key, Controller
        # keyboard = Controller()
        # keyboard.press(Key.right)
        # keyboard.release(Key.right)