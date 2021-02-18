#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):

    """Rectangle class which inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation of Rectangle
        Args:
            width (int): Rectangle width
            height (int): Rectangle height
            x (int): the x coordinate of the rectangle
            y (int): the y coordinate of the rectangle
            id (int): Rectangle id
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
