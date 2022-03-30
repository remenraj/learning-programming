# Automated Cookie Clicker Game Playing Bot: https://orteil.dashnet.org/cookieclicker/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

if __name__ == "__main__":
    # webdriver location
    try:
        chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
    except FileNotFoundError:
        print(f"Webdriver not found")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://orteil.dashnet.org/cookieclicker/")


    # waiting for the webpage to load
    time.sleep(5)


    # <---------importing the save data ----------------------------------------------------------------------------------------------->

    # importing the data from text file
    try:
        SAVE_DATA_FILE = r"learning-programming\Python\51-100\57-automated-cookie-clicker-game-playing-bot\data.txt"
    except FileNotFoundError:
        print("Save data file not found")
    with open(SAVE_DATA_FILE, "r") as save_file:
        save_data = save_file.read()

    # loading the save data
    options = driver.find_element(by=By.ID, value="prefsButton")
    options.click()

    import_save = driver.find_element(by=By.XPATH, value="//*[@id='menu']/div[3]/div[3]/a[2]")
    import_save.click()

    text_area = driver.find_element(by=By.ID, value="textareaPrompt")
    text_area.send_keys(save_data)

    load = driver.find_element(by=By.ID, value="promptOption0")
    load.click()


    # waiting to complete the importing of save data
    time.sleep(3)


    # <---------running the bot-------------------------------------------------------------------------------------------------------->

    cookie = driver.find_element(by=By.ID, value="bigCookie")

    # 5 minutes from now
    five_min = time.time() + 300
    # 5 second interval for checking the available items to purchase
    five_sec_check = time.time() + 5

    while True:
        # clicking the cookie
        cookie.click()

        # break the loop after 5 minutes
        if time.time() > five_min:
            break
        
        if time.time() > five_sec_check:
            
            # scraping the available products to purchase and sorting it in the descending order
            available_products = driver.find_elements(by=By.CSS_SELECTOR, value=".product.unlocked.enabled") 
            available_products.reverse()

            # product ids of the items in the availabe products to purchase
            product_ids = ["product"+str(i) for i in range(len(available_products))]    # list 
            print(product_ids)
            product_ids.reverse()
            
            # purchasing the items
            for product_id in product_ids:
                try:
                    purchase = driver.find_element(by=By.ID, value=product_id)
                    purchase.click()
                except:
                    print("Not enough cookies to purchase")
                    
            # updating the time interval for checking the available items to purchase
            five_sec_check = time.time() + 5
            
            
            
    # <---------exporting the save data ---------------------------------------------------------------------------------------------->

    export_save = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[18]/div[2]/div[4]/div[3]/div[3]/a[1]")
    export_save.click()

    text_area = driver.find_element(by=By.ID, value="textareaPrompt")
    save_data = text_area.text
    print(save_data)
    # writing the save data into a file
    with open(SAVE_DATA_FILE, "w") as save_file:
        save_file.write(save_data)
        
    all_done = driver.find_element(by=By.ID, value="promptOption0")
    all_done.click()        



    # scraping the current total cookies, cookies per second and printing it
    cookie_details = driver.find_element(by=By.ID, value="cookies").text
    print(f"cookie details: {cookie_details}")
    total_cookies = int(cookie_details.split(" ")[0])
    cookies_per_second = int(cookie_details.split(": ")[1])
    print(f"total: {total_cookies}")
    print(f"per second: {cookies_per_second}")


