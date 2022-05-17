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
