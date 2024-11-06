import time
import pytest
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def screenshot_on_failure(request, appium_driver):
    """
        Takes a screenshot on test failure and attaches it to the allure report
    """
    yield
    if request.node.rep_call.failed:
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )


pytestmark = [allure.epic("Customers Epic"), allure.feature("Test Customers Table")]


@allure.id(1)
@allure.story("Login and open the Customers page")
@allure.title("Connect to Home Page")
@pytest.mark.usefixtures("screenshot_on_failure")
def test_open(appium_driver):
    """
    Open the ResourceZen website
    """
    with allure.step("Open ResourceZen and login"):
        appium_driver.get("https://develop.resourcezen.co.za/home")
        time.sleep(4)
        try:
            appium_driver.find_element(
                AppiumBy.XPATH, '//input[@name="email"]'
            ).send_keys("ross@al.co.za")
            appium_driver.find_element(
                AppiumBy.XPATH, '//input[@name="password"]'
            ).send_keys("P@ssword2")
            appium_driver.find_element(AppiumBy.XPATH, "//form").click()
            time.sleep(2)
            appium_driver.find_element(AppiumBy.XPATH, '//button[@id="login"]').click()
            time.sleep(4)
        except NoSuchElementException:
            pass

@allure.story("Login and open the Customers page")
@allure.title("Open the Customers page")
@pytest.mark.usefixtures("screenshot_on_failure")
def test_open_menu_then_customers(appium_driver):
    """
    Open the Customers page
    """
    with allure.step("Open menu"):
        appium_driver.find_element(AppiumBy.XPATH, '//button[@aria-label="open drawer"]').click()
        time.sleep(1)
        appium_driver.find_element(AppiumBy.XPATH, '//div[@id="Customers"]').click()
        time.sleep(3)


@allure.story("Test the create modal submissions")
@allure.title("Test the create modal")
@pytest.mark.usefixtures("screenshot_on_failure")
def test_cannot_submit_form(appium_driver):
    """
    Test that the form cannot be submitted without required fields
    """
    with allure.step("Open form"):
        appium_driver.find_element(
            AppiumBy.XPATH,
            '//button[@id="create-customer-button"]',
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
        appium_driver.find_element(
            AppiumBy.XPATH,
            '//p[@id="customer_display_name-helper-text"]',
        )

@allure.story("Test the create modal submissions")
@allure.title("Test the create modal")
@pytest.mark.usefixtures("screenshot_on_failure")
def test_can_submit_form(appium_driver):
    """
    Test that the form can be submitted and the snackbar is working
    """        
    with allure.step("Submit form"):
        time.sleep(2)
        appium_driver.find_element(
            AppiumBy.XPATH,
            '//input[@id="customer_display_name"]',
        ).send_keys("Test Customer")
        appium_driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": 500,
                "top": 300,
                "width": 200,
                "height": 1000,
                "direction": "up",
                "percent": 1,
            },
        )
        time.sleep(2)
        appium_driver.find_element(AppiumBy.XPATH, '//button[text()="Submit"]').click()
        time.sleep(3)
        appium_driver.find_element(AppiumBy.XPATH, '//div[@role="alert"]')
