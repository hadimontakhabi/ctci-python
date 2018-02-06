#!/usr/bin/python3

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        r_str = strs[0]
        for str in strs:
            length = len(str) if (len(str) < len(r_str)) else len(r_str) 
            print ("length= ", length)
            if length == 0: return ""
            r_str = r_str[0:length]
            for i in range(length):
                print ("i= ", i)
                print ("str= ", str)
                print ("r_str= ", r_str)
                if r_str[i] != str[i]:
                    if i==0: return ""
                    else:
                        r_str = r_str[0:i]
                        break
        return r_str

def test():
    sol = Solution()
    lcp = sol.longestCommonPrefix(["flower", "flow", "flight"])
    print (lcp)

test()
