class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                # ans[i] = "FizzBuzz"
                ans.append("FizzBuzz")
            #elif i % 3 == 0 and i % 5 !=0 :
            #ans[i] = "Fizz"
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0: #and i % 3 != 0:
                ans.append('Buzz')
            
            else:
                ans.append(str(i))
            
        return ans
            
        