a = int(input())
b = int(input())
c = int(input())

multiple = a * b * c

count_str = str(multiple)

for i in range(10):
    print(count_str.count(str(i)))