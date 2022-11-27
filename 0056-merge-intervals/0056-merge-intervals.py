#感觉很像calendar的题目
#需要新建数组吗？如何记录每一次merge之后的结果，在原数组上修改吗？
# 因为我们要取最左边界和最右边界，左边界通过排序，右边界通过比较。
# 3 将排序后的intervals[0]的左右端点当做start和end，之后从1-len(intervals)开始比较。
# 4 当intervals[i][0] > end,标识此处断开。此时将start和end加入ret待返回的数组。更新start和end的做法
# 5 当intervals[i][0] < end,标识此处未断开。此时end 应该等于max(end,intervals[i][1])
# 6 之后intervals[i]的左右边界作为新的start和end。
# 7 持续4、5、6 操作，知道数组遍历结束。此时最后一个数组没有比较，则直接将start和当前的end加入ret待返回数组。
# 8.返回ret即可


class Solution:    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] > end:
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
                
        res.append([start, end])
        return res