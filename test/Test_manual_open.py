# import time
# import allure
# from appium import webdriver
# from appium.options.android import UiAutomator2Options
# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.common.exceptions import NoSuchElementException

# desired_caps = dict(
#     platformName="Android",
#     deviceName="Android",
#     automationName="UiAutomator2",
# )

# capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
# driver = webdriver.Remote("http://localhost:4723", options=capabilities_options)
# driver.implicitly_wait(2)

# pytestmark = [allure.epic("Google Epic"), allure.feature("Manually open google")]

# @allure.id(1)
# @allure.story("Simple Google story")
# @allure.title("Simple Google Test")
# def test_open_chrome():
#     with allure.step("Open Chrome"):
#         driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Chrome").click()

# @allure.step("If terms are displayed, accept them")
# def test_accept_terms():
#     try:
#         terms_accept_button = driver.find_element(
#             AppiumBy.ID, "com.android.chrome:id/terms_accept"
#         )
#         with allure.step("Terms detected, accept them"):
#             terms_accept_button.click()
#     except NoSuchElementException:
#         pass

# @allure.step("After accepting terms, dismiss sync")
# def test_dismiss_negative_button():
#     try:
#         negative_button = driver.find_element(
#             AppiumBy.ID, "com.android.chrome:id/negative_button"
#         )
#         negative_button.click()
#     except NoSuchElementException:
#         pass    

# @allure.step("Type Hello World in the search box")
# def test_search_in_chrome():
#     driver.find_element(AppiumBy.ID, "com.android.chrome:id/search_box_text").send_keys(
#         "Hello World"
#     )
#     allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
