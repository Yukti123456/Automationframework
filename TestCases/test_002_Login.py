import pytest
from PageObjects.HomePage import HomePage
from PageObjects.AccountLogin import  AccountLoginPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import  os
from time import sleep
from Utilities import readProperties
from Utilities.customLogger import LogGen
from Utilities.readProperties import ReadConfig


class Test_001_Account_Login:
    #Fetching the base URL from config.ini file using ReadConfig class
    baseURL = readProperties.ReadConfig.getApplicationURL()
    loggen = LogGen.logger()
    user = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_account_reg(self,setup):
        self.loggen.info("******Login Started******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loggen.info("******Launcing Application******")
        self.driver.maximize_window()

        #Page object class object Creation of Home Page
        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.loggen.info("Click on Register Button******")
        self.hp.clickLogin()

        #Page object class object Creation of Registration Page
        self.logPage = AccountLoginPage(self.driver)
        self.loggen.info("******Entering Name******")
        self.logPage.setEmail(self.user)
        self.logPage.setPassword(self.password)
        self.logPage.ClickBtn()
        sleep(3)
        self.confirm = self.logPage.getConfirmation()

        if self.confirm == True:
            assert True
            self.loggen.info("******Account Login Successful******")
        else:
            self.loggen.error("******Account Login Failed******")
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\ScreenShots\\" + "test_account_login.png")
            assert False
        self.driver.quit()
        self.loggen.info("******Login Ended******")
