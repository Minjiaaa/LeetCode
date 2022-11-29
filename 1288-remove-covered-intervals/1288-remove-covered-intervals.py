class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0], - x[1])) #对起点按升序排列，若起点相同，则对终点按降序排列。#贪心思想？
        cnt = 1 #不被前一个区间覆盖
        pre = intervals[0] #pre前一个未被覆盖的区间
        for e in intervals[1:]:
            if pre[1] < e[1]:
                cnt += 1
                pre = e
        return cnt
        # for i in range(len(intervals) - 1):
        #     if intervals[i][1] <= intervals[i+1][1] and intervals[i][0] >= intervals[i+1][0]:
        #         cnt += 1
        # return len(intervals) - cnt
        