class Circle:

    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.1416 * (self._radius **2)
    
    @property
    def radius(self) -> float:
        return self.__radius
    
circle = Circle(5)
print(circle.area)