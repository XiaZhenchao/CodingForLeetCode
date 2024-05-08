from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # if n == 0:
        #     return True
        # if len(flowerbed) == 1:
        #     if flowerbed[0] == 0:
        #         return True
        #     else:
        #         return False
        
        # if len(flowerbed)>= 2:
        #     if flowerbed[0] == 0 and flowerbed[1] == 0:
        #         flowerbed[0] = 1
        #         n = n-1
        #     if flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
        #         flowerbed[len(flowerbed)-1] = 1
        #         n = n-1
        

        # for i in range(1,len(flowerbed)-2):
        #  if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] != 1:
        #     flowerbed[i] = 1
        #     n = n-1
        # if n >0:
        #     return False
        # else:
        #     return True
        ## optimazation
        flowerbed = [0]+flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n = n-1 
        return n < 0 or n == 0
      

if __name__ == "__main__":
    # flowerbed = [1,0,0,0,0,0,1]
    # n = 2
    # flowerbed = [1,0,0,0,1]
    # n = 1
    # flowerbed =[1,0,1,0,1,0,1]
    # n = 1
    # flowerbed =[0]
    # n = 1
    # flowerbed =[1]
    # n = 1
    flowerbed =[1]
    n = 0
    solution = Solution()
    print(solution.canPlaceFlowers(flowerbed, n))