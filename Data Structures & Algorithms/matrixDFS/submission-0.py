class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        r = 0
        c = 0
        
        def dfs(grid, r, c, visited):
            ROWS = len(grid)
            COLS = len(grid[0])
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 1 or (r,c) in visited:
                return 0
            if r == ROWS - 1 and c == COLS - 1:
                return 1
            
            count = 0
            visited.add((r, c))

            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r, c + 1, visited)
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r, c - 1, visited)

            visited.remove((r, c))

            return count
        
        return dfs(grid, r, c, visited)