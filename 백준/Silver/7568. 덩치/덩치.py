n = int(input())
physical = []

for _ in range(n):
    weight, height = map(int, input().split())
    physical.append((weight, height))

ranks = []
for i in range(n):
    rank = 1
    for j in range(n):
        if i != j:
            if physical[j][0] > physical[i][0] and physical[j][1] > physical[i][1]:
                rank += 1
    ranks.append(rank)

print(*ranks)