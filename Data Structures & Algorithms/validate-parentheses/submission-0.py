class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lastToFirst = { '}' : '{', ']' : '[', ')' : '('}

        for c in s:
            if c in lastToFirst:
                if stack and stack[-1] == lastToFirst[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

            