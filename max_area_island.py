class solution:
    def maxarea(self, matrix):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.cur_area = 0
                    self.dfs(grid, i, j)
                    res = max(res, self.cur_area)
        return res

    def dfs(self, matrix, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != 1:
            return
        self.cur_area += 1
        grid[i][j] = 0
        self.dfs(grid, i, j-1)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i+1, j)
