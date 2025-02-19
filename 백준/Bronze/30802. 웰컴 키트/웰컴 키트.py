import math

n = int(input())

size = map(int, input().split())
t, p = map(int, input().split())

t_bundle = sum(math.ceil(s / t) for s in size)
p_bundle = math.ceil(n / p)

print(t_bundle)
print(n // p , n % p)
