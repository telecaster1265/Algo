def is_palindrome(n):
    return n == n[::-1]
    

n = input()
if is_palindrome(n):
    print(1)
else:
    print(0)
        