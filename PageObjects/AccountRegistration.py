from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class AccountRegistrationPage(object):

    first_name = "firstname"
    last_name = "lastname"
    email_name = "email"
    telephone_name = "telephone"
    password_name = "password"
    #confpassword_name = "confirm"
    chk_policy_name = "agree"
    btn_cont_xpath = "//button[normalize-space()='Continue']"
    account_Creation = "//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver
    def setFirstName(self, fname):
        self.driver.find_element(By.NAME, self.first_name).send_keys(fname)
    def setLastName(self, lname):
         self.driver.find_element(By.NAME, self.last_name).send_keys(lname)
    def setEmailName(self, email):
        self.driver.find_element(By.NAME, self.email_name).send_keys(email)
    def setTelephone(self, tel):
        self.driver.find_element(By.NAME, self.telephone_name).send_keys(tel)
    def setPassword(self, pwd):
        self.driver.find_element(By.NAME, self.password_name).send_keys(pwd)
    #def setConfirmPassword(self, cnfpwd):
        #self.driver.find_element(By.NAME, self.confpassword_name).send_keys(cnfpwd)
    def setPolicyName(self):
        ActionChains(self.driver).send_keys(Keys.END).perform()
        button = self.driver.find_element(By.NAME, self.chk_policy_name)
        button.click()

    def ClickContinue(self):
            ActionChains(self.driver).send_keys(Keys.END).perform()
            button = self.driver.find_element(
                By.XPATH,
                self.btn_cont_xpath
            )
            button.click()

    def getConfirmation(self):
        try:
            return self.driver.find_element(By.XPATH, self.account_Creation).text
        except:
            None

