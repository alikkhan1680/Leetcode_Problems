# def myAtoi(s):
#     s = s.strip()  # Boshlanishdagi bo‘sh joylarni olib tashlaymiz
#     if not s:
#         return 0  # Agar bo‘sh bo‘lsa, 0 qaytaramiz
#
#     sign = 1  # Ijobiy deb faraz qilamiz
#     i = 0
#     if s[0] in ['+', '-']:  # Agar belgi bo‘lsa
#         if s[0] == '-':
#             sign = -1
#         i += 1  # Belgidan keyingi indexdan boshlaymiz
#
#     result = 0
#     while i < len(s) and s[i].isdigit():  # Raqamlar tugamaguncha
#         result = result * 10 + int(s[i])  # Sonni hosil qilamiz
#         i += 1
#
#     result *= sign  # Belgini qo‘llaymiz
#
#     # 32-bit signed integer chegarasini tekshiramiz
#     if result < -2**31:
#         return -2**31
#     elif result > 2**31 - 1:
#         return 2**31 - 1
#     else:
#         return result
#
#
# print(myAtoi('345'))         # 345
# print(myAtoi('   -42'))      # -42
# print(myAtoi('+100'))        # 100
# print(myAtoi('words123'))    # 0
# print(myAtoi('91283472332')) # 2147483647 (chegaradan katta)
from django.db.models.expressions import result


def myAtoi(s):
    s = s.strip()
    if not s:
        return 0

    sign = 1
    i = 0
    if s[0] in ['-', '+']:
        if s[0] == '-':
            sign = -1
        i += 1


    result = 0
    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    result *= sign

    if result < -2**31:
        return 2**31
    elif result > 2**31 -1:
        return 2**31 -1
    else:
        return result
print(myAtoi('345'))         # 345
print(myAtoi('   -42'))      # -42
print(myAtoi('+100'))        # 100
print(myAtoi('words123'))    # 0
print(myAtoi('91283472332')) # 2147483647 (chegaradan katta)
