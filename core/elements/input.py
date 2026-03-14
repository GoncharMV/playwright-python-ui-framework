from allure import step

from core.element import Element


class Input(Element):
    @property
    def type_of(self) -> str:
        return "Input"

    def type(self, text: str, clear: bool = True, **kwargs) -> None:
        if clear:
            self.clear(**kwargs)

        with step(f"Type '{text}' into {self.type_of} '{self._description}'"):
            self._get_locator(**kwargs).type(text=text, timeout=self._timeout)

    def clear(self, **kwargs) -> None:
        with step(f"Clear input field '{self._description}'"):
            self._get_locator(**kwargs).clear(timeout=self._timeout)

    def set_input_files(self, files: str, **kwargs) -> None:
        with step(f"Send files '{files}' to '{self._description}'"):
            self._get_locator(**kwargs).set_input_files(files=files, timeout=self._timeout)
