from playwright.sync_api import Locator


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


    def _get_locator(self, **kwargs) -> Locator:
        locator = self._selector.format(**kwargs)
        return self._browser.page.locator(locator)
