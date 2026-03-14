from abc import ABC, abstractmethod

from playwright.sync_api import Locator, expect


class Condition(ABC):
    @abstractmethod
    def assert_(self, locator: Locator, timeout: int | None = None) -> None:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass


class Visible(Condition):
    def assert_(self, locator: Locator, timeout: int | None = None) -> None:
        expect(locator).to_be_visible(timeout=timeout)

    @property
    def description(self) -> str:
        return "is visible"


class Hidden(Condition):
    def assert_(self, locator: Locator, timeout: int | None = None) -> None:
        expect(locator).to_be_hidden(timeout=timeout)

    @property
    def description(self) -> str:
        return "is hidden"


class _Be:
    @property
    def visible(self) -> Visible:
        return Visible()

    @property
    def hidden(self) -> Hidden:
        return Hidden()

be = _Be()