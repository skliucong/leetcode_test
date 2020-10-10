"""
1. 根据索引找出最长回文串，从中间向两边发散
"""
class Solution:
    def longestPalindrome(self, s) -> str:
        def PalindromeLength(start,end):

            if start<0 or end>len(s)-1:
                return ""
            if end==0 or start==len(s)-1:
                return s[k]
            this_str=""
            while start>=0 and end<=len(s)-1:
                if s[start]==s[end]:
                    this_str=s[start:end+1]
                    start-=1
                    end+=1
                else:
                    break
            return this_str
        m_length=0
        m_str=s[0]
        for k in range(len(s)):
            str1=PalindromeLength(k,k+1)
            if len(str1)>m_length:
                m_length=len(str1)
                m_str=str1
            str2=PalindromeLength(k-1,k+1)
            if len(str2)>m_length:
                m_length=len(str2)
                m_str=str2
        return m_str

if __name__ == '__main__':
    c=Solution().longestPalindrome("bb")
    print(c)