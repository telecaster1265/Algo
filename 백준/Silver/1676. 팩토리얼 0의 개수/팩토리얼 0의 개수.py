# 3! = 3*2*1 10! = 10*9*8*7*6*5*4*3*2*1

n = int(input())
cnt = 0

while n >= 5:
    cnt += n //5
    n //= 5
print(cnt)