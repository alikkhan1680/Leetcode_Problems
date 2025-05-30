def moveZeroes(nums):
    left = nums[0]
    right = nums[1]
    nut = []

    for i in range(len(nums) +1):
        if nums[i] > 0:
            nut.append(sorted(i))
        else:
            nums[i -1]  = i
    return sorted(nut)


print(moveZeroes([0, 1, 0, 3, 12]))