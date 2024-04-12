
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains

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

    profile = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='win30div$ICField21']/img"))
    )
    
    profile = driver.find_element(By.XPATH, "//*[@id='win30div$ICField21']")
    
    profile.click()

    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "HCR_PERSON_I_BIRTHDATE"))
)


    soup = BeautifulSoup(driver.page_source, "html.parser")
    DOB = soup.find(id = "HCR_PERSON_I_BIRTHDATE")
    Gender = soup.find(id = "HCR_PER_PDE_I_SEX")
    Country = soup.find(id = "ZCCV_CITIZEN_VW_DESCR1")
    Status = soup.find(id = "ZCCV_CITIZEN_VW_DESCR")
    SIN = soup.find(id = "SCC_PROF_FL_DRV_NATIONAL_ID")
    info["DateOfBirth"] = DOB.text
    info["Gender"] = Gender.text
    info["Country"] = Country.text
    info["Status"] = Status.text
    info["SIN"] = SIN.text

    nameSect = driver.find_element(By.XPATH, "//*[@id='SCC_NAMES_H$0_row_0']/td[1]")
    ActionChains(driver).move_to_element(nameSect).perform()
    nameSect.click()

    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//*[@id='HCR_UPDNMFL_DVW_FIRST_NAME$1']"))
)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    firstName = soup.find(id = "HCR_UPDNMFL_DVW_FIRST_NAME$1").text
    middleName = soup.find(id = "HCR_UPDNMFL_DVW_MIDDLE_NAME$2").text
    lastName = soup.find(id = "HCR_UPDNMFL_DVW_MIDDLE_NAME").text

    info["Name"] = f"{firstName} {middleName} {lastName}"

openProfile()
print(info)