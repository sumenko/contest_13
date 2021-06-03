from io import StringIO
from unittest.mock import patch


class Calculator():
    def __init__(self, expression):
        self.expression = expression

    def calculate(self):
        return self.expression


def main():
    c = Calculator(input())
    print(c.calculate())


if __name__ == '__main__':
    tests = (
        ('2 1 + 3 *\n', 9),
        ('7 2 + 4 * 2 +\n', 38)
    )

    main()
