class CalFunc:
    """Defined all functions of the calculator."""

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def divide(self):
        try:
            result = self.x / self.y
        except ZeroDivisionError:
            print("You can't divide zero!")
        else:
            return round(result, 2)

    def multiply(self):
        return self.x * self.y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y
