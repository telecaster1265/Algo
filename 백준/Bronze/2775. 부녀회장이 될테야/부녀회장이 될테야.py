t = int(input())

apt = [[0] * 15 for _ in range(15)]

for i in range(1, 15):
    apt[0][i] = i

for k in range(1, 15):
    for n in range(1, 15):
        apt[k][n] = apt[k][n - 1] + apt[k - 1][n]

for _ in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n])