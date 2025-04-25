# k-1 k  k+1 
# 0 3 // 1 2 3
# 1 5 // 2 4 5 
# 45 50 // 46 48 49 50

def jump(x,y):
    d = y -x
    n = 1
    move = 0
    while n * (n + 1) < d:
        n += 1
    if d <= n * n:
        return (2 * n) - 1
    else:
        return 2 * n

t = int(input())        
for _ in range(t):
    x, y = map(int, input().split())
    print(jump(x,y))
            