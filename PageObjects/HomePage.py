from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObjects import AccountRegistration
class HomePage():
    lnk_my_account_xpath  = "//span[contains(text(),'My Account')]"
    lnk_register_xpath = "//a[normalize-space()='Register']"
    lnk_login_xpath = "//a[normalize-space()='Login']"
    driver = webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_my_account_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH,self.lnk_register_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.lnk_login_xpath).click()