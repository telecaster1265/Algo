import sys

input = sys.stdin.readline


while True:
    string = input().rstrip()
    if string == ".":
        break

    stack = []
    b = True

    for char in string:
        if char == "(" or char == "[":
            stack.append(char)
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                b = False
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                b = False
                break

    if b and not stack:
        print("yes")
    else:
        print("no")