from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s = s + f"{len(i)}#{i}"
        return s

    def decode(self, s: str) -> List[str]:
        strs,i= [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(f"{s=}\n{i=}\n{j=}\n{strs=}\n{s[i:j]=}")
            len_of_str = int(s[i:j])
            i = j + 1
            j = i + len_of_str
            strs.append(s[i:j])
            i = j
        return strs
            