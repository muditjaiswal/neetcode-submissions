class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()

        # find all treasure chests
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        # run BFS
        distance = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()
                if distance < grid[row][col]:
                    grid[row][col] = distance

                neighbours = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dr, dc in neighbours:
                    if min(row + dr, col + dc) < 0 or row + dr == ROWS or col + dc == COLS or grid[row + dr][col + dc] == -1 or (row + dr, col + dc) in visited:
                        continue
                    queue.append((row + dr, col + dc))
                    visited.add((row + dr, col + dc))
            distance += 1