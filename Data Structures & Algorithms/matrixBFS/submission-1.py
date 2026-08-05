class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        r = 0
        c = 0
        visited = set()
        queue = deque()

        visited.add((r, c))
        queue.append((r, c))
        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length
                
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or (r + dr, c + dc) in visited or grid[r + dr][c + dc] == 1:
                        continue
                    visited.add((r + dr, c + dc))
                    queue.append((r + dr, c + dc))
            length += 1
        return -1
            