def productExceptSelf(nums):
    val = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j != i:
                product *= nums[j]
        val.append(product)
    return val

print(productExceptSelf([1, 2, 3, 4]))