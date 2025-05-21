import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []

for _ in range(n):
    row = input().strip()
    board.append(row)

def chess(x, y, board):
    w_cnt = 0  
    b_cnt = 0  

    for i in range(8):
        for j in range(8):
            current = board[x + i][y + j]
            if (i + j) % 2 == 0:  
                if current != 'W':
                    w_cnt += 1
                if current != 'B':
                    b_cnt += 1
            else:  
                if current != 'B':
                    w_cnt += 1
                if current != 'W':
                    b_cnt += 1
    return min(w_cnt, b_cnt)

result = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        need = chess(i, j, board)
        if need < result:
            result = need

print(result)