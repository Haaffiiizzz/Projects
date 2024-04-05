
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

url = "https://www.beartracks.ualberta.ca/"

# userCCID = input("Please enter your CCID: ").lower()
# userPassword = input("Please enter your password: ")


def openProfile():

    driver = webdriver.Edge()
    
    driver.get(url)

    signOn = driver.find_element(By.ID, "button")
    signOn.click()

    ccid = driver.find_element(By.ID, "username")
    ccid.send_keys("aodada")

    password = driver.find_element(By.ID, "user_pass")
    password.send_keys("Jss3ajdssk06.")

    login = driver.find_element(By.XPATH, "//*[@id='loginform']/input[3]")
    login.click()
        
    profile = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "win2div$ICField3"))
    )
    
    profile.click()
    time.sleep(3)
    print("driver shii", "\n\n\n", driver.page_source)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    DOBEL = soup.find(id = "HCR_PERSON_I_BIRTHDATE")
    print(DOBEL.text())
    
    

openProfile()
