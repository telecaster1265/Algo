t = int(input())

for i in range(1, t+1):
    odd = list(map(int, input().split()))
    odd_sum = 0

    for j in odd:
        if j % 2 != 0:
            odd_sum += j

    print(f'#{i} {odd_sum}')