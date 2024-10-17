import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

pytestmark = [allure.epic("JobCard Epic"), allure.feature("Test JobCard")]

@allure.id(2)
@allure.story("JobCard Story")
@allure.title("JobCardTest")

def test_open(appium_driver):
    """
    Open the ResourceZen website
    """
    with allure.step("Open ResourceZen"):
        appium_driver.get("https://develop.resourcezen.co.za/home")
        time.sleep(4)


def test_sign_in(appium_driver):
    """
    Sign in to the application if not automatically logged in
    """
    try:
        with allure.step("Sign in"):
            appium_driver.find_element(AppiumBy.XPATH, '//input[@name="email"]').send_keys(
                "ross@al.co.za"
            )
            appium_driver.find_element(AppiumBy.XPATH, '//input[@name="password"]').send_keys(
                "P@ssword2"
            )
            appium_driver.find_element(AppiumBy.XPATH, "//form").click()
            time.sleep(2)
            appium_driver.find_element(by=AppiumBy.XPATH, value="//form/button").click()
            allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="sign-in",
            attachment_type=allure.attachment_type.PNG,
            )
    except NoSuchElementException:
        pass


def test_close_modal(appium_driver):
    """
    open JobCard view modal and close it
    """
    with allure.step("close modal"):
        time.sleep(3)
        appium_driver.find_element(
            by=AppiumBy.XPATH,
            value='//button[@aria-label="view"]',
        ).click()
        time.sleep(3)
        appium_driver.find_element(
            by=AppiumBy.XPATH, value="//button[@data-testid='modal-close']"
        ).click()
