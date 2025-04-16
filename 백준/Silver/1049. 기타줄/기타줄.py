n,m = map(int,input().split())
pack = []
ea = []

for _ in range(m):
    a,b = map(int,input().split())
    pack.append(a)
    ea.append(b)

min_pack = min(pack)
min_ea = min(ea)

cost1 = min_ea * n
cost2 = ((n+5) // 6) * min_pack
cost3 = (n // 6) * min_pack + (n % 6) * min_ea
print(min(cost1,cost2,cost3))
        