"""
Develop Rectangle class with following content:
    2 private fields type of float `side_a` and `side_b` (sides А and В of the rectangle);
    One constructor with two optional parameters a and b (parameters specify rectangle sides). Side А of a rectangle
    defaults to 4, side В - 3. Raise ValueError if received parameters are less than or equal to 0;
    Method `get_side_a`, returning value of the side А;
    Method `get_side_b`, returning value of the side В;
    Method `area`, calculating and returning the area value;
    Method `perimeter`, calculating and returning the perimeter value;
    Method `is_square`, checking whether current rectangle is square or not. Returns True if the shape is square and
    False in another case;
    Method `replace_sides`, swapping rectangle sides.

Develop class ArrayRectangles, in which declare:
    Private attribute `rectangle_array` (list of rectangles);
    One constructor that creates a list of rectangles with length `n` filled with `None` and that receives an
    arbitrary amount of objects of type `Rectangle` or a list of objects of type `Rectangle` (the list must be
    unpacked inside the constructor so that there will be no nested arrays). If both objects and length are passed,
    at first creates a list with received objects and then add the required number of Nones to achieve the
    desired length. If `n` is less than the number of received objects, the length of the list will be equal to the
    number of objects;
    Code like ArrayRectangles(Rectangle(),[Rectangle(),Rectangle()]) should be valid;
    Method `add_rectangle` that adds a rectangle of type `Rectangle` to the array on the nearest free place and
    returning True, or returning False, if there is no free space in the array;
    Method `number_max_area`, that returns order number (index) of the first rectangle with the maximum area value
    (numeration starts from zero);
    Method `number_min_perimeter`, that returns order number (index) of the first rectangle with the minimum area value
    (numeration starts from zero);
    Method `number_square`, that returns the number of squares in the array of rectangles
"""


class Rectangle:

    def __init__(self, a: float = 4.0, b: float = 3.0):
        if a <= 0 or b <= 0:
            raise ValueError
        self.__side_a = a
        self.__side_b = b

    def get_side_a(self):
        return self.__side_a

    def get_side_b(self):
        return self.__side_b

    def area(self):
        return self.__side_a * self.__side_b

    def perimeter(self):
        return (self.__side_a + self.__side_b) * 2

    def is_square(self) -> bool:
        return True if self.__side_a == self.__side_b else False

    def replace_sides(self):
        a1 = self.__side_a
        self.__side_a = self.__side_b
        self.__side_b = a1


class ArrayRectangles:
    def __init__(self, *args, n=0):
        self.__rectangle_array = []
        self.n = n
        for arg in args:
            if isinstance(arg, list):
                self.__rectangle_array += arg
            else:
                self.__rectangle_array.append(arg)
        if len(self.__rectangle_array) < self.n:
            self.__rectangle_array += (self.n - len(self.__rectangle_array)) * [None]

    def add_rectangle(self, rectangle: Rectangle):
        if None in self.__rectangle_array:
            for i in range(len(self.__rectangle_array)):
                if self.__rectangle_array[i] is None:
                    self.__rectangle_array[i] = rectangle
                    return True
        return False

    def number_max_area(self):
        index = 0
        max_area = self.__rectangle_array[0].area()
        count = 0
        for rectangle in self.__rectangle_array:
            if rectangle is not None and rectangle.area() > max_area:
                max_area = rectangle.area()
                index = count
            count += 1
        return index

    def number_min_perimeter(self):
        index = 0
        min_perimeter = self.__rectangle_array[0].perimeter()
        count = 0
        for rectangle in self.__rectangle_array:
            if rectangle is not None and rectangle.perimeter() < min_perimeter:
                min_perimeter = rectangle.perimeter()
                index = count
            count += 1
        return index

    def number_square(self) -> int:
        count = 0
        for rectangle in self.__rectangle_array:
            if rectangle is not None and rectangle.is_square():
                count += 1
        return count

    def __str__(self):
        return str(self.__rectangle_array)
