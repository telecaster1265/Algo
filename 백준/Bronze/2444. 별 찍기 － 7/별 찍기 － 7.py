n = int(input())
for i in range(n):
    star = 2*i + 1
    blank = n-i - 1
    print(" " * blank + "*" * star)
    
for i in range(n-2, -1, -1):
   star = 2*i + 1
   blank = n-i - 1
   print(" " * blank + "*" * star)