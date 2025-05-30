def largestAltitude(nums):
    qiymat = 0
    max_val = 0

    for i in range(len(nums)):
        qiymat += nums[i]

        if qiymat > max_val:
            max_val = qiymat
    return max_val





print(largestAltitude([-5,1,5,0,-7]))