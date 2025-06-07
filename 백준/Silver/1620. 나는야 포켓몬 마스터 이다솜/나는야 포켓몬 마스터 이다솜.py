import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pokemons = []
dic = {}

for i in range(n):
    name = input().strip()
    pokemons.append(name)
    dic[name] = i + 1

for _ in range(m):
    ins = input().strip()
    if ins.isdigit():
        num = int(ins)
        print(pokemons[num - 1])
    else:
        print(dic[ins])