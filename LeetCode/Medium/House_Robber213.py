def rob(nums):
    n = len(nums) # n = 4
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    dp = [0] * n # dp = [0, 0, 0, 0]
    dp[0] = nums[0] # dp[0] = 2
    dp[1] = max(nums[0], nums[1]) # dp[1] = 3

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        print(dp[i])

    return dp[n-1]








print(rob([2, 3, 1, 5,6, 3, 2, ]))