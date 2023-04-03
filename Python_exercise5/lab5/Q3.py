# for drawing will include in next assignment or submit later

import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Quadrilateral:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        self.p3 = Point(x3, y3)
        self.p4 = Point(x4, y4)
        print(f"The coordinates are {(x1, y1)} and {(x2, y2)} and {(x3, y3)} and {(x4, y4)}")

    def lengthA(self):
        return math.sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

    def lengthB(self):
        return math.sqrt((self.p3.x - self.p2.x) ** 2 + (self.p3.y - self.p2.y) ** 2)

    def lengthC(self):
        return math.sqrt((self.p4.x - self.p3.x) ** 2 + (self.p4.y - self.p3.y) ** 2)

    def lengthD(self):
        return math.sqrt((self.p1.x - self.p4.x) ** 2 + (self.p1.y - self.p4.y) ** 2)

    def getPerimeter(self):
        perimeter = self.lengthA() + self.lengthB() + self.lengthC() + self.lengthD()
        print(f"Perimeter: {perimeter:.2f} ")
        return perimeter

    def getArea(self):
        area = 0.5 * abs(
            (self.p1.x * self.p2.y + self.p2.x * self.p3.y + self.p3.x * self.p4.y + self.p4.x * self.p1.y) -
            (self.p2.x * self.p1.y + self.p3.x * self.p2.y + self.p4.x * self.p3.y + self.p1.x * self.p4.y))
        print(f"Area: {area:.2f}")
        return area

    def draw(self):
        widths = sorted([self.p1.x, self.p2.x, self.p3.x, self.p4.x])
        heights = sorted([self.p1.y, self.p2.y, self.p3.y, self.p4.y])
        width = widths[3] - widths[0]
        height = heights[3] - heights[0]
        shape = [[0] * (width + 1)] * (height + 1)
        print("widths:", widths)
        print("heights:", heights)
        print("shape:", shape)
        # print(shape)
        self.p1.x = self.p1.x - widths[0]
        self.p2.x = self.p2.x - widths[0]
        self.p3.x = self.p3.x - widths[0]
        self.p4.x = self.p4.x - widths[0]

        self.p1.y = heights[3] - self.p1.y
        self.p2.y = heights[3] - self.p2.y
        self.p3.y = heights[3] - self.p3.y
        self.p4.y = heights[3] - self.p4.y
        print(f"{self.p1.x, self.p1.y},{self.p2.x, self.p2.y},{self.p3.x, self.p3.y},{self.p4.x, self.p4.y} ")

        k1 = "" if (self.p2.x - self.p1.x) == 0 else ((self.p2.y - self.p1.y) / (self.p2.x - self.p1.x))
        k2 = "" if (self.p3.x - self.p2.x) == 0 else ((self.p3.y - self.p2.y) / (self.p3.x - self.p2.x))
        k3 = "" if (self.p4.x - self.p3.x) == 0 else ((self.p4.y - self.p3.y) / (self.p4.x - self.p3.x))
        k4 = "" if (self.p1.x - self.p4.x) == 0 else ((self.p1.y - self.p4.y) / (self.p1.x - self.p4.x))

        print(f"k1={k1} k2={k2} k3={k3} k4={k4}")

        print("-------------------------------")
        for row in shape:
            for col in row:
                print(col, end=" ")
            print()
        print("-------------------------------")

        if k1 == "":
            if self.p2.y > self.p1.y:
                for y in range(self.p1.y, self.p2.y + 1):
                    shape[y][self.p1.x] = "*"
            else:
                for y in range(self.p2.y, self.p1.y + 1):
                    shape[y][self.p1.x] = "*"
        else:
            if self.p2.y > self.p1.y:
                if self.p2.x > self.p1.x:
                    for y in range(self.p1.y, self.p2.y + 1):
                        for r in range(self.p1.x, self.p2.x + 1):
                            if y == (k1 * (r - self.p1.x) + self.p1.y):
                                shape[y][r] = "*"

                else:
                    for y in range(self.p1.y, self.p2.y + 1):
                        for r in range(self.p2.x, self.p1.x + 1):
                            if y == (k1 * (r - self.p1.x) + self.p1.y):
                                shape[y][r] = "*"

            else:
                if self.p2.x > self.p1.x:
                    for y in range(self.p2.y, self.p1.y + 1):
                        for r in range(self.p1.x, self.p2.x + 1):
                            if y == (k1 * (r - self.p1.x) + self.p1.y):
                                shape[y][r] = "*"
                else:
                    for y in range(self.p2.y, self.p1.y + 1):
                        for r in range(self.p2.x, self.p1.x + 1):
                            if y == (k1 * (r - self.p1.x) + self.p1.y):
                                shape[y][r] = "*"
        #
        # if k2 == "":
        #     if self.p3.y > self.p2.y:
        #         for y in range(self.p2.y, self.p3.y + 1):
        #             shape[y][self.p2.x] = "*"
        #     else:
        #         for y in range(self.p3.y, self.p2.y + 1):
        #             shape[y][self.p2.x] = "*"
        # else:
        #     if self.p3.y > self.p2.y:
        #         if self.p3.x > self.p2.x:
        #             for y in range(self.p2.y, self.p3.y + 1):
        #                 for r in range(self.p2.x, self.p3.x + 1):
        #                     if y == (k2 * (r - self.p2.x) + self.p2.y):
        #                         shape[y][r] = "*"
        #
        #         else:
        #             for y in range(self.p2.y, self.p3.y + 1):
        #                 for r in range(self.p3.x, self.p2.x + 1):
        #                     if y == (k2 * (r - self.p2.x) + self.p2.y):
        #                         shape[y][r] = "*"
        #
        #     else:
        #         if self.p3.x > self.p2.x:
        #             for y in range(self.p3.y, self.p2.y + 1):
        #                 for r in range(self.p2.x, self.p3.x + 1):
        #                     if y == (k2 * (r - self.p2.x) + self.p2.y):
        #                         shape[y][r] = "*"
        #         else:
        #             for y in range(self.p3.y, self.p2.y + 1):
        #                 for r in range(self.p3.x, self.p2.x + 1):
        #                     if y == (k2 * (r - self.p2.x) + self.p2.y):
        #                         shape[y][r] = "*"
        #
        # if k3 == "":
        #     if self.p4.y > self.p3.y:
        #         for y in range(self.p3.y, self.p4.y + 1):
        #             shape[y][self.p3.x] = "*"
        #     else:
        #         for y in range(self.p4.y, self.p3.y + 1):
        #             shape[y][self.p3.x] = "*"
        # else:
        #     if self.p4.y > self.p3.y:
        #         if self.p4.x > self.p3.x:
        #             for y in range(self.p3.y, self.p4.y + 1):
        #                 for r in range(self.p3.x, self.p4.x + 1):
        #                     if y == (k3 * (r - self.p3.x) + self.p3.y):
        #                         shape[y][r] = "*"
        #
        #         else:
        #             for y in range(self.p3.y, self.p4.y + 1):
        #                 for r in range(self.p4.x, self.p3.x + 1):
        #                     if y == (k3 * (r - self.p3.x) + self.p3.y):
        #                         shape[y][r] = "*"
        #
        #     else:
        #         if self.p4.x > self.p3.x:
        #             for y in range(self.p4.y, self.p3.y + 1):
        #                 for r in range(self.p3.x, self.p4.x + 1):
        #                     if y == (k3 * (r - self.p3.x) + self.p3.y):
        #                         shape[y][r] = "*"
        #         else:
        #             for y in range(self.p4.y, self.p3.y + 1):
        #                 for r in range(self.p4.x, self.p3.x + 1):
        #                     if y == (k3 * (r - self.p3.x) + self.p3.y):
        #                         shape[y][r] = "*"
        #
        # if k4 == "":
        #     if self.p1.y > self.p4.y:
        #         for y in range(self.p4.y, self.p1.y + 1):
        #             shape[y][self.p4.x] = "*"
        #     else:
        #         for y in range(self.p1.y, self.p4.y + 1):
        #             shape[y][self.p4.x] = "*"
        # else:
        #     if self.p1.y > self.p4.y:
        #         if self.p1.x > self.p4.x:
        #             for y in range(self.p4.y, self.p1.y + 1):
        #                 for r in range(self.p4.x, self.p1.x + 1):
        #                     if y == (k4 * (r - self.p4.x) + self.p4.y):
        #                         shape[y][r] = "*"
        #
        #         else:
        #             for y in range(self.p4.y, self.p1.y + 1):
        #                 for r in range(self.p1.x, self.p4.x + 1):
        #                     if y == (k4 * (r - self.p4.x) + self.p4.y):
        #                         shape[y][r] = "*"
        #
        #     else:
        #         if self.p1.x > self.p4.x:
        #             for y in range(self.p1.y, self.p4.y + 1):
        #                 for r in range(self.p4.x, self.p1.x + 1):
        #                     if y == (k4 * (r - self.p4.x) + self.p4.y):
        #                         shape[y][r] = "*"
        #         else:
        #             for y in range(self.p1.y, self.p4.y + 1):
        #                 for r in range(self.p1.x, self.p4.x + 1):
        #                     if y == (k4 * (r - self.p4.x) + self.p4.y):
        #                         shape[y][r] = "*"

        print("-------------------------------")
        for row in shape:
            for col in row:
                print(col, end=" ")
            print()
        print("-------------------------------")


