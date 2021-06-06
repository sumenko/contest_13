# Рекурсивные числы Фибоначчи

def trainee_commits(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return trainee_commits(n-2) + trainee_commits(n - 1)


if __name__ == '__main__':
    tests = (
        (3, 3),
        (0, 1),
        (4, 5),
        (6, 13)
    )
    for num, result in tests:
        assert trainee_commits(num) == result

    num = int(input())
    if 0 <= num <= 32:
        print(trainee_commits(num))
