from abc import ABC, abstractmethod

class Shape(ABC):
    """Shapes"""
    @abstractmethod
    def area(self):
        """Tagastab kujundi pindala"""
        pass 


class Rectangle(Shape):
    """Rectangle"""
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
    
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"width: {self.width}, height: {self.height}"
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, new_width: int):
        if new_width > 0:
            self._width = new_width
    
    @height.setter
    def height(self, new_height: int):
        if new_height > 0:
            self._height = new_height


class Square(Rectangle):
    """Square"""
    def __init__(self, size: int):
        self.size = size
    
    def area(self):
        return self._size * self._size
    
    def __str__(self):
        return f"size: {self.size}"


if __name__ == "__main__":

    r = Rectangle(2, 3)
s = Square(5)

print(r)
print(s)

print(f"Rectangle area: {r.area}")
print(f"Square area: {s.area}")

r = Rectangle(2,5)
