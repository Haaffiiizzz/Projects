
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

url = "https://www.beartracks.ualberta.ca/"

userCCID = input("Please enter your CCID: ").lower()
userPassword = input("Please enter your password: ")
info = {}

def openProfile():

    driver = webdriver.Edge()
    
    driver.get(url)

    signOn = driver.find_element(By.ID, "button")
    signOn.click()

    ccid = driver.find_element(By.ID, "username")
    ccid.send_keys(userCCID)

    password = driver.find_element(By.ID, "user_pass")
    password.send_keys(userPassword)

    login = driver.find_element(By.XPATH, "//*[@id='loginform']/input[3]")
    login.click()
        
    profile = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "win2div$ICField3"))
    )
    
    profile.click()
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    DOBEL = soup.find(id = "HCR_PERSON_I_BIRTHDATE")
    Gender = soup.find(id = "HCR_PER_PDE_I_SEX")
    Country = soup.find(id = "ZCCV_CITIZEN_VW_DESCR1")
    Status = soup.find(id = "ZCCV_CITIZEN_VW_DESCR")
    SIN = soup.find(id = "SCC_PROF_FL_DRV_NATIONAL_ID")
    info["DateOfBirth"] = DOBEL.text
    info["Gender"] = Gender.text
    info["Country"] = Country.text
    info["Status"] = Status.text
    info["SIN"] = SIN.text
    
    

openProfile()
print(info)