class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = len(s)
        t_freq = len(t)
        seen = set()
        if s_freq != t_freq:
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -=1
        for val in count:
            if val != 0:
                return False

        return True
