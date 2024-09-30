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
driver.start_recording_screen()

driver.get("https://google.com")
driver.implicitly_wait(5)

driver.find_element(AppiumBy.XPATH, '//*[@name="q"]').send_keys("Hello World")

video_rawdata = driver.stop_recording_screen()

video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

filepath = f"videos/{video_name}.mp4"

with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_rawdata))
