n = 4

j = 3
v = 3

for i in range(20):
    if j:
        j-=1
    else:
        j = n - 1
    v = (v - 1) % n
    print(j, v)
