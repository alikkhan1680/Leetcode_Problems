def pivotIndex(nums):
    ong = 0
    chap = 0

    for i in range(len(nums)):
        chap = sum(nums[0:i])
        ong = sum(nums[i+1: len(nums)])
        if chap == ong:
            return i
    return -1





print(pivotIndex([1,7,3,6,5,6]))