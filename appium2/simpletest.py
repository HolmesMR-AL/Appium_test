import time
import os
import base64
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(
    platformName="Android",
    deviceName="Android",
    browserName="chrome",
    automationName="UiAutomator2",
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://127.0.0.1:4723", options=capabilities_options)
print("Driver is ready")
# driver.start_recording_screen()
# driver.get("https://google.com")
driver.implicitly_wait(5)
driver.find_element(AppiumBy.XPATH, '//*[@name="q"]').send_keys("Hello World")