

def reverseVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word = []
    new_word = []

    for ch in s:
        if ch in vowels:
            word.append(ch)

    for ch in s:
        if ch in vowels:
            new_word.append(word.pop())
        else:
            new_word.append(ch)

    return ''.join(new_word)




print(reverseVowels('hello'))  # chiqishi kerak: "mECrEAIc"
