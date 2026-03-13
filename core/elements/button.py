from core.element import Element


class Button(Element):
    def click(self, force=False, **kwargs):
        self._get_locator(**kwargs).click(force=force, timeout=self._timeout)
