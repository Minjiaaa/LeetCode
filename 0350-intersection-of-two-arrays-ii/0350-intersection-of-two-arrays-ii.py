class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        count = Counter(nums1)
        res = []
        
        for x in nums2:
            if count[x] > 0:
                res.append(x)
                count[x] -= 1 #计数结束的就被消除了
        return res
        # for i in range(len(nums1)):
        #     count[nums1[i]] = count.get(nums1[i], 0) + 1
        # for x in nums2:
        #     if count[x] > 0:
        #         res.append(x)
        #         count[x] -= 1
        #     # if nums1.count(i) > nums2.count(i): #这一步不会操作
        #     #     res.append(nums1[i])
        
        return res