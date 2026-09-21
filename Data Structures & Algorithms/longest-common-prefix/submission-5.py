class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        if len(strs) < 2:
            return ''
        
        common =""
        i = 0 # letter in each word
        while True:
            if (i+1) <= len(strs[0]):
                base_letter = strs[0][i]
            else: 
                return common
            for word in strs:
                if (i + 1) > len(word) or word[i] != base_letter:
                    return common
            common += base_letter
            i += 1
                
