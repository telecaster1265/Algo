import sys

input = sys.stdin.readline

n = int(input())
atm = list(map(int, input().split()))

atm.sort()

time = 0
sum = 0

for i in atm:
    sum += i
    time += sum
print(time)