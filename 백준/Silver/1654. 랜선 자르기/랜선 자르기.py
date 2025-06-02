import sys

input = sys.stdin.readline

k, n = map(int, input().split())


def max_lan(k, n, lines):
    start = 1
    end = max(lines)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        count = sum(line // mid for line in lines)

        if count >= n:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

lan = []
for _ in range(k):
    length = int(input())
    lan.append(length)

print(max_lan(k, n, lan))