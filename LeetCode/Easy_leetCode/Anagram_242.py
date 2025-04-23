           # Anagram 242 Easy
# sorted bilan qilingan yondoshuv
def isAnagram(s, t):
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))
print(isAnagram("car", "rat"))

# hash_map bilan yechilgan usulda
def IsAnagram(s, t):
    if len(s) != len(t): # qatorlar uzunligini tekshiradi agar tafovuut bo'lsa shu yerda False qaytaradi
        return False

    hash_map = {}

    for char in s:
        hash_map[char] = hash_map.get(char, 0) + 1

    for char in t:
        if char in hash_map:
            hash_map[char] -= 1
        else:
            False
    return all(value == 0 for value in hash_map.values())

print(IsAnagram('anagram', 'nagaram'))

