import json
import sys
from styles import *
from icons import *
from draw_factory import *
from component import Container, Leaf

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def build_structure(data, name="root", level=0):
    container = Container(name, level)
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                container.add(build_structure(value, key, level + 1))
            else:
                leaf = Leaf(f"{key}: {value}", level + 1)
                container.add(leaf)
        return container
    else:
        return Leaf(data, level)

def main():
    if len(sys.argv) < 7:
        print("Usage: fje.py -f <json_file> -s <style> -i <icon_family>")
        sys.exit(1)

    json_file = sys.argv[2]
    style_type = sys.argv[4]
    icon_type = sys.argv[6]

    data = load_json(json_file)
    structure = build_structure(data)

    if style_type == "tree":
        style_factory = TreeStyleFactory()
    elif style_type == "rectangle":
        style_factory = RectangleStyleFactory()
    else:
        print(f"Unknown style: {style_type}")
        sys.exit(1)

    style = style_factory.create_style()

    if icon_type == "normal":
        icons_factory = NormalIconFactory()
    elif icon_type == "other":
        icons_factory = OtherIconFactory()
    else:
        print(f"Unknown icon type: {icon_type}")
        sys.exit(1)

    icon = icons_factory.create_Icons()

    draw = Draw()
    draw.draw_func(structure, icon, style)

if __name__ == "__main__":
    main()
