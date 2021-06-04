def calculator(expr):
    if expr == '':
        return None

    task = expr.split()

    stack = []
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
