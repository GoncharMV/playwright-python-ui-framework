import pytest
from playwright.sync_api import Locator
from allure import step
from core.conditions import Condition


class Element:
    _browser = None

    @classmethod
    def set_browser(cls, browser):
        cls._browser = browser

    def __init__(self,
                 selector: str,
                 description: str | None = None,
                 timeout: int = 10,
                 ):
        self._selector = selector
        self._description = description
        self._timeout = timeout * 1000

    @property
    def type_of(self) -> str:
        return "element"

    def _get_locator(self, **kwargs) -> Locator:
        locator = self._selector.format(**kwargs)
        return self._browser.page.locator(locator)


    def should(self, condition: Condition, timeout: int | None = None):
        timeout = timeout * 1000 if timeout is not None else self._timeout
        locator = self._get_locator()

        with step(f"Check that {self.type_of} {self._description} {condition.description}"):
            try:
                condition.assert_(locator=locator, timeout=timeout)
            except AssertionError as e:
                pytest.fail(f"Locator {self._selector}\nError {str(e)}")


