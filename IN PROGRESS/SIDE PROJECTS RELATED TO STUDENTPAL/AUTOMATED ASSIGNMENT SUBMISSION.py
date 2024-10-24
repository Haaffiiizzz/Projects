import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

userCCID = input("Please enter your CCID: ").lower()
userPassword = input("Please enter your password: ")

driver = webdriver.Chrome()
driver.get("https://eclass.srv.ualberta.ca/portal/")

creditCourse = driver.find_element(By.ID, "uofa")
creditCourse.click()

ccid = driver.find_element(By.ID, "username")
ccid.send_keys(userCCID)

password = driver.find_element(By.ID, "user_pass")
password.send_keys(userPassword)

login = driver.find_element(By.XPATH, "//*[@value='Login']")
login.click()

menu = driver.find_element(By.ID, "user-menu-toggle")
menu.click()

profile = driver.find_element(By.XPATH, "//*[@id='carousel-item-main']/a[1]" )
profile.click()
#commit





