class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        max_num = 0
        seen = set()
        for n in range(0, len(s)):
            while s[right] in seen:
                if len(seen) > max_num:
                    max_num = len(seen)
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            right += 1
        return max(max_num, len(seen))
                        
#abc

#two variables, left and right
#move right by 1 down
#check if duplicates in that
    #if length of set is equal to regular length of list, no duplicate
    # if unequal, duplicates
#if duplicates, move left up till no more duplicates 
    # while set length == length of values
#with the new list, check if the length