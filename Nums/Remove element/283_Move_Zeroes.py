#same position swape till zero -> swape with 0
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        index = 0
        for i in range(len(nums)):
            print(i)
            if nums[i] != 0:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
         
 #Double pointer
 class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            fast += 1
            
            if nums[slow] != 0:
                slow += 1
            
