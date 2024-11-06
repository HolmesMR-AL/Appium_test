import time
import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

pytestmark = [allure.epic("JobCard Epic"), allure.feature("Test JobCard")]

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
@allure.story("JobCard Story")
@allure.title("JobCardTest")
def test_open(appium_driver):
    """
    Open the ResourceZen website
    """
    with allure.step("Open ResourceZen"):
        appium_driver.get("https://develop.resourcezen.co.za/home")
        time.sleep(3)

def test_close_modal(appium_driver):
    """
    open JobCard view modal and close it
    """
    with allure.step("close modal"):
        time.sleep(3)
        appium_driver.find_element(
            AppiumBy.XPATH,
            '//button[@aria-label="view"]',
        ).click()
        time.sleep(3)
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="full-page",
            attachment_type=allure.attachment_type.PNG,
        )
        appium_driver.find_element(
            AppiumBy.XPATH, "//button[@data-testid='modal-close']"
        ).click()
