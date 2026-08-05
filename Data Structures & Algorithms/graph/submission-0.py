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

        return dfs(src, dst, visit)