class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for n in range(0, len(s)):
            if stack and s[n] in mapping and mapping[s[n]] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[n])
        if len(stack) == 0:
            return True
        else:
            return False 
# s="()[)]{}" 
#s = "[{()}]" 
#[]
#True
#stack[-1]

#dictionary:
#key: value