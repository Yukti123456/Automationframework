from PageObjects.HomePage import HomePage
from PageObjects.MyAccount import MyAccountPage
from PageObjects.AccountLogin import AccountLoginPage
from Utilities import randomString
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Utilities import XLUtils
import  os
from time import sleep
from Utilities import readProperties
from Utilities.customLogger import LogGen

class Test_001_AccountLogin_DDT:
    #Fetching the base URL from config.ini file using ReadConfig class
    baseURL = readProperties.ReadConfig.getApplicationURL()
    loggen = LogGen.logger()
    path = os.path.abspath((os.curdir)+ "\\TestData\\TestData.xlsx")

    def test_login_ddt(self,setup):
        self.loggen.info("**** Starting test_003 Login_Datadriven****")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status =[] # Empty List to store Results

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp = HomePage(self.driver) # Homepage object class
        self.lp = AccountLoginPage(self.driver) # AccountLoginpage object class
        self.account = MyAccountPage(self.driver) # AccountRegistrationpage object

        for r in range(2,self.rows+1):
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email = XLUtils.readData(self.path,"Sheet1",r,1)
            self.password = XLUtils.readData(self.path, "Sheet1",r,2)
            self.exp = XLUtils.readData(self.path, "Sheet1",r,3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.ClickBtn()
            sleep(2)
            self.res= self.lp.getConfirmation()

            if self.exp=="Valid":
               if self.res == True:
                   lst_status.append("Pass")
                   self.account.clickMyAccount()
                   self.account.clickLogout()
               else:
                   lst_status.append("Fail")
            elif self.exp=="Invalid":
                if self.res == False:
                   lst_status.append("pass")
                else:
                    lst_status.append("Fail")
                    self.account.clickMyAccount()
                    self.account.clickLogout()
        self.driver.close()
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.loggen.info("***End of test_003 Login_Datadriven****")



