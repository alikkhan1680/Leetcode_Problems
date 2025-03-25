
# Valid Parentheses 20

def isValid(s):
    stack = []
    matching = {')' : "(",  "]": "[",   "}":"{"}
    for char in s:
        if char in matching:
            if stack and stack[-1] == matching[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack



print(isValid("[}"))
print(isValid("(){}"))
print(isValid("({[]})"))