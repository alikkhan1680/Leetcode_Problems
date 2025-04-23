def reverseVowels(s: str) -> str:
    vowels = set("aeiouAEIOU")  # Unli harflarni to‘plam sifatida saqlaymiz
    s = list(s)  # Stringni listga o‘tkazamiz (immutable bo‘lgani uchun)

    left, right = 0, len(s) - 1  # Ikki pointer

    while left < right:
        while left < right and s[left] not in vowels:  # Chapdan unli harfni topamiz
            left += 1
        while left < right and s[right] not in vowels:  # O‘ngdan unli harfni topamiz
            right -= 1

        s[left], s[right] = s[right], s[left]  # Unlilarni almashtiramiz
        left += 1
        right -= 1

    return "".join(s)  # Listni yana stringga aylantiramiz


# Misollar
print(reverseVowels("hello"))  # "holle"
print(reverseVowels("leetcode"))  # "leotcede"
