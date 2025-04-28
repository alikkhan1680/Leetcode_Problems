def longestPalindrome(s):
    longest = ""  # Eng uzun palindromni saqlash

    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1]:  # Substring teskari o'zi bilan tengmi?
                if len(substring) > len(longest):  # Agar uzunroq bo'lsa
                    longest = substring  # Yangilaymiz

    return longest

print(longestPalindrome('abaab'))

