import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        div = 1
        while x > div * 10:
            div = div * 10
        
        while x != 0:
            right = x % 10
            left = x // div

            if right != left: return False

            x = (x % div) // 10
            div = div / 100
        return True