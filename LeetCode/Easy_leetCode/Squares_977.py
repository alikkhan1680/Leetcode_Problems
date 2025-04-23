def sortedArray(nums):
    response = [] #javob uchun yangi list ro'yhati

    for num in nums:# for ishlataamiz har bi rqiymat ucun
        square = num ** 2  #har bir qiymatni  kvadratga ko'taramiz
        response.append(square) # javob listiga qo'shamiz kvadratga ko'tarilgan qiymatlarni
    return sorted(response)  #va barcha tayor kvadratga ko'tarilgan variantni tartiblab qaytarammiz

print(sortedArray([-3, 1, 3, 5]))# eng sodda usulda yechilgan masala ishlaydi lekin optimal yechuim emas