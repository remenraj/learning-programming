from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    # webdriver location
    try:
        firefox_driver_path = r"C:\webdrivers\geckodriver.exe"
        chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
    except FileNotFoundError:
        print(f"Webdriver not found")

    # # deprecated method
    # driver = webdriver.Chrome(executable_path=chrome_driver_path)
    # driver.get("https://www.google.com/")


    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    # driver = webdriver.Firefox(service=service)   # for firefox browser

    driver.get("https://python.org")

    # intro = driver.find_element_by_class_name("introduction") # deprecated method

    # finding by class name
    intro = driver.find_element(by=By.CLASS_NAME, value="introduction")
    print(intro.text)

    # getting the placeholder from search bar
    search_bar = driver.find_element(by=By.NAME, value="q")
    print(search_bar.get_attribute("placeholder"))

    # getting the documentation link by using css selector
    documentation_link = driver.find_element(
        by=By.CSS_SELECTOR,
        value=".small-widget.documentation-widget p a",  # .small-widget.documentation-widget is div class name with spaces (class="small-widget documentation-widget")
    )
    print(documentation_link.get_attribute("href"))
    print(documentation_link.text)

    # by using XPath
    submit_bug_link = driver.find_element(
        by=By.XPATH, value="//*[@id='site-map']/div[2]/div/ul/li[3]/a"
    )  # xpath is copied from the browser
    print(submit_bug_link.text)


    # close the tab
    driver.close()

    # close the browser
    driver.quit()
