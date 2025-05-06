#1/usr/bin/python3
"""Class Inheritance"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """Full rectangle"""
    def __init__(self, width, height):
        """Instantiation with width"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area calculations"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        rec_def = "[" +str(self.__class__.__name__) + "] "
        rec_def += str(self.__width) + "/" + str(self.__height)
        return (rec_def)
