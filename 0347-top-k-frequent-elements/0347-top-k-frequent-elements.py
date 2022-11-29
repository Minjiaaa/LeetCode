class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #O(1) time
        if k == len(nums):
            return nums
        # 1.build hashmap: char and frequency
        count = Counter(nums)
        
        # 2-3 build heap of top k frequent elements and convert it into an output array
        uniqueNums = list(count.keys())
        # turn the hashmap into a priotity queue (key, value) in order
        pq = [(count[num], num) for num in uniqueNums[:k]]
        heapq.heapify(pq)
        for num in uniqueNums[k:]:
            heapq.heappush(pq, (count[num], num)) # insert and adjust the order
            heapq.heappop(pq)
        
        return [ele[1] for ele in pq]
        