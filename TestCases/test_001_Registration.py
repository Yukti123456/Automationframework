from PageObjects.HomePage import HomePage
from PageObjects.AccountRegistration import  AccountRegistrationPage
from Utilities import randomString
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import  os
from time import sleep
from Utilities import readProperties
from Utilities.customLogger import LogGen
class Test_001_AccountReg:
    #Fetching the base URL from config.ini file using ReadConfig class
    baseURL = readProperties.ReadConfig.getApplicationURL()
    loggen = LogGen.logger()
    def test_account_reg(self,setup):
        self.loggen.info("******Registration Started******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.loggen.info("******Launcing Application******")
        self.driver.maximize_window()
        #Page object class object Creation of Home Page
        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.loggen.info("Click on Register Button******")
        self.hp.clickRegister()
        #Page object class object Creation of Registration Page
        self.regPage = AccountRegistrationPage(self.driver)
        self.loggen.info("******Entering Name******")
        self.regPage.setFirstName("John")
        self.loggen.info("******Entering Last Name******")
        self.regPage.setLastName("Deo")
        self.email=randomString.random_string_generator()+'@gmail.com'
        self.regPage.setEmailName(self.email)
        self.loggen.info("******Entering Email******")
        self.regPage.setPassword("John@123")
        sleep(5)
        #self.regPage.setPolicyName()
        #self.regPage.ClickContinue()
        self.confmsg=self.regPage.getConfirmation()

        if self.confmsg == "Your Account Has Been Created!":
            assert True
            self.loggen.info("******Account Registration Successful******")
            self.driver.close()
        else:
            self.loggen.error("******Account Registration Failed******")
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\ScreenShots\\"+"test_account_reg.png")
            self.driver.close()
            assert False
        self.driver.close()
        self.loggen.info("******Registration Ended******")
