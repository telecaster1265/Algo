import sys

input = sys.stdin.readline

import sys

input = sys.stdin.readline

isbn = input().strip() 

weights = [1 if i % 2 == 0 else 3 for i in range(12)]
broken = isbn.index('*')

total = 0
for i in range(12):
    if i == broken:
        continue
    total += int(isbn[i]) * weights[i]

check = int(isbn[12])

for j in range(10):
    if (total + j * weights[broken] + check) % 10 == 0:
        print(j)
        break