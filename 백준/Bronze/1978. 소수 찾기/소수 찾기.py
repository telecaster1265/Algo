def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
numbers = map(int, input().split())

cnt = 0
for i in numbers:
    if is_prime(i):
        cnt += 1
print(cnt)