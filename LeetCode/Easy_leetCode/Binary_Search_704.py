
#   Binar Search 704


def binar_serach(nums, target):
    left , right = 0, len(nums)-1

    while left <= right:
        min = (left + right) // 2
        if nums[min] == target:
            return min
        elif nums[min] < target:
            left = min +1
        else:
            right = min -1
    return -1

nums = [1, 2, 3, 4, 5, 6,  7, 8, 9, 10]

print(binar_serach(nums,  6))