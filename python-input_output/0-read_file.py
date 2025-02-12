#!/usr/bin/python3
"""
Ouvre un fichier en lecture et affiche son contenu sur la console.

:param filename: Nom du fichier à lire.
"""


def read_file(filename=""):
    """
    Ouvre un fichier en lecture et affiche son contenu sur la console.

    param filename: Nom du fichier à lire.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
