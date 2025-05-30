def Is_Subsequence(s, t):
    i = 0

    for char in t:
        if i < len(s) and char == s[i]:
            i += 1

    if i == len(s):
        return True
    else:
        return False





print(Is_Subsequence('abc', 'hbgdc'))