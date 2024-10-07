import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile('[\W_]+')
        s = pattern.sub('', s).lower()
        j = len(s) - 1

        for i in range(len(s)):
            if s[i] != s[j]:
                return False
            j -= 1
        return True
        