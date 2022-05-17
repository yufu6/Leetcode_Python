#List Time exceeded
nums = [1,2,3,1,2,3]
k = 2

for i in range(len(nums)):
    for j in range(1, len(nums)):
        if nums[i] == nums[j] and i != j:
            print('i', i)
            print('j', j)
            subs = j - i
            if subs <= k and j > i:
                print('subs', subs)
            else:
                continue
        else:
            continue

            
#Accepted version
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashT = set()
        
        for i in range(len(nums)):
            if nums[i] in hashT:
                return True
            else:
                hashT.add(nums[i])
                
            if len(hashT) > k:
                hashT.remove(nums[i - k])
                
        return False
