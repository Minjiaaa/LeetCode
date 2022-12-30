class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # 折半搜索法：把 A， B的和放在一个哈希表中，然后找C D的和的负数是否在前面的哈希表中
            counter = {}
            for a in nums1:
                for b in nums2:
                    counter[a + b] = counter.get(a + b, 0) + 1
            res = 0
            for c in nums3:
                for d in nums4:
                    res += counter.get(-c-d, 0)
            return res
        