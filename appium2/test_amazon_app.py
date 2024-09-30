import time
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = dict(

    deviceName='Android',
    platformName='Android',
    # appPackage='com.google.android.apps.nexuslauncher',
    # appActivity='com.amazon.mShop.navigation.MainActivity ',
    automationName='UiAutomator2'
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote('http://192.168.3.25:4723',options = capabilities_options)
driver.implicitly_wait(5)

driver.find_element(AppiumBy.ID,'com.google.android.apps.nexuslauncher:id/page_indicator').click()
# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/one').click()
# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/two').click()
# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/three').click()
# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/five').click()

# driver.find_element(AppiumBy.ID,'com.google.android.dialer:id/dialpad_voice_call_button').click()


time.sleep(2)
driver.quit()
