#!/usr/bin/python3
"""And now, the Square!"""
from models.rectangle import Rectangle
class Square(Rectangle):
    """Describes a square class that inherits from a rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a class instance"""
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """Retrieve size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set value for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes to the class instance"""
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for idx, value in enumerate(args):
                if idx > len(attrs):
                    break
                setattr(self, attrs[idx], value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
