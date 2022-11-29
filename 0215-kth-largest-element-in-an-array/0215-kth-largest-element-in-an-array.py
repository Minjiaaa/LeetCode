class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a min-heap with size of k
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]
        
        #quick select, O(n)
#         pivot = nums[0]
#         left  = [l for l in nums if l < pivot]
#         equal = [e for e in nums if e == pivot]
#         right = [r for r in nums if r > pivot]
        
#         if k <= len(right):
#             return self.findKthLargest(right, k)
#         elif (k - len(right)) <= len(equal):
#             return equal[0]
#         else:
#             return self.findKthLargest(left, k - len(right) - len(equal))
    

        #bruteforce
#         n = len(nums)
#         nums.sort()
#         return nums[n-k]
        