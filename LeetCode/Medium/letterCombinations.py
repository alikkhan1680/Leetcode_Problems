def letterCombinations(digits):
    if not digits:
        return []

    # Telefon klaviaturasidagi harflarni lug'at ko‘rinishida yozamiz
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    result = [""]  # Boshlanishda bitta bo‘sh kombinatsiya bor

    for digit in digits:
        letters = phone_map[digit]  # Masalan, "2" uchun "abc"
        temp = []  # Yangi kombinatsiyalarni shu yerga yig'amiz
        for combination in result:
            for letter in letters:
                temp.append(combination + letter)  # Eski kombinatsiyalarga yangi harfni qo‘shamiz
        result = temp  # Endi result bu yangi kombinatsiyalar

    return result
