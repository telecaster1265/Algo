import sys

input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    tri = sorted([a, b, c])

    if a == b == c == 0:
        break
    
    if tri[2] >= tri[0] + tri[1]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")