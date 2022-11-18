class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        nums.sort()
        for s in nums:
            cnt[s] = cnt.get(s, 0) + 1
        return sorted(cnt, key = cnt.get, reverse=True)[:k]
        