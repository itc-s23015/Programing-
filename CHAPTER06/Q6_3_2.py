class Rectangle:
    """長方形"""

    angle = 90

    def __init__(self, width, height):
        self.name = "rectangle"
        self.width = width
        self.height = height
        self.perimeter = self.clac_perimeter()
        self.area = self.clac_area()

    def clac_perimeter(self):
        w = self.width
        h = self.height
        return (w + h) * 2

    def clac_area(self):
        w = self.width
        h = self.height
        return w * h

    def show_attributes(self):
        ang = self.angle
        n = self.name
        w = self.width
        h = self.height
        p = self.perimeter
        a = self.area
        print("name: {}, width: {}, height: {}, angle: {}".
              format(n, w, h, ang))
        print("perimeter: {}, area: {}".format(p, a))


class Square(Rectangle):
    """正方形"""

    def __init__(self, width):
        super().__init__(width, width)
        self.name = "square"


s1 = Square(4)
s1.show_attributes()
