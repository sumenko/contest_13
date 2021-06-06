# Спринт 13. Задача B
# Суменко В.А.
# попытки: 51820227

class StackIsFull(Exception):
    pass


class StackIsEmpty(Exception):
    pass


class Stack():
    class Node():
        def __init__(self, x, next=None):
            self.value = x
            self.next = next
            self.prev = None

    def __init__(self):
        self.node = None

    def append(self, x):
        self.node = self.Node(x, self.node)
        self.node.prev = self.node

    def pop(self):
        value = self.node.value
        self.node = self.node.prev
        return value

def calculator(expr):
    if expr == '':
        return None

    task = expr.split()

    max_length = len(task)
    stack = Stack()

    action = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b,
    }
    while task:
        x = task.pop(0)
        if x not in '+-/*':
            stack.append(int(x))
        else:
            b, a = stack.pop(), stack.pop()
            res = action[x](a, b)
            stack.append(res)
    result = stack.pop()
    return result


def main():
    expr = input()
    print(calculator(expr))


if __name__ == '__main__':
    x = Stack()
    x.append(1)
    x.append(2)
    x.append(3)
    print(x.pop())

    tests = (
        ('2 1 + 3 *\n', 9),
        ('7 2 + 4 * 2 +\n', 38),
        ('1 2 + 3 + 4 + 5 +', 15),
        ('4 13 5 / +', 6),
        ('4 2 * 4 / 25 * 2 - 12 / 500 2 * + 2 / -999 + 71 + -1 *', 426),
        ('1\n', 1),
        ('0\n', 0)
    )
    for expr, res in tests:
        assert calculator(expr) == res

    main()
