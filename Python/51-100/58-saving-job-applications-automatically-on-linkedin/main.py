#! usr/bin/env python3

# Saving job applications on Linkedin automatically
# program that can use LinkedIn's "Easy Apply" function to send applications to all the jobs 
# that meet your criteria (instead of just a single listing)

import os, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    # webdriver location
    try:
        chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
    except FileNotFoundError:
        print(f"Webdriver not found")

    URL = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

    # launching the browser and navigating to the URL
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(URL)

    # clicking on sign in button
    sign_in = driver.find_element(by=By.LINK_TEXT, value="Sign in")
    sign_in.click()

    # filling in sign in details
    LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
    LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")


    # entering the email and password
    email = driver.find_element(by=By.ID, value="username")
    email.send_keys(LINKEDIN_EMAIL)
    password = driver.find_element(by=By.ID, value="password")
    password.send_keys(LINKEDIN_PASSWORD)
    # clicking on sign in button
    sign_in = driver.find_element(by=By.CSS_SELECTOR, value=".btn__primary--large.from__button--floating")
    sign_in.click()

    # saving the first 5 job listings
    for i in range(1, 5):
        job_listing = driver.find_element(by=By.XPATH, value=f"/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{i}]")
        job_listing.click()
        
        time.sleep(2)
        
        save = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/div[1]/div/div[2]/div[3]/div/button/span[1]")
        save.click()




