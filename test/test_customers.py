import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

pytestmark = [allure.epic("Customers Epic"), allure.feature("Test Customers Table")]

@allure.id(2)
@allure.story("Customer Table Story")
@allure.title("Customer Table Test")


# @allure.step("If terms are displayed, accept them")
# def test_accept_terms():
#     """
#     Accept the terms
#     """
#     try:
#         terms_accept_button = appium_driver.find_element(
#             AppiumBy.ID, "com.android.chrome:id/terms_accept"
#         )
#         with allure.step("Terms detected, accept them"):
#             terms_accept_button.click()
#     except NoSuchElementException:
#         pass


def test_open(appium_driver):
    """
    Open the ResourceZen website
    """
    with allure.step("Open ResourceZen"):
        appium_driver.get("https://develop.resourcezen.co.za/home")
        time.sleep(4)


def test_sign_in(appium_driver):
    """
    Sign in to the application if not automatically logged in
    """
    try:
        with allure.step("Sign in"):
            appium_driver.find_element(AppiumBy.XPATH, '//input[@name="email"]').send_keys(
                "ross@al.co.za"
            )
            appium_driver.find_element(AppiumBy.XPATH, '//input[@name="password"]').send_keys(
                "P@ssword2"
            )
            appium_driver.find_element(AppiumBy.XPATH, "//form").click()
            time.sleep(2)
            appium_driver.find_element(by=AppiumBy.XPATH, value="//form/button").click()
            allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="sign-in",
            attachment_type=allure.attachment_type.PNG,
            )
    except NoSuchElementException:
        pass


@allure.title("Open Dashboard Menu")
def test_open_menu_then_customers(appium_driver):
    """
    Open the Customers page
    """
    with allure.step("Open menu"):
        appium_driver.find_element(by=AppiumBy.XPATH, value="//header/div/button").click()
        time.sleep(1)
        appium_driver.find_element(by=AppiumBy.XPATH, value="//ul/div[6]").click()


@allure.title("Open Dashboard Menu")
def test_cannot_submit_form(appium_driver):
    """
    Test that the form cannot be submitted without required fields
    """
    with allure.step("Open form"):
        try:
            appium_driver.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="CREATE CUSTOMER"]',
            ).click()
        except NoSuchElementException:
            pass
        
        time.sleep(1)
        actions = ActionChains(appium_driver)
        # override as 'touch' pointer action
        actions.w3c_actions = ActionBuilder(appium_driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(870, 2600)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(2)
        actions.w3c_actions.pointer_action.move_to_location(870, 1000)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
    with allure.step("Submit form"):
        appium_driver.find_element(by=AppiumBy.XPATH, value="//button[@id='submit']").click()
        appium_driver.find_elements(
            AppiumBy.ID,
            "customer_display_name-helper-text",
        )
    allure.attach(
        appium_driver.get_screenshot_as_png(),
        name="full-page",
        attachment_type=allure.attachment_type.PNG,
    )
