import sys
input = sys.stdin.readline

alphabets = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
n = input().strip()

cnt = 0

for alphabet in alphabets:
    while alphabet in n:
        n = n.replace(alphabet, " ", 1)  # replace 메서드 1개씩만 교체
        cnt += 1

cnt += len(n.replace(" ", ""))
print(cnt)
