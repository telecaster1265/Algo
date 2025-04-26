points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))
    
x_list = [p[0] for p in points]
y_list = [p[1] for p in points]

for i in x_list:
    cnt_x = 0
    for j in x_list:
        if i == j:
            cnt_x += 1
    if cnt_x == 1:
        x_ans = i
        
for i in y_list:
    cnt_y = 0
    for j in y_list:
        if i == j:
            cnt_y += 1
    if cnt_y == 1:
        y_ans = i
        
print(x_ans, y_ans)
