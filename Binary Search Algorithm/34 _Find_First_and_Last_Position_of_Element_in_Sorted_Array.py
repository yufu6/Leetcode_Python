#https://programmercarl.com/0034.在排序数组中查找元素的第一个和最后一个位置.html#其他语言版本
# 解法2
# 1、首先，在 nums 数组中二分查找 target；
# 2、如果二分查找失败，则 binarySearch 返回 -1，表明 nums 中没有 target。此时，searchRange 直接返回 {-1, -1}；
# 3、如果二分查找成功，则 binarySearch 返回 nums 中值为 target 的一个下标。然后，通过左右滑动指针，来找到符合题意的区间

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(nums: List[int], target: int) -> int:
            left, right= 0, len(nums) 

            while left < right:
                mid = left + ((right - left) // 2)

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid 
                else:
                    return mid
            return -1
        
        index = binarySearch(nums, target)
        if index == -1:
            return [-1, -1]
        
        left, right = index, index
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
            
        return [left, right]


      
