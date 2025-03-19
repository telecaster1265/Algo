L = int(input())
st = str(input())
r = 31
m = 1234567891
hash = 0

for i in range(L):
    hash = (hash + (ord(st[i]) - ord('a') + 1 ) * pow(r, i, m)) % m
print(hash)