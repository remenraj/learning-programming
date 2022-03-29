# Using Selenium to interact with a website: https://en.wikipedia.org/wiki/Main_Page/

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


    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://en.wikipedia.org/wiki/Main_Page/")


    # scraping the total number of articles
    article_count = driver.find_element(by=By.CSS_SELECTOR
                                        , value="#articlecount > a:nth-child(1)")                      
    # article_count.click()   # click on the article count  
    print(f"Total article count: {article_count.text}")


    # clicking a link by using find element by link text
    all_portals = driver.find_element(by=By.LINK_TEXT, value="All portals")
    # all_portals.click()


    # entering a search term in the search box
    search = driver.find_element(by=By.NAME, value="search")
    search.send_keys("Python")
    search.send_keys(Keys.RETURN)

    # closing the browser
    # driver.quit()








