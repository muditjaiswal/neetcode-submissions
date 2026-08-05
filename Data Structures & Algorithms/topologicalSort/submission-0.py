class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = {i:[] for i in range(n)}
        for s, d in edges:
            if s not in adj_list:
                adj_list[s] = []
            adj_list[s].append(d)
        
        visited = set()
        path = set()
        topSort = []

        for s in range(n):
            if self.dfs(s, adj_list, visited, path, topSort) == False:
                return []
        topSort.reverse()
        return topSort
        
    def dfs(self, s, adj_list, visited, path, topSort):
        if s in path:
            return False
        if s in visited:
            return True
        
        path.add(s)
        
        for neighbour in adj_list[s]:
            if self.dfs(neighbour, adj_list, visited, path, topSort) == False:
                return False
        
        path.remove(s)
        topSort.append(s)
        visited.add(s)
        return True