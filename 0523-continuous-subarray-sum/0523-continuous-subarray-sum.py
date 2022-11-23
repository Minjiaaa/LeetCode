class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSumModK = 0
        table = {0 : -1} #1改成-1之后就通过了
        res = 0
        for i in range(len(nums)):
            preSumModK = (nums[i] + preSumModK) % k
            if preSumModK in table:
                if i - table[preSumModK] >= 2:
                    return True
            else:
                table[preSumModK] = i
        
        return False
            