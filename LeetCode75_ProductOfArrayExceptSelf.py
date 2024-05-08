from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left_nums = nums[:len(nums)//2]
        # right_nums = nums[len(nums)//2:]
        # middle = int(len(nums)/2)
        # left_sum = 1
        # right_sum = 1
        # result_num = []
        # temp_sum = 1
        # for i in range(len(nums)):
        #     if i < middle:
        #         left_sum *= nums[i]
        #     else:
        #         right_sum *= nums[i]

        # for i in range(len(nums)):
        #     if i < middle:
        #         index = 0
        #         while index<middle:
                    
        #             if index != i:
        #                 temp_sum *= nums[index]
        #             index = index+1
        #         temp_sum *= right_sum
        #         result_num.append(temp_sum)
        #         temp_sum = 1
        #     else:
        #         index = middle
        #         while index<len(nums):
        #             if index != i:
        #                 temp_sum *= nums[index]
        #             index = index+1
        #         temp_sum *= left_sum
        #         result_num.append(temp_sum)
        #         temp_sum = 1

        # return result_num
        #optimization
        nums_length = len(nums)
        prefix = [0]* nums_length
        suffix = [0]* nums_length
        prefix[0] = 1
        suffix[nums_length-1] = 1
        nums_result = [0]*nums_length

        for i in range(1,nums_length):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(nums_length-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]
        
        for i in range(nums_length):
            nums_result[i] = prefix[i]*suffix[i]

        return nums_result
                  

if __name__ == "__main__":
    nums = [1,2,3,4]
    solution = Solution()
    print(solution.productExceptSelf(nums))