class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        if not tickets:
            return res
        
        graph = defaultdict(list)
        for depart, arrive in tickets:
            graph[depart].append(arrive)
        
        for k in graph:
            graph[k].sort()
        
        def visit(graph, src, res):
            while graph[src]:
                visit(graph, graph[src].pop(0), res)
            res.insert(0, src)
        visit(graph, "JFK", res)
        return res
        
