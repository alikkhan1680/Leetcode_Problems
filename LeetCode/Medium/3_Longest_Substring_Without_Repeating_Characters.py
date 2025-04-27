def Substring(s):
    seen = set()
    left = 0
    maxLength = 0 #1,2,3,4


    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        maxLength = max(maxLength, right - left +1)
    return maxLength


print(Substring('abctc'))
                #"tc"