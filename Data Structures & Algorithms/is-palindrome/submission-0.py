class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(char for char in s if char.isalnum())
        s1 = s1.lower()

        i,j = 0, len(s1)-1

        while i < j:
            if s1[i] != s1[j]:
                return False
            i = i+1
            j = j-1
        return True