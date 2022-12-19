class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        
        fizz_buzz_dict = {3: 'Fizz', 5: 'Buzz'}
        divisors = [3, 5]
        
        for num in range(1, n + 1):
            
            ans_str = [] #设置中间收集单一结果的变量
            
            # see whether the num is divisible by key, and add corresponding string map
            for key in divisors:
               
                if num % key == 0:
                    ans_str.append(fizz_buzz_dict[key]) 
                
            if not ans_str:
                ans_str.append(str(num))

            ans.append(''.join(ans_str))
        
        return ans
            
            
            
        