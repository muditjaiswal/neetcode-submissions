class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        self.adj_list[src].add(dst) 


    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        self.adj_list[src].remove(dst)
        return True


    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()

        def dfs(src, dst, visit):
            if src == dst:
                return True

            visit.add(src)
            
            for neighbour in self.adj_list[src]:
                if dfs(neighbour, dst, visit):
                    return True
            
            visit.remove(src)
            return False

        def bfs(src, dst, visit):
            queue = deque()
            queue.append(src)
            visit.add(src)

            while queue:
                for i in range(len(queue)):
                    node = queue.popleft()
                    if node == dst:
                        return True
                    
                    for neighbour in self.adj_list[node]:
                        if neighbour not in visit:
                            visit.add(neighbour)
                            queue.append(neighbour)
            return False

        return bfs(src, dst, visit)