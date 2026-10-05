from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_valid_login_displays_logout_button():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")

        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(
            "student"
        )
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()

        logout_button = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Log out"))
        )
        assert logout_button.is_displayed()
    finally:
        driver.quit()
