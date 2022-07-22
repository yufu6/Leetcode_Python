class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, last = 0, len(nums)-1, len(nums)-1
        final = [-1] * (len(nums))
        
        while left <= right:
            sl = nums[left] ** 2
            sr = nums[right] ** 2
            if sl < sr:
                final[last] = sr
                right -= 1
            else:
                final[last] = sl
                left += 1
            last -= 1
        return final
