def sortedArray(nums):
    response = []

    for num in nums:
        square = num ** 2
        response.append(square)
    return sorted(response)

print(sortedArray([-3, 1, 3, 5]))# eng sodda usulda yechilgan masala ishlaydi lekin optimal yechuim emas