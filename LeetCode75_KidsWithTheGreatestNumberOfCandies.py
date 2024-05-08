from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Largest_num = candies[0]
        # Result = []
        # for i in candies:
        #     if i > Largest_num or i == Largest_num:
        #         Largest_num = i
        # for i in range(len(candies)):
        #     if candies[i] + extraCandies >= Largest_num:
        #         Result.append(True)
        #     else:
        #         Result.append(False)
        # return Result
        ## optimization
        Largest_num = max(candies)
        Result = [(candy + extraCandies >= Largest_num) for candy in candies]
        return Result



if __name__ == "__main__":
    List = [2,3,5,1,3]
    extra = 3
    solution = Solution()
    print(solution.kidsWithCandies(List, extra))