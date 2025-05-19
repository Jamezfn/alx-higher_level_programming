#!/usr/bin/python3
"""And now, the Square!"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Describes a square obj that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return informal string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """Size getter"""
        return self.height

    @size.setter
    def size(self, value):
        """Setter for size - both height and width"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assign arguments to attributes in order or by keyword."""
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i > len(attrs):
                    break
                setattr(self, attrs[i], value)

        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key,value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        return {
                'id' : self.id,
                'size' : self.size,
                'x' : self.x,
                'y' : self.y
                }
