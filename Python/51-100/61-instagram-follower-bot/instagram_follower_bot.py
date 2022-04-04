from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
import time, random


class InstagramFollowerBot():

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password
                
        
        # webdriver location
        try:
            self.chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
        except FileNotFoundError:
            print(f"Webdriver not found")
            
        service = Service(self.chrome_driver_path)
        self.browser = webdriver.Chrome(service= service)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 60)
        
        
    
    def login(self) -> None:
        """ Logs into instagram """
        
        self.browser.get("https://www.instagram.com/accounts/login/")
        
        # find the username and password fields
        username_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        username_field.send_keys(self.username)
        password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field.send_keys(self.password)
        
        # find the login button and click it
        login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button")))
        login_button.click()
        
        # clicking on save info
        save_info_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/main/div/div/div/section/div/button")))
        save_info_button.click()

        # disable turn on notifications
        not_now_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")))
        not_now_button.click()
    
    def find_followers(self, target_username: str) -> None:
        """ Finds the followers of the target username """
        
        # navigate to the target user's profile
        self.browser.get(f"https://www.instagram.com/{target_username}/")
        
        # clicking on followers
        followers_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/section/main/div/header/section/ul/li[2]/a/div")))
        followers_button.click()
        
        # loading followers, at a time around 15 followers are shown, scrolling down to load more
        followers_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div[2]")))
        
        for _ in range(3):
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
            time.sleep(5)


    
    def follow(self) -> None:
        """ Follows the followers of the target username """
        # scrolling
        followers_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div/div[2]")))
        
        # scrolling down three times to load more followers
        for _ in range(3):
            self.browser.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
            time.sleep(5)

        # following the followers: follow_buttons contains a list of all the follow buttons currently loaded
        follow_buttons = self.browser.find_elements(by=By.CSS_SELECTOR, value=".sqdOP.L3NKy.y3zKF")
        for follow_button in follow_buttons:
            try:
                follow_button.click()
                
            except ElementClickInterceptedException:
                # when you are already following the user, prompt appears and cancel button is clicked
                cancel_button = self.driver.find_elements_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()
                
            else:
                # waiting for sometime to avoid being detected as a bot
                time.sleep(random.randint(1, 5))
