class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #使用set进行计数
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        for x in set1:
            if x in set2:
                res.append(x)
        return res
        