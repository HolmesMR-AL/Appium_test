import time
import base64
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    automationName='UiAutomator2'
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://127.0.0.1:4723',options = capabilities_options)
driver.implicitly_wait(5)
driver.start_recording_screen()

driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Chrome').click()

driver.find_element(AppiumBy.XPATH, '//*[@name="q"]').send_keys("Hello World")

video_rawdata = driver.stop_recording_screen()

video_name = driver.current_activity + time.strftime("%Y_%m_%d_%H%M%S")

filepath = f"videos/{video_name}.mp4"

with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_rawdata))
# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/one').click()
# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/two').click()
# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/three').click()
# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/five').click()

# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/dialpad_voice_call_button').click()


time.sleep(2)
driver.quit()
