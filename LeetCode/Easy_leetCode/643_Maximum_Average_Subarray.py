def Maximum_Average_Subarray(nums, k):
    current_sum = sum(nums[:k])
    max_avg = current_sum / k

    for i in range(1, len(nums) - k + 1):
        current_sum = current_sum - nums[i - 1] + nums[i + k - 1]

        max_avg = max(max_avg, current_sum / k)
    return max_avg

print(Maximum_Average_Subarray([10, 20, 30, 40, 50, 60], 3))
