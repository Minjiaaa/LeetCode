class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        preSum = 0
        cnt = 0
        oddNum = 0
        table = {0 : 1}
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                oddNum += 1
            if oddNum in table:
                table[oddNum] += 1
            else:
                table[oddNum] = 1
            if oddNum - k in table:
                cnt += table[oddNum - k]
            
        
        return cnt