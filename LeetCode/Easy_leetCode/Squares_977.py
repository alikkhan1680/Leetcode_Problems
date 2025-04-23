from orca.debug import printInputEvent


def sortedArray(nums):
    response = [] #javob uchun yangi list ro'yhati

    for num in nums:# for ishlataamiz har bi rqiymat ucun
        square = num ** 2  #har bir qiymatni  kvadratga ko'taramiz
        response.append(square) # javob listiga qo'shamiz kvadratga ko'tarilgan qiymatlarni
    return sorted(response)  #va barcha tayor kvadratga ko'tarilgan variantni tartiblab qaytarammiz

print(sortedArray([-3, 1, 3, 5]))# eng sodda usulda yechilgan masala ishlaydi lekin optimal yechuim emas



def SortedArray(nums):
    n = len(nums)
    ans = [0] * n
    left = 0
    right = n-1
    loc = n-1

    while left <= right:
        left_sq = nums[left] ** 2
        right_sq = nums[right] **2

        if left_sq > right_sq:
            ans[loc] = left_sq
            left += 1
        else:
            ans[loc] = right_sq
            right -= 1

        loc -= 1
    return f'{ans} ans'


print(SortedArray([-2, 1, 2, 5]))