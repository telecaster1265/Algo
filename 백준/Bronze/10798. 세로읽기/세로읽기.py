import sys

input = sys.stdin.readline

texts = []
for _ in range(5):
    text = input().strip()
    texts.append(text)
    
for j in range(15):
    for i in range(5):
        if j < len(texts[i]):
            print(texts[i][j], end='')