from component import Container, Leaf

class Visitor:
    def visit_container(self, container):
        pass

    def visit_leaf(self, leaf):
        pass
#
# class DrawVisitor(Visitor):
#     def __init__(self, icon, style):
#         self.icon = icon
#         self.style = style
#
#     def visit_container(self, container):
#         indent = "│  " * container.level + "├─ "
#         print(f"{indent}{self.icon.get_icon(container)}{container.name}")
#         for child in container:
#             child.accept(self)
#
#     def visit_leaf(self, leaf):
#         indent = "│  " * leaf.level + "├─ "
#         print(f"{indent}{self.icon.get_icon(leaf)}{leaf.name}")
class DrawVisitor(Visitor):
    def __init__(self, icon, style):
        self.icon = icon
        self.style = style

    def visit_container(self, container):
        if self.style.get_style() == "tree":
            self.draw_tree(container)
        elif self.style.get_style() == "rectangle":
            self.draw_rectangle(container)

    def visit_leaf(self, leaf):
        if self.style.get_style() == "tree":
            self.draw_tree_leaf(leaf)
        elif self.style.get_style() == "rectangle":
            self.draw_rectangle_leaf(leaf)

    def draw_tree(self, container):
        indent = "│  " * container.level + "├─ "
        print(f"{indent}{self.icon.get_icon(container)}{container.name}")
        for child in container:
            child.accept(self)

    def draw_tree_leaf(self, leaf):
        indent = "│  " * leaf.level + "├─ "
        print(f"{indent}{self.icon.get_icon(leaf)}{leaf.name}")

    def draw_rectangle(self, container):
        indent = "│  " * container.level + "├─ "
        output_string = f"{indent}{self.icon.get_icon(container)}{container.name}"
        dashes_needed = 50 - len(output_string) - 1
        dashes = '-' * dashes_needed + '│'
        print(output_string + dashes)
        for child in container:
            child.accept(self)

    def draw_rectangle_leaf(self, leaf):
        indent = "│  " * leaf.level + "├─ "
        output_string = f"{indent}{self.icon.get_icon(leaf)}{leaf.name}"
        dashes_needed = 50 - len(output_string) - 1
        dashes = '-' * dashes_needed + '│'
        print(output_string + dashes)
