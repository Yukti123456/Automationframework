from datetime import datetime

import pytest
from selenium import webdriver
import os
@pytest.fixture()
def setup(browser):
#Close browser testing
    if browser == 'edge':
        driver = webdriver.Edge()
        print("Launcing Edge Browser")
    elif browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launcing Chrome Browser")
    else:
        driver = webdriver.Firefox()
        print("Launcing Firefox Browser")
    return driver

def pytest_addoption(parser): #This will get the value from CLI/hooks
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):# This will return the browser value to setup method
    return request.config.getoption("--browser")

#**********Pytest HTML Report **********
# ---------------------------------------------------------
# 1. Add environment information to HTML report
# ---------------------------------------------------------

def pytest_configure(config):
    """
    Add project/environment information to HTML report.
    """

    if hasattr(config, "_metadata"):
        config._metadata["Project Name"] = "OpenCart Automation"
        config._metadata["Module Name"] = "Registration"
        config._metadata["Tester"] = "Yukti Sahu"
        config._metadata["Environment"] = "QA"
        config._metadata["Browser"] = "Chrome"


# ---------------------------------------------------------
# 2. Modify environment information before HTML report
# ---------------------------------------------------------

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    """
    Modify metadata displayed in the HTML report.
    """

    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

    metadata["Project Name"] = "OpenCart Automation"
    metadata["Module Name"] = "Registration"
    metadata["Tester"] = "Yukti Sahu"
    metadata["Environment"] = "QA"
    metadata["Browser"] = "Chrome"

#Specifying report location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
     config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html" #due to this we no nmeed to wrie command in command prompt
