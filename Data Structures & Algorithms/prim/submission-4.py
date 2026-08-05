class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        
        # build adjacency list
        adj_list = {}
        
        for s, d, w in edges:
            if s not in adj_list:
                adj_list[s] = []
            adj_list[s].append((d, w))
            if d not in adj_list:
                adj_list[d] = []
            adj_list[d].append((s, w))

        if len(adj_list) < n:
            return -1

        minheap = []
        for d, w in adj_list[0]:
            heapq.heappush(minheap, (w, 0, d))

        mst = 0
        visited = set()
        visited.add(0)

        while minheap:
            w, s, d = heapq.heappop(minheap)
            if d in visited:
                continue
            mst += w
            visited.add(d)

            for neighbour, weight in adj_list[d]:
                if neighbour not in visited:
                    heapq.heappush(minheap, (weight, d, neighbour))
        
        if len(visited) != n:
            return -1

        return mst


