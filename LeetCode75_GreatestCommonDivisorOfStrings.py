class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
       if(str1 + str2 != str2 + str1):
           return ""
       else:
           from math import gcd
           return str1[:gcd(len(str1), len(str2))]

    


if __name__ == "__main__":
    solution = Solution()
    str1 = "ABCABCABCABC"
    str2 = "ABCABC"
    print(solution.gcdOfStrings(str1, str2))
