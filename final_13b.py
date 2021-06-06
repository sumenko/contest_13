# Спринт 13. Задача B
# Суменко В.А.
# попытки: 51820227

class StackIsFull(Exception):
    pass


class StackIsEmpty(Exception):
    pass


class Stack():
    def __init__(self, size):
        self.size = size
        self.stack = [None * size]
        self.idx = 0

    def append(self, x):
        if self.idx == self.size:
            raise StackIsFull

        self.stack[self.idx] = x
        self.idx += 1

    def pop(self):
        if self.idx:
            value = self.stack[self.idx]
            self.idx -= 1
            return value
        raise StackIsEmpty


# class Stack():
#     class Node():
#         def __init__(self, num, next=None):
#             self.value = num
#             self.next = next
    
#     def __init__(self):
#         self.next = None
    
#     def push(self, num):
#         self.next = self.Node(num, self.next)
    
#     def pop(self):
#         if self.next:
#             value = self.next.value

#         return value

def calculator(expr):
    if expr == '':
        return None

    task = expr.split()

    max_length = len(task)
    stack = Stack(max_length)

    # stack = []
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
            stack.insert(0, res)
    result = stack.pop()
    return result


def main():
    expr = input()
    print(calculator(expr))


if __name__ == '__main__':
    tests = (
        ('2 1 + 3 *\n', 9),
        ('7 2 + 4 * 2 +\n', 38),
        ('1\n', 1),
        ('0\n', 0)
    )
    for expr, res in tests:
        assert calculator(expr) == res

    main()
