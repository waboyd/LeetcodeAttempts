# reversestring344.py
# For LeetCode problem 344: Reverse String
# Written by Will Boyd

class Solution(object):
    def reverseString(self, s):
        """ Returns the reversed version of the input string s.
        :type s: str
        :rtype: str
        """
        if s is None:
            return None
        if s == "":
            return ""
        max_index = len(s) - 1
        # for index in range(len(s)):
        #     s_reverse += s[s_size-index-1]
        s_reverse =\
            "".join([s[max_index-index] for index in range(max_index + 1)])
        return s_reverse
