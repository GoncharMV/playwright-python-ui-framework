from core.element import Element
from allure import step

class Button(Element):
    def click(self, force=False, **kwargs):
        with step(f"Click on: {self._description}"):
            self._get_locator(**kwargs).click(force=force, timeout=self._timeout)


    @property
    def type_of(self) -> str:
        return "button"
