matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

def maximal_square(matrix):
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    res = 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if matrix[i-1][j-1] == "1":
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                res = max(res, dp[i][j])
    return res * res

print(maximal_square(matrix))
