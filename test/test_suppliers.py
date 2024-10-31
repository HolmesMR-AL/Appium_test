import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

pytestmark = [allure.epic("Suppliers Epic"), allure.feature("Test Suppliers Table")]


@allure.id(3)
@allure.story("Supplier Table Story")
@allure.title("ResourceZen Home")
def test_open(appium_driver):
    """
    Open the ResourceZen home page
    """
    with allure.step("Open ResourceZen"):
        appium_driver.get("https://develop.resourcezen.co.za/home")
        time.sleep(4)


@allure.title("Open Dashboard Menu")
def test_open_menu_then_suppliers(appium_driver):
    """
    Open the Suppliers page
    """
    with allure.step("Open menu"):
        appium_driver.find_element(AppiumBy.XPATH, '//button[@aria-label="open drawer"]').click()
        time.sleep(1)
        appium_driver.find_element(AppiumBy.XPATH, '//div[@id="Suppliers"]').click()
        time.sleep(3)


@allure.title("Open Dashboard Menu")
def test_cannot_submit_form(appium_driver):
    """
    Test that the form cannot be submitted without required fields
    """
    with allure.step("Open form"):
        appium_driver.find_element(
            AppiumBy.XPATH,
            '//button[@id="create-supplier-button"]',
        ).click()

        time.sleep(2)
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
        time.sleep(2)
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="full-page",
            attachment_type=allure.attachment_type.PNG,
        )
        appium_driver.find_element(
            AppiumBy.XPATH,
            '//p[@id="supplier_name-helper-text"]',
        )
        time.sleep(2)
