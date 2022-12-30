class TwoSum:

    def __init__(self):
        #initialize the data structure
        self.count = {}
        
    # add the number to the internal data structure
    # return nothing
    def add(self, number: int) -> None:
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1
        #self.table[number] = self.table.get(number, 0) + 1;

    # find if there exisis any pair of numbers which sum is equal to the value
    # return true if can be found or false
    def find(self, value: int) -> bool:
        for num in self.count:
            if value - num in self.count and \
                (value - num != num or self.count[num] > 1):
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)