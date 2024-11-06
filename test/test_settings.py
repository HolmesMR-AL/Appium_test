import time
import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

pytestmark = [allure.epic("Settings Epic"), allure.feature("Test Settings")]

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

@allure.id(2)
@allure.story("Settings Story")
@allure.title("Redirect to Home")
def test_open(appium_driver):
    """
    Open the ResourceZen website
    """
    with allure.step("Open ResourceZen"):
        appium_driver.get("https://develop.resourcezen.co.za/home")
        time.sleep(3)

@allure.title("Open Dashboard Menu")
@pytest.mark.usefixtures("screenshot_on_failure")
def test_open_menu_then_settings(appium_driver):
    """
    Open the Settings page
    """
    with allure.step("Open menu"):
        appium_driver.find_element(AppiumBy.XPATH, '//button[@aria-label="open drawer"]').click()
        time.sleep(1)
        appium_driver.find_element(AppiumBy.XPATH, '//div[@id="Settings"]').click()
        time.sleep(3)
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="full-page",
            attachment_type=allure.attachment_type.PNG,
        )
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
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="full-page",
            attachment_type=allure.attachment_type.PNG,
        )
        appium_driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": 500,
                "top": 300,
                "width": 200,
                "height": 1000,
                "direction": "down",
                "percent": 0.75,
            },
        )

@allure.title("Open Add Org Profile")
@pytest.mark.usefixtures("screenshot_on_failure")
def test_open_add_org(appium_driver):
    """
    Open the Add org page
    """
    with allure.step("Open Add Org page"):
        appium_driver.find_element(AppiumBy.XPATH, '//div[@id="add-org-profile"]').click()
        time.sleep(1)
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="full-page",
            attachment_type=allure.attachment_type.PNG,
        )
        appium_driver.find_element(AppiumBy.XPATH, '//button[@id="back-arrow"]').click()
        time.sleep(2)

@allure.title("Manage Current Org Profile")
@pytest.mark.usefixtures("screenshot_on_failure")
def test_manage_org_profile(appium_driver):
    """
    Open the manage current org page
    """
    with allure.step("Open Add Org page"):
        appium_driver.find_element(AppiumBy.XPATH, '//div[@id="manage-org-profile"]').click()
        time.sleep(1)
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="full-page",
            attachment_type=allure.attachment_type.PNG,
        )
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
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="full-page",
            attachment_type=allure.attachment_type.PNG,
        )
        appium_driver.execute_script(
            "mobile: swipeGesture",
            {
                "left": 500,
                "top": 300,
                "width": 200,
                "height": 1000,
                "direction": "down",
                "percent": 0.75,
            },
        )
        time.sleep(1)
        appium_driver.find_element(AppiumBy.XPATH, '//button[@id="back-arrow"]').click()
