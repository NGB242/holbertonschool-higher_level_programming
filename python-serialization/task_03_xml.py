#!/usr/bin/env python3

import xml.etree.ElementTree as ET

def serialize_to_xml(data, filename):
    root = ET.Element("root")
    
    for key, value in data.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, "wb") as f:
        tree.write(f)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    data = {child.tag: child.text for child in root}
    return data