from iterator import Iterator

class Container:
    def __init__(self, name, level=0):
        self.name = name
        self.level = level
        self.children = []

    def add(self, child):
        self.children.append(child)

    def accept(self, visitor):
        visitor.visit_container(self)

    def __iter__(self):
        return Iterator(self)

class Leaf(Container):
    def __init__(self, name, level=0):
        super().__init__(name, level)

    def accept(self, visitor):
        visitor.visit_leaf(self)
