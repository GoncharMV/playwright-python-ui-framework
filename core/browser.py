from dataclasses import dataclass

from playwright.sync_api import sync_playwright


@dataclass
class BrowserConfig:
    browser: str = "chromium"
    headless: bool = False
    base_url: str | None = None


class Browser:
    def __init__(self, config: BrowserConfig):
        self.config = config
        self._playwright = None
        self._browser = None
        self._context = None
        self._page = None


    def _start(self):
        self._playwright = sync_playwright().start()
        browser_type = getattr(self._playwright, self.config.browser)

        self._browser = browser_type.launch(headless=self.config.headless)

        context_options = self._build_context_options()
        self._context = self._browser.new_context(**context_options)
        self._page = self._context.new_page()


    def _build_context_options(self):
        options = {}

        options["base_url"] = self.config.base_url

        return options


    @property
    def page(self):
        if not self._page:
            self._start()

        return self._page

    def open(self, url: str):
        self.page.goto(url)


    def close(self):
        if self._context:
            self._context.close()
        if self._browser:
            self._browser.close()
        if self._playwright:
            self._playwright.stop()
