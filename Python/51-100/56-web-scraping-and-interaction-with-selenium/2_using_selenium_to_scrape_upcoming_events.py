# Using selenium to scrape upcoming events from https://www.python.org/ and convert it to a dictionary

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    ## webdriver location
    try:
        chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
    except FileNotFoundError:
        print(f"Webdriver not found")


    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://python.org")

    upcoming_events = {}

    event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
    for time in event_times:
        print(time.text)

    event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget ul li a")
    for name in event_names:
        print(name.text)

    # using dictionary comprehension to create the dictionary
    upcoming_events = {i: {"time": event_times[i].text, "name": event_names[i].text} for i in range(len(event_names))}

    print(upcoming_events)



    # quiting the browser
    driver.quit()

