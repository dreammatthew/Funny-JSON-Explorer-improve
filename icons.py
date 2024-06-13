from abc import ABC, abstractmethod
from component import Container, Leaf

class Icons(ABC):
    def __init__(self, name):
        self.name = name

    def get_icon(self, structure):
        raise NotImplementedError("This method should be overridden by subclasses")

class Normal_Icon(Icons):
    def __init__(self, name="normal"):
        super().__init__(name)

    def get_icon(self, structure):
        return ''

class Other_Icon(Icons):
    def __init__(self, name="other"):
        super().__init__(name)

    def get_icon(self, structure):
        if isinstance(structure, Leaf):
            return '♤'
        elif isinstance(structure, Container):
            return '♢'
        else:
            return '·'

class IconsFactory(ABC):
    @abstractmethod
    def create_Icons(self) -> Icons:
        pass

class NormalIconFactory(IconsFactory):
    def create_Icons(self) -> Icons:
        return Normal_Icon()

class OtherIconFactory(IconsFactory):
    def create_Icons(self) -> Icons:
        return Other_Icon()
