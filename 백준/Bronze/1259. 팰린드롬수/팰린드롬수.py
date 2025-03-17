import sys

def is_palindrome(s):
    return s == s[::-1]

while True:
    t = input().strip()
    if t == "0":
        break
    if is_palindrome(t):
        print("yes")
    else:
        print("no")