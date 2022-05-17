
nums = list()


hashT = dict()
count = 0
for i in nums:
    if i in hashT:
        print(True)
    else:
        hashT[i] = i
        count = count + 1
print(False)
