a, b, v = map(int, input().split())
up = a - b
days = (v - a) // up

if (v - a) % up != 0:
    days += 1
    
print(days + 1)