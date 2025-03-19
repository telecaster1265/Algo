n = int(input())

if n == 1:
    print(1)
    exit()

start = 1
end = 1

while end < n:
    end += 6 * start
    start += 1
    
print(start)
    
    