# 1, Two Summ    Easy


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums )):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print(twoSum([2, 2, 4,5,  11, 15, 9], 9))
