class Solution:
    def longestCommonPrefix(self, strs):
        if (len(strs) == 0):
            return ""
        length = min(len(word) for word in strs)
        output = ""
        for index in range(length):
            for loops in range(len(strs)-1):
                if(strs[0][index] != strs[loops+1][index]):
                    return output
            output = output + strs[0][index]
        return output