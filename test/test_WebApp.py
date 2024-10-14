import time
import allure
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

desired_caps = dict(
    platformName="Android",
    deviceName="Android",
    automationName="UiAutomator2",
    browserName="chrome",
)

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
driver = webdriver.Remote("http://localhost:4723", options=capabilities_options)
driver.implicitly_wait(15)

pytestmark = [allure.epic("Customers Epic"), allure.feature("Test Customers Table")]


@allure.id(2)
@allure.story("Customer Table Story")
@allure.title("Customer Table Test")
# def test_open_chrome():
#     """
#     Open chrome
#     """
#     with allure.step("Open Chrome"):
#         driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Chrome").click()
#         time.sleep(2)


# @allure.step("If terms are displayed, accept them")
# def test_accept_terms():
#     """
#     Accept the terms
#     """
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
#     """
#     close the sync modal
#     """
#     try:
#         negative_button = driver.find_element(
#             AppiumBy.ID, "com.android.chrome:id/negative_button"
#         )
#         negative_button.click()
#     except NoSuchElementException:
#         pass


def test_open():
    """
    Open the ResourceZen website
    """
    with allure.step("Open ResourceZen"):
        driver.get("https://develop.resourcezen.co.za/home")
        time.sleep(4)


def test_sign_in():
    """
    Sign in to the application
    """
    with allure.step("Sign in"):
        driver.find_element(AppiumBy.XPATH, '//input[@name="email"]').send_keys(
            "ross@al.co.za"
        )
        driver.find_element(AppiumBy.XPATH, '//input[@name="password"]').send_keys(
            "P@ssword2"
        )
        driver.find_element(AppiumBy.XPATH, "//form").click()
        time.sleep(2)
        driver.find_element(by=AppiumBy.XPATH, value="//form/button").click()


def test_close_modal():
    """
    close modal
    """
    with allure.step("close modal"):
        time.sleep(3)
        driver.find_element(
            by=AppiumBy.XPATH,
            value='//button[@aria-label="view"]',
        ).click()
        time.sleep(3)
        driver.find_element(
            by=AppiumBy.XPATH, value="//button[@data-testid='modal-close']"
        ).click()


@allure.title("Open Dashboard Menu")
def test_open_menu_then_customers():
    """
    Open the Customers page
    """
    with allure.step("Open menu"):
        driver.find_element(by=AppiumBy.XPATH, value="//header/div/button").click()
        time.sleep(1)
        driver.find_element(by=AppiumBy.XPATH, value="//ul/div[6]").click()


@allure.title("Open Dashboard Menu")
def test_cannot_submit_form():
    """
    Test that the form cannot be submitted without required fields
    """
    with allure.step("Open form"):
        try:
            driver.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="CREATE CUSTOMER"]',
            ).click()
        except NoSuchElementException:
            pass
        
        time.sleep(1)
        actions = ActionChains(driver)
        # override as 'touch' pointer action
        actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(870, 2600)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(2)
        actions.w3c_actions.pointer_action.move_to_location(870, 1000)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
    with allure.step("Submit form"):
        driver.find_element(by=AppiumBy.XPATH, value="//button[@id='submit']").click()
        driver.find_elements(
            AppiumBy.ID,
            "customer_display_name-helper-text",
        )
    allure.attach(
        driver.get_screenshot_as_png(),
        name="full-page",
        attachment_type=allure.attachment_type.PNG,
    )
