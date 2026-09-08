from selenium.webdriver.common.by import By
from PageObjects.HomePage import HomePage

class MyAccountPage():
    lnk_my_account_xpath = "//span[contains(text(),'My Account')]"
    lnk_logout_xpath = "//a[@class='dropdown-item'][normalize-space()='Logout']"

    def __init__(self, driver):
            self.driver = driver

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH,self.lnk_my_account_xpath).click()


    def clickLogout(self):
         self.driver.find_element(By.XPATH, self.lnk_logout_xpath).click()