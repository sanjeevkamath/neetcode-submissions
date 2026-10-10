class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_s = {}
        word_t = {}

        for letter in s:
            if letter in word_s:
                word_s[letter] += 1
            else:
                word_s[letter] = 1
        for letter in t:
            if letter in word_t:
                word_t[letter] += 1
            else:
                word_t[letter] = 1

        return word_s == word_t