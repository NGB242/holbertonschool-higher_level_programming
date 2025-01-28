#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Initialise un nouveau carré.
        
        Args:
            size (int): La taille d'un côté du carré. Par défaut, elle est 0.
        """
        self.__size = size

    def area(self):
        """Calcule l'aire du carré.
        
        Returns:
            int: L'aire du carré.
        """
        return self.__size ** 2
