a = input()
t = 0
tele = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

for i in a:
    for j in range(len(tele)):
        if i in tele[j]:
            t += j + 3
print(t)