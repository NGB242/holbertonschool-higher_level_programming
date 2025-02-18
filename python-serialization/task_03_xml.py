#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Create the root element
    """
    root = ET.Element("data")

    """
    Iterate through the dictionary items and add them as child elements
    """
    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    """
    Create an ElementTree object and write it to the provided filename
    """
    tree = ET.ElementTree(root)
    try:
        tree.write(filename)
        return True
    except Exception as e:
        print(f"Serialization error: {e}")
        return False


def deserialize_from_xml(filename):
    try:
        """
        Parse the XML file
        """
        tree = ET.parse(filename)
        root = tree.getroot()

        """
        Reconstruct the dictionary from the XML elements
        """
        dictionary = {child.tag: child.text for child in root}

        """
        Convert values to appropriate data types if necessary
        """
        for key, value in dictionary.items():
            if value.isdigit():
                dictionary[key] = int(value)
            elif value.lower() == 'true':
                dictionary[key] = True
            elif value.lower() == 'false':
                dictionary[key] = False

        return dictionary
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except Exception as e:
        print(f"Deserialization error: {e}")
        return None
