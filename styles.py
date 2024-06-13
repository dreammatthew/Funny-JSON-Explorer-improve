from abc import ABC, abstractmethod

class Style(ABC):
    def get_style(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class TreeStyle(Style):
    def get_style(self):
        return "tree"

class RectangleStyle(Style):
    def get_style(self):
        return "rectangle"

class StyleFactory(ABC):
    @abstractmethod
    def create_style(self) -> Style:
        pass

class TreeStyleFactory(StyleFactory):
    def create_style(self) -> Style:
        return TreeStyle()

class RectangleStyleFactory(StyleFactory):
    def create_style(self) -> Style:
        return RectangleStyle()
