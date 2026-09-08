from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class AccountLoginPage:
    email = "input-email"
    password_id="input-password"
    login_btn ="//button[normalize-space()='Login']"
    account_confirm = "//h1[normalize-space()='My Account']"
    def __init__(self, driver):
        self.driver = driver
    def setEmail(self, user):
        self.driver.find_element(By.ID, self.email).send_keys(user)
    def setPassword(self, password):
         self.driver.find_element(By.ID, self.password_id).send_keys(password)
    def ClickBtn(self):
         self.driver.find_element(By.XPATH, self.login_btn).click()
    def getConfirmation(self):
        try:
            return self.driver.find_element(By.XPATH, self.account_confirm).is_displayed()
        except:
            return False