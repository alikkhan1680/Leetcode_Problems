# # 1, Two Summ    Easy
#

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums )):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []
#
#
# print(twoSum([2, 2, 4,5,  11, 15, 9], 9))


def twoSum(nums, target):
    hash_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i

    return []


print(twoSum([2, 3, 5, 7, 8], 12))


