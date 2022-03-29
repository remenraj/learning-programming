# Automate filling out forms and clicking buttons with selenium at: https://secure-retreat-92358.herokuapp.com/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":
    ## webdriver location
    try:
        chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
    except FileNotFoundError:
        print(f"Webdriver not found")

    # opening the browser and navigating to the website
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://secure-retreat-92358.herokuapp.com/")

    # entering the details
    first_name = driver.find_element(by=By.NAME, value="fName")
    first_name.send_keys("John")
    last_name = driver.find_element(by=By.NAME, value="lName")
    last_name.send_keys("Doe")
    email = driver.find_element(by=By.NAME, value="email")
    email.send_keys("johndoe@gmail.com")

    # clicking the sign up button
    sign_up_button = driver.find_element(by=By.CLASS_NAME, value="btn")
    sign_up_button.click()
