import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

a_set= set(a)

m = int(input())
numbers = list(map(int,input().split()))

for number in numbers:
    if number in a_set:
        print(1)
    else:
        print(0)