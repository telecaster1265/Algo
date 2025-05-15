import sys

input = sys.stdin.readline


while True:
    n = int(input())
    if n == -1:
        break

    div = []
    for i in range(1,n):
        if n % i == 0:
            div.append(i)

    if sum(div) == n:
        print(f"{n} = {' + '.join(map(str, div))}")
    else:
        print(f"{n} is NOT perfect.")
