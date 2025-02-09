num = [int(input()) for _ in range(10)]
cnt = {n % 42 for n in num}
print(len(cnt))