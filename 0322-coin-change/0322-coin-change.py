class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [float('inf')] * (amount + 1)
        min_coins[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
        
        return -1 if min_coins[amount] == float('inf') else min_coins[amount]
        
