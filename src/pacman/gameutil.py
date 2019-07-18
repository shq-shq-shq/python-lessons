class Vector:
    def __init__(self, *args):
        if len(args) == 1 and len(args[0]) == 2:
            self.x, self.y = args[0]
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 0:
            self.x = self.y = 0
        else:
            raise ValueError

    def toInt(self):
        return Vector(int(self.x), int(self.y))

    def xy(self):
        return (self.x, self.y)

    def __len__(self):
        return 2

    def __getitem__(self, item):
        return (self.x, self.y)[item]

    def __eq__(self, other):
        if type(other) == Vector:
            return self.x == other.x and self.y == other.y
        else:
            return self.x == other[0] and self.y == other[0]

    def __add__(self, other):
        return Vector(self.x + other[0], self.y + other[1])

    def __sub__(self, other):
        return Vector(self.x - other[0], self.y - other[1])

    def __mul__(self, other):
        if type(other) is Vector or type(other) is list or type(other) is tuple:
            return Vector(self.x * other[0], self.y * other[1])
        else:
            return Vector(self.x * other, self.y * other)

    def __floordiv__(self, other):
        if type(other) is Vector or type(other) is list or type(other) is tuple:
            return Vector(self.x // other[0], self.y // other[1])
        else:
            return Vector(self.x // other, self.y // other)

    def __truediv__(self, other):
        if type(other) is Vector or type(other) is list or type(other) is tuple:
            return Vector(self.x / other[0], self.y / other[1])
        else:
            return Vector(self.x / other, self.y / other)

    def __mod__(self, other):
        if type(other) is Vector or type(other) is list or type(other) is tuple:
            return Vector(self.x % other[0], self.y % other[1])
        else:
            return Vector(self.x % other, self.y % other)

    def __str__(self):
        return "V(%d, %d)" % (self.x, self.y)
