import time

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

desired_caps = dict(
    deviceName="Android", platformName="Android", automationName="UiAutomator2"
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options=capabilities_options)
driver.implicitly_wait(5)

def test_open_chrome():
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Chrome").click()


def test_accept_terms():
    try:
        terms_accept_button = driver.find_element(
            AppiumBy.ID, "com.android.chrome:id/terms_accept"
        )
        terms_accept_button.click()
    except NoSuchElementException:
        pass


def test_dismiss_negative_button():
    try:
        negative_button = driver.find_element(
            AppiumBy.ID, "com.android.chrome:id/negative_button"
        )
        negative_button.click()
    except NoSuchElementException:
        pass


def test_search_in_chrome():
    driver.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text").send_keys(
        "Hello World"
    )
