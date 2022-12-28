class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 构建图，代表（先修课 ->多个后修课）的映射
        # 图的初始化，每个先修课 -> 空先修课list
        graph = [[] for i in range(numCourses)]
        
        # 1. 统计每个点的入度，并构建图
        in_degree = [0] * numCourses
        for node_in, node_out in prerequisites:
            graph[node_out].append(node_in)
            in_degree[node_in] += 1
            #print(node_in, node_out)
            
        # 2. 将每个入度为0的点放入队列（queue）作为起始节点
        queue = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # 记录已修课程的数量
        num_choose = 0
        
        # 记录拓扑排序
        topo_order = []
        
        # 3. 不断从队列中拿出一个点，去掉这个点的所有连边（指向其他店点的边）
        # 其他店的响应的入读-1
        while queue:
            cur_pos = queue.popleft()
            topo_order.append(cur_pos)
            num_choose += 1
            # 当前点的所有邻居的入度减2， 表示每个后修课的一门先修课已经完成
            for next_pos in graph[cur_pos]:
                in_degree[next_pos] -= 1
                # 4. 一旦发现新的入度为0的点，丢回队列中
                # 表示一门后修课的所有先修课已经完成，可以被修
                if in_degree[next_pos] == 0:
                    queue.append(next_pos)
        #如果全部课程已经被修过，那么返回拓扑排序，否则返回空
        return topo_order if num_choose == numCourses else []