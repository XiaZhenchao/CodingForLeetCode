class Solution:
    def reverseWords(self, s: str) -> str:
        # s_list = list(s)
        # s_list.insert(0,' ')
        # s_list.append(' ')
        # s_result = []
        # word = []
        # for i in range(1,len(s_list)):
        #     if (' ' in s_list[i-1] and s_list[i].isalnum()) == True or (s_list[i-1].isalnum() and s_list[i].isalnum()):
        #         word.append(s_list[i])
               
        #     else:
        #         if len(word)!= 0:
        #             for i in range(len(word)):
        #                 s_result.insert(i,word[i])
        #             s_result.insert(len(word)," ")
        #             print(s_result)
        #             word = []
        # s_result = s_result[:-1]
        # return ''.join(s_result)
        # uptimization  
        return " ".join(reversed(s.split()))



if __name__ == "__main__":

    # s = "the sky is blue"
    # s = "  hello world  "
    s = "a good   example"
    solution = Solution()
    print(solution.reverseWords(s))