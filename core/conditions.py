from abc import ABC, abstractmethod

from playwright.sync_api import Locator, expect


class Condition(ABC):
    @abstractmethod
    def assert_(self, locator: Locator, timeout: int | None = None) -> None:
        pass

    @abstractmethod
    @property
    def description(self) -> str:
        pass


class Visible(Condition):
    def assert_(self, locator: Locator, timeout: int | None = None) -> None:
        expect(locator).to_be_visible(timeout=timeout)

    @property
    def description(self) -> str:
        return "visible"


class Hidden(Condition):
    def assert_(self, locator: Locator, timeout: int | None = None) -> None:
        expect(locator).to_be_hidden(timeout=timeout)

    @property
    def description(self) -> str:
        return "hidden"
