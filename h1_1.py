class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        strs.sort()
        p=""
        for x,y in zip(strs[0],strs[-1]):
            xx = list(zip(strs[0],strs[-1]))
            if x==y:
                p+=x
            else:
                break
        return p

l1 = Solution()
print(l1.longestCommonPrefix(['abcasad','abckadadsa','abhasdasdsa','abgasdasda']))