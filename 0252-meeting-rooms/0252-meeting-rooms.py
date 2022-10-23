class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # #不知道如何表示overlap，两两比较, 暴力法会超出时间限制
        # def overlap(interval1: List[int], interval2: List[int]) -> bool:
        #     return (interval1[0] >= interval2[0] and interval1[0] < interval2[1]) or (interval2[0] >= interval1[0] and interval2[0] < interval1[1])
        # for i in range(len(intervals)):
        #     for j in range(i + 1, len(intervals)):
        #         if overlap(intervals[i], intervals[j]):
        #             return False
        # return True
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True
        