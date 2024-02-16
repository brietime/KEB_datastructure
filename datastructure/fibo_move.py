def fibo_repetition(number: int) -> int:
    """
    fibonacci function by repetition.
    :param number: integer number
    :return: integer number
    """
    a = 0
    b = 1
    for _ in range(number):
        a, b = b, a + b
    return a

def fibo_memoization(ROW,COL):
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    memo = [[0 for _ in range(COL)] for _ in range(ROW)]
    memo[0][0] = fibo_memoization[0][0]
    row_sum = memo[0][0]
    
    # if memo[number] is not None:
    #     return memo[number]
    # if number < 2:
    #     result = number
    # else:
    #     result = fibo_memoization(number-1) + fibo_memoization(number-2)
    #     memo[number] = result
    # return result
    
    for i in range(1, ROW):
        row_sum += fibo_memoization[0][i]
        memo[0][i] = row_sum

    col_sum = memo[0][0]
    for i in range(1, COL):
        col_sum += fibo_memoization[i][0]
        memo[i][0] = col_sum

    for row in range(1, COL):
        for col in range(1, ROW):
            if (memo[row][col - 1] > memo[row - 1][col]):   # 부등호 방향으로 최소/ 최대 가능
                memo[row][col] = memo[row][col - 1] + fibo_memoization[row][col]
            else:
                memo[row][col] = memo[row - 1][col] + fibo_memoization[row][col]

    return memo[COL-1][ROW-1]


n = int(input("Input number : "))

for i in range(0, n):
    print(i)
    print(fibo_memoization(i,i))

print("===========================")
for i in range(0, n):
    print(i)
    print(fibo_repetition(i))
    