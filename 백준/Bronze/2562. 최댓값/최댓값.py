numbers = [int(input()) for _ in range(9)]

maxV = max(numbers)
maxI = numbers.index(maxV) + 1

print(maxV)
print(maxI)