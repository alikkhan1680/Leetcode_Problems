def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')

    for i in nums:
        if i <= first:
            first = i
        elif i <= second:
            second = i
        else:
            return True
    return False




print(increasingTriplet([5, 4, 3, 2, 1]))
print(increasingTriplet([1, 2, 3, 4, 5]))
