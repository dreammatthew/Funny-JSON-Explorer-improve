class Iterator:
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.container.children):
            result = self.container.children[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
