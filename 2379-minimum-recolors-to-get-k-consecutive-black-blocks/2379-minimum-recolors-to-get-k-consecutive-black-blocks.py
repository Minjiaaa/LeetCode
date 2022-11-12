class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = k
        total = 0
        for i in range(left, right):
            if blocks[i] == 'W':
                total += 1
        minOp = total
        for i in range(len(blocks) - k):
            if blocks[left] == 'W':
                total -= 1
            left += 1
            if blocks[right] == 'W':
                total += 1
            right += 1
            minOp = min(minOp, total)

        
        return minOp
                
            
            
            
        