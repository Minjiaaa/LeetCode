class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph) - 1
        path = []
        
        # x：目前遍历的节点
        # graph：存当前的图
        def helper(graph, x):
        # 要求从节点 0 到节点 n-1 的路径并输出，所以是 graph.size() - 1
        # 找到符合条件的一条路径
            if x == target:
                res.append(path[:])
                return
            
            for i in range(len(graph[x])): # 遍历节点n链接的所有节点
                path.append(graph[x][i]) #遍历到的节点加入到路径中来
                helper(graph, graph[x][i]) # 进入下一层递归
                path.pop()
        path.append(0)
        helper(graph, 0)
        return res