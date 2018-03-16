# coding:utf-8

class Solution(object):
    @classmethod
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        mid = len(s)/2
        left_length = self.lengthOfLongestSubstring(s[:mid])
        right_length = self.lengthOfLongestSubstring(s[mid:])
        cross_length = self.findLongestSubStringCrossMid(s, 0, len(s) -1, mid)
        # print left_length,right_length,cross_length
        if cross_length >= left_length and cross_length >= right_length:
            return cross_length
        elif left_length >= cross_length and left_length >= right_length:
            return left_length
        else:
            return right_length
        
    @classmethod
    def findLongestSubStringCrossMid(self, s, low, high, mid):
        """
        查找到穿越中点的longest substring
        """
        substring = []
        length = 0
        i = mid
        while i >= low:
            if s[i] not in substring:
                substring.append(s[i])
                length = length + 1
            else:
                break
            i = i - 1
        
        i = mid + 1
        while i <= high:
            if s[i] not in substring:
                substring.append(s[i])
                length = length + 1
            else:
                break
            i = i + 1
        return length
    
if __name__ == '__main__':
    A = "anviaj"
    b = Solution()
    print b.lengthOfLongestSubstring(A)