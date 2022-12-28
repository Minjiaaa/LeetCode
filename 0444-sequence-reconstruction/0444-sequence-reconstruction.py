class Solution:
    def sequenceReconstruction(self, nums: List[int], seqs: List[List[int]]) -> bool:
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == nums
    
    def build_graph(self, seqs):
        # initialize graph
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
            
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])
                    
        return graph
    
    def get_indegrees(self, graph):
        indegrees = {
            node : 0
            for node in graph
        }
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees
    
    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)
        
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        
        topo_order = []
        while queue:
            # there must exisit more than one topo order
            if len(queue) > 1:
                return None
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        if len(topo_order) == len(graph):
            return topo_order
        return None