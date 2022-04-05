from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DataEntry():
    """Enters the data into a google form"""
    def __init__(self, url, headers) -> None:
        """Initializes the driver"""
        # webdriver location
        try:
            self.chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
        except FileNotFoundError:
            print(f"Webdriver not found")
        
        self.url = url
        service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service= service)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 60)
    
    def submit_data(self, data) -> None:
        """Submits data into the form"""

        for property in data:
            self.driver.get(self.url)
            
            time.sleep(3)
            
            # enter address
            address_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")))
            address_box.send_keys(property["address"])
            
            # enter rent
            rent_box = self.driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
            rent_box.send_keys(property["rent"])
            
            # enter link
            link_box = self.driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
            link_box.send_keys(property["link"])
            
            # click on submit button
            submit_button = self.driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
            submit_button.click()
            time.sleep(5)
            