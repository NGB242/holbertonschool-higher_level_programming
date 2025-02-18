#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Create the root element
    """
    root = ET.Element("root")

    """
    Iterate through the dictionary items and add them as child elements
    """
    for key, value in data.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    """
    Create an ElementTree object and write it to the provided filename
    """
    tree = ET.ElementTree(root)
    with open(filename, "wb") as f:
        tree.write(f)


def deserialize_from_xml(filename):

    """
    Parse the XML file
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {child.tag: child.text for child in root}
    return data
