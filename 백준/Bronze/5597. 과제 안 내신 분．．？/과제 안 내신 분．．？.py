all = list(range(1,31))
n = [int(input()) for _ in range(28)]
non = []
for i in all:
    if i not in n:
        non.append(i)
non.sort()
print(non[0])
print(non[1])