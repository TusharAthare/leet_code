
class Solution:
    def __init__(self,s: str, t:str) -> None:
        self.s = s
        self.t = t

    def find_anagram1(self):
        """
        Create a hash map of count of chars and iterate through counts.
        Time Complexity : O(s+t)
        Space Complexity : O(s+t)
        """
        s_map = {}
        t_map = {}
        if len(self.s) != len(self.t):
            return False

        for i, j in zip(self.s,self.t):
            s_map[i] = s_map.get(i,0) + 1
            t_map[j] = t_map.get(j,0) + 1
        for c in s_map:
            if s_map[c] != t_map.get(c,0):
                return False
        return True

    def find_anagram2(self):
        """
        Make use of Counter data structure
        """
        from collections import Counter
        return Counter(self.s) == Counter(self.t)

    def find_anagram3(self):
        """
        Use sorting algorithms
        Time Complexity : O(n), O(nlogn)
        Space Complexity : O(1)
        """
        return sorted(self.s) == sorted(self.t)
    

if __name__ == "__main__":
    string_1 = 'anagram'
    string_2 = 'nagaram'
    solution = Solution(string_1,string_2)
    # 1st solution
    print(f"{solution.find_anagram1()=}")
    # 2nd solution
    print(f"{solution.find_anagram2()=}")
    # 3rd solution
    print(f"{solution.find_anagram3()=}")
