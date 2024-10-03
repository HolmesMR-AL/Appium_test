import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(
    platformName="Android",
    deviceName="Android",
    automationName="UiAutomator2",
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=capabilities_options)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Chrome").click()
driver.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text").send_keys(
    "develop.resourcezen.co.za"
)
time.sleep(2)
driver.find_element(
    AppiumBy.XPATH,
    '//android.widget.TextView[@resource-id="com.android.chrome:id/line_1" and @text="https://develop.resourcezen.co.za/home"]',
).click()
time.sleep(4)
driver.find_element(
    AppiumBy.XPATH, '//android.widget.EditText[@resource-id="email"]'
).send_keys("ross@al.co.za")
driver.find_element(
    AppiumBy.XPATH, '//android.widget.EditText[@resource-id="password"]'
).send_keys("P@ssword2")
time.sleep(3)
driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="LOG IN"]').click()
time.sleep(3)
driver.find_element(AppiumBy.XPATH, '//*[@data-testid="VisibilityIcon"]').click()
time.sleep(3)
driver.find_element(AppiumBy.XPATH, '//*[@data-testid="CrossIcon"]').click()
driver.find_element(AppiumBy.XPATH, '//*[@data-testid="MenuIcon"]').click()
time.sleep(2)

# comment for PR to test the workflow to master not main
