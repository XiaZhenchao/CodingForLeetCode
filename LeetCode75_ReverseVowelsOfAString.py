class Solution:    
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s_list = list(s)
        left = 0
        right = len(s_list)-1
        while left < right:
            if s_list[left] in vowels and s_list[right] in vowels:
                temp = s_list[right]
                s_list[right] = s_list[left]
                s_list[left] = temp
                right -= 1
                left += 1
            if s_list[left] not in vowels:
                left +=1
            if s_list[right] not in vowels:
                right -=1
        return ''.join(s_list)


    # def checkVowels(c:str) -> bool:
    #     if c == 'a' or c == 'A' or c == 'e' or c == 'E' or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'U':
    #         return True
    #     else:
    #         return False
        # return c == chr(65) or c == chr(97) or c == chr(69) or c == chr(101) or c == chr(73) or c == chr(105) or c == chr(79) or c == chr(111) or c == chr(85) or c == chr(117)



if __name__ == "__main__":
    # s = "hello"
    s = "leetcode"
    solution = Solution()
    print(solution.reverseVowels(s))