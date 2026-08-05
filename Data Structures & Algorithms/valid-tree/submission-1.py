class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True

        adj_list = {i : [] for i in range(n)}
        for start, end in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False 

            visited.add(node)
            for j in adj_list[node]:
                if j == prev:
                    continue
                if dfs(j, node) == False:
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n