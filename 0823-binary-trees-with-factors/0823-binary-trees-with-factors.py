class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD = 10**9 + 7
        
        dp = {}
        for n in arr:
            dp[n] = 1
        
        for k, v in enumerate(arr):
            for i in range(k):
                if not(v % arr[i]) and v // arr[i] in dp:
                    dp[v] += dp[arr[i]] * dp[v//arr[i]]
                    dp[v] %= MOD
        return sum(dp.values()) % MOD
        
        