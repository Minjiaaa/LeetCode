class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Create a dictionary to store the last index of each character
        last = {c : i for i, c in enumerate(s)} 
        
        # Initialize variables to store the start and end indices of the current partition
        start = end = 0 # start of the current partition
        ans = []
        
        # Iterate through the string
        # Update the end index to be the maximum of the current end index and the last index of the current character
        for i, c in enumerate(s):
            end = max(end, last[c])
            
        # If we have reached the end of the current partition, append it to the list of partitions and reset the start and end indices
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
                
        return ans
                
            
        