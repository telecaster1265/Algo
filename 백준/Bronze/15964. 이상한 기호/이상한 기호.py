def op(a, b):
    return (a + b) * (a - b)

a, b = map(int, input().split())
print(op(a,b))