from heapq import heappush, heappop, heapify
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = self.build_graph(words)
        # 如果数据不合理，graph为空，返回空字符串
        if not graph:
            return ""
        return self.topological_sort(graph)

    def build_graph(self, words):
        # 存放（字母->右边的多个字母）的映射关系
        graph = {}
        
        # 生成所有的点，每个点的后续点暂时为空
        # initialize the graph
        for word in words:
            for c in word:
                if c not in graph:
                    graph[c] = set()
        
        # 生成所有的边，找到一个点之后的点，并且建立连接
        n = len(words)
        for i in range(n - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break
                    #如果输入['abc', "ab", "abc"出现在“ab”前面，不合法，返回null]
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                           return None
        return graph
    def topological_sort(self, graph):
        # 1. 统计每个点的入数
        indegree = self.get_indegree(graph)
        
        # 2. 将每个入度为0的点放入队列中作为起始节点
        queue = [node for node in graph if indegree[node] == 0]
        # 要求： 这里可能有多个有效的字母顺序，返回以正常字典顺序看来最小的
        # 所以这里要heapify，从所有可以出队的元素中，先出队字典序比较小的元素
        heapify(queue)

        # 记录拓扑排序（外星人字典排序）
        topo_order = ""

        # 3. 不断从队列中拿出一个点，去掉这个点的所有连边（指向其他点的边）
        #  其他店的相应的入度 -1
        while queue:
            node = heappop(queue)
            topo_order += node
            for neighbor in graph[node]:
                # 当前点的邻居的入度减1
                indegree[neighbor] -= 1
                # 4. 一旦发现新的入度为0， 丢回队列中
                if indegree[neighbor] == 0:
                    heappush(queue, neighbor) # heap谁最小谁先出
        
        # 如果有些字母没有出现在字典排序中，那么没有答案
        return topo_order if len(topo_order) == len(graph) else ""

    # 统计每个点的入度。如果一个点的入度为0， 那么这个点依然存在于dict中，对应入度为0
    def get_indegree(self, graph):
        # 初始化所有点的入度为0
        indegree = {node: 0 for node in graph}
        
        for node in graph:
            #所有邻居的入度+1
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree

