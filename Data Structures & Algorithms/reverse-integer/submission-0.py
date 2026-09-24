class Solution:
    def reverse(self, x: int) -> int:
        min_int = - (2 ** 31)
        max_int = (2 ** 31) - 1
        
        sign = 1
        if x < 0:
            sign = -1
    
        string = str(abs(x))
        reversed = int(string[::-1])
        reversed *= sign

        if reversed > max_int or reversed < min_int:
            return 0
        else:
            return reversed
