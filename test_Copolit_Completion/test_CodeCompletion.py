from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.get("https://example.com/login")  # Replace with the actual login URL

    # Create an instance of the AccountLoginPage
    login_page = AccountLoginPage(driver)

    # Set email and password
    login_page.setEmail("