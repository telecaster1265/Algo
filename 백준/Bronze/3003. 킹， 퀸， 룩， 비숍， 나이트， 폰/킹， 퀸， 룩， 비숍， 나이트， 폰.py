piece = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

result = [chess[i] - piece[i] for i in range(6)]
print(*result)