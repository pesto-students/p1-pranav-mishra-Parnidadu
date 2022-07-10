class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def find(x):
            while x != root[x]:
                x = root[x]
            return x
		
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX

        def connected(x, y):
            return find(x) == find(y)
        
        root = [i for i in range(n)]
        
        for u, v in edges:
            union(u, v)
            
        return connected(source,destination)
