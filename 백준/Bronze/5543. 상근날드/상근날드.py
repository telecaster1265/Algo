import sys

input = sys.stdin.readline

a= int(input())
b= int(input())
c= int(input())
d= int(input())
e= int(input())

burger = min(a,b,c) + min(d,e) - 50
print(burger)