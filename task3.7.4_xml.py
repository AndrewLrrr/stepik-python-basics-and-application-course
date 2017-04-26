from xml.etree import ElementTree


def count_colors(root, dlevel):
    attrs = root.attrib
    for attr, val in attrs.items():
        if attr == 'color' and val in colors:
            colors[val] += dlevel
    if root.getchildren():
        for child in root:
            if child.tag == 'cube':
                count_colors(child, dlevel + 1)

xml_str = input().strip()

root = ElementTree.fromstring(xml_str)

colors = {
    'red': 0,
    'blue': 0,
    'green': 0,
}

count_colors(root, 1)

print(colors['red'], colors['green'], colors['blue'])
