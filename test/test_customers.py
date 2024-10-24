import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

pytestmark = [allure.epic("Customers Epic"), allure.feature("Test Customers Table")]


@allure.id(1)
@allure.story("Customer Table Story")
@allure.title("Customer Table Test")
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
            appium_driver.find_element(
                AppiumBy.XPATH, '//input[@name="email"]'
            ).send_keys("ross@al.co.za")
            appium_driver.find_element(
                AppiumBy.XPATH, '//input[@name="password"]'
            ).send_keys("P@ssword2")
            appium_driver.find_element(AppiumBy.XPATH, "//form").click()
            time.sleep(2)
            appium_driver.find_element(AppiumBy.XPATH, "//form/button").click()
            allure.attach(
                appium_driver.get_screenshot_as_png(),
                name="sign-in",
                attachment_type=allure.attachment_type.PNG,
            )
    except NoSuchElementException:
        pass


@allure.title("Open Dashboard Menu")
def test_open_menu_then_customers(appium_driver):
    """
    Open the Customers page
    """
    with allure.step("Open menu"):
        appium_driver.find_element(AppiumBy.XPATH, "//header/div/button").click()
        time.sleep(1)
        appium_driver.find_element(AppiumBy.XPATH, "//ul/div[6]").click()
        time.sleep(3)


@allure.title("Open Dashboard Menu")
def test_cannot_submit_form(appium_driver):
    """
    Test that the form cannot be submitted without required fields
    """
    with allure.step("Open form"):
        appium_driver.find_element(
            AppiumBy.XPATH,
            '//button[contains(text(), "reate")]',
        ).click()

        time.sleep(5)
    with allure.step("Submit form"):
        appium_driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": 500,
                "top": 300,
                "width": 200,
                "height": 1000,
                "direction": "up",
                "percent": 0.75,
            },
        )
        time.sleep(2)
        appium_driver.find_element(AppiumBy.XPATH, '//button[text()="Submit"]').click()
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="full-page",
            attachment_type=allure.attachment_type.PNG,
        )
        appium_driver.find_elements(
            AppiumBy.ID,
            "customer_display_name-helper-text",
        )
