# Транспонирование матрицы


def transpos(n, m, source):
    # инициализация двумерного массива
    
    t = [['' for _ in range(n)] for _ in range(m)]
    for row in range(n):
        for col in range(m):
            t[col][row] = source[row][col]

    return [' '.join(a) for a in t]

n = 4 #int(input())
m = 3 #int(input())
# array = []
# for _ in range(n):
#     array.append(input().split())
t = transpos(n, m, [['1','2','3'], ['0', '2', '6'], ['7','4','1'], ['2','7','0']])
# t = transpos(n, m, array)

print(*t, sep='\n')
# assert transposition