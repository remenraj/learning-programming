# To import selenium, you need to run: "from selenium import webdriver" (and not "import selenium").
# To open the browser, run: browser = webdriver.Firefox()
# To send the browser to a URL, run: browser.get(‘https://inventwithpython.com')
# The browser.find_elements_by_css_selector() method will return a list of WebElement objects: elems = browser.find_elements_by_css_selector(‘img')
# WebElement objects have a "text" variable that contains the element's HTML in a string: elems[0].text
# The click() method will click on an element in the browser.
# The send_keys() method will type into a specific element in the browser.
# The submit() method will simulate clicking on the Submit button for a form.
# The browser can also be controlled with these methods: back(), forward(), refresh(), quit().

from selenium import webdriver
from selenium.webdriver.firefox.service import Service


# webdriver location
try:
    firefox_driver_path = r"C:\webdrivers\geckodriver.exe"
    chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
except FileNotFoundError:
    print(f"Webdriver not found")

# open the browser
service = Service(firefox_driver_path)
browser = webdriver.Firefox(service=service)

browser.get("https://automatetheboringstuff.com/")

element = browser.find_element_by_css_selector(
    ".main > main:nth-child(1) > div:nth-child(1) > ul:nth-child(19) > li:nth-child(1) > a:nth-child(1)"
)
element.click()

# # search the website
# search_element = browser.find_element_by_css_selector("#s")
# search_element.send_keys("something to search")
# search_element.submit()

# go back to the previous page
browser.back()

# go forward to the next page
browser.forward()

# refresh the page
browser.refresh()

# entire page source
element = browser.find_element_by_css_selector("html")
element.text

# close the tab
browser.quit()