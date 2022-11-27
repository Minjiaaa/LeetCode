#如何处理这些动态的数组
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        res = []
        def intersected(a, b):
            if a[0] > b[1] or a[1] < b[0]:
                return False
            return True
        #前
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1 
            
        #中
        while i < n and intersected(intervals[i], newInterval):
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        res.append(newInterval)
        
        #后
        while i < n:
            res.append(intervals[i])
            i += 1
        
        return res
        