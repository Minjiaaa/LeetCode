class Solution:
    #1.对p取余数，记录余数mod
    #2.求前缀和：遍历数组
    #3.因为题目不是固定顺序，需要快速查找，所以使用哈希表进行查找
    #注意题目说是subarray，不是零散的字符
    #一开始先把minLen设为nums的长度
    #curMod可能比mod要小，避免target出现负数，在target中多加一个p
    #不知道自己哪里错了
    #剪枝：如果mod = 0， 说明不需要去除任何数，返回0
    #求前缀和数组，使用累加就可以
    #求当前的前缀和，然后对p取余；求目标前缀和对p取余
    #将当前位置的前缀和存储起来
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        mod = sum(nums) % p
        cnt = {0:-1}
        n = len(nums)
        minLen = n
        curSum = 0
        # preFix = [0] * (n + 1)
        
        if mod == 0:
            return 0

        for i in range(n):
            # preFix[i] += nums[i] 
            # curMod = preFix[i] % p
            curSum += nums[i] #构造前缀和数组出问题
            curMod = curSum % p
            cnt[curMod] = i
            
            if curMod >= mod:
                target = (curMod - mod) % p
            else:
                target = (curMod - mod + p) % p
            if target in cnt:
                minLen = min(minLen, i - cnt[target])
            
        if minLen == n:
            minLen = -1
            
        return minLen
                

            
            