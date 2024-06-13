from visitor import *

class Draw:
    def draw_func(self, structure, icon, style):
        visitor = DrawVisitor(icon, style)
        structure.accept(visitor)
