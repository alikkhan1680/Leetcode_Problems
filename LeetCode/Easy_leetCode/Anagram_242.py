           # Anagram 242 Easy

def isAnagram(s, t):
    if sorted(s) != sorted(t):
        return False
    return True


print(isAnagram("anagram", "nagaram"))
print(isAnagram("car", "rat"))