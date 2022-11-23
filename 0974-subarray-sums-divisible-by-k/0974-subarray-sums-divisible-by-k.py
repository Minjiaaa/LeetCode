class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #前缀和+HashMap+同余定理
        #原题目可以转化成
        #1. 子数组的元素之和, nums[i] -- nums[j]的和等价于前缀和preSum[j] - PreSum[i-1]
        #2. 元素和可以被k整除的子数组的数目，等价于有多少种i和j的组合，可以保证(preSum[j] - PreSum[i-1]) % k == 0 <-> preSum[j]% k == preSum[i-1]) % k
            # 前提是preSum[i-1] preSum[j]为正整数，负数单独处理
        # 如何优化i和j两层循环的情况？
            # 前缀和%k的值有哪些，以及出现这个值的次数
            # 使用哈希表存储前缀和%k的值
                #key：前缀和%k
                #value：这个值出现的次数
                
            #找preSumModK的递推关系
             # (a+b) % k = (a % k + b % k) % k
             # preSum[i] % k = (preSum[i-1] + nums[i]) % k
        
        #presSum[-1] = 0，map中提前放入0:1键值对，相当于前缀和%k=0的情况出现了一次。
        #遍历数组，求当前项preSum%k,存入map
            #没有存过，则作为key存入，value为1
            #存过了，则value+1
        #边存边查看，如果map中已经存在key等于当前的preSum%k
            #说明存在preSum%k等于历史的preSum%k,把key对应的出现次数，累加给count
                #key对应出现次数，就相当于有多少个不同的满足条件的字数组，可以进行相减。得到不同的子数组
        
        cnt = 0
        table = {0:1} #计数器初始中默认存在一个哨兵节点
        preSumModK = 0
        
        #前缀和就是数组求和公式，#设置荒谬的情况，让边界情况的计算也能套上公式
        #构造前缀和数组
        
        for i in range(len(nums)):
            preSumModK = (nums[i] + preSumModK) % k
            if preSumModK < 0:
                preSumModK += k
            if preSumModK in table:
                cnt += table[preSumModK] 
                table[preSumModK] += 1
            else:
                table[preSumModK] = 1
            
        return cnt
                
            
        preSum = 0
        
        #前缀和就是数组求和公式，#设置荒谬的情况，让边界情况的计算也能套上公式
        #构造前缀和数组
# 这么写效率低，慢，因为要不停计算取模结果，不如直接递推
#         for i in range(len(nums)):
#             preSum += nums[i] #应该还是prefix公式搞错了
#             if preSum % k < 0:
#                 curMod = k + preSum % k
#             curMod = preSum % k
#             if curMod in table:
#                 cnt += table[curMod] 
#                 table[curMod] += 1
#             else:
#                 table[curMod] = 1
            
#         return cnt
        
        
        
        
        