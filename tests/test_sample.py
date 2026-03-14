from components import examples
from core.conditions import be


def test_dummy(browser):

    browser.open("/")
    examples.web_inputs.click()
    browser.page.wait_for_timeout(2000)
    examples.web_inputs.should(be.hidden)
