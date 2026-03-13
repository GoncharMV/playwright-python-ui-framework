from components import examples


def test_dummy(browser):

    browser.open("/")
    examples.web_inputs.click()
    browser.page.wait_for_timeout(2000)
