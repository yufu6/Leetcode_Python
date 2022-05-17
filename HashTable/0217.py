class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashT = dict()
        for i in nums:
            if i in hashT:
                return True
            else:
                hashT[i] = i
        return False
        