class Trapzoid(Quadrilateral):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)
        self.baseA = self.lengthA()
        self.baseC = self.lengthC()
        self.sideB = self.lengthB()
        self.sideD = self.lengthD()


class Parallelogram(Trapzoid):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)
        self.sideA = self.lengthA()
        self.sideB = self.lengthB()


class Rectangle(Parallelogram):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)
        self.length = self.lengthA()
        self.width = self.lengthB()


class Square(Rectangle):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        super().__init__(x1, y1, x2, y2, x3, y3, x4, y4)
        self.side = self.lengthA()


def main():
    print("Example of Square:")
    square = Square(0, 2, 1, 1, 2, 2, 1, 3)
    square.getArea()
    square.getPerimeter()
    square.draw()

    print("\n\nExample of Rectangle:")
    rectangle = Rectangle(0, 2, 1, 1, 3, 3, 2, 4)
    rectangle.getArea()
    rectangle.getPerimeter()
    rectangle.draw()

    print("\n\nExample of Parallelogram:")
    parallelogram = Parallelogram(0, 0, 2, 0, 4, 2, 2, 2)
    parallelogram.getArea()
    parallelogram.getPerimeter()
    parallelogram.draw()

    print("\n\nExample of Trapzoid:")
    trapzoid = Trapzoid(0, 0, 6, 0, 4, 2, 2, 2)
    trapzoid.getArea()
    trapzoid.getPerimeter()
    trapzoid.draw()

    print("\n\nExample of Quadrilateral:")
    quadrilateral = Quadrilateral(0, 0, 5, 0, 5, 1, 3, 3)
    quadrilateral.getArea()
    quadrilateral.getPerimeter()
    quadrilateral.draw()


main()
