## 함수 선언부
def grow_rich() :
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = gold_maze[0][0]

    row_sum = memo[0][0]
    for i in range(1, ROW):
    row_sum += gold_maze[0][i]
    memo[0][i] = row_sum

    col_sum = memo[0][0]
    for i in range(1, COL):
    col_sum += gold_maze[i][0]
    memo[i][0] = col_sum

    for row in range(1, ROW):
    for col in range(1, COL):
        if (memo[row][col - 1] < memo[row - 1][col]):   # 부등호 방향으로 최소/ 최대 가능
            memo[row][col] = memo[row][col - 1] + gold_maze[row][col]
        else:
            memo[row][col] = memo[row - 1][col] + gold_maze[row][col]

    return memo[ROW-1][COL-1]


## 전역 변수부
ROW, COL = 5, 5
gold_maze = [    [1, 4, 4, 2, 2],
                [1, 3, 3, 0, 5],
                [1, 2, 4, 3, 0],
                [3, 3, 0, 4, 2],
                [1, 3, 4, 5, 3]   ]

## 메인 코드부
macolGold = grow_rich()
print('압정 미로에서 밟은 최소 압정 개수 -->', macolGold)