import time
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

pytestmark = [allure.epic("Suppliers Epic"), allure.feature("Test Suppliers Table")]

@allure.id(2)
@allure.story("Supplier Table Story")
@allure.title("ResourceZen Home")
def test_open(appium_driver):
    """
    Open the ResourceZen website
    """
    with allure.step("Open ResourceZen"):
        appium_driver.get("https://develop.resourcezen.co.za/home")
        time.sleep(4)

@allure.title("Sign In")
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

@allure.title("Supplier Table Test")
def test_close_modal(appium_driver):
    """
    close modal
    """
    with allure.step("close modal"):
        time.sleep(3)
        appium_driver.find_element(
            by=AppiumBy.XPATH,
            value='//button[@aria-label="view"]',
        ).click()
        time.sleep(3)
        appium_driver.find_element(
            by=AppiumBy.XPATH, value="//button[@data-testid='modal-close']"
        ).click()


@allure.title("Open Dashboard Menu")
def test_open_menu_then_suppliers(appium_driver):
    """
    Open the Suppliers page
    """
    with allure.step("Open menu"):
        appium_driver.find_element(by=AppiumBy.XPATH, value="//header/div/button").click()
        time.sleep(1)
        appium_driver.find_element(by=AppiumBy.XPATH, value="//ul/div[5]").click()


@allure.title("Open Dashboard Menu")
def test_cannot_submit_form(appium_driver):
    """
    Test that the form cannot be submitted without required fields
    """
    with allure.step("Open form"):
        try:
            appium_driver.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.Button[@text="CREATE SUPPLIER"]',
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
            "suppliers_name-helper-text",
        )
    allure.attach(
        appium_driver.get_screenshot_as_png(),
        name="full-page",
        attachment_type=allure.attachment_type.PNG,
    )
