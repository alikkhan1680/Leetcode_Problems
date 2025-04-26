# def Climbing_Stairs (n):
#     if n <= 2:
#         return
#
#     first = 1
#     second = 2
#
#     for i in range(3, n + 1 ):
#         third = first + second
#         first = second
#         second = third
#
#     return second
#  bu masalani ikkita o'zgaruvchi orqali yechilishi

def Climbing_Stairs(n):
    if n <= 2:
        return n

    dp = [0] * (n +1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i -1] + dp[i-2]

    return dp[n]

print(Climbing_Stairs(5))

# bu masalan ikkinchi ishlanish usuli dinamik programming yo'lida
