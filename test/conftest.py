import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def appium_driver(request):
    """
    Fixture for the module

    Yields:
        driver
    """
    desired_caps = dict(
        platformName="Android",
        deviceName="Android",
        automationName="UiAutomator2",
        browserName="chrome",
    )
    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote("http://localhost:4723", options=capabilities_options)
    driver.implicitly_wait(10)

    def fin():
        driver.quit()

    request.addfinalizer(fin)

    return driver

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
