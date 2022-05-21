class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path, result = [[0]],[]
        
        while path:
            new = []
            for way in path:
                for next_node in graph[way[-1]]:
                    destination = result if next_node == len(graph)-1 else new
                    destination.append(way[:]+ [next_node])
            path = new
        return result