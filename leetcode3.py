class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_len=len(s)
        if s_len<=1:
            return s_len
        end=1
        start=0
        max_len=0
        while end<s_len+1:
            if self.is_unit(s[start:end]):
                if (end-start)>=max_len:
                    max_len=end-start
                end += 1
            else:
                start+=1
        return max_len
    def is_unit(self,s):
        return len(s)==len(set(s))
if __name__ == '__main__':
    c=Solution().lengthOfLongestSubstring("dvdf")
    print(c)