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


pytestmark = [allure.epic("Dashboard Epic"), allure.feature("Test RZEN dashboard")]


@allure.id(2)

@allure.title("ResourceZen Home")
def test_open(appium_driver):
    """
    Open the ResourceZen home page
    """
    with allure.step("Open ResourceZen"):
        appium_driver.get("https://develop.resourcezen.co.za/home")
        time.sleep(4)

# @allure.title("Switch Organization")
# @pytest.mark.usefixtures("screenshot_on_failure")
# def test_switch_org(appium_driver):
#     """
#     Switch Organization
#     """
#     with allure.step("Open org list"):
#         appium_driver.find_element(AppiumBy.XPATH, '//div[@aria-label="Select Organisation"]').click()
#         time.sleep(2)
#         allure.attach(
#             appium_driver.get_screenshot_as_png(),
#             name="screenshot",
#             attachment_type=allure.attachment_type.PNG,
#         )
#         current_org = appium_driver.find_element(AppiumBy.XPATH, '//input')
#         if current_org.get_attribute("value") == "HolmesBro":
#             appium_driver.find_element(AppiumBy.XPATH, '//ul[@id=":r1j:"]/li[1]').click()
#         else:
#             appium_driver.find_element(AppiumBy.XPATH, '//ul[@id=":r1j:"]/li[2]').click()
