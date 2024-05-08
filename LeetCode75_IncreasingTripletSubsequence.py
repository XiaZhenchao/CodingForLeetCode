from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # for i in range(len(nums)):
        #     first_num = nums[i]
        #     for j in range(i+1,len(nums)):
        #         second_num = nums[j]
        #         if second_num > first_num:
        #             for k in range(j+1,len(nums)):
        #                 third_num = nums[k]
        #                 if third_num > second_num:
        #                     return True
        # return False
        #optimization
        first_num = float('inf')
        second_num = float('inf')
        for i in nums:
            if i <= first_num:
                first_num = i
                print("first num!")
            elif i <= second_num:
                second_num = i
            else:
                return True
        return False
 


if __name__ == "__main__":
    #nums = [1,2,3,4,5]
    nums = [5,4,3,2,1]
    #nums = [2,1,5,0,4,6]
    solution = Solution()
    print(solution.increasingTriplet(nums))