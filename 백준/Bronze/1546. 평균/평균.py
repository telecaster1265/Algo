n = int(input())
score = list(map(int, input().split()))

m = max(score)
jujak = [(i / m) * 100 for i in score]
average = sum(jujak) / n

print(average)