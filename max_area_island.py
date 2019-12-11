class solution:
    def maxarea(self, matrix):
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    self.current_area =0
                    self.dfs(matrix, i, j)
                    max_area = max(max_area, self.current_area)
        return max_area

    def dfs(self, matrix, i, j):
        self.current_area += 1
        matrix[i][j] = 0
        if j - 1 >= 0 and grid[i][j-1] == 1:
            self.dfs(grid, i, j-1)
        if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
            self.dfs(grid, i, j+1)
        if i - 1 >= 0 and grid[i-1][j] == 1:
            self.dfs(grid, i-1, j)
        if i + 1 < len(grid) and grid[i+1][j] == 1:
            self.dfs(grid, i+1, j)
