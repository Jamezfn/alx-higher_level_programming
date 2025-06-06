#!/usr/bin/python3
"""First Rectangle"""
from models.base import Base

class Rectangle(Base):
    """Describes a class that inherits from the base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > than 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character '#'."""
        for _ in range(self.__y):
            print("")
        for _ in range(self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def __str__(self):
        """Return informal string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assign arguments to attributes in order: id, width, height, x, y."""
        attrs = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i >= len(attrs):
                    break
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
                'id' : self.id,
                'width' : self.width,
                'height' : self.height,
                'x' : self.x,
                'y' : self.y
                }
