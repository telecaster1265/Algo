max_train = 0
train_in = 0

for _ in range(4):
    a, b = map(int,input().split())
    train_in -= a
    train_in += b
    max_train = max(max_train, train_in)

print(max_train)