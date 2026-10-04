Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def reverse(self, x: int) -> int:
        min_int , max_int = -2**31 , 2**31 -1 

        result =0 

        sign =-1 
        if x < 0:
            sign =-1 
        else:
            sign =1 

        x = abs(x)

        while x :
            digit = x % 10 
            x = x//10

            if ( result > max_int //10 ) or ( result == max_int // 10  and digit > max_int %10):
                return 0
            
            result = result*10 + digit
        
        return sign * result 
