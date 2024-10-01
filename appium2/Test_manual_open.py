import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture(scope="module")
def driver_setup():
    desired_caps = dict(
        deviceName="Android", platformName="Android", automationName="UiAutomator2"
    )

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://127.0.0.1:4723", options=capabilities_options)
    driver.implicitly_wait(5)
    time.sleep(2)
    yield driver   # Provide the WebDriver instance to the test functions
    driver.quit()  # Teardown: Quit the WebDriver instance


def test_open_chrome(driver):
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Chrome").click()


def test_accept_terms(driver):
    try:
        terms_accept_button = driver.find_element(
            AppiumBy.ID, "com.android.chrome:id/terms_accept"
        )
        terms_accept_button.click()
    except NoSuchElementException:
        pass


def test_dismiss_negative_button(driver):
    try:
        negative_button = driver.find_element(
            AppiumBy.ID, "com.android.chrome:id/negative_button"
        )
        negative_button.click()
    except NoSuchElementException:
        pass


def test_search_in_chrome(driver):
    driver.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text").send_keys(
        "Hello World"
    )
